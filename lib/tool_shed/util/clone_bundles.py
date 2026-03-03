import configparser
import logging
import os
import subprocess
from typing import TYPE_CHECKING

from galaxy.util import (
    directory_hash_id,
    unicodify,
)

if TYPE_CHECKING:
    from tool_shed.structured_app import ToolShedApp
    from tool_shed.webapp.model import Repository

log = logging.getLogger(__name__)

BUNDLE_FILENAME = "bundle.hg"
BUNDLE_TYPE = "gzip-v2"


def get_bundle_dir_for_repo(clone_bundles_dir: str, repository_id: int) -> str:
    hash_dir = os.path.join(*directory_hash_id(repository_id))
    return os.path.join(clone_bundles_dir, hash_dir, f"repo_{repository_id}")


def get_bundle_url_for_repo(
    app: "ToolShedApp",
    repository: "Repository",
) -> str:
    if app.config.clone_bundles_external_url:
        base_url = app.config.clone_bundles_external_url.rstrip("/")
        hash_dir = os.path.join(*directory_hash_id(repository.id))
        return f"{base_url}/{hash_dir}/repo_{repository.id}/{BUNDLE_FILENAME}"
    else:
        owner = repository.user.username
        name = repository.name
        return f"/repos/{owner}/{name}/clone_bundle"


def generate_bundle(repo_path: str, bundle_dir: str) -> str:
    os.makedirs(bundle_dir, exist_ok=True)
    bundle_path = os.path.join(bundle_dir, BUNDLE_FILENAME)
    tmp_bundle_path = bundle_path + ".tmp"
    cmd = [
        "hg", "bundle",
        "--all",
        "--type", BUNDLE_TYPE,
        tmp_bundle_path,
    ]
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, cwd=repo_path, stdin=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        output = unicodify(e.output)
        if "no changesets found" in output:
            # Empty repository, nothing to bundle
            if os.path.exists(tmp_bundle_path):
                os.remove(tmp_bundle_path)
            if os.path.exists(bundle_path):
                os.remove(bundle_path)
            return ""
        raise Exception(f"Error generating bundle for {repo_path}: {output}")
    # Atomic rename to avoid serving partial files
    os.replace(tmp_bundle_path, bundle_path)
    log.debug("Generated clone bundle at %s", bundle_path)
    return bundle_path


def update_manifest(repo_path: str, bundle_url: str) -> None:
    manifest_path = os.path.join(repo_path, ".hg", "clonebundles.manifest")
    if not bundle_url:
        # No bundle available (empty repo), remove manifest if it exists
        if os.path.exists(manifest_path):
            os.remove(manifest_path)
        return
    manifest_line = f"{bundle_url} BUNDLESPEC={BUNDLE_TYPE}\n"
    with open(manifest_path, "w") as f:
        f.write(manifest_line)


def enable_clonebundles_extension(repo_path: str) -> None:
    hgrc_path = os.path.join(repo_path, ".hg", "hgrc")
    if not os.path.exists(hgrc_path):
        return
    config = configparser.ConfigParser()
    config.read(hgrc_path)
    if not config.has_section("extensions"):
        config.add_section("extensions")
    if config.has_option("extensions", "clonebundles"):
        return
    config.set("extensions", "clonebundles", "")
    with open(hgrc_path, "w") as f:
        config.write(f)


def regenerate_bundle(app: "ToolShedApp", repository: "Repository") -> None:
    if not app.config.clone_bundles_enabled:
        return
    try:
        repo_path = repository.repo_path(app)
        bundle_dir = get_bundle_dir_for_repo(app.config.clone_bundles_dir, repository.id)
        bundle_url = get_bundle_url_for_repo(app, repository)
        enable_clonebundles_extension(repo_path)
        bundle_path = generate_bundle(repo_path, bundle_dir)
        if bundle_path:
            update_manifest(repo_path, bundle_url)
        else:
            update_manifest(repo_path, "")
        log.info("Regenerated clone bundle for repository %s/%s", repository.user.username, repository.name)
    except Exception:
        log.exception("Failed to regenerate clone bundle for repository %s", repository.name)
