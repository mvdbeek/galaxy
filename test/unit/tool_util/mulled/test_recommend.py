from typing import Tuple

import pytest
from requests import (
    ConnectionError as RequestsConnectionError,
    HTTPError,
)

from galaxy.tool_util.deps.mulled import (
    recommend,
    util,
)
from galaxy.tool_util.deps.mulled.recommend import (
    ContainerRecommendation,
    MatchQuality,
    PackageSpec,
    recommend_container,
    RecommendationSource,
)
from galaxy.tool_util.deps.mulled.util import (
    build_target,
    v2_image_name,
)
from ..util import external_dependency_management


def _version_hash(*name_versions: Tuple[str, str]) -> str:
    """The mulled-v2 version-hash for a set of (name, version) pairs.

    Computes a *real* hash (not mocked) via the production hashing helpers, so it
    can be seeded into a faked tag list -- the test then exercises the real
    version-matching logic with only the network faked.
    """
    targets = [build_target(name, version=version) for name, version in name_versions]
    return v2_image_name(targets).split(":")[1]


def _package_repo(*names: str) -> str:
    """The mulled-v2 repo name (package names only) for a set of packages."""
    return v2_image_name([build_target(n) for n in names]).split(":")[0]


def _patch_tags(monkeypatch, fake) -> None:
    """Fake mulled_tags_for everywhere the recommender reaches it.

    The recommender calls it directly (candidate-version lookups, the partial-repo
    fetch) and indirectly via the shared ``find_remote_mulled_name`` in util, so both
    name bindings must be patched.
    """
    monkeypatch.setattr(recommend, "mulled_tags_for", fake)
    monkeypatch.setattr(util, "mulled_tags_for", fake)


@pytest.fixture(autouse=True)
def _clear_cache():
    # recommend_container memoizes in a module-level cache; clear it around every
    # test so results don't leak between cases.
    recommend._cache.clear()
    yield
    recommend._cache.clear()


# --- single-package recommend_container (mocked network) --------------------


def test_single_exact_version(monkeypatch):
    _patch_tags(monkeypatch, lambda *a, **k: ["1.17--h00cdaf9_0", "1.16--h0_0"])
    rec = recommend_container([PackageSpec("samtools", "1.17")])
    assert rec.image == "quay.io/biocontainers/samtools:1.17--h00cdaf9_0"
    assert rec.source == RecommendationSource.QUAY_SINGLE
    assert rec.match_quality == MatchQuality.EXACT_VERSION
    assert not rec.multi_package


def test_single_name_only_when_version_missing(monkeypatch):
    _patch_tags(monkeypatch, lambda *a, **k: ["1.17--h0_0"])
    rec = recommend_container([PackageSpec("samtools", "9.9")])
    assert rec.image == "quay.io/biocontainers/samtools:1.17--h0_0"
    assert rec.match_quality == MatchQuality.NAME_ONLY
    assert rec.notes  # explanatory note present


def test_single_no_version(monkeypatch):
    _patch_tags(monkeypatch, lambda *a, **k: ["1.17--h0_0", "1.16--h0_0"])
    rec = recommend_container([PackageSpec("samtools")])
    assert rec.image == "quay.io/biocontainers/samtools:1.17--h0_0"
    assert rec.match_quality == MatchQuality.NAME_ONLY


def test_single_uppercase_name_normalized(monkeypatch):
    seen = {}

    def fake_tags(namespace, image, **k):
        seen["image"] = image
        return ["1.17--h0_0"]

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("SamTools", "1.17")])
    assert seen["image"] == "samtools"
    assert rec.image == "quay.io/biocontainers/samtools:1.17--h0_0"


def test_single_repo_absent_404(monkeypatch):
    def fake_tags(*a, **k):
        raise HTTPError("404")

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("nopackage", "1.0")])
    assert rec.image is None
    assert rec.source == RecommendationSource.NONE
    assert rec.match_quality == MatchQuality.NOT_FOUND


def test_single_network_error_is_lookup_failed(monkeypatch):
    def fake_tags(*a, **k):
        raise RequestsConnectionError("boom")

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("samtools", "1.0")])
    assert rec.image is None
    assert rec.source == RecommendationSource.NONE
    assert any("lookup failed" in n for n in rec.notes)


# --- multi-package recommend_container (mocked network) ---------------------


def test_multi_exact_version(monkeypatch):
    repo = _package_repo("bwa", "samtools")
    vh = _version_hash(("bwa", "0.7.17"), ("samtools", "1.17"))

    def fake_tags(namespace, image, **k):
        return [f"{vh}-1", f"{vh}-0", "other-0"] if image == repo else []

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("bwa", "0.7.17"), PackageSpec("samtools", "1.17")])
    assert rec.image == f"quay.io/biocontainers/{repo}:{vh}-1"
    assert rec.source == RecommendationSource.QUAY_MULLED_V2
    assert rec.match_quality == MatchQuality.EXACT_VERSION
    assert rec.multi_package


def test_multi_exact_combination_not_built_name_only(monkeypatch):
    repo = _package_repo("bwa", "samtools")

    def fake_tags(namespace, image, **k):
        return ["unrelatedhash-0"] if image == repo else []

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("bwa", "0.7.17"), PackageSpec("samtools", "1.17")])
    assert rec.image == f"quay.io/biocontainers/{repo}:unrelatedhash-0"
    assert rec.match_quality == MatchQuality.NAME_ONLY
    assert any("exact version combination not built" in n for n in rec.notes)


def test_multi_not_present(monkeypatch):
    _patch_tags(monkeypatch, lambda *a, **k: [])
    rec = recommend_container([PackageSpec("bwa", "0.7.17"), PackageSpec("samtools", "1.17")])
    assert rec.image is None
    assert rec.source == RecommendationSource.NONE


def test_multi_network_error_is_lookup_failed(monkeypatch):
    def fake_tags(*a, **k):
        raise RequestsConnectionError("boom")

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("bwa", "0.7.17"), PackageSpec("samtools", "1.17")])
    assert rec.image is None
    assert any("lookup failed" in n for n in rec.notes)


def test_multi_partial_versions_dropped_when_resolution_off(monkeypatch):
    repo = _package_repo("bwa", "samtools")

    def fake_tags(namespace, image, **k):
        return ["somehash-0"] if image == repo else []

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("bwa", "0.7.17"), PackageSpec("samtools")], resolve_versions=False)
    assert rec.match_quality == MatchQuality.NAME_ONLY
    assert rec.image == f"quay.io/biocontainers/{repo}:somehash-0"
    assert any("not all packages were versioned" in n for n in rec.notes)


def test_multi_resolve_finds_built_combination(monkeypatch):
    """An unpinned package's version is resolved so a pinned+unpinned set matches exactly."""
    repo = _package_repo("bwa", "samtools")
    target_hash = _version_hash(("bwa", "0.7.17"), ("samtools", "1.17"))

    def fake_tags(namespace, image, **k):
        if image == repo:
            return [f"{target_hash}-0", "olderhash-0"]  # tags actually built for the repo
        if image == "bwa":
            return ["0.7.18--h0_0", "0.7.17--h0_0", "0.7.16--h0_0"]  # candidate versions, newest first
        return []

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("samtools", "1.17"), PackageSpec("bwa")])
    assert rec.match_quality == MatchQuality.EXACT_VERSION
    assert rec.image == f"quay.io/biocontainers/{repo}:{target_hash}-0"
    assert any("resolved version(s): bwa=0.7.17" in n for n in rec.notes)


def test_multi_resolve_no_built_combination_falls_back(monkeypatch):
    """When no tried combination is built, fall back to a name-only newest tag."""
    repo = _package_repo("bwa", "samtools")

    def fake_tags(namespace, image, **k):
        if image == repo:
            return ["unbuiltcombohash-0"]  # repo exists but no candidate combo hashes to this
        if image == "bwa":
            return ["0.7.18--h0_0", "0.7.17--h0_0"]
        return []

    _patch_tags(monkeypatch, fake_tags)
    rec = recommend_container([PackageSpec("samtools", "1.17"), PackageSpec("bwa")])
    assert rec.match_quality == MatchQuality.NAME_ONLY
    assert rec.image == f"quay.io/biocontainers/{repo}:unbuiltcombohash-0"
    assert any("could not resolve" in n for n in rec.notes)


def test_empty_packages():
    rec = recommend_container([])
    assert rec.image is None
    assert rec.source == RecommendationSource.NONE


def test_cache_avoids_second_lookup(monkeypatch):
    calls = {"n": 0}

    def fake_tags(*a, **k):
        calls["n"] += 1
        return ["1.17--h0_0"]

    _patch_tags(monkeypatch, fake_tags)
    first = recommend_container([PackageSpec("samtools", "1.17")])
    second = recommend_container([PackageSpec("samtools", "1.17")])
    assert calls["n"] == 1
    assert first == second


# --- live smoke tests (hit quay.io; skipped without the marker) -------------


@external_dependency_management
def test_live_single_samtools():
    rec = recommend_container([PackageSpec("samtools", "1.17")], use_cache=False)
    assert rec.image is not None
    assert rec.image.startswith("quay.io/biocontainers/samtools:1.17")
    assert rec.match_quality == MatchQuality.EXACT_VERSION


@external_dependency_management
def test_live_multi_bamtools_samtools():
    rec = recommend_container([PackageSpec("bamtools", "2.4.0"), PackageSpec("samtools", "1.3.1")], use_cache=False)
    assert rec.image is not None
    assert rec.image.startswith("quay.io/biocontainers/mulled-v2-")
    assert isinstance(rec, ContainerRecommendation)


@external_dependency_management
def test_live_multi_resolves_unpinned_versions():
    """Two unpinned packages resolve to a real, built mulled-v2 image."""
    rec = recommend_container([PackageSpec("bwa"), PackageSpec("samtools")], use_cache=False)
    assert rec.image is not None
    assert rec.match_quality == MatchQuality.EXACT_VERSION
    assert any("resolved version(s)" in n for n in rec.notes)
