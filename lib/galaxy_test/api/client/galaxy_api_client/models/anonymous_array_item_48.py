from typing import TypeAlias

from .container_requirement import ContainerRequirement
from .javascript_requirement import JavascriptRequirement
from .resource_requirement import ResourceRequirement

__all__ = ["AnonymousArrayItem48"]

AnonymousArrayItem48: TypeAlias = JavascriptRequirement | ResourceRequirement | ContainerRequirement
