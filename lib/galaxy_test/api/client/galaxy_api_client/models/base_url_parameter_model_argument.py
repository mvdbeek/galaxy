from typing import TypeAlias

__all__ = ["BaseUrlParameterModelArgument"]

BaseUrlParameterModelArgument: TypeAlias = str | None
"""Alias for If the parameter reflects just one command line argument of a certain tool, this tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is implicit)."""
