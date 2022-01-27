"""
API operations on Group objects.
"""
import logging

from galaxy.managers.context import ProvidesAppContext
from galaxy.managers.group_users import GroupUsersManager
from galaxy.schema.fields import DecodedDatabaseIdField
from galaxy.web import (
    expose_api,
    require_admin,
)
from . import BaseGalaxyAPIController, depends

log = logging.getLogger(__name__)


class GroupUsersAPIController(BaseGalaxyAPIController):
    manager: GroupUsersManager = depends(GroupUsersManager)

    @require_admin
    @expose_api
    def index(self, trans: ProvidesAppContext, group_id: DecodedDatabaseIdField, **kwd):
        """
        GET /api/groups/{encoded_group_id}/users
        Displays a collection (list) of groups.
        """
        return self.manager.index(trans, group_id)

    @require_admin
    @expose_api
    def show(self, trans: ProvidesAppContext, id: DecodedDatabaseIdField, group_id: DecodedDatabaseIdField, **kwd):
        """
        GET /api/groups/{encoded_group_id}/users/{encoded_user_id}
        Displays information about a group user.
        """
        return self.manager.show(trans, id, group_id)

    @require_admin
    @expose_api
    def update(self, trans: ProvidesAppContext, id: DecodedDatabaseIdField, group_id: DecodedDatabaseIdField, **kwd):
        """
        PUT /api/groups/{encoded_group_id}/users/{encoded_user_id}
        Adds a user to a group
        """
        return self.manager.update(trans, id, group_id)

    @require_admin
    @expose_api
    def delete(self, trans: ProvidesAppContext, id: DecodedDatabaseIdField, group_id: DecodedDatabaseIdField, **kwd):
        """
        DELETE /api/groups/{encoded_group_id}/users/{encoded_user_id}
        Removes a user from a group
        """
        return self.manager.delete(trans, id, group_id)
