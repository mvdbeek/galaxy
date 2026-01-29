from typing import TypeAlias

from .template_secret import TemplateSecret

__all__ = ["FileSourceTemplateSummarySecrets"]

FileSourceTemplateSummarySecrets: TypeAlias = list[TemplateSecret] | None
