import logging
import os

from fastapi import Response
from fastapi.responses import FileResponse

from tool_shed.structured_app import ToolShedApp
from tool_shed.util.clone_bundles import (
    BUNDLE_FILENAME,
    get_bundle_dir_for_repo,
)
from tool_shed.webapp.model.db import get_repository_by_name_and_owner
from . import (
    depends,
    DependsOnApp,
    Router,
    UsernameIdPathParam,
)

log = logging.getLogger(__name__)

router = Router(tags=["clone_bundles"])


@router.get(
    "/repos/{username}/{name}/clone_bundle",
    summary="Download a prebuilt clone bundle for a repository",
    response_class=Response,
    operation_id="clone_bundles__get",
)
def get_clone_bundle(
    username: str = UsernameIdPathParam,
    name: str = "",
    app: ToolShedApp = DependsOnApp,
):
    if not app.config.clone_bundles_enabled:
        return Response(content="Clone bundles are not enabled", status_code=404)
    repository = get_repository_by_name_and_owner(app.model.context, name, username)
    if repository is None:
        return Response(content="Repository not found", status_code=404)
    bundle_dir = get_bundle_dir_for_repo(app.config.clone_bundles_dir, repository.id)
    bundle_path = os.path.join(bundle_dir, BUNDLE_FILENAME)
    if not os.path.exists(bundle_path):
        return Response(content="No clone bundle available for this repository", status_code=404)
    # Support nginx X-Accel-Redirect for production deployments
    nginx_base = app.config.nginx_x_accel_redirect_base
    if nginx_base:
        rel_path = os.path.relpath(bundle_path, app.config.clone_bundles_dir)
        redirect_path = os.path.join(nginx_base, "clone_bundles", rel_path)
        return Response(
            headers={
                "X-Accel-Redirect": redirect_path,
                "Content-Type": "application/octet-stream",
                "Content-Disposition": f"attachment; filename={BUNDLE_FILENAME}",
            }
        )
    return FileResponse(
        bundle_path,
        media_type="application/octet-stream",
        filename=BUNDLE_FILENAME,
    )
