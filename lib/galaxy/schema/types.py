from datetime import datetime
from typing import (
    Annotated,
    Literal,
)

from pydantic import (
    Field,
    ValidationInfo,
)
from pydantic.functional_validators import AfterValidator

from galaxy.util import MAX_ANNOTATION_SIZE

# Input constraint only: response/export fields must accept existing annotations.
Annotation = Annotated[str, Field(max_length=MAX_ANNOTATION_SIZE)]

# Relative URLs cannot be validated with AnyUrl, they need a scheme.
# Making them an alias of `str` for now
RelativeUrl = str

# TODO: we may want to add a custom validator for this and for RelativeUrl
AbsoluteOrRelativeUrl = RelativeUrl

LatestLiteral = Literal["latest"]


def strip_tzinfo(v: datetime, info: ValidationInfo) -> datetime:
    if v.tzinfo:
        if offset := v.utcoffset():
            return v.replace(tzinfo=None) - offset
        return v.replace(tzinfo=None)
    return v


OffsetNaiveDatetime = Annotated[datetime, AfterValidator(strip_tzinfo)]

CoercedStringType = Annotated[
    str | int | float | bool, AfterValidator(lambda val: val if isinstance(val, str) else str(val))
]
