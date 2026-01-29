from dataclasses import dataclass

from .notification_create_data import NotificationCreateData
from .notification_recipients_request import NotificationRecipientsRequest

__all__ = ["NotificationCreateRequest"]


@dataclass
class NotificationCreateRequest:
    """
    NotificationCreateRequest dataclass

    Args:
        notification (NotificationCreateData)
                                 : Basic common fields for all notification create requests.
        recipients (NotificationRecipientsRequest)
                                 :
    """

    notification: NotificationCreateData  # Basic common fields for all notification create requests.
    recipients: NotificationRecipientsRequest

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "notification": "notification",
            "recipients": "recipients",
        }
        key_transform_with_dump = {
            "notification": "notification",
            "recipients": "recipients",
        }
