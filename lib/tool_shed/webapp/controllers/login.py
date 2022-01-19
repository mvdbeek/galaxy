import logging

from galaxy import web
from galaxy.webapps.base.controller import BaseUIController

log = logging.getLogger(__name__)


class LoginController(BaseUIController):

    @web.expose
    def index(self, trans, **kwargs):
        # Redirect to login page of toolshed. This is required because the Toolshed uses Galaxy's
        # `require_login` decorator which redirects to `login` instead of `user/login`.
        login_url = web.url_for(controller='user', action='login')
        return trans.response.send_redirect(login_url)
