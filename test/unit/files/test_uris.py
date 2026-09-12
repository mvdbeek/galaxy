import ipaddress

import pytest

from galaxy.exceptions import (
    AdminRequiredException,
    ConfigDoesNotAllowException,
)
from galaxy.files.uris import (
    validate_non_local,
    validate_uri_access,
)


def test_validate_local_ip_access():
    assert validates_as_non_local("http://google.com", [])
    assert not validates_as_non_local("http://127.0.0.1/secrets.txt", [])
    assert validates_as_non_local("http://127.0.0.1/secrets.txt", [ipaddress.ip_address("127.0.0.1")])
    assert validates_as_non_local("http://127.0.0.1/secrets.txt", [ipaddress.ip_network("127.0.0.0/24")])
    assert not validates_as_non_local("http://127.0.0.1/secrets.txt", [ipaddress.ip_network("127.0.0.0/32")])
    assert validates_as_non_local(
        "http://127.0.0.1/secrets.txt", [ipaddress.ip_network("127.0.0.0/32"), ipaddress.ip_network("127.0.0.1/32")]
    )


def test_validate():
    # Check the non local ip address checks from above...
    assert validates("http://google.com", False, [])
    assert not validates("http://127.0.0.1/secrets.txt", False, [])
    assert validates("http://127.0.0.1/secrets.txt", False, [ipaddress.ip_address("127.0.0.1")])
    assert validates("http://127.0.0.1/secrets.txt", False, [ipaddress.ip_network("127.0.0.0/24")])
    assert not validates("http://127.0.0.1/secrets.txt", False, [ipaddress.ip_network("127.0.0.0/32")])
    assert validates(
        "http://127.0.0.1/secrets.txt",
        False,
        [ipaddress.ip_network("127.0.0.0/32"), ipaddress.ip_network("127.0.0.1/32")],
    )

    # check that only admins can acess files...
    assert not validates("file://foo/bar", False, [])
    assert validates("file://foo/bar", True, [])


def validates_as_non_local(uri: str, allow_list):
    try:
        validate_non_local(uri, allow_list)
    except ConfigDoesNotAllowException:
        return False
    return True


def validates(uri: str, is_admin, allow_list):
    try:
        validate_uri_access(uri, is_admin, allow_list)
    except (ConfigDoesNotAllowException, AdminRequiredException):
        return False
    return True


@pytest.mark.parametrize(
    "url, allowlist_entry",
    [
        ("ftp://user:pass@127.0.0.1:2121/data", ipaddress.ip_address("127.0.0.1")),
        ("FTP://127.0.0.1/data", ipaddress.ip_network("127.0.0.0/24")),
        ("ftps://127.0.0.1/data", ipaddress.ip_address("127.0.0.1")),
        ("ftp://[::1]:2121/data", ipaddress.ip_network("::1/128")),
    ],
)
def test_validate_ftp_access(url, allowlist_entry):
    with pytest.raises(ConfigDoesNotAllowException):
        validate_non_local(url, [])
    assert validate_non_local(url, [allowlist_entry]) == url
