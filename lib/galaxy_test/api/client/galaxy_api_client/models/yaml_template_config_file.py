from dataclasses import dataclass

from .yaml_template_config_file_filename import YamlTemplateConfigFileFilename
from .yaml_template_config_file_name import YamlTemplateConfigFileName

__all__ = ["YamlTemplateConfigFile"]


@dataclass
class YamlTemplateConfigFile:
    """
    YamlTemplateConfigFile dataclass

    Args:
        content (str)            :
        eval_engine (str | None) :
        filename (YamlTemplateConfigFileFilename | None)
                                 :
        name (YamlTemplateConfigFileName | None)
                                 :
    """

    content: str
    eval_engine: str | None = "ecmascript"
    filename: YamlTemplateConfigFileFilename | None = None
    name: YamlTemplateConfigFileName | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content": "content",
            "eval_engine": "eval_engine",
            "filename": "filename",
            "name": "name",
        }
        key_transform_with_dump = {
            "content": "content",
            "eval_engine": "eval_engine",
            "filename": "filename",
            "name": "name",
        }
