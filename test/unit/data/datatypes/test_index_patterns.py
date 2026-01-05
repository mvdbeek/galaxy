"""
Unit tests for the index_patterns module.
"""

import os
import tempfile
from pathlib import Path

import pytest

from galaxy.datatypes.index_patterns import (
    detect_secondary_files,
    get_all_supported_extensions,
    get_secondary_file_patterns,
    SECONDARY_FILE_PATTERNS,
    SecondaryFilePattern,
)


class TestSecondaryFilePatterns:
    """Tests for the SecondaryFilePattern dataclass and registry."""

    def test_bam_patterns_exist(self):
        """Test that BAM patterns are registered."""
        patterns = get_secondary_file_patterns("bam")
        assert len(patterns) >= 2  # At least .bai and .csi
        metadata_keys = [p.metadata_key for p in patterns]
        assert "bam_index" in metadata_keys
        assert "bam_csi_index" in metadata_keys

    def test_vcf_bgzip_patterns_exist(self):
        """Test that VCF bgzip patterns are registered."""
        patterns = get_secondary_file_patterns("vcf_bgzip")
        assert len(patterns) >= 1  # At least .tbi
        metadata_keys = [p.metadata_key for p in patterns]
        assert "tabix_index" in metadata_keys

    def test_cram_patterns_exist(self):
        """Test that CRAM patterns are registered."""
        patterns = get_secondary_file_patterns("cram")
        assert len(patterns) >= 1  # At least .crai
        metadata_keys = [p.metadata_key for p in patterns]
        assert "cram_index" in metadata_keys

    def test_unknown_extension_returns_empty(self):
        """Test that unknown extensions return empty list."""
        patterns = get_secondary_file_patterns("unknown_format")
        assert patterns == []

    def test_get_all_supported_extensions(self):
        """Test that we can get all supported extensions."""
        extensions = get_all_supported_extensions()
        assert "bam" in extensions
        assert "vcf_bgzip" in extensions
        assert "cram" in extensions

    def test_pattern_has_required_fields(self):
        """Test that SecondaryFilePattern has all required fields."""
        patterns = get_secondary_file_patterns("bam")
        for pattern in patterns:
            assert isinstance(pattern, SecondaryFilePattern)
            assert pattern.primary_extension == "bam"
            assert pattern.secondary_extension is not None
            assert pattern.metadata_key is not None
            assert pattern.description is not None
            assert pattern.suffixes is not None
            assert len(pattern.suffixes) > 0


class TestDetectSecondaryFiles:
    """Tests for the detect_secondary_files function."""

    def test_detect_bai_index_with_bam_bai_suffix(self):
        """Test detection of .bam.bai index file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            bam_path = os.path.join(tmpdir, "test.bam")
            bai_path = os.path.join(tmpdir, "test.bam.bai")

            Path(bam_path).touch()
            Path(bai_path).touch()

            detected = detect_secondary_files(bam_path, "bam")

            assert len(detected) >= 1
            bam_index = next((d for d in detected if d.metadata_key == "bam_index"), None)
            assert bam_index is not None
            assert bam_index.path == bai_path

    def test_detect_bai_index_with_bai_suffix(self):
        """Test detection of .bai index file (without .bam prefix)."""
        with tempfile.TemporaryDirectory() as tmpdir:
            bam_path = os.path.join(tmpdir, "test.bam")
            bai_path = os.path.join(tmpdir, "test.bai")

            Path(bam_path).touch()
            Path(bai_path).touch()

            detected = detect_secondary_files(bam_path, "bam")

            assert len(detected) >= 1
            bam_index = next((d for d in detected if d.metadata_key == "bam_index"), None)
            assert bam_index is not None
            assert bam_index.path == bai_path

    def test_detect_csi_index(self):
        """Test detection of .csi index file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            bam_path = os.path.join(tmpdir, "test.bam")
            csi_path = os.path.join(tmpdir, "test.bam.csi")

            Path(bam_path).touch()
            Path(csi_path).touch()

            detected = detect_secondary_files(bam_path, "bam")

            csi_index = next((d for d in detected if d.metadata_key == "bam_csi_index"), None)
            assert csi_index is not None
            assert csi_index.path == csi_path

    def test_detect_multiple_indexes(self):
        """Test detection of both .bai and .csi indexes."""
        with tempfile.TemporaryDirectory() as tmpdir:
            bam_path = os.path.join(tmpdir, "test.bam")
            bai_path = os.path.join(tmpdir, "test.bam.bai")
            csi_path = os.path.join(tmpdir, "test.bam.csi")

            Path(bam_path).touch()
            Path(bai_path).touch()
            Path(csi_path).touch()

            detected = detect_secondary_files(bam_path, "bam")

            assert len(detected) >= 2
            metadata_keys = [d.metadata_key for d in detected]
            assert "bam_index" in metadata_keys
            assert "bam_csi_index" in metadata_keys

    def test_no_index_detected_when_missing(self):
        """Test that no index is detected when files don't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            bam_path = os.path.join(tmpdir, "test.bam")
            Path(bam_path).touch()

            detected = detect_secondary_files(bam_path, "bam")

            assert detected == []

    def test_extension_inference_from_path(self):
        """Test that extension can be inferred from the file path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            bam_path = os.path.join(tmpdir, "test.bam")
            bai_path = os.path.join(tmpdir, "test.bam.bai")

            Path(bam_path).touch()
            Path(bai_path).touch()

            # Don't provide extension, should be inferred
            detected = detect_secondary_files(bam_path)

            assert len(detected) >= 1
            bam_index = next((d for d in detected if d.metadata_key == "bam_index"), None)
            assert bam_index is not None

    def test_tbi_index_detection(self):
        """Test detection of .tbi tabix index."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # vcf_bgzip uses compound extension but file is named .vcf.gz
            vcf_path = os.path.join(tmpdir, "test.vcf.gz")
            tbi_path = os.path.join(tmpdir, "test.vcf.gz.tbi")

            Path(vcf_path).touch()
            Path(tbi_path).touch()

            detected = detect_secondary_files(vcf_path, "vcf_bgzip")

            assert len(detected) >= 1
            tabix_index = next((d for d in detected if d.metadata_key == "tabix_index"), None)
            assert tabix_index is not None
            assert tabix_index.path == tbi_path

    def test_detected_secondary_file_has_correct_attributes(self):
        """Test that DetectedSecondaryFile has all expected attributes."""
        with tempfile.TemporaryDirectory() as tmpdir:
            bam_path = os.path.join(tmpdir, "test.bam")
            bai_path = os.path.join(tmpdir, "test.bam.bai")

            Path(bam_path).touch()
            Path(bai_path).touch()

            detected = detect_secondary_files(bam_path, "bam")

            assert len(detected) >= 1
            bam_index = detected[0]
            assert hasattr(bam_index, "path")
            assert hasattr(bam_index, "metadata_key")
            assert hasattr(bam_index, "description")
            assert hasattr(bam_index, "pattern")
            assert isinstance(bam_index.pattern, SecondaryFilePattern)

    def test_cram_index_detection(self):
        """Test detection of .crai CRAM index."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cram_path = os.path.join(tmpdir, "test.cram")
            crai_path = os.path.join(tmpdir, "test.cram.crai")

            Path(cram_path).touch()
            Path(crai_path).touch()

            detected = detect_secondary_files(cram_path, "cram")

            assert len(detected) >= 1
            cram_index = next((d for d in detected if d.metadata_key == "cram_index"), None)
            assert cram_index is not None
            assert cram_index.path == crai_path
