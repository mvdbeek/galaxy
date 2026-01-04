from dataclasses import dataclass

from .contents import Contents
from .drs_uri import DrsUri
from .id_ import Id_

__all__ = ["ContentsObject2"]


@dataclass
class ContentsObject2:
    """
    ContentsObject2 dataclass.

    Args:
        name (str)               : A name declared by the bundle author that must be used
                                   when materialising this object, overriding any name
                                   directly associated with the object itself. The name must
                                   be unique within the containing bundle. This string is
                                   made up of uppercase and lowercase letters, decimal
                                   digits, hyphen, period, and underscore [A-Za-z0-9.-_].
                                   See http://pubs.opengroup.org/onlinepubs/9699919799/based
                                   efs/V1_chap03.html#tag_03_282[portable filenames].
        contents (Optional[Contents])
                                 : The items matching the search query. Only the items
                                   fitting in the current page limit will be returned.
        drs_uri (Optional[DrsUri]): A list of full DRS identifier URI paths that may be used
                                    to obtain the object. These URIs may be external to this
                                    DRS instance.
        id_ (Optional[Id_])      : The encoded ID of the dataset/dataset collection.
    """

    name: str  # A name declared by the bundle author that must be used when materialising this object, overriding any name directly associated with the object itself. The name must be unique within the containing bundle. This string is made up of uppercase and lowercase letters, decimal digits, hyphen, period, and underscore [A-Za-z0-9.-_]. See http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_282[portable filenames].
    contents: Contents | None = (
        None  # The items matching the search query. Only the items fitting in the current page limit will be returned.
    )
    drs_uri: DrsUri | None = (
        None  # A list of full DRS identifier URI paths that may be used to obtain the object. These URIs may be external to this DRS instance.
    )
    id_: Id_ | None = None  # The encoded ID of the dataset/dataset collection.
