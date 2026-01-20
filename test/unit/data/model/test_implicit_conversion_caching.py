"""Tests for implicit conversion dataset association caching.

Regression tests for: https://github.com/galaxyproject/galaxy/issues/21573

The issue is that the implicitly_converted_datasets relationship can be cached
and subsequent accesses within the same session don't see newly created ICDAs,
potentially causing duplicate conversions.
"""

import uuid

import galaxy.datatypes.registry
from galaxy import model
from galaxy.model import mapping
from galaxy.util.unittest import TestCase

datatypes_registry = galaxy.datatypes.registry.Registry()
datatypes_registry.load_datatypes()
model.set_datatypes_registry(datatypes_registry)

DB_URI = "sqlite:///:memory:"


class MockObjectStore:
    def __init__(self):
        pass

    def size(self, dataset):
        return 100

    def exists(self, dataset, **kwargs):
        return True

    def get_filename(self, dataset, **kwargs):
        return "test_path"

    def update_from_file(self, dataset, file_name=None, create=False, **kwargs):
        return True


class TestImplicitConversionCaching(TestCase):
    """Tests for implicit conversion dataset association caching."""

    model: mapping.GalaxyModelMapping

    @classmethod
    def setUpClass(cls):
        cls.model = mapping.init("/tmp", DB_URI, create_tables=True)
        model.setup_global_object_store_for_models(MockObjectStore())
        assert cls.model.engine is not None

    def session(self):
        return self.model.session

    def persist(self, *args, commit=True, expunge=False):
        session = self.session()
        for arg in args:
            session.add(arg)
        if commit:
            session.commit()
        if expunge:
            session.flush()
            session.expunge_all()

    def _create_user_and_history(self):
        """Create a test user and history with unique email."""
        unique_email = f"test_{uuid.uuid4().hex}@example.com"
        user = model.User(email=unique_email, password="password")
        self.persist(user)
        history = model.History(name="Test History", user=user)
        self.persist(history)
        return user, history

    def test_attach_implicitly_converted_dataset_expires_relationship(self):
        """Test that attach_implicitly_converted_dataset expires the relationship cache.

        This ensures that subsequent accesses to implicitly_converted_datasets
        within the same session see the newly created ICDA.
        """
        user, history = self._create_user_and_history()

        # Create a parent HDA
        parent_hda = model.HistoryDatasetAssociation(
            history=history,
            extension="vcf",
            create_dataset=True,
            sa_session=self.session(),
        )
        parent_hda.dataset.state = model.Dataset.states.OK
        self.persist(parent_hda)

        # Access the relationship to cache it (should be empty)
        initial_count = len(list(parent_hda.implicitly_converted_datasets))
        assert initial_count == 0, f"Expected 0 initial ICDAs, got {initial_count}"

        # Create a converted HDA
        converted_hda = model.HistoryDatasetAssociation(
            history=history,
            extension="vcf_bgzip",
            create_dataset=True,
            sa_session=self.session(),
        )
        converted_hda.dataset.state = model.Dataset.states.NEW
        self.persist(converted_hda, commit=False)

        # Attach the converted dataset (this should flush and expire the relationship)
        parent_hda.attach_implicitly_converted_dataset(self.session(), converted_hda, "vcf_bgzip")

        # Now check the relationship - it should show the new ICDA
        # If the relationship is still cached, this would return 0
        icda_list = list(parent_hda.implicitly_converted_datasets)
        assert len(icda_list) == 1, (
            f"Expected 1 ICDA but found {len(icda_list)}. "
            "The relationship cache was not invalidated after attach_implicitly_converted_dataset."
        )
        assert icda_list[0].type == "vcf_bgzip"
        assert icda_list[0].dataset == converted_hda

    def test_get_converted_files_by_type_sees_new_icda(self):
        """Test that get_converted_files_by_type sees newly attached ICDAs.

        This tests the code path that checks for existing conversions.
        """
        user, history = self._create_user_and_history()

        # Create a parent HDA
        parent_hda = model.HistoryDatasetAssociation(
            history=history,
            extension="vcf",
            create_dataset=True,
            sa_session=self.session(),
        )
        parent_hda.dataset.state = model.Dataset.states.OK
        self.persist(parent_hda)

        # First check - should return None (no conversion exists)
        result = parent_hda.get_converted_files_by_type("vcf_bgzip")
        assert result is None, "Should not find conversion before it's created"

        # Create and attach a converted HDA
        converted_hda = model.HistoryDatasetAssociation(
            history=history,
            extension="vcf_bgzip",
            create_dataset=True,
            sa_session=self.session(),
        )
        converted_hda.dataset.state = model.Dataset.states.NEW
        self.persist(converted_hda, commit=False)

        parent_hda.attach_implicitly_converted_dataset(self.session(), converted_hda, "vcf_bgzip")

        # Second check - should find the conversion now
        result = parent_hda.get_converted_files_by_type("vcf_bgzip")
        assert result is not None, (
            "get_converted_files_by_type should find the conversion after attach. "
            "The relationship cache might not be invalidated."
        )
        assert result == converted_hda

    def test_multiple_attach_operations_in_same_session(self):
        """Test that multiple attach operations in the same session all see each other.

        This simulates chained conversions where multiple ICDAs are created
        in sequence within the same session.
        """
        user, history = self._create_user_and_history()

        # Create a parent HDA
        parent_hda = model.HistoryDatasetAssociation(
            history=history,
            extension="interval",
            create_dataset=True,
            sa_session=self.session(),
        )
        parent_hda.dataset.state = model.Dataset.states.OK
        self.persist(parent_hda)

        # First conversion: interval -> bgzip
        bgzip_hda = model.HistoryDatasetAssociation(
            history=history,
            extension="bgzip",
            create_dataset=True,
            sa_session=self.session(),
        )
        bgzip_hda.dataset.state = model.Dataset.states.NEW
        self.persist(bgzip_hda, commit=False)
        parent_hda.attach_implicitly_converted_dataset(self.session(), bgzip_hda, "bgzip")

        # Check that the first conversion is visible
        result1 = parent_hda.get_converted_files_by_type("bgzip")
        assert result1 == bgzip_hda, "First conversion should be visible"

        # Second conversion: interval -> tabix
        tabix_hda = model.HistoryDatasetAssociation(
            history=history,
            extension="tabix",
            create_dataset=True,
            sa_session=self.session(),
        )
        tabix_hda.dataset.state = model.Dataset.states.NEW
        self.persist(tabix_hda, commit=False)
        parent_hda.attach_implicitly_converted_dataset(self.session(), tabix_hda, "tabix")

        # Both conversions should be visible
        result1_again = parent_hda.get_converted_files_by_type("bgzip")
        result2 = parent_hda.get_converted_files_by_type("tabix")

        assert result1_again == bgzip_hda, "First conversion should still be visible"
        assert result2 == tabix_hda, "Second conversion should be visible"

        # Total ICDA count should be 2
        icda_list = list(parent_hda.implicitly_converted_datasets)
        assert len(icda_list) == 2, f"Expected 2 ICDAs but found {len(icda_list)}"

    def test_expire_needed_for_raw_sql_inserts(self):
        """Test that session.expire is needed when ICDAs are created via raw SQL.

        This tests the scenario where an ICDA is inserted without going through
        the ORM's back_populates mechanism. The expire() call in
        attach_implicitly_converted_dataset ensures the relationship cache
        is invalidated even in edge cases.

        Note: The normal code path uses the ORM which triggers back_populates,
        so expire() is primarily defensive. This test documents when it would
        be necessary.
        """
        from sqlalchemy import text

        user, history = self._create_user_and_history()

        # Create a parent HDA
        parent_hda = model.HistoryDatasetAssociation(
            history=history,
            extension="vcf",
            create_dataset=True,
            sa_session=self.session(),
        )
        parent_hda.dataset.state = model.Dataset.states.OK
        self.persist(parent_hda)

        # Reload to get a fresh object
        parent_id = parent_hda.id
        self.session().expire_all()
        parent_hda = self.session().get(model.HistoryDatasetAssociation, parent_id)

        # Access relationship to cache it (should be empty)
        initial = list(parent_hda.implicitly_converted_datasets)
        assert len(initial) == 0, "Should start with no ICDAs"

        # Insert ICDA via raw SQL (bypasses ORM back_populates)
        self.session().execute(
            text("""
                INSERT INTO implicitly_converted_dataset_association
                (hda_parent_id, hda_id, type, deleted, metadata_safe)
                VALUES (:parent_id, :parent_id, :type, 0, 0)
            """),
            {"parent_id": parent_id, "type": "vcf_bgzip"},
        )
        self.session().flush()

        # Without expire, the cached relationship is stale
        stale_result = list(parent_hda.implicitly_converted_datasets)
        assert len(stale_result) == 0, (
            "Without expire, relationship should return cached (stale) value"
        )

        # After expire, the relationship is reloaded from DB
        self.session().expire(parent_hda, ["implicitly_converted_datasets"])
        fresh_result = list(parent_hda.implicitly_converted_datasets)
        assert len(fresh_result) == 1, (
            f"After expire, should find the raw SQL inserted ICDA. Got {len(fresh_result)}"
        )
