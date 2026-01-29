from datetime import datetime
from typing import TypeAlias

__all__ = ["NotificationBroadcastUpdateRequestPublicationTime"]

NotificationBroadcastUpdateRequestPublicationTime: TypeAlias = datetime | None
"""Alias for The time when the notification should be published. Notifications can be created and then scheduled to be published at a later time."""
