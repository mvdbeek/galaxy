from typing import TypeAlias

from .list_jstree_response import ListJstreeResponse
from .list_uri_response import ListUriResponse

__all__ = ["RemoteFilesIndex200Response2"]

RemoteFilesIndex200Response2: TypeAlias = ListUriResponse | ListJstreeResponse
