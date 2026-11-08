from unittest import mock

import pytest

from galaxy.exceptions import ConfigDoesNotAllowException
from galaxy.tools.actions.upload_common import persist_uploads
from galaxy.webapps.galaxy.services._fetch_util import validate_and_normalize_targets


def _trans() -> mock.MagicMock:
    trans = mock.MagicMock()
    trans.app.config.fetch_url_allowlist_ips = []
    return trans


def test_fetch_request_refuses_private_ftp_url():
    payload = {
        "targets": [{"destination": {"type": "hdas"}, "elements": [{"src": "url", "url": "ftp://127.0.0.1/f"}]}],
    }
    with pytest.raises(ConfigDoesNotAllowException):
        validate_and_normalize_targets(_trans(), payload)


def test_upload_request_refuses_private_ftp_url():
    params = {"files": [{"file_data": "", "url_paste": "ftp://127.0.0.1/f"}]}
    with pytest.raises(ConfigDoesNotAllowException):
        persist_uploads(params, _trans())
