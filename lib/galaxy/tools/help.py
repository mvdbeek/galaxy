"""Image URLs for the help of locally installed tools."""

import re
from urllib.parse import (
    quote,
    urlencode,
    urlsplit,
)


def set_local_image_paths(text: str, tool_id: str, tool_version: str) -> str:
    """Route relative RST images through Galaxy, preserving static and remote URLs."""

    def replace(match: re.Match[str]) -> str:
        prefix, image_file = match.groups()
        image_file = image_file.strip()
        if image_file.startswith("$PATH_TO_IMAGES/"):
            image_file = image_file[len("$PATH_TO_IMAGES/") :]
        elif image_file.startswith(("/", "${static_path}", "${host_url}", "#")) or urlsplit(image_file).scheme:
            return match.group(0)
        query = urlencode({"tool_version": tool_version, "image_file": image_file})
        return f"{prefix}${{host_url}}api/tools/{quote(tool_id, safe='')}/help_image?{query}"

    return re.sub(
        r"^([ \t]*\.\. (?:\|[^|\r\n]+\|[ \t]+)?(?:image|figure)::[ \t]+)([^\r\n]+)",
        replace,
        text,
        flags=re.MULTILINE,
    )
