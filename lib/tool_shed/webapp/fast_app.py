from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

from galaxy.webapps.base.api import (
    add_exception_handler,
    add_request_id_middleware,
    include_all_package_routers,
)


def initialize_fast_app(wsgi_app, app):
    asgi_app = FastAPI(
        title="Galaxy Tool Shed API",
        description=(
            "This API allows you to manage the Tool Shed repositories."
        ),
        docs_url="/api/docs",
    )
    add_exception_handler(asgi_app)
    add_request_id_middleware(asgi_app)
    include_all_package_routers(asgi_app, 'tool_shed.webapp.api')
    wsgi_handler = WSGIMiddleware(wsgi_app)
    asgi_app.mount(app.config.url_prefix, wsgi_handler)
    if app.config.url_prefix != '/':
        parent_app = FastAPI()
        parent_app.mount(app.config.url_prefix, app=app)
        return parent_app
    return asgi_app
