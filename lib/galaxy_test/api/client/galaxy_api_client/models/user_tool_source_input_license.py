from typing import TypeAlias

__all__ = ["UserToolSourceInputLicense"]

UserToolSourceInputLicense: TypeAlias = str | None
"""Alias for A full URI or a a short [SPDX](https://spdx.org/licenses/) identifier for a license for this tool wrapper. The tool wrapper license can be independent of the underlying tool license. This license covers the tool yaml and associated scripts shipped with the tool."""
