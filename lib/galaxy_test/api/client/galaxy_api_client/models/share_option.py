from typing import TypeAlias

__all__ = ["ShareOption"]

ShareOption: TypeAlias = str | None
"""Alias for User choice for sharing resources which its contents may be restricted:
 - None: The user did not choose anything yet or no option is needed.
 - make_public: The contents of the resource will be made publicly accessible.
 - make_accessible_to_shared: This will automatically create a new `sharing role` allowing protected contents to be accessed only by the desired users.
 - no_changes: This won't change the current permissions for the contents. The user which this resource will be shared may not be able to access all its contents.
"""
