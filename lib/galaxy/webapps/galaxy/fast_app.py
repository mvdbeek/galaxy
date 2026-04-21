import logging
from contextlib import asynccontextmanager
from typing import (
    Any,
    TYPE_CHECKING,
)
from urllib.parse import urljoin

from a2wsgi import WSGIMiddleware
from fastapi import (
    FastAPI,
    Request,
)
from fastapi.openapi.constants import REF_TEMPLATE
from slowapi import (
    _rate_limit_exceeded_handler,
    Limiter,
)
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.datastructures import MutableHeaders
from starlette.middleware.cors import CORSMiddleware
from tuspyserver import create_tus_router

from galaxy.schema.generics import ref_to_name
from galaxy.version import VERSION
from galaxy.webapps.base.api import (
    add_exception_handler,
    add_raw_context_middlewares,
    add_request_id_middleware,
    build_route_name_index,
    GalaxyFileResponse,
    include_all_package_routers,
)
from galaxy.webapps.base.webapp import (
    _is_embed_request,
    config_allows_origin,
)
from galaxy.webapps.openapi._compat.v2 import GenerateJsonSchema
from galaxy.webapps.openapi.utils import get_openapi

if TYPE_CHECKING:
    from pydantic.json_schema import (
        CoreModeRef,
        DefsRef,
    )

# https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-tags
api_tags_metadata = [
    {
        "name": "configuration",
        "description": "Configuration-related endpoints.",
    },
    {"name": "datasets", "description": "Operations on datasets."},
    {"name": "dataset collections"},
    {
        "name": "datatypes",
        "description": "Operations with supported data types.",
    },
    {
        "name": "datatypes",
        "description": "Operations on dataset collections.",
    },
    {
        "name": "genomes",
        "description": "Operations with genome data.",
    },
    {
        "name": "group_roles",
        "description": "Operations with group roles.",
    },
    {
        "name": "groups",
        "description": "Operations with groups.",
    },
    {
        "name": "group_users",
        "description": "Operations with group users.",
    },
    {"name": "histories"},
    {"name": "libraries"},
    {"name": "data libraries folders"},
    {"name": "job_lock"},
    {"name": "default"},
    {"name": "users"},
    {"name": "jobs"},
    {"name": "roles"},
    {"name": "quotas"},
    {"name": "visualizations"},
    {"name": "pages"},
    {
        "name": "licenses",
        "description": "Operations with [SPDX licenses](https://spdx.org/licenses/).",
    },
    {
        "name": "tags",
        "description": "Operations with tags.",
    },
    {
        "name": "tool data tables",
        "description": "Operations with tool [Data Tables](https://galaxyproject.org/admin/tools/data-tables/).",
    },
    {
        "name": "tours",
        "description": "Operations with interactive tours.",
    },
    {
        "name": "remote files",
        "description": "Operations with remote dataset sources.",
    },
    {"name": "undocumented", "description": "API routes that have not yet been ported to FastAPI."},
    {
        "name": "ai",
        "description": "**BETA**: AI agent operations. This API is experimental and may change without notice.",
    },
    {
        "name": "chat",
        "description": "**BETA**: Chat interface for AI agents. This API is experimental and may change without notice.",
    },
]


class GalaxyCORSMiddleware(CORSMiddleware):
    def __init__(self, *args, **kwds):
        self.config = kwds.pop("config")
        super().__init__(*args, **kwds)

    def is_allowed_origin(self, origin: str) -> bool:
        return config_allows_origin(origin, self.config)


class XFrameOptionsMiddleware:
    def __init__(self, app, x_frame_options: str):
        self.app = app
        self.x_frame_options = x_frame_options

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request = Request(scope)

        async def send_with_header(message):
            if message["type"] == "http.response.start":
                if not _is_embed_request(request.url.path, str(request.url.query)):
                    headers = MutableHeaders(scope=message)
                    headers.append("X-Frame-Options", self.x_frame_options)
            await send(message)

        await self.app(scope, receive, send_with_header)


def add_galaxy_middleware(app: FastAPI, gx_app):
    if x_frame_options := gx_app.config.x_frame_options:
        app.add_middleware(XFrameOptionsMiddleware, x_frame_options=x_frame_options)

    GalaxyFileResponse.nginx_x_accel_redirect_base = gx_app.config.nginx_x_accel_redirect_base
    GalaxyFileResponse.apache_xsendfile = gx_app.config.apache_xsendfile

    if gx_app.config.get("allowed_origin_hostnames", None):
        app.add_middleware(
            GalaxyCORSMiddleware,
            config=gx_app.config,
            allow_headers=["*"],
            allow_methods=["*"],
            max_age=600,
        )


def _build_merged_openapi(app, gx_app):
    openapi_schema = get_openapi(
        title="Galaxy API",
        version=VERSION,
        routes=app.routes,
        tags=api_tags_metadata,
    )
    legacy_openapi = gx_app.api_spec.to_dict()
    legacy_openapi["paths"].update(openapi_schema["paths"])
    openapi_schema["paths"] = legacy_openapi["paths"]
    return openapi_schema


def include_legacy_openapi(app, gx_app):
    """Install a lazy ``app.openapi`` override that merges the legacy paste
    API spec with the FastAPI-generated schema.

    The previous implementation built the full schema eagerly at server
    startup, which added 3-5s to every test server launch (``get_openapi``
    walks every route and every referenced Pydantic model). Since the merged
    schema is only needed when ``/api/openapi.json`` (or the docs pages) is
    actually requested, defer the work to the first such request. FastAPI's
    default behaviour caches the result on ``app.openapi_schema``.
    """
    if app.openapi_schema:
        return app.openapi_schema

    def _openapi() -> dict:
        if app.openapi_schema is None:
            app.openapi_schema = _build_merged_openapi(app, gx_app)
        return app.openapi_schema

    app.openapi = _openapi
    return None


def get_fastapi_instance(root_path="", lifespan=None) -> FastAPI:
    return FastAPI(
        title="Galaxy API",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_tags=api_tags_metadata,
        license_info={"name": "MIT", "url": "https://github.com/galaxyproject/galaxy/blob/dev/LICENSE.txt"},
        root_path=root_path,
        lifespan=lifespan,
    )


class CustomJsonSchema(GenerateJsonSchema):
    def get_defs_ref(self, core_mode_ref: "CoreModeRef") -> "DefsRef":
        full_def = super().get_defs_ref(core_mode_ref)
        choices = self._prioritized_defsref_choices[full_def]
        ref, mode = core_mode_ref
        if ref in ref_to_name:
            for i, choice in enumerate(choices):
                choices[i] = choice.replace(choices[0], ref_to_name[ref])  # type: ignore[call-overload]
        return full_def


def get_openapi_schema() -> dict[str, Any]:
    """
    Dumps openAPI schema without starting a full app and webserver.
    """
    app = get_fastapi_instance()
    include_all_package_routers(app, "galaxy.webapps.galaxy.api")
    return get_openapi(
        title=app.title,
        version=app.version,
        openapi_version="3.1.0",
        description=app.description,
        routes=app.routes,
        license_info=app.license_info,
        schema_generator=CustomJsonSchema(ref_template=REF_TEMPLATE),
    )


def include_tus(app: FastAPI, gx_app):
    config = gx_app.config
    root_path = "" if config.galaxy_url_prefix == "/" else config.galaxy_url_prefix
    upload_tus_router = create_tus_router(
        prefix=urljoin(root_path, "api/upload/resumable_upload"),
        files_dir=config.tus_upload_store or config.new_file_path,
        max_size=config.maximum_upload_file_size,
    )
    job_files_tus_router = create_tus_router(
        prefix=urljoin(root_path, "api/job_files/resumable_upload"),
        files_dir=config.tus_upload_store_job_files or config.tus_upload_store or config.new_file_path,
        max_size=config.maximum_upload_file_size,
    )
    app.include_router(upload_tus_router)
    app.include_router(job_files_tus_router)


log = logging.getLogger(__name__)


def get_mcp_lifespan(gx_app):
    """Get MCP lifespan if enabled, or (None, None)."""
    if not gx_app.config.enable_mcp_server:
        return None, None

    try:
        from galaxy.webapps.galaxy.api.mcp import get_mcp_app

        mcp_app = get_mcp_app(gx_app)
        return mcp_app, mcp_app.lifespan
    except ImportError:
        log.info("MCP server dependencies not installed (fastmcp), skipping")
        return None, None
    except Exception:
        log.exception("Failed to initialize MCP server")
        return None, None


def include_mcp(app: FastAPI, gx_app, mcp_app):
    """Mount the MCP server if it was initialized."""
    if mcp_app is None:
        return

    try:
        mcp_path = gx_app.config.mcp_server_path
        app.mount(mcp_path, mcp_app)
        log.info(f"MCP server (Streamable HTTP) mounted at {mcp_path}")
    except Exception as e:
        log.error(f"Failed to mount MCP server: {e}")


def initialize_fast_app(gx_wsgi_webapp, gx_app):
    from galaxy.util import ExecutionTimer

    total_timer = ExecutionTimer()
    root_path = "" if gx_app.config.galaxy_url_prefix == "/" else gx_app.config.galaxy_url_prefix

    mcp_timer = ExecutionTimer()
    mcp_app, mcp_lifespan = get_mcp_lifespan(gx_app)
    log.info("initialize_fast_app: mcp_lifespan resolved %s", mcp_timer)

    if mcp_lifespan:

        @asynccontextmanager
        async def combined_lifespan(app: FastAPI):
            async with mcp_lifespan(app):
                yield

        app = get_fastapi_instance(root_path=root_path, lifespan=combined_lifespan)
    else:
        app = get_fastapi_instance(root_path=root_path)

    middleware_timer = ExecutionTimer()
    add_exception_handler(app)
    add_galaxy_middleware(app, gx_app)
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)  # type: ignore[arg-type]
    if gx_app.config.use_access_logging_middleware:
        add_raw_context_middlewares(app)
    else:
        add_request_id_middleware(app)
    log.info("initialize_fast_app: middleware added %s", middleware_timer)

    routers_timer = ExecutionTimer()
    include_all_package_routers(app, "galaxy.webapps.galaxy.api")
    log.info("initialize_fast_app: include_all_package_routers %s", routers_timer)

    openapi_timer = ExecutionTimer()
    include_legacy_openapi(app, gx_app)
    log.info("initialize_fast_app: include_legacy_openapi %s", openapi_timer)

    wsgi_timer = ExecutionTimer()
    wsgi_handler = WSGIMiddleware(gx_wsgi_webapp)
    gx_app.haltables.append(("WSGI Middleware threadpool", wsgi_handler.executor.shutdown))
    log.info("initialize_fast_app: WSGIMiddleware built %s", wsgi_timer)

    tus_timer = ExecutionTimer()
    include_tus(app, gx_app)
    log.info("initialize_fast_app: include_tus %s", tus_timer)

    route_index_timer = ExecutionTimer()
    app.state.route_name_index = build_route_name_index(app)
    log.info("initialize_fast_app: build_route_name_index %s", route_index_timer)

    include_mcp_timer = ExecutionTimer()
    include_mcp(app, gx_app, mcp_app)
    log.info("initialize_fast_app: include_mcp %s", include_mcp_timer)

    mount_timer = ExecutionTimer()
    app.mount("/", wsgi_handler)  # type: ignore[arg-type]
    log.info("initialize_fast_app: wsgi mount %s", mount_timer)

    if gx_app.config.galaxy_url_prefix != "/":
        parent_app = FastAPI()
        parent_app.mount(gx_app.config.galaxy_url_prefix, app=app)
        log.info("initialize_fast_app: total (with url_prefix wrapper) %s", total_timer)
        return parent_app
    log.info("initialize_fast_app: total %s", total_timer)
    return app


def galaxy_rate_limit_key(request: Request) -> str:
    api_key = request.headers.get("x-api-key") or request.query_params.get("key")
    if api_key:
        return f"api_key:{api_key}"
    session_key = request.cookies.get("galaxysession")
    if session_key:
        return f"session:{session_key}"
    return get_remote_address(request)


limiter = Limiter(key_func=galaxy_rate_limit_key)

__all__ = (
    "add_galaxy_middleware",
    "initialize_fast_app",
)
