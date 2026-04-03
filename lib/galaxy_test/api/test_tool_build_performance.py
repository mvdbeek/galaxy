"""Performance test for tool build endpoint with many datasets and collections.

Verifies that building tool forms remains fast when a history contains
many datasets and collections, testing the batch matching optimization
that avoids N+1 queries on dataset_states_and_extensions_summary.
"""

import time

from galaxy_test.base.populators import (
    DatasetCollectionPopulator,
    DatasetPopulator,
    skip_without_tool,
)
from ._framework import ApiTestCase

NUM_DATASETS = 100
NUM_COLLECTIONS = 100
MAX_BUILD_SECONDS = 10.0


class TestToolBuildPerformance(ApiTestCase):
    dataset_populator: DatasetPopulator

    def setUp(self):
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        self.dataset_collection_populator = DatasetCollectionPopulator(self.galaxy_interactor)

    @skip_without_tool("cat1")
    def test_tool_build_with_many_datasets_and_collections(self):
        with self.dataset_populator.test_history() as history_id:
            # Bulk-upload datasets via fetch API (single job)
            items = [
                {
                    "src": "pasted",
                    "paste_content": f"dataset {i}\n",
                    "name": f"dataset_{i}",
                    "ext": "txt",
                    "dbkey": "?",
                }
                for i in range(NUM_DATASETS)
            ]
            self.dataset_populator.fetch_hdas(history_id, items, wait=True)

            # Create collections via fetch API
            for i in range(NUM_COLLECTIONS):
                self.dataset_collection_populator.create_pair_in_history(
                    history_id,
                    contents=[f"coll {i} fwd\n", f"coll {i} rev\n"],
                    wait=True,
                )

            # Measure tool build time (best of 3 runs)
            timings = []
            for _ in range(3):
                start = time.time()
                build = self.dataset_populator.build_tool_state("cat1", history_id)
                elapsed = time.time() - start
                timings.append(elapsed)

            best = min(timings)

            # Verify the build response contains expected data
            inputs = build["inputs"]
            data_input = [i for i in inputs if i["name"] == "input1"][0]
            hda_options = data_input["options"]["hda"]
            hdca_options = data_input["options"]["hdca"]
            assert len(hda_options) >= NUM_DATASETS, (
                f"Expected at least {NUM_DATASETS} HDA options, got {len(hda_options)}"
            )
            assert len(hdca_options) >= NUM_COLLECTIONS, (
                f"Expected at least {NUM_COLLECTIONS} HDCA options, got {len(hdca_options)}"
            )

            assert best < MAX_BUILD_SECONDS, (
                f"Tool build took {best:.2f}s (best of 3) with {NUM_DATASETS} datasets and "
                f"{NUM_COLLECTIONS} collections, exceeding {MAX_BUILD_SECONDS}s threshold"
            )
