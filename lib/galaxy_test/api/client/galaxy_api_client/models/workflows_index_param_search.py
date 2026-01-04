from typing import TypeAlias

__all__ = ["WorkflowsIndexParamSearch"]

WorkflowsIndexParamSearch: TypeAlias = str | None
"""Alias for A mix of free text and GitHub-style tags used to filter the index operation.

## Query Structure

GitHub-style filter tags (not be confused with Galaxy tags) are tags of the form
`<tag_name>:<text_no_spaces>` or `<tag_name>:'<text with potential spaces>'`. The tag name
*generally* (but not exclusively) corresponds to the name of an attribute on the model
being indexed (i.e. a column in the database).

If the tag is quoted, the attribute will be filtered exactly. If the tag is unquoted,
generally a partial match will be used to filter the query (i.e. in terms of the implementation
this means the database operation `ILIKE` will typically be used).

Once the tagged filters are extracted from the search query, the remaining text is just
used to search various documented attributes of the object.

## GitHub-style Tags Available

`name`
: The stored workflow's name. (The tag `n` can be used a short hand alias for this tag to filter on this attribute.)

`tag`
: The workflow's tag, if the tag contains a colon an approach will be made to match the key and value of the tag separately. (The tag `t` can be used a short hand alias for this tag to filter on this attribute.)

`user`
: The stored workflow's owner's username. (The tag `u` can be used a short hand alias for this tag to filter on this attribute.)

`is:published`
: Include only published workflows in the final result. Be sure the query parameter `show_published` is set to `true` if to include all published workflows and not just the requesting user's.

`is:importable`
: Include only importable workflows in the final result.

`is:deleted`
: Include only deleted workflows in the final result.

`is:shared_with_me`
: Include only workflows shared with the requesting user.  Be sure the query parameter `show_shared` is set to `true` if to include shared workflows.

`is:bookmarked`
: Include only workflows bookmarked by the requesting user.

## Free Text

Free text search terms will be searched against the following attributes of the
Stored Workflows: `name`, `tag`, `user`.

"""
