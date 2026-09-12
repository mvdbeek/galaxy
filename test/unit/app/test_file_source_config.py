import json

import pytest

from galaxy import config
from galaxy.files import ConfiguredFileSources
from galaxy.files.models import FileSourcePluginsConfig
from galaxy.files.uris import stream_url_to_file


@pytest.mark.parametrize("allowlist", ["127.0.0.1", "127.0.0.0/24"])
def test_file_source_allowlist_from_app_config(tmp_path, httpserver, allowlist):
    appconfig = config.GalaxyAppConfiguration(
        override_tempdir=False,
        fetch_url_allowlist=allowlist,
        file_sources_config_file=str(tmp_path / "absent.yml"),
        file_sources=[],
    )
    sources = ConfiguredFileSources(FileSourcePluginsConfig.from_app_config(appconfig), load_stock_plugins=True)
    serialized = json.loads(json.dumps(sources.to_dict(for_serialization=True)))
    recovered = ConfiguredFileSources.from_dict(serialized)
    httpserver.expect_request("/data").respond_with_data("allowed content")
    for configured in (sources, recovered):
        target = tmp_path / "download"
        stream_url_to_file(
            httpserver.url_for("/data").replace("localhost", "127.0.0.1"),
            file_sources=configured,
            target_path=str(target),
        )
        assert target.read_text() == "allowed content"
