from dataclasses import dataclass

from .default_value import DefaultValue
from .description import Description
from .restrictions import Restrictions
from .suggestions import Suggestions
from .type_ import Type_
from .validators import Validators

__all__ = ["SampleSheetColumnDefinitionModel"]


@dataclass
class SampleSheetColumnDefinitionModel:
    """
    SampleSheetColumnDefinitionModel dataclass.

    Args:
        name (str)               :
        optional (bool)          :
        type_ (Type_)            : The type of content to be created in the history.
        default_value (Optional[DefaultValue])
                                 :
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        restrictions (Optional[Restrictions])
                                 :
        suggestions (Optional[Suggestions])
                                 :
        validators (Optional[Validators])
                                 :
    """

    name: str
    optional: bool
    type_: Type_  # The type of content to be created in the history.
    default_value: DefaultValue | None = None
    description: Description | None = ""  # Detailed text description for this Quota.
    restrictions: Restrictions | None = None
    suggestions: Suggestions | None = None
    validators: Validators | None = None
