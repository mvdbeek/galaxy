from dataclasses import dataclass

from .collection_type import CollectionType
from .default import Default
from .label import Label
from .optional_bool import OptionalBool
from .position import Position
from .restrict_on_connections import RestrictOnConnections
from .restrictions import Restrictions
from .suggestions import Suggestions

__all__ = ["AddInputAction"]


@dataclass
class AddInputAction:
    """
    AddInputAction dataclass.

    Args:
        action_type (str)        :
        type_ (str)              :
        collection_type (Optional[CollectionType])
                                 : The type of the collection, can be `list`, `paired`, or
                                   define subcollections using `:` as separator like
                                   `list:paired` or `list:list`.
        default (Optional[Default])
                                 : Whether or not this is a default quota. Valid values are
                                   ``no``, ``unregistered``, ``registered``. Calling this
                                   method with ``default="no"`` on a non-default quota will
                                   throw an error. Not passing this parameter is equivalent
                                   to passing ``no``.
        label (Optional[Label])  : Label of the input.
        optional (Optional[OptionalBool])
                                 :
        position (Optional[Position])
                                 : The location of the step in the Galaxy workflow editor.
        restrict_on_connections (Optional[RestrictOnConnections])
                                 :
        restrictions (Optional[Restrictions])
                                 :
        suggestions (Optional[Suggestions])
                                 :
    """

    action_type: str
    type_: str
    collection_type: CollectionType | None = (
        None  # The type of the collection, can be `list`, `paired`, or define subcollections using `:` as separator like `list:paired` or `list:list`.
    )
    default: Default | None = (
        None  # Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. Calling this method with ``default="no"`` on a non-default quota will throw an error. Not passing this parameter is equivalent to passing ``no``.
    )
    label: Label | None = None  # Label of the input.
    optional: OptionalBool | None = False
    position: Position | None = None  # The location of the step in the Galaxy workflow editor.
    restrict_on_connections: RestrictOnConnections | None = None
    restrictions: Restrictions | None = None
    suggestions: Suggestions | None = None
