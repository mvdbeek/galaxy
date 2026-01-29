from dataclasses import dataclass

__all__ = ["ImportToolDataBundleUriSource"]


@dataclass
class ImportToolDataBundleUriSource:
    """
    ImportToolDataBundleUriSource dataclass.

    Args:
        src (str)                : Indicates that the tool data should be resolved by a URI.
        uri (str)                : URI to fetch tool data bundle from (file:// URIs are fine
                                   because this is an admin-only operation)
    """

    src: str  # Indicates that the tool data should be resolved by a URI.
    uri: str  # URI to fetch tool data bundle from (file:// URIs are fine because this is an admin-only operation)
