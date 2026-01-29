from typing import TypeAlias

from .list_jstree_response import ListJstreeResponse
from .list_uri_response import ListUriResponse

__all__ = ["RemoteFilesIndex200Response"]

RemoteFilesIndex200Response: TypeAlias = ListUriResponse | ListJstreeResponse
