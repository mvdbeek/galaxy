import pytest

from galaxy.model import (
    Notification,
    User,
    UserNotificationAssociation,
)
from galaxy.model.scoped_session import galaxy_scoped_session
from galaxy.model.unittest_utils import GalaxyDataTestApp


@pytest.fixture
def sa_session():
    app = GalaxyDataTestApp()
    return app.model.session


def create_user_notification_association():
    # Take the stuff from test_create_notification so we don't need to repeat this all the
    pass


def test_create_notification(sa_session: galaxy_scoped_session):
    notification = Notification()
    sa_session.add(notification)
    sa_session.flush()
    assert notification.id is not None
    user = User(email="test@test.com", password="abcde", username="notification_user")
    sa_session.add(user)
    sa_session.flush()
    assert user.id is not None
    una = UserNotificationAssociation()
    una.user_id = user.id
    una.notification_id = notification.id
    sa_session.add(una)
    sa_session.flush()
    assert una.id is not None
    assert una.user == user
    assert una.notification == notification
    # test backref from Notifcation to UserNotificationAssociation
    assert notification.user_notification_associations == [una]
    pass


def test_get_all_notification_for_user():
    pass


def test_get_notification_unseen_for_user():
    pass


def test_mark_notification_seen():
    pass
