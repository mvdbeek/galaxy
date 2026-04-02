import hashlib
import logging
from typing import (
    Any,
    Optional,
)

from starlette.requests import Request

from galaxy.managers.configuration import ConfigurationManager
from galaxy.managers.context import ProvidesUserContext
from galaxy.managers.users import CurrentUserSerializer
from galaxy.model import JWTSessionAdapter
from galaxy.schema import SerializationParams
from galaxy.schema.schema import Model
from galaxy.webapps.galaxy.api import (
    depends,
    DependsOnTrans,
    Router,
)

log = logging.getLogger(__name__)

router = Router(tags=["context"])


class ContextResponse(Model):
    config: dict[str, Any]
    session_csrf_token: Optional[str] = None
    user: dict[str, Any]


@router.cbv
class FastAPIContext:
    configuration_manager: ConfigurationManager = depends(ConfigurationManager)
    user_serializer: CurrentUserSerializer = depends(CurrentUserSerializer)

    @router.get("/context", summary="Return bootstrapped client context")
    def index(self, request: Request, trans: ProvidesUserContext = DependsOnTrans) -> ContextResponse:
        config = self.configuration_manager.get_configuration(trans, SerializationParams(view="all"))
        session_csrf_token = _get_csrf_token(trans, request)
        return ContextResponse(
            config=config,
            session_csrf_token=session_csrf_token,
            user=self.user_serializer.serialize_to_view(trans.user, "detailed"),
        )


def _get_csrf_token(trans: ProvidesUserContext, request: Request) -> Optional[str]:
    if not trans.galaxy_session:
        return None
    session_id = trans.galaxy_session.id
    if session_id is not None:
        return trans.app.security.encode_id(session_id, kind="csrf")
    if isinstance(trans.galaxy_session, JWTSessionAdapter):
        cookie_value = request.cookies.get("galaxysession", "")
        return hashlib.sha256(cookie_value.encode()).hexdigest()[:32]
    return None
