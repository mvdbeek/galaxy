"""
Generate prebuilt Mercurial clone bundles for all Tool Shed repositories.
Run this script from the root folder, example:

$ python scripts/tool_shed/generate_clone_bundles.py -c config/tool_shed.yml

When clone_bundles_enabled is set to true in the Tool Shed config,
bundles are regenerated automatically after each commit. This script
is useful for:
  * Initial setup: generating bundles for all existing repositories
  * Catch-up: regenerating bundles that may be stale or missing
  * Forced regeneration: using --force to rebuild all bundles

This script expects the Tool Shed's runtime virtualenv to be active.
"""

import argparse
import logging
import os
import sys

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "lib")))

from sqlalchemy import (
    false,
    select,
)

from galaxy.util import directory_hash_id
from galaxy.util.script import (
    app_properties_from_args,
    populate_config_args,
)
from tool_shed.util.clone_bundles import (
    BUNDLE_FILENAME,
    enable_clonebundles_extension,
    generate_bundle,
    get_bundle_dir_for_repo,
    get_bundle_url_for_repo,
    update_manifest,
)
from tool_shed.util.hgweb_config import hgweb_config_manager
from tool_shed.webapp import config as ts_config
from tool_shed.webapp import model
import tool_shed.webapp.model.mapping as ts_mapping

log = logging.getLogger()
log.addHandler(logging.StreamHandler(sys.stdout))


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate prebuilt Mercurial clone bundles for Tool Shed repositories."
    )
    populate_config_args(parser)
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="Print extra info")
    parser.add_argument(
        "--repository",
        default=None,
        help="Generate bundle for a specific repository only (format: owner/name)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        default=False,
        help="Regenerate bundles even if they already exist",
    )
    args = parser.parse_args()
    app_properties = app_properties_from_args(args)
    config = ts_config.ToolShedAppConfiguration(**app_properties)
    args.dburi = config.database_connection
    args.file_path = config.file_path
    args.hgweb_config_dir = config.hgweb_config_dir
    args.hgweb_repo_prefix = config.hgweb_repo_prefix
    args.clone_bundles_dir = config.clone_bundles_dir
    args.clone_bundles_external_url = config.clone_bundles_external_url
    args.config = config
    if args.debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    return args


def main():
    args = parse_arguments()
    clone_bundles_dir = args.clone_bundles_dir
    os.makedirs(clone_bundles_dir, exist_ok=True)

    mapping = ts_mapping.init(args.dburi, engine_options={}, create_tables=False)
    sa_session = mapping.session

    hgwcm = hgweb_config_manager
    hgwcm.hgweb_config_dir = args.hgweb_config_dir
    hgwcm.hgweb_repo_prefix = args.hgweb_repo_prefix

    Repository = model.Repository
    stmt = (
        select(Repository)
        .where(Repository.deleted == false())
        .where(Repository.deprecated == false())
    )
    if args.repository:
        owner, name = args.repository.split("/")
        stmt = stmt.where(Repository.name == name)
        # Filter by owner requires a join
        stmt = stmt.join(model.User).where(model.User.username == owner)

    repositories = sa_session.scalars(stmt).all()
    total = len(repositories)
    generated = 0
    skipped = 0
    errors = 0

    log.info("Found %d repositories to process", total)

    for i, repository in enumerate(repositories, 1):
        owner = repository.user.username
        repo_name = repository.name
        log.info("[%d/%d] Processing %s/%s", i, total, owner, repo_name)

        try:
            entry = hgwcm.get_entry(os.path.join(args.hgweb_repo_prefix, owner, repo_name))
        except Exception:
            log.warning("  Could not find hgweb entry for %s/%s, skipping", owner, repo_name)
            skipped += 1
            continue

        repo_path = os.path.join(args.hgweb_config_dir, entry)
        if not os.path.exists(repo_path):
            log.warning("  Repository path %s does not exist, skipping", repo_path)
            skipped += 1
            continue

        bundle_dir = get_bundle_dir_for_repo(clone_bundles_dir, repository.id)
        bundle_path = os.path.join(bundle_dir, BUNDLE_FILENAME)

        if not args.force and os.path.exists(bundle_path):
            log.debug("  Bundle already exists, skipping (use --force to regenerate)")
            skipped += 1
            continue

        try:
            enable_clonebundles_extension(repo_path)
            result = generate_bundle(repo_path, bundle_dir)
            if result:
                if args.clone_bundles_external_url:
                    base_url = args.clone_bundles_external_url.rstrip("/")
                    hash_dir = os.path.join(*directory_hash_id(repository.id))
                    bundle_url = f"{base_url}/{hash_dir}/repo_{repository.id}/{BUNDLE_FILENAME}"
                else:
                    bundle_url = f"/repos/{owner}/{repo_name}/clone_bundle"
                update_manifest(repo_path, bundle_url)
                generated += 1
                log.info("  Generated bundle (%d bytes)", os.path.getsize(result))
            else:
                update_manifest(repo_path, "")
                skipped += 1
                log.info("  Empty repository, no bundle generated")
        except Exception:
            errors += 1
            log.exception("  Error generating bundle for %s/%s", owner, repo_name)

    log.info("Done. Generated: %d, Skipped: %d, Errors: %d", generated, skipped, errors)


if __name__ == "__main__":
    main()
