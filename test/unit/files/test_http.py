import io
import json
import os
import urllib
from ipaddress import ip_network
from typing import Any
from unittest import mock

import pytest

from galaxy import exceptions
from galaxy.files import ConfiguredFileSources
from galaxy.files.models import FileSourcePluginsConfig
from galaxy.files.uris import stream_url_to_file
from ._util import (
    assert_realizes_as,
    assert_realizes_contains,
    configured_file_sources,
    user_context_fixture,
)

SCRIPT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
FILE_SOURCES_CONF = os.path.join(SCRIPT_DIRECTORY, "http_file_sources_conf.yml")
FILE_SOURCES_CONF_WITHOUT_STOCK = os.path.join(SCRIPT_DIRECTORY, "http_without_stock_file_sources_conf.yml")


@pytest.mark.usefixtures("fake_public_dns")
def test_file_source_http_specific():
    test_url = "https://www.usegalaxy.org/myfile.txt"

    def check_specific_header(request, **kwargs):
        assert request.headers["Authorization"] == "Bearer IBearTokens"
        response: Any = io.StringIO("hello specific world")
        response.headers = {}
        response.geturl = lambda: test_url
        return response

    with mock.patch.object(urllib.request, "urlopen", new=check_specific_header):
        user_context = user_context_fixture()
        file_sources = configured_file_sources(FILE_SOURCES_CONF)
        file_source_pair = file_sources.get_file_source_path(test_url)

        assert file_source_pair.path == test_url
        assert file_source_pair.file_source.id == "test1"

        assert_realizes_as(file_sources, test_url, "hello specific world", user_context=user_context)


@pytest.mark.usefixtures("fake_public_dns")
def test_file_source_another_http_specific():
    test_url = "http://www.galaxyproject.org/anotherfile.txt"

    def check_another_header(request, **kwargs):
        assert request.headers["Another_header"] == "found"
        response: Any = io.StringIO("hello another world")
        response.geturl = lambda: test_url
        response.headers = {}
        return response

    with mock.patch.object(urllib.request, "urlopen", new=check_another_header):
        user_context = user_context_fixture()
        file_sources = configured_file_sources(FILE_SOURCES_CONF)
        file_source_pair = file_sources.get_file_source_path(test_url)

        assert file_source_pair.path == test_url
        assert file_source_pair.file_source.id == "test2"

        assert_realizes_as(file_sources, test_url, "hello another world", user_context=user_context)


@pytest.mark.usefixtures("fake_public_dns")
def test_file_source_http_generic():
    test_url = "https://www.elsewhere.org/myfile.txt"

    def check_generic_headers(request, **kwargs):
        assert not request.headers
        response: Any = io.StringIO("hello generic world")
        response.headers = {}
        response.geturl = lambda: test_url
        return response

    with mock.patch.object(urllib.request, "urlopen", new=check_generic_headers):
        user_context = user_context_fixture()
        file_sources = configured_file_sources(FILE_SOURCES_CONF)
        file_source_pair = file_sources.get_file_source_path(test_url)

        assert file_source_pair.path == test_url
        assert file_source_pair.file_source.id == "test3"

        assert_realizes_as(file_sources, test_url, "hello generic world", user_context=user_context)


@pytest.mark.usefixtures("fake_public_dns")
def test_file_source_ftp_url():
    test_url = "ftp://ftp.gnu.org/README"

    def check_generic_headers(request, **kwargs):
        assert not request.headers
        response: Any = io.StringIO("This is ftp.gnu.org, the FTP server of the the GNU project.")
        response.headers = {}
        response.geturl = lambda: test_url
        return response

    with mock.patch.object(urllib.request, "urlopen", new=check_generic_headers):
        user_context = user_context_fixture()
        file_sources = configured_file_sources(FILE_SOURCES_CONF)
        file_source_pair = file_sources.get_file_source_path(test_url)

        assert file_source_pair.path == test_url
        assert file_source_pair.file_source.id == "test3"

        assert_realizes_contains(
            file_sources,
            test_url,
            "This is ftp.gnu.org, the FTP server of the the GNU project.",
            user_context=user_context,
        )


def test_file_source_http_without_stock_generic():
    test_url = "https://www.elsewhere.org/myfile.txt"
    file_sources = configured_file_sources(FILE_SOURCES_CONF_WITHOUT_STOCK)
    with pytest.raises(exceptions.RequestParameterInvalidException, match="Could not find handler for URI"):
        file_sources.get_file_source_path(test_url)


@pytest.mark.usefixtures("fake_public_dns")
def test_file_source_http_without_stock_specific():
    test_url = "https://www.usegalaxy.org/myfile2.txt"

    def check_specific_header(request, **kwargs):
        assert request.headers["Authorization"] == "Bearer IBearTokens"
        response: Any = io.StringIO("hello specific world 2")
        response.headers = {}
        response.geturl = lambda: test_url
        return response

    with mock.patch.object(urllib.request, "urlopen", new=check_specific_header):
        user_context = user_context_fixture()
        file_sources = configured_file_sources(FILE_SOURCES_CONF_WITHOUT_STOCK)
        file_source_pair = file_sources.get_file_source_path(test_url)

        assert file_source_pair.path == test_url
        assert file_source_pair.file_source.id == "test1"

        assert_realizes_as(file_sources, test_url, "hello specific world 2", user_context=user_context)


def test_private_http_url_requires_allowlist(tmp_path, httpserver):
    httpserver.expect_request("/data").respond_with_data("private content")
    url = httpserver.url_for("/data").replace("localhost", "127.0.0.1")
    target = tmp_path / "download"
    with pytest.raises(exceptions.ConfigDoesNotAllowException):
        stream_url_to_file(url, target_path=str(target))
    assert httpserver.log == []
    assert not target.exists()

    # Job-side file sources must retain the allowlist after JSON serialization.
    sources = ConfiguredFileSources(
        FileSourcePluginsConfig(fetch_url_allowlist=[ip_network("127.0.0.0/24")]), load_stock_plugins=True
    )
    serialized = json.loads(json.dumps(sources.to_dict(for_serialization=True)))
    stream_url_to_file(url, file_sources=ConfiguredFileSources.from_dict(serialized), target_path=str(target))
    assert target.read_text() == "private content"
