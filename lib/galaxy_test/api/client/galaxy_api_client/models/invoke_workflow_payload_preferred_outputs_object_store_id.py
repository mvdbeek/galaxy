from typing import TypeAlias

__all__ = ["InvokeWorkflowPayloadPreferredOutputsObjectStoreId"]

InvokeWorkflowPayloadPreferredOutputsObjectStoreId: TypeAlias = str | None
"""Alias for The ID of the object store that should be used to store the marked output datasets of this workflow - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences."""
