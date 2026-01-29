from dataclasses import dataclass

from .badge_dict import BadgeDict
from .object_store_template_summary_description import ObjectStoreTemplateSummaryDescription
from .object_store_template_summary_name import ObjectStoreTemplateSummaryName
from .object_store_template_summary_secrets import ObjectStoreTemplateSummarySecrets
from .object_store_template_summary_variables import ObjectStoreTemplateSummaryVariables
from .type__10 import Type10

__all__ = ["ObjectStoreTemplateSummary"]


@dataclass
class ObjectStoreTemplateSummary:
    """
    ObjectStoreTemplateSummary dataclass

    Args:
        badges (List[BadgeDict]) :
        description (ObjectStoreTemplateSummaryDescription)
                                 :
        id_ (str)                : Maps from 'id'
        name (ObjectStoreTemplateSummaryName)
                                 :
        type_ (Type10)           : Maps from 'type'
        hidden (bool | None)     :
        secrets (ObjectStoreTemplateSummarySecrets | None)
                                 :
        variables (ObjectStoreTemplateSummaryVariables | None)
                                 :
        version (int | None)     :
    """

    badges: list[BadgeDict]
    description: ObjectStoreTemplateSummaryDescription
    id_: str  # Maps from 'id'
    name: ObjectStoreTemplateSummaryName
    type_: Type10  # Maps from 'type'
    hidden: bool | None = False
    secrets: ObjectStoreTemplateSummarySecrets | None = None
    variables: ObjectStoreTemplateSummaryVariables | None = None
    version: int | None = 0

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "badges": "badges",
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
            "badges": "badges",
            "description": "description",
            "hidden": "hidden",
            "id_": "id",
            "name": "name",
            "secrets": "secrets",
            "type_": "type",
            "variables": "variables",
            "version": "version",
        }
