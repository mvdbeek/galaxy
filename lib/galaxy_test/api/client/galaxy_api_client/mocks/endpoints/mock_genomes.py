from typing import TYPE_CHECKING, Any

from ...models.anonymous_array_item_89 import AnonymousArrayItem89
from ...models.genomes_index_param_run_as import GenomesIndexParamRunAs
from ...models.genomes_indexes_indexes_param_run_as import GenomesIndexesIndexesParamRunAs
from ...models.genomes_sequences_sequences_param_run_as import GenomesSequencesSequencesParamRunAs
from ...models.genomes_show_param_run_as import GenomesShowParamRunAs

if TYPE_CHECKING:
    pass


class MockGenomesClient:
    """
    Mock implementation of GenomesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestGenomesClient(MockGenomesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def genomes_index(
        self,
        chrom_info: bool | None = None,
        run_as: GenomesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem89]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGenomesClient.genomes_index() not implemented. Override this method in your test subclass."
        )

    async def genomes_show(
        self,
        id_: str,
        reference: bool | None = None,
        num: int | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format_: str | None = None,
        run_as: GenomesShowParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGenomesClient.genomes_show() not implemented. Override this method in your test subclass."
        )

    async def genomes_indexes_indexes(
        self,
        id_: str,
        type_: str | None = None,
        format_: str | None = None,
        run_as: GenomesIndexesIndexesParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGenomesClient.genomes_indexes_indexes() not implemented. Override this method in your test subclass."
        )

    async def genomes_sequences_sequences(
        self,
        id_: str,
        reference: bool | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format_: str | None = None,
        run_as: GenomesSequencesSequencesParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockGenomesClient.genomes_sequences_sequences() not implemented. Override this method in your test subclass."
        )
