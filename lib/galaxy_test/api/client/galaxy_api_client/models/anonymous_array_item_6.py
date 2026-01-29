from typing import TypeAlias

from .container_requirement import ContainerRequirement
from .javascript_requirement import JavascriptRequirement
from .resource_requirement import ResourceRequirement

__all__ = ["AnonymousArrayItem6"]

AnonymousArrayItem6: TypeAlias = JavascriptRequirement | ResourceRequirement | ContainerRequirement
