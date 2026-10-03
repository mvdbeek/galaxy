from html import unescape
from urllib.parse import (
    parse_qs,
    urlsplit,
)

import pytest

from galaxy.app_unittest_utils.tools_support import mock_app_for_tool_support
from galaxy.tool_util.parser import get_tool_source
from galaxy.tools import Tool
from galaxy.tools.help import set_local_image_paths


@pytest.mark.parametrize("directive", ["image", "figure", "|plot| image"])
@pytest.mark.parametrize("image_file", ["plot.png", "images/a plot+#?.svg", "$PATH_TO_IMAGES/plot.png"])
def test_local_image_url(directive, image_file):
    text = f"  .. {directive}:: {image_file}\n      :width: 300\n\nOther help."
    result = set_local_image_paths(text, "local: tool", "1.0+test")
    url = result.splitlines()[0].split(":: ")[1].replace("${host_url}", "/galaxy/")
    parsed = urlsplit(url)
    assert parsed.path == "/galaxy/api/tools/local%3A%20tool/help_image"
    assert parse_qs(parsed.query) == {
        "tool_version": ["1.0+test"],
        "image_file": [image_file.removeprefix("$PATH_TO_IMAGES/")],
    }
    assert result.splitlines()[1:] == text.splitlines()[1:]


@pytest.mark.parametrize(
    "url",
    [
        "https://example.com/image.png",
        "http://example.com/image.png",
        "//example.com/image.png",
        "/static/images/image.png",
        "${static_path}/images/image.png",
        "${host_url}static/images/image.png",
        "data:image/png;base64,AAAA",
    ],
)
def test_existing_image_urls_are_preserved(url):
    text = f".. image:: {url}\n"
    assert set_local_image_paths(text, "local", "1.0") == text


def test_tool_renders_local_image_with_galaxy_prefix(tmp_path):
    tool_file = tmp_path / "tool.xml"
    tool_file.write_text(
        '<tool id="local" name="Local" version="1.0"><command>echo hello</command>'
        "<help>.. image:: $PATH_TO_IMAGES/plot.png\n    :width: 300\n</help></tool>"
    )
    tool = Tool(str(tool_file), get_tool_source(str(tool_file)), mock_app_for_tool_support())
    rendered = unescape(tool.render_help("/galaxy/static", "https://example.com/galaxy/"))
    assert (
        'src="https://example.com/galaxy/api/tools/local/help_image?tool_version=1.0&image_file=plot.png"' in rendered
    )
    assert "width: 300px" in rendered
