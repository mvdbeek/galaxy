"""
Integration tests for secondary file (index) detection and import.

Tests the functionality to detect and import pre-existing secondary files
(like .bai for BAM files) instead of regenerating them during metadata setting.
"""

import os
import shutil
from tempfile import mkdtemp
from typing import ClassVar

from galaxy_test.base.populators import DatasetPopulator
from galaxy_test.driver import integration_util


class TestSecondaryFilesIntegration(integration_util.IntegrationTestCase):
    """Integration tests for secondary file detection and import."""

    dataset_populator: DatasetPopulator
    library_dir: ClassVar[str]
    root: ClassVar[str]

    framework_tool_and_types = True

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        root = os.path.realpath(mkdtemp())
        cls._test_driver.temp_directories.append(root)
        cls.root = root
        cls.library_dir = os.path.join(root, "library")
        config["library_import_dir"] = cls.library_dir
        config["metadata_strategy"] = "extended"

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

        if os.path.exists(self.library_dir):
            shutil.rmtree(self.library_dir)
        os.mkdir(self.library_dir)

    def test_secondary_files_detection_endpoint(self):
        """Test the /api/remote_files/secondary_files endpoint."""
        # Create test BAM and BAI files in the library directory
        bam_path = os.path.join(self.library_dir, "test.bam")
        bai_path = os.path.join(self.library_dir, "test.bam.bai")

        # Create dummy files
        with open(bam_path, "wb") as f:
            f.write(b"dummy bam content")
        with open(bai_path, "wb") as f:
            f.write(b"dummy bai content")

        # Call the detection endpoint
        target = f"gximport://{bam_path}"
        response = self.galaxy_interactor.get(
            f"remote_files/secondary_files?target={target}&extension=bam"
        )
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"

        detected = response.json()
        # Should detect the .bai file
        assert len(detected) >= 1, f"Expected at least 1 detected file, got {len(detected)}"

        # Find the bam_index entry
        bam_index = next((d for d in detected if d.get("metadata_key") == "bam_index"), None)
        assert bam_index is not None, "bam_index not found in detected files"
        assert "bai" in bam_index.get("path", "").lower() or "bai" in bam_index.get("description", "").lower()

    def test_secondary_files_detection_no_index(self):
        """Test detection endpoint when no index exists."""
        # Create test BAM file without index
        bam_path = os.path.join(self.library_dir, "no_index.bam")

        with open(bam_path, "wb") as f:
            f.write(b"dummy bam content")

        target = f"gximport://{bam_path}"
        response = self.galaxy_interactor.get(
            f"remote_files/secondary_files?target={target}&extension=bam"
        )
        assert response.status_code == 200

        detected = response.json()
        # Should return empty list when no index exists
        assert len(detected) == 0, f"Expected 0 detected files, got {len(detected)}"

    def test_secondary_files_schema_includes_field(self):
        """Test that the fetch data schema includes secondary_files field."""
        # This tests that the schema was properly extended
        # We can verify by attempting a fetch with secondary_files parameter
        # and ensuring it doesn't fail with schema validation

        # Create a simple test file
        test_path = os.path.join(self.library_dir, "test.txt")
        with open(test_path, "w") as f:
            f.write("test content")

        # Fetch with secondary_files in the payload - should not fail schema validation
        fetch_response = self.dataset_populator.fetch(
            {
                "targets": [
                    {
                        "destination": {"type": "hdas"},
                        "elements": [
                            {
                                "src": "path",
                                "path": test_path,
                                "name": "test.txt",
                                "ext": "txt",
                                "secondary_files": [],  # Empty but valid
                            }
                        ],
                    }
                ]
            },
            assert_ok=True,
        )

        # Should complete successfully
        assert fetch_response is not None


class TestSecondaryFilesDetectionPatterns(integration_util.IntegrationTestCase):
    """Test secondary file detection for various file types."""

    dataset_populator: DatasetPopulator
    library_dir: ClassVar[str]
    root: ClassVar[str]

    framework_tool_and_types = True

    @classmethod
    def handle_galaxy_config_kwds(cls, config):
        super().handle_galaxy_config_kwds(config)
        root = os.path.realpath(mkdtemp())
        cls._test_driver.temp_directories.append(root)
        cls.root = root
        cls.library_dir = os.path.join(root, "library")
        config["library_import_dir"] = cls.library_dir

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)

        if os.path.exists(self.library_dir):
            shutil.rmtree(self.library_dir)
        os.mkdir(self.library_dir)

    def test_vcf_tbi_detection(self):
        """Test detection of .tbi index for VCF files."""
        vcf_path = os.path.join(self.library_dir, "test.vcf.gz")
        tbi_path = os.path.join(self.library_dir, "test.vcf.gz.tbi")

        with open(vcf_path, "wb") as f:
            f.write(b"dummy vcf content")
        with open(tbi_path, "wb") as f:
            f.write(b"dummy tbi content")

        target = f"gximport://{vcf_path}"
        response = self.galaxy_interactor.get(
            f"remote_files/secondary_files?target={target}&extension=vcf_bgzip"
        )
        assert response.status_code == 200

        detected = response.json()
        assert len(detected) >= 1

        tabix_index = next((d for d in detected if d.get("metadata_key") == "tabix_index"), None)
        assert tabix_index is not None, "tabix_index not found in detected files"

    def test_cram_crai_detection(self):
        """Test detection of .crai index for CRAM files."""
        cram_path = os.path.join(self.library_dir, "test.cram")
        crai_path = os.path.join(self.library_dir, "test.cram.crai")

        with open(cram_path, "wb") as f:
            f.write(b"dummy cram content")
        with open(crai_path, "wb") as f:
            f.write(b"dummy crai content")

        target = f"gximport://{cram_path}"
        response = self.galaxy_interactor.get(
            f"remote_files/secondary_files?target={target}&extension=cram"
        )
        assert response.status_code == 200

        detected = response.json()
        assert len(detected) >= 1

        cram_index = next((d for d in detected if d.get("metadata_key") == "cram_index"), None)
        assert cram_index is not None, "cram_index not found in detected files"

    def test_bam_csi_detection(self):
        """Test detection of .csi index for BAM files (large contigs)."""
        bam_path = os.path.join(self.library_dir, "test.bam")
        csi_path = os.path.join(self.library_dir, "test.bam.csi")

        with open(bam_path, "wb") as f:
            f.write(b"dummy bam content")
        with open(csi_path, "wb") as f:
            f.write(b"dummy csi content")

        target = f"gximport://{bam_path}"
        response = self.galaxy_interactor.get(
            f"remote_files/secondary_files?target={target}&extension=bam"
        )
        assert response.status_code == 200

        detected = response.json()
        # Should detect CSI index
        csi_index = next((d for d in detected if d.get("metadata_key") == "bam_csi_index"), None)
        assert csi_index is not None, "bam_csi_index not found in detected files"
