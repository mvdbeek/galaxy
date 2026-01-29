from dataclasses import dataclass

__all__ = ["ServiceType"]


@dataclass
class ServiceType:
    """
    ServiceType dataclass.

    Args:
        artifact (str)           : Name of the API or GA4GH specification implemented.
                                   Official GA4GH types should be assigned as part of
                                   standards approval process. Custom artifacts are
                                   supported.
        group (str)              : Namespace in reverse domain name format. Use `org.ga4gh`
                                   for implementations compliant with official GA4GH
                                   specifications. For services with custom APIs not
                                   standardized by GA4GH, or implementations diverging from
                                   official GA4GH specifications, use a different namespace
                                   (e.g. your organization's reverse domain name).
        version (str)            : Version of the API or specification. GA4GH specifications
                                   use semantic versioning.
    """

    artifact: str  # Name of the API or GA4GH specification implemented. Official GA4GH types should be assigned as part of standards approval process. Custom artifacts are supported.
    group: str  # Namespace in reverse domain name format. Use `org.ga4gh` for implementations compliant with official GA4GH specifications. For services with custom APIs not standardized by GA4GH, or implementations diverging from official GA4GH specifications, use a different namespace (e.g. your organization's reverse domain name).
    version: str  # Version of the API or specification. GA4GH specifications use semantic versioning.
