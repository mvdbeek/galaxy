import datetime
import os
import pathlib
import subprocess
from dataclasses import dataclass
from typing import (
    Any,
    List,
    Optional,
    Set,
)
from click.core import Context, Parameter
from packaging.version import Version

import click
from github import (
    Github,
    PullRequest,
)

g = Github(os.environ.get("GITHUB_AUTH"))
PROJECT_OWNER = "galaxyproject"
PROJECT_NAME = "galaxy"
REPO = f"{PROJECT_OWNER}/{PROJECT_NAME}"


class ClickVersion(click.ParamType):
    name = "pep440 version"

    def convert(self, value: Any, param: Optional[Parameter], ctx: Optional[Context]) -> Version:
        try:
            return Version(value)
        except Exception as e:
            self.fail(f"{value!r} is not a valid PEP440 version number: {str(e)}", param, ctx)


@dataclass
class Package:
    path: pathlib.Path
    current_version: str
    next_version: Optional[str] = None
    commits: Optional[Set[str]] = None
    prs: Optional[Set[PullRequest.PullRequest]] = None

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def setup_cfg(self) -> pathlib.Path:
        return self.path / "setup.cfg"

    @property
    def history_rst(self) -> pathlib.Path:
        return self.path / "HISTORY.rst"

    def __repr__(self) -> str:
        pretty_string = f"[Package: {self.name}, Current Version: {self.current_version}"
        if self.next_version:
            pretty_string = f"{pretty_string[:-1]}, Next Version: {self.next_version}"
        return pretty_string


def get_sorted_package_paths(galaxy_root: pathlib.Path) -> List[pathlib.Path]:
    root_package_path = galaxy_root.joinpath("packages")
    sorted_packages = root_package_path.joinpath("packages_by_dep_dag.txt").read_text().splitlines()
    # Check that all packages are listed in packages_by_dep_dag.txt ?
    return [root_package_path.joinpath(package) for package in sorted_packages]


def read_package(package_path: pathlib.Path) -> Package:
    setup_cfg = package_path / "setup.cfg"
    with setup_cfg.open() as content:
        for line in content:
            if line.startswith("version = "):
                version = line.strip().split("version = ")[-1]
                return Package(path=package_path, current_version=version)
    raise ValueError(f"{setup_cfg} does not contain version line")


def bump_package_version(package: Package, new_version: str):
    new_content = []
    content = package.setup_cfg.read_text().splitlines()
    for line in content:
        if line.startswith("version = "):
            line = f"version = {new_version}"
        new_content.append(line)
    package.setup_cfg.write_text("\n".join(new_content))


def get_commits_since_last_version(package: Package, last_version_tag: str):
    print(f"finding commits for {package.name}")
    package_source_paths = []
    commits = set()
    for code_dir in ["galaxy", "tests", "galaxy_test"]:
        package_code_path = package.path / code_dir
        if package_code_path.exists():
            # get all symlinks pointing to a directory
            for item in package_code_path.iterdir():
                # Check if the item is a symlink and if its target points to a directory
                if item.is_symlink() and item.resolve().is_dir():
                    package_source_paths.append(item.resolve())
    for package_source_path in package_source_paths:
        result = subprocess.run(
            [
                "git",
                "log",
                "--oneline",
                "--no-merges",
                "--pretty=format:%h",
                f"{last_version_tag}..HEAD",
                package_source_path,
            ],
            cwd=package.path,
            capture_output=True,
            text=True,
        )
        result.check_returncode()
        for line in result.stdout.splitlines():
            if line:
                commits.add(line)
    package.commits = commits


def commits_to_prs(packages: List[Package]):
    commits = set.union(*(p.commits for p in packages))
    pr_cache = {}
    commit_to_pr = {}
    for commit in commits:
        # Get the list of pull requests associated with the commit
        commit_obj = g.get_repo(REPO).get_commit(commit)
        prs = commit_obj.get_pulls()
        if not prs:
            raise Exception(f"commit {commit} has no associated PRs")
        for pr in prs:
            if pr.number not in pr_cache:
                pr_cache[pr.number] = pr
            commit_to_pr[commit] = pr_cache[pr.number]
    for package in packages:
        package.prs = set(commit_to_pr[commit] for commit in package.commits)


def write_package_history(package: Package, new_version: str):
    history = package.history_rst.read_text().splitlines()
    assert history[3] == ".. to_doc", f"{package.history_rst} has invalid structure"
    assert history[5].startswith("---"), f"{package.history_rst} has invalid structure"
    assert history[7].startswith("---"), f"{package.history_rst} has invalid structure"
    dev_version = Version(history[6])
    assert (
        dev_version.is_devrelease
    ), f"{package.history_rst} line 7 should have dev release as latest changelog entry. You have to fix this manually"
    now = datetime.datetime.now()
    history[6] = f"{new_version} ({now.year}-{now.month}-{now.day})"
    if not package.prs:
        # Skip publishing packages if no change ?
        history.insert(7, "No recorded changes since last release")
    else:
        for pr in sorted(package.prs, key=lambda pr: pr.number):
            history.insert(8, f"* {pr.title} by {pr.user.login} in {pr.html_url}")

    package.history_rst.write_text("\n".join(history))


def build_package(package: Package):
    print(f"Running make clean for package {package.name}")
    subprocess.run(["make", "clean"], cwd=package.path)
    print(f"running make dist for package {package.name}")
    subprocess.run(["make", "clean"], cwd=package.path)


def get_root_version(galaxy_root: pathlib.Path) -> str:
    version_py = galaxy_root / "lib" / "galaxy" / "version.py"
    version_py_contents = version_py.read_text().splitlines()
    assert len(version_py_contents) == 3
    major_version = version_py_contents[0].split('"')[1]
    minor_version = version_py_contents[1].split('"')[1]
    return f"{major_version}.{minor_version}"


def set_root_version(galaxy_root: pathlib.Path, new_version: Version):
    major_galaxy_release_string = f"{new_version.major}.{new_version.minor}"
    minor_galaxy_release_string = str(new_version).replace(f"{major_galaxy_release_string}.", "")
    VERSION_PY_TEMPLATE = f"""VERSION_MAJOR = "{major_galaxy_release_string}"
VERSION_MINOR = "{minor_galaxy_release_string}"
VERSION = VERSION_MAJOR + (f".{{VERSION_MINOR}}" if VERSION_MINOR else "")
"""
    version_py = galaxy_root / "lib" / "galaxy" / "version.py"
    version_py.write_text(VERSION_PY_TEMPLATE)


@click.command("Create a new point release")
@click.option("--galaxy-root", type=click.Path(exists=True, file_okay=False, resolve_path=True, path_type=pathlib.Path))
@click.option("--new-version", type=ClickVersion(), help="Specify new release version. Must be valid PEP 440 version")
@click.option("--last-commit", type=str)
@click.option("--build-packages", type=bool, is_flag=True, default=False)
@click.option("--packages", "package_subset", multiple=True, type=str, default=None)
def main(
    galaxy_root: pathlib.Path,
    new_version: Optional[Version],
    build_packages: bool,
    last_commit=Optional[str],
    package_subset=List[str],
):
    root_version = get_root_version(galaxy_root)
    print(f"Current Galaxy version is {root_version}")
    # TODO: confirmation
    if new_version:
        set_root_version(galaxy_root, new_version)
    packages = []
    for package_path in get_sorted_package_paths(galaxy_root):
        if package_subset and package_path.name not in package_subset:
            continue
        package = read_package(package_path)
        packages.append(package)
        get_commits_since_last_version(package, last_commit)
    commits_to_prs(packages)
    for package in packages:
        if new_version:
            bump_package_version(package, str(new_version))
            write_package_history(package, str(new_version))
        if build_packages:
            build_package(package)


if __name__ == "__main__":
    main()
