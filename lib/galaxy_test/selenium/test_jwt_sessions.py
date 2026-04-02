"""Selenium tests that verify Galaxy works correctly with JWT-based sessions.

These tests run the same scenarios as the standard anonymous history and
login/logout tests, but with ``use_jwt_sessions=True`` in the Galaxy config
so that the JWT session code path is exercised end-to-end.
"""

from galaxy_test.base.decorators import requires_new_user
from .framework import (
    selenium_test,
    SeleniumTestCase,
)


class JWTSessionSeleniumTestCase(SeleniumTestCase):
    """Base class for selenium tests that run with JWT sessions enabled."""

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        config["use_jwt_sessions"] = True


class TestAnonymousHistoriesJWT(JWTSessionSeleniumTestCase):
    """Anonymous history tests with JWT sessions enabled.

    Mirrors TestAnonymousHistories but exercises the JWT code path:
    - Anonymous visitors get a JWT cookie (no DB session row)
    - Creating a history lazily creates a DB session
    - Registering transfers the anonymous history to the new user
    """

    @selenium_test
    def test_anon_history_landing(self):
        self.home()
        self.assert_initial_history_panel_state_correct()
        self.history_element("editor toggle").wait_for_present()
        self.history_element("name display").wait_for_present()

    @selenium_test
    def test_anon_history_upload(self):
        self.home()
        self.perform_upload(self.get_filename("1.txt"))
        self.wait_for_history()
        # Reload the history and make sure the state is preserved.
        self.home()
        self.history_panel_wait_for_hid_state(1, "ok")

        # empty should be NO LONGER be displayed
        self.components.history_panel.empty_message.assert_absent_or_hidden()

    @selenium_test
    @requires_new_user
    def test_anon_history_after_registration(self):
        self._upload_file_anonymous_then_register_user()
        self.home()
        self.history_panel_wait_for_hid_state(1, "ok")

    @selenium_test
    @requires_new_user
    def test_clean_anon_history_after_logout(self):
        self._upload_file_anonymous_then_register_user()
        self.logout_if_needed()
        # Give Galaxy the chance to load a new empty history for that now
        # anonymous user. Make sure this new history is empty.
        self.home()
        self.history_panel_wait_for_history_loaded()
        history_contents = self.history_contents()
        assert len(history_contents) == 0

    def _upload_file_anonymous_then_register_user(self):
        self.home()
        self.perform_upload(self.get_filename("1.txt"))
        self.wait_for_history()
        self.register()


class TestLoginJWT(JWTSessionSeleniumTestCase):
    """Login tests with JWT sessions enabled.

    Verifies that the JWT login flow (access token + refresh token cookies)
    works correctly end-to-end.
    """

    @selenium_test
    def test_logging_in(self):
        email = self._get_random_email()
        self.register(email)
        self.logout_if_needed()
        self.home()
        self.submit_login(email, assert_valid=True)
        self.assert_no_error_message()
        assert self.is_logged_in()

    @selenium_test
    def test_invalid_logins(self):
        bad_emails = ["test2@test.org", "test"]
        for bad_email in bad_emails:
            self.home()
            self.submit_login(bad_email, assert_valid=False)
            self.assert_error_message()


class TestSignOutJWT(JWTSessionSeleniumTestCase):
    """Sign-out tests with JWT sessions enabled.

    Verifies that logging out revokes the refresh token and issues
    a new anonymous JWT.
    """

    @selenium_test
    def test_sign_out(self):
        email = self._get_random_email()
        self.register(email)
        self.navigate_to_user_preferences()
        self.components.preferences.sign_out.wait_for_and_click()
        self.components.sign_out.cancel_button.wait_for_and_click()
        assert self.is_logged_in()
        new_email = self.find_element_by_id("user-preferences-current-email").text
        assert email == new_email
        self.components.preferences.sign_out.wait_for_and_click()
        self.components.sign_out.sign_out_button.wait_for_and_click()
        self.sleep_for(self.wait_types.UX_TRANSITION)
        assert not self.is_logged_in()


class TestRegistrationJWT(JWTSessionSeleniumTestCase):
    """Registration tests with JWT sessions enabled.

    Verifies that new user registration works with JWT sessions and
    that logout after registration correctly transitions to anonymous JWT.
    """

    @selenium_test
    def test_registration(self):
        self.home()
        self.register()

    @selenium_test
    def test_logout(self):
        self.home()
        self.register()
        assert self.is_logged_in()
        self.logout_if_needed()
        assert not self.is_logged_in()
        self.home()
        self.components.masthead.username.assert_absent_or_hidden()
