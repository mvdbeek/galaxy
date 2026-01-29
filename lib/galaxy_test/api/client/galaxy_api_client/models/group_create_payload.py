from dataclasses import dataclass, field

__all__ = ["GroupCreatePayload"]


@dataclass
class GroupCreatePayload:
    """
    Payload schema for creating a group.

    Args:
        name (str)               :
        role_ids (List[str] | None)
                                 :
        user_ids (List[str] | None)
                                 :
    """

    name: str
    role_ids: list[str] | None = field(default_factory=list)
    user_ids: list[str] | None = field(default_factory=list)

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "role_ids": "role_ids",
            "user_ids": "user_ids",
        }
        key_transform_with_dump = {
            "name": "name",
            "role_ids": "role_ids",
            "user_ids": "user_ids",
        }
