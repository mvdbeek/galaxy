"""
Registry of known secondary file (index) patterns for datatypes.

This module provides infrastructure for detecting secondary files (like .bai for BAM)
that exist alongside primary data files. The patterns are used by the upload system
to allow users to import pre-existing indexes instead of regenerating them.
"""

import os
from dataclasses import dataclass
from typing import (
    List,
    Optional,
    Tuple,
)


@dataclass
class SecondaryFilePattern:
    """Describes a secondary file pattern for a datatype."""

    primary_extension: str
    """The primary file extension (e.g., 'bam')"""

    secondary_extension: str
    """The secondary file extension (e.g., 'bai')"""

    metadata_key: str
    """The metadata key to store the file (e.g., 'bam_index')"""

    description: str
    """Human-readable description of the secondary file"""

    suffixes: Tuple[str, ...]
    """Possible suffixes to detect (e.g., ('.bai', '.bam.bai'))"""


# Registry of secondary file patterns organized by primary extension
SECONDARY_FILE_PATTERNS: dict[str, List[SecondaryFilePattern]] = {
    "bam": [
        SecondaryFilePattern(
            primary_extension="bam",
            secondary_extension="bai",
            metadata_key="bam_index",
            description="BAM Index (.bai)",
            suffixes=(".bai", ".bam.bai"),
        ),
        SecondaryFilePattern(
            primary_extension="bam",
            secondary_extension="bam.csi",
            metadata_key="bam_csi_index",
            description="BAM CSI Index (.csi)",
            suffixes=(".csi", ".bam.csi"),
        ),
    ],
    "cram": [
        SecondaryFilePattern(
            primary_extension="cram",
            secondary_extension="crai",
            metadata_key="cram_index",
            description="CRAM Index (.crai)",
            suffixes=(".crai", ".cram.crai"),
        ),
    ],
    "vcf_bgzip": [
        SecondaryFilePattern(
            primary_extension="vcf_bgzip",
            secondary_extension="tbi",
            metadata_key="tabix_index",
            description="Tabix Index (.tbi)",
            suffixes=(".tbi", ".vcf.gz.tbi"),
        ),
        SecondaryFilePattern(
            primary_extension="vcf_bgzip",
            secondary_extension="csi",
            metadata_key="csi_index",
            description="CSI Index (.csi)",
            suffixes=(".csi", ".vcf.gz.csi"),
        ),
    ],
    "bed_tabix": [
        SecondaryFilePattern(
            primary_extension="bed_tabix",
            secondary_extension="tbi",
            metadata_key="tabix_index",
            description="Tabix Index (.tbi)",
            suffixes=(".tbi",),
        ),
    ],
    "gff_tabix": [
        SecondaryFilePattern(
            primary_extension="gff_tabix",
            secondary_extension="tbi",
            metadata_key="tabix_index",
            description="Tabix Index (.tbi)",
            suffixes=(".tbi",),
        ),
    ],
}


def get_secondary_file_patterns(extension: str) -> List[SecondaryFilePattern]:
    """
    Get secondary file patterns for a given primary file extension.

    Args:
        extension: The primary file extension (e.g., 'bam', 'vcf_bgzip')

    Returns:
        List of SecondaryFilePattern objects for the extension, or empty list if none.
    """
    return SECONDARY_FILE_PATTERNS.get(extension, [])


@dataclass
class DetectedSecondaryFile:
    """Information about a detected secondary file."""

    path: str
    """Full path to the detected secondary file"""

    metadata_key: str
    """Metadata key to store this file (e.g., 'bam_index')"""

    description: str
    """Human-readable description"""

    pattern: SecondaryFilePattern
    """The pattern that matched"""


def detect_secondary_files(
    primary_path: str,
    extension: Optional[str] = None,
) -> List[DetectedSecondaryFile]:
    """
    Detect existing secondary files for a primary file.

    This function looks for known secondary files (like .bai for BAM files)
    that exist alongside the primary file.

    Args:
        primary_path: Full path to the primary file
        extension: File extension hint. If not provided, will be inferred from path.

    Returns:
        List of DetectedSecondaryFile objects for files that exist.

    Example:
        >>> detect_secondary_files("/data/sample.bam", "bam")
        [DetectedSecondaryFile(path="/data/sample.bam.bai", metadata_key="bam_index", ...)]
    """
    if extension is None:
        # Try to infer extension from path
        _, ext = os.path.splitext(primary_path)
        extension = ext.lstrip(".") if ext else ""

    patterns = get_secondary_file_patterns(extension)
    results: List[DetectedSecondaryFile] = []

    for pattern in patterns:
        detected_path = _find_secondary_file(primary_path, pattern)
        if detected_path:
            results.append(
                DetectedSecondaryFile(
                    path=detected_path,
                    metadata_key=pattern.metadata_key,
                    description=pattern.description,
                    pattern=pattern,
                )
            )

    return results


def _find_secondary_file(primary_path: str, pattern: SecondaryFilePattern) -> Optional[str]:
    """
    Find a secondary file matching the given pattern.

    Tries each suffix in order and returns the first match that exists.

    Args:
        primary_path: Path to the primary file
        pattern: The secondary file pattern to match

    Returns:
        Path to the secondary file if found, None otherwise.
    """
    base_without_ext = _strip_extension(primary_path, pattern.primary_extension)

    for suffix in pattern.suffixes:
        # Try appending suffix to full path (e.g., file.bam.bai)
        candidate = primary_path + suffix
        if os.path.exists(candidate):
            return candidate

        # Try replacing extension (e.g., file.bam -> file.bai)
        if not suffix.startswith("."):
            suffix = "." + suffix
        candidate = base_without_ext + suffix
        if os.path.exists(candidate):
            return candidate

    return None


def _strip_extension(path: str, extension: str) -> str:
    """
    Strip the extension from a path.

    Handles both simple extensions (.bam) and compound extensions (.vcf.gz).

    Args:
        path: File path
        extension: Extension to strip (without leading dot)

    Returns:
        Path without the extension
    """
    # Handle compound extensions like vcf.gz
    if "." in extension:
        parts = extension.split(".")
        for _ in parts:
            path, _ = os.path.splitext(path)
        return path
    else:
        base, _ = os.path.splitext(path)
        return base


def get_all_supported_extensions() -> List[str]:
    """
    Get list of all primary extensions that have secondary file patterns.

    Returns:
        List of extension strings (e.g., ['bam', 'cram', 'vcf_bgzip'])
    """
    return list(SECONDARY_FILE_PATTERNS.keys())
