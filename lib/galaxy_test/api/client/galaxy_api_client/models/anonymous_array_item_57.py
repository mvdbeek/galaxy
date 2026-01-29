from typing import TypeAlias

from .template_variable_boolean import TemplateVariableBoolean
from .template_variable_integer import TemplateVariableInteger
from .template_variable_path_component import TemplateVariablePathComponent
from .template_variable_string import TemplateVariableString

__all__ = ["AnonymousArrayItem57"]

AnonymousArrayItem57: TypeAlias = (
    TemplateVariableString | TemplateVariableInteger | TemplateVariablePathComponent | TemplateVariableBoolean
)
