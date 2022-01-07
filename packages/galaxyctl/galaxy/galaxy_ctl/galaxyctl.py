import click



def setup_directories():
    DIRECTORIES = ['config', 'log', 'data']


@click.group()
def main():
    pass


@main.command(help="Control Galaxy")
def galaxy():
    print('galaxy')


@main.group(help="Configure your Galaxy installation")
def setup():
    print('setup')


@main.group(help="Maintainance commands for your Galaxy instance")
def maintainance():
    pass

@setup.command(help="Initialize a new galaxyctl configuration file")
def init_config():
    print('init')


@setup.command(help="Edit galaxyctl configuration file")
def edit_config():
    print('edit')


@setup.command(help="Initialize galaxy data directory")
@click.argument('galaxy')
def init_galaxy_data_dir():
    print('init galaxy root')