from typing import TYPE_CHECKING, Any

from ...models.datatype_converter_list import DatatypeConverterList
from ...models.datatype_visualization_mappings_list import DatatypeVisualizationMappingsList
from ...models.datatypes_combined_map import DatatypesCombinedMap
from ...models.datatypes_edam_data_edam_data_200_response import DatatypesEdamDataEdamData200Response
from ...models.datatypes_edam_details_dict_2 import DatatypesEdamDetailsDict2
from ...models.datatypes_edam_formats_edam_formats_200_response import DatatypesEdamFormatsEdamFormats200Response
from ...models.datatypes_index_200_response import DatatypesIndex200Response
from ...models.datatypes_index_param_extension_only import DatatypesIndexParamExtensionOnly
from ...models.datatypes_index_param_upload_only import DatatypesIndexParamUploadOnly
from ...models.datatypes_map import DatatypesMap
from ...models.datatypes_types_and_mapping_types_and_mapping_param_extension_only import (
    DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly,
)
from ...models.datatypes_types_and_mapping_types_and_mapping_param_upload_only import (
    DatatypesTypesAndMappingTypesAndMappingParamUploadOnly,
)

if TYPE_CHECKING:
    pass


class MockDatatypesClient:
    """
    Mock implementation of DatatypesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestDatatypesClient(MockDatatypesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def datatypes_index(
        self,
        extension_only: DatatypesIndexParamExtensionOnly | None = None,
        upload_only: DatatypesIndexParamUploadOnly | None = None,
    ) -> DatatypesIndex200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_index() not implemented. Override this method in your test subclass."
        )

    async def datatypes_converters_converters(
        self,
    ) -> DatatypeConverterList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_converters_converters() not implemented. Override this method in your test subclass."
        )

    async def datatypes_edam_data_edam_data(
        self,
    ) -> DatatypesEdamDataEdamData200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_edam_data_edam_data() not implemented. Override this method in your test subclass."
        )

    async def datatypes_edam_data_detailed_edam_data_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_edam_data_detailed_edam_data_detailed() not implemented. Override this method in your test subclass."
        )

    async def datatypes_edam_formats_edam_formats(
        self,
    ) -> DatatypesEdamFormatsEdamFormats200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_edam_formats_edam_formats() not implemented. Override this method in your test subclass."
        )

    async def datatypes_edam_formats_detailed_edam_formats_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_edam_formats_detailed_edam_formats_detailed() not implemented. Override this method in your test subclass."
        )

    async def datatypes_mapping_mapping(
        self,
    ) -> DatatypesMap:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_mapping_mapping() not implemented. Override this method in your test subclass."
        )

    async def datatypes_sniffers_sniffers(
        self,
    ) -> list[str]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_sniffers_sniffers() not implemented. Override this method in your test subclass."
        )

    async def datatypes_types_and_mapping_types_and_mapping(
        self,
        extension_only: DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly | None = None,
        upload_only: DatatypesTypesAndMappingTypesAndMappingParamUploadOnly | None = None,
    ) -> DatatypesCombinedMap:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_types_and_mapping_types_and_mapping() not implemented. Override this method in your test subclass."
        )

    async def datatypes_show(
        self,
        datatype: str,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_show() not implemented. Override this method in your test subclass."
        )

    async def datatypes_visualizations_visualization_for_datatype(
        self,
        datatype: str,
    ) -> DatatypeVisualizationMappingsList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatatypesClient.datatypes_visualizations_visualization_for_datatype() not implemented. Override this method in your test subclass."
        )
