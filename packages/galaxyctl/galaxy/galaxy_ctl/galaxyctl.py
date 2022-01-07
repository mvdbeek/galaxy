import yaml
import os
import subprocess
from importlib import resources
from pathlib import Path

import click

CONFIG_DIR = Path(os.path.expanduser('~')) / '.config'
if 'XDG_CONFIG_HOME' in os.environ:
    CONFIG_DIR = Path(os.environ['XDG_CONFIG_HOME'])
DEFAULT_CONFIG_FILE = CONFIG_DIR / '.galaxy_ctl.yml'


class Settings:

    def __init__(self, config_file):
        self.config_file = config_file

class DataDirExistsException(click.ClickException):
    pass


def setup_directories(base_dir):
    config_dir = base_dir / 'config'
    data_dir = base_dir / 'data'
    managed_config_dir = base_dir / 'data' / 'config'
    log_dir = base_dir / 'log'
    base_dir = Path(base_dir)
    if not base_dir.exists():
        base_dir.mkdir()
    for directory in (config_dir, data_dir, managed_config_dir, log_dir):
        directory = base_dir / directory
        if directory.exists():
            raise DataDirExistsException(f"{str(directory)} exists, cannot setup directories")
        directory.mkdir()
    init_sample_config_files(config_dir=config_dir, managed_config_dir=managed_config_dir, data_dir=data_dir)
    init_supervisor(config_dir)


def init_sample_config_files(config_dir, managed_config_dir, data_dir):
    galaxy_config_sample_path = resources.files('galaxy.config') / 'sample/galaxy.yml.sample'
    galaxy_config = galaxy_config_sample_path.read_text()
    # Should probably just write out a clean yaml file ?
    galaxy_config = galaxy_config.replace("  #config_dir: null", f"  config_dir: {config_dir}")
    galaxy_config = galaxy_config.replace("  #managed_config_dir: null", f"  managed_config_dir: {managed_config_dir}")
    galaxy_config = galaxy_config.replace("  #data_dir: null", f"  data_dir: {data_dir}")
    (config_dir / 'galaxy.yml').write_text(galaxy_config)


def init_supervisor(config_dir):
    config_files = resources.files('galaxy.config')
    config_files


@click.group()
@click.option('--config_file', type=click.Path(path_type=Path), default=DEFAULT_CONFIG_FILE)
@click.pass_context
def main(ctx, config_file):
    ctx.obj = Settings(config_file)


@main.group(help="Control Galaxy")
def galaxy():
    print('galaxy')


@galaxy.command("start")
def galaxy_start():
    print('start')


@galaxy.command('status')
def galaxy_status():
    # How do I find supervisor socket ?
    # Specify in config file ?
    subprocess.run("supervisorctl status")


@main.group(help="Configure your Galaxy installation")
def setup():
    print('setup')


@main.group(help="Maintainance commands for your Galaxy instance")
def maintainance():
    pass


@setup.command(help="Edit galaxyctl configuration file")
def edit_config():
    print('edit')


@setup.command(help="Initialize galaxy directory")
@click.pass_context
@click.argument('data_dir', type=click.Path(file_okay=False, path_type=Path))
def init_galaxy_data_dir(ctx, data_dir):
    click.echo(f"Creating data directory at {data_dir}")
    setup_directories(data_dir)
    with open(ctx.parent.obj.config_file, 'w') as out:
        out.write(yaml.safe_dump({'galaxy_directory': str(data_dir)}))