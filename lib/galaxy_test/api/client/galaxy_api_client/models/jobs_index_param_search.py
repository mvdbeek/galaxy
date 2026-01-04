from typing import TypeAlias

__all__ = ["JobsIndexParamSearch"]

JobsIndexParamSearch: TypeAlias = str | None
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

`user`
: The user email of the user that executed the Job. (The tag `u` can be used a short hand alias for this tag to filter on this attribute.)

`tool_id`
: The tool ID corresponding to the job. (The tag `t` can be used a short hand alias for this tag to filter on this attribute.)

`runner`
: The job runner name used to execute the job. (The tag `r` can be used a short hand alias for this tag to filter on this attribute.) This tag is only available for requests using admin keys and/or sessions.

`handler`
: The job handler name used to execute the job. (The tag `h` can be used a short hand alias for this tag to filter on this attribute.) This tag is only available for requests using admin keys and/or sessions.

## Free Text

Free text search terms will be searched against the following attributes of the
Jobs: `user`, `tool`, `handler`, `runner`.

"""
