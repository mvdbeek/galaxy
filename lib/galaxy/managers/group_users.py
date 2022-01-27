import logging
from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from galaxy import model
from galaxy.app import MinimalManagerApp
from galaxy.exceptions import (
    ObjectNotFound,
)
from galaxy.managers.context import ProvidesAppContext
from galaxy.schema.fields import DecodedDatabaseIdField
from galaxy.web import url_for

log = logging.getLogger(__name__)


class GroupUsersManager:
    """Interface/service object shared by controllers for interacting with group users."""

    def __init__(self, app: MinimalManagerApp) -> None:
        self._app = app

    def index(
        self, trans: ProvidesAppContext, group_id: DecodedDatabaseIdField
    ) -> List[Dict[str, Any]]:
        """
        Returns a collection (list) with some information about users associated with the given group.
        """
        group = self._get_group(trans, group_id)
        rval = []
        for uga in group.users:
            group_user = self._serialize_group_user(group_id, uga.user)
            rval.append(group_user)
        return rval

    def show(
        self,
        trans: ProvidesAppContext,
        id: DecodedDatabaseIdField,
        group_id: DecodedDatabaseIdField,
    ) -> Dict[str, Any]:
        """
        Returns information about a group user.
        """
        user_id = id
        group = self._get_group(trans, group_id)
        user = self._get_user(trans, user_id)
        group_user = self._get_group_user(trans, group, user)
        if group_user is None:
            raise ObjectNotFound(f"User {user.email} not in group {group.name}")

        return self._serialize_group_user(group_id, user)

    def update(
        self,
        trans: ProvidesAppContext,
        id: DecodedDatabaseIdField,
        group_id: DecodedDatabaseIdField,
    ):
        """
        Adds a user to a group.
        """
        user_id = id
        group = self._get_group(trans, group_id)
        user = self._get_user(trans, user_id)
        group_user = self._get_group_user(trans, group, user)
        if group_user is None:
            self._add_user_to_group(trans, group, user)

        return self._serialize_group_user(group_id, user)

    def delete(
        self,
        trans: ProvidesAppContext,
        id: DecodedDatabaseIdField,
        group_id: DecodedDatabaseIdField,
    ):
        """
        Removes a user from a group.
        """
        user_id = id
        group = self._get_group(trans, group_id)
        user = self._get_user(trans, user_id)
        group_user = self._get_group_user(trans, group, user)
        if group_user is None:
            raise ObjectNotFound(f"User {user.email} not in group {group.name}")
        self._remove_user_from_group(trans, group_user)
        return self._serialize_group_user(group_id, user)

    def _get_group(
        self, trans: ProvidesAppContext, group_id: DecodedDatabaseIdField
    ) -> Any:
        group = trans.sa_session.query(model.Group).get(group_id)
        if group is None:
            raise ObjectNotFound("Group not found.")
        return group

    def _get_user(
        self, trans: ProvidesAppContext, user_id: DecodedDatabaseIdField
    ) -> model.User:
        user = trans.sa_session.query(model.User).get(user_id)
        if user is None:
            raise ObjectNotFound("User not found.")
        return user

    def _get_group_user(
        self, trans: ProvidesAppContext, group: model.Group, user: model.User
    ) -> Optional[model.UserGroupAssociation]:
        return (
            trans.sa_session.query(model.UserGroupAssociation)
            .filter(model.UserGroupAssociation.user == user, model.UserGroupAssociation.group == group)
            .one_or_none()
        )

    def _add_user_to_group(self, trans: ProvidesAppContext, group: model.Group, user: model.User):
        gra = model.UserGroupAssociation(user, group)
        trans.sa_session.add(gra)
        trans.sa_session.flush()

    def _remove_user_from_group(self, trans: ProvidesAppContext, group_user: model.UserGroupAssociation):
        trans.sa_session.delete(group_user)
        trans.sa_session.flush()

    def _serialize_group_user(
        self, encoded_group_id: DecodedDatabaseIdField, user: model.User
    ):
        encoded_user_id = self._app.security.encode_id(user.id)
        return {
            "id": encoded_user_id,
            "email": user.email,
            "url": url_for("group_user", group_id=encoded_group_id, id=encoded_user_id),
        }
