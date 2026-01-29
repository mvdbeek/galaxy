from typing import TypeAlias

from .yaml_template_config_file import YamlTemplateConfigFile

__all__ = ["Configfiles"]

Configfiles: TypeAlias = list[YamlTemplateConfigFile] | None
"""Alias for A list of config files for this tool."""
