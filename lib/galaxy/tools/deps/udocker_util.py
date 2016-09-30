"""Utilities for building up Docker commands...

...using common defaults and configuration mechanisms.
"""
import os
from .commands import argv_to_str, shell_quote
import docker_util

DEFAULT_DOCKER_COMMAND = "udocker.py"
DEFAULT_SUDO = False
DEFAULT_SUDO_COMMAND = None
DEFAULT_HOST = None
DEFAULT_VOLUME_MOUNT_TYPE = ""
DEFAULT_WORKING_DIRECTORY = None
DEFAULT_NET = None
DEFAULT_MEMORY = None
DEFAULT_VOLUMES_FROM = None
DEFAULT_AUTO_REMOVE = True
DEFAULT_SET_USER = "$UID"
DEFAULT_RUN_EXTRA_ARGUMENTS = None


class UDockerVolume(object):

    def __init__(self, path, to_path=None, how=DEFAULT_VOLUME_MOUNT_TYPE):
        self.from_path = path
        self.to_path = to_path or path
        if not UDockerVolume.__valid_how(how):
            raise ValueError("Invalid way to specify docker volume %s" % how)
        self.how = how

    @staticmethod
    def volumes_from_str(volumes_as_str):
        if not volumes_as_str:
            return []
        volume_strs = [v.strip() for v in volumes_as_str.split(",")]
        return map(UDockerVolume.volume_from_str, volume_strs)

    @staticmethod
    def volume_from_str(as_str):
        if not as_str:
            raise ValueError("Failed to parse docker volume from %s" % as_str)
        parts = as_str.split(":", 2)
        kwds = dict(path=parts[0])
        if len(parts) == 2:
            if UDockerVolume.__valid_how(parts[1]):
                kwds["how"] = parts[1]
            else:
                kwds["to_path"] = parts[1]
        elif len(parts) == 3:
            kwds["to_path"] = parts[1]
            kwds["how"] = parts[2]
        return UDockerVolume(**kwds)

    @staticmethod
    def __valid_how(how):
        return how in ["ro", "rw", ""]

    def __str__(self):
        return ":".join([self.from_path, self.to_path])

def kill_command(
    container,
    signal=None,
    **kwds
):
    raise Exception('Not implemented')


def logs_command(
    container,
    **kwds
):
    raise Exception('Not implemented')


def build_command(
    image,
    docker_build_path,
    **kwds
):
    raise Exception('Not implemented')


def build_save_image_command(
    image,
    destination,
    **kwds
):
    raise Exception('Not implemented')


def build_pull_command(
    tag,
    **kwds
):
    return command_list("pull", [tag], **kwds)


def build_docker_cache_command(
    image,
    **kwds
):
    inspect_image_command = command_shell("inspect", [image], **kwds)
    pull_image_command = command_shell("pull", [image], **kwds)
    cache_command = "%s > /dev/null 2>&1\n[ $? -ne 0 ] && %s > /dev/null 2>&1\n" % (inspect_image_command, pull_image_command)
    return cache_command


def build_docker_images_command(truncate=True, **kwds):
    #args = ["--no-trunc"] if not truncate else[]
    #return command_shell("images", args, **kwds)
    raise Exception('Not implemented')


def build_docker_load_command(**kwds):
    return command_shell("load", [])


def build_docker_run_command(
    container_command,
    image,
    interactive=False,
    terminal=False,
    tag=None,
    volumes=[],
    volumes_from=DEFAULT_VOLUMES_FROM,
    memory=DEFAULT_MEMORY,
    env_directives=[],
    working_directory=DEFAULT_WORKING_DIRECTORY,
    name=None,
    net=DEFAULT_NET,
    run_extra_arguments=DEFAULT_RUN_EXTRA_ARGUMENTS,
    docker_cmd=DEFAULT_DOCKER_COMMAND,
    sudo=DEFAULT_SUDO,
    sudo_cmd=DEFAULT_SUDO_COMMAND,
    auto_rm=DEFAULT_AUTO_REMOVE,
    set_user=DEFAULT_SET_USER,
    host=DEFAULT_HOST,
):
    command_parts = _docker_prefix(
        docker_cmd='udocker.py',
        sudo=None,
        sudo_cmd=None,
        host=None
    )
    command_parts.append("run")
    for env_directive in env_directives:
        command_parts.extend(["-e", env_directive])
    for volume in volumes:
        command_parts.extend(["--volume", shell_quote(str(volume))])
    if working_directory:
        command_parts.extend(["--workdir=%s" %shell_quote(working_directory)])
    if auto_rm:
        command_parts.append("--rm")
    if run_extra_arguments:
        command_parts.append(run_extra_arguments)
    full_image = image
    if tag:
        full_image = "%s:%s" % (full_image, tag)
    command_parts.append(shell_quote(full_image))
    command_parts.append(container_command)
    return " ".join(command_parts)


def command_list(command, command_args=[], **kwds):
    """Return Docker command as an argv list."""
    command_parts = _docker_prefix(**kwds)
    command_parts.append(command)
    command_parts.extend(command_args)
    return command_parts


def command_shell(command, command_args=[], **kwds):
    """Return Docker command as a string for a shell."""
    return argv_to_str(command_list(command, command_args, **kwds))


def _docker_prefix(
    docker_cmd=DEFAULT_DOCKER_COMMAND,
    sudo=DEFAULT_SUDO,
    sudo_cmd=DEFAULT_SUDO_COMMAND,
    host=DEFAULT_HOST,
    **kwds
):
    """Prefix to issue a docker command."""
    command_parts = []
    command_parts.append(docker_cmd)
    return command_parts
