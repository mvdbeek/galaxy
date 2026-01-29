from dataclasses import dataclass

from .link import Link

__all__ = ["DisplayApplication"]


@dataclass
class DisplayApplication:
    """
    DisplayApplication dataclass

    Args:
        filename (str)           : Maps from 'filename_'
        id_ (str)                : Maps from 'id'
        links (List[Link])       :
        name (str)               :
        version (str)            :
    """

    filename: str  # Maps from 'filename_'
    id_: str  # Maps from 'id'
    links: list[Link]
    name: str
    version: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "filename_": "filename",
            "id": "id_",
            "links": "links",
            "name": "name",
            "version": "version",
        }
        key_transform_with_dump = {
            "filename": "filename_",
            "id_": "id",
            "links": "links",
            "name": "name",
            "version": "version",
        }
