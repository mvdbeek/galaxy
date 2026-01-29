from typing import TypeAlias

from .template_secret import TemplateSecret

__all__ = ["ObjectStoreTemplateSummarySecrets"]

ObjectStoreTemplateSummarySecrets: TypeAlias = list[TemplateSecret] | None
