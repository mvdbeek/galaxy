import pytest
from galaxy.model import Notification
from galaxy.model.scoped_session import galaxy_scoped_session
from galaxy.model.unittest_utils import GalaxyDataTestApp


@pytest.fixture
def sa_session():
    app = GalaxyDataTestApp()
    return app.model.session


def test_notification_create(sa_session: galaxy_scoped_session):
    notification = Notification()
    sa_session.add(notification)
    sa_session.flush()
    assert notification.id is not None