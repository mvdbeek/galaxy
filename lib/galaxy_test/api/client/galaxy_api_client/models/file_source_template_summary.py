from dataclasses import dataclass

from .file_source_template_summary_description import FileSourceTemplateSummaryDescription
from .file_source_template_summary_name import FileSourceTemplateSummaryName
from .file_source_template_summary_secrets import FileSourceTemplateSummarySecrets
from .file_source_template_summary_variables import FileSourceTemplateSummaryVariables
from .type__7 import Type7

__all__ = ["FileSourceTemplateSummary"]


@dataclass
class FileSourceTemplateSummary:
    """
    FileSourceTemplateSummary dataclass

    Args:
        description (FileSourceTemplateSummaryDescription)
                                 :
        id_ (str)                : Maps from 'id'
        name (FileSourceTemplateSummaryName)
                                 :
        type_ (Type7)            : Maps from 'type'
        hidden (bool | None)     :
        secrets (FileSourceTemplateSummarySecrets | None)
                                 :
        variables (FileSourceTemplateSummaryVariables | None)
                                 :
        version (int | None)     :
    """

    description: FileSourceTemplateSummaryDescription
    id_: str  # Maps from 'id'
    name: FileSourceTemplateSummaryName
    type_: Type7  # Maps from 'type'
    hidden: bool | None = False
    secrets: FileSourceTemplateSummarySecrets | None = None
    variables: FileSourceTemplateSummaryVariables | None = None
    version: int | None = 0

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "hidden": "hidden",
            "id": "id_",
            "name": "name",
            "secrets": "secrets",
            "type": "type_",
            "variables": "variables",
            "version": "version",
        }
        key_transform_with_dump = {
            "description": "description",
            "hidden": "hidden",
            "id_": "id",
            "name": "name",
            "secrets": "secrets",
            "type_": "type",
            "variables": "variables",
            "version": "version",
        }
