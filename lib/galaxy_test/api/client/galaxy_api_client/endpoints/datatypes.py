from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.datatype_converter_list import DatatypeConverterList
from ..models.datatype_visualization_mappings_list import DatatypeVisualizationMappingsList
from ..models.datatypes_combined_map import DatatypesCombinedMap
from ..models.datatypes_edam_data_edam_data_200_response import DatatypesEdamDataEdamData200Response
from ..models.datatypes_edam_details_dict_2 import DatatypesEdamDetailsDict2
from ..models.datatypes_edam_formats_edam_formats_200_response import DatatypesEdamFormatsEdamFormats200Response
from ..models.datatypes_index_200_response import DatatypesIndex200Response
from ..models.datatypes_index_param_extension_only import DatatypesIndexParamExtensionOnly
from ..models.datatypes_index_param_upload_only import DatatypesIndexParamUploadOnly
from ..models.datatypes_map import DatatypesMap
from ..models.datatypes_types_and_mapping_types_and_mapping_param_extension_only import (
    DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly,
)
from ..models.datatypes_types_and_mapping_types_and_mapping_param_upload_only import (
    DatatypesTypesAndMappingTypesAndMappingParamUploadOnly,
)


@runtime_checkable
class DatatypesClientProtocol(Protocol):
    """Protocol defining the interface of DatatypesClient for dependency injection."""

    async def datatypes_index(
        self,
        extension_only: DatatypesIndexParamExtensionOnly | None = None,
        upload_only: DatatypesIndexParamUploadOnly | None = None,
    ) -> DatatypesIndex200Response: ...

    async def datatypes_index(
        self,
        extension_only: DatatypesIndexParamExtensionOnly | None = None,
        upload_only: DatatypesIndexParamUploadOnly | None = None,
    ) -> DatatypesIndex200Response: ...

    async def datatypes_converters_converters(
        self,
    ) -> DatatypeConverterList: ...

    async def datatypes_converters_converters(
        self,
    ) -> DatatypeConverterList: ...

    async def datatypes_edam_data_edam_data(
        self,
    ) -> DatatypesEdamDataEdamData200Response: ...

    async def datatypes_edam_data_edam_data(
        self,
    ) -> DatatypesEdamDataEdamData200Response: ...

    async def datatypes_edam_data_detailed_edam_data_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2: ...

    async def datatypes_edam_data_detailed_edam_data_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2: ...

    async def datatypes_edam_formats_edam_formats(
        self,
    ) -> DatatypesEdamFormatsEdamFormats200Response: ...

    async def datatypes_edam_formats_edam_formats(
        self,
    ) -> DatatypesEdamFormatsEdamFormats200Response: ...

    async def datatypes_edam_formats_detailed_edam_formats_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2: ...

    async def datatypes_edam_formats_detailed_edam_formats_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2: ...

    async def datatypes_mapping_mapping(
        self,
    ) -> DatatypesMap: ...

    async def datatypes_mapping_mapping(
        self,
    ) -> DatatypesMap: ...

    async def datatypes_sniffers_sniffers(
        self,
    ) -> list[str]: ...

    async def datatypes_sniffers_sniffers(
        self,
    ) -> list[str]: ...

    async def datatypes_types_and_mapping_types_and_mapping(
        self,
        extension_only: DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly | None = None,
        upload_only: DatatypesTypesAndMappingTypesAndMappingParamUploadOnly | None = None,
    ) -> DatatypesCombinedMap: ...

    async def datatypes_types_and_mapping_types_and_mapping(
        self,
        extension_only: DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly | None = None,
        upload_only: DatatypesTypesAndMappingTypesAndMappingParamUploadOnly | None = None,
    ) -> DatatypesCombinedMap: ...

    async def datatypes_show(
        self,
        datatype: str,
    ) -> dict[str, Any]: ...

    async def datatypes_show(
        self,
        datatype: str,
    ) -> dict[str, Any]: ...

    async def datatypes_visualizations_visualization_for_datatype(
        self,
        datatype: str,
    ) -> DatatypeVisualizationMappingsList: ...

    async def datatypes_visualizations_visualization_for_datatype(
        self,
        datatype: str,
    ) -> DatatypeVisualizationMappingsList: ...


class DatatypesClient(DatatypesClientProtocol):
    """Client for datatypes endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def datatypes_index(
        self,
        extension_only: DatatypesIndexParamExtensionOnly | None = None,
        upload_only: DatatypesIndexParamUploadOnly | None = None,
    ) -> DatatypesIndex200Response:
        """
        Lists all available data types

        Gets the list of all available data types.

        Args:
            extension_only (DatatypesIndexParamExtensionOnly | None)
                                     : Whether to return only the datatype's extension rather
                                       than the datatype's details
            upload_only (DatatypesIndexParamUploadOnly | None)
                                     : Whether to return only datatypes which can be uploaded

        Returns:
            DatatypesIndex200Response: List of data types

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes"

        params: dict[str, Any] = {
            **({"extension_only": DataclassSerializer.serialize(extension_only)} if extension_only is not None else {}),
            **({"upload_only": DataclassSerializer.serialize(upload_only)} if upload_only is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesIndex200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_index(
        self,
        extension_only: DatatypesIndexParamExtensionOnly | None = None,
        upload_only: DatatypesIndexParamUploadOnly | None = None,
    ) -> DatatypesIndex200Response:
        """
        Lists all available data types

        Gets the list of all available data types.

        Args:
            extension_only (DatatypesIndexParamExtensionOnly | None)
                                     : Whether to return only the datatype's extension rather
                                       than the datatype's details
            upload_only (DatatypesIndexParamUploadOnly | None)
                                     : Whether to return only datatypes which can be uploaded

        Returns:
            DatatypesIndex200Response: List of data types

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes"

        params: dict[str, Any] = {
            **({"extension_only": DataclassSerializer.serialize(extension_only)} if extension_only is not None else {}),
            **({"upload_only": DataclassSerializer.serialize(upload_only)} if upload_only is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesIndex200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_converters_converters(
        self,
    ) -> DatatypeConverterList:
        """
        Returns the list of all installed converters

        Gets the list of all installed converters.

        Returns:
            DatatypeConverterList: List of all datatype converters

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/converters"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypeConverterList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_converters_converters(
        self,
    ) -> DatatypeConverterList:
        """
        Returns the list of all installed converters

        Gets the list of all installed converters.

        Returns:
            DatatypeConverterList: List of all datatype converters

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/converters"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypeConverterList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_edam_data_edam_data(
        self,
    ) -> DatatypesEdamDataEdamData200Response:
        """
        Returns a dictionary/map of datatypes and EDAM data

        Gets a map of datatypes and their corresponding EDAM data.

        Returns:
            DatatypesEdamDataEdamData200Response: Dictionary/map of datatypes and EDAM data

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/edam_data"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesEdamDataEdamData200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_edam_data_edam_data(
        self,
    ) -> DatatypesEdamDataEdamData200Response:
        """
        Returns a dictionary/map of datatypes and EDAM data

        Gets a map of datatypes and their corresponding EDAM data.

        Returns:
            DatatypesEdamDataEdamData200Response: Dictionary/map of datatypes and EDAM data

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/edam_data"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesEdamDataEdamData200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_edam_data_detailed_edam_data_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2:
        """
        Returns a dictionary of datatypes and EDAM data details

        Gets a map of datatypes and their corresponding EDAM data. EDAM data contains the EDAM
        iri, label, and definition.

        Returns:
            DatatypesEdamDetailsDict2: Dictionary of EDAM data details containing the EDAM iri,
                                       label, and definition

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/edam_data/detailed"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesEdamDetailsDict2)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_edam_data_detailed_edam_data_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2:
        """
        Returns a dictionary of datatypes and EDAM data details

        Gets a map of datatypes and their corresponding EDAM data. EDAM data contains the EDAM
        iri, label, and definition.

        Returns:
            DatatypesEdamDetailsDict2: Dictionary of EDAM data details containing the EDAM iri,
                                       label, and definition

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/edam_data/detailed"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesEdamDetailsDict2)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_edam_formats_edam_formats(
        self,
    ) -> DatatypesEdamFormatsEdamFormats200Response:
        """
        Returns a dictionary/map of datatypes and EDAM formats

        Gets a map of datatypes and their corresponding EDAM formats.

        Returns:
            DatatypesEdamFormatsEdamFormats200Response: Dictionary/map of datatypes and EDAM
                                                        formats

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/edam_formats"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesEdamFormatsEdamFormats200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_edam_formats_edam_formats(
        self,
    ) -> DatatypesEdamFormatsEdamFormats200Response:
        """
        Returns a dictionary/map of datatypes and EDAM formats

        Gets a map of datatypes and their corresponding EDAM formats.

        Returns:
            DatatypesEdamFormatsEdamFormats200Response: Dictionary/map of datatypes and EDAM
                                                        formats

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/edam_formats"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesEdamFormatsEdamFormats200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_edam_formats_detailed_edam_formats_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2:
        """
        Returns a dictionary of datatypes and EDAM format details

        Gets a map of datatypes and their corresponding EDAM formats. EDAM formats contain the
        EDAM iri, label, and definition.

        Returns:
            DatatypesEdamDetailsDict2: Dictionary of EDAM format details containing the EDAM
                                       iri, label, and definition

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/edam_formats/detailed"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesEdamDetailsDict2)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_edam_formats_detailed_edam_formats_detailed(
        self,
    ) -> DatatypesEdamDetailsDict2:
        """
        Returns a dictionary of datatypes and EDAM format details

        Gets a map of datatypes and their corresponding EDAM formats. EDAM formats contain the
        EDAM iri, label, and definition.

        Returns:
            DatatypesEdamDetailsDict2: Dictionary of EDAM format details containing the EDAM
                                       iri, label, and definition

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/edam_formats/detailed"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesEdamDetailsDict2)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_mapping_mapping(
        self,
    ) -> DatatypesMap:
        """
        Returns mappings for data types and their implementing classes

        Gets mappings for data types.

        Returns:
            DatatypesMap: Dictionary to map data types with their classes

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/mapping"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesMap)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_mapping_mapping(
        self,
    ) -> DatatypesMap:
        """
        Returns mappings for data types and their implementing classes

        Gets mappings for data types.

        Returns:
            DatatypesMap: Dictionary to map data types with their classes

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/mapping"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesMap)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_sniffers_sniffers(
        self,
    ) -> list[str]:
        """
        Returns the list of all installed sniffers

        Gets the list of all installed data type sniffers.

        Returns:
            List[str]: List of datatype sniffers

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/sniffers"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[str], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_sniffers_sniffers(
        self,
    ) -> list[str]:
        """
        Returns the list of all installed sniffers

        Gets the list of all installed data type sniffers.

        Returns:
            List[str]: List of datatype sniffers

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/sniffers"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[str], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_types_and_mapping_types_and_mapping(
        self,
        extension_only: DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly | None = None,
        upload_only: DatatypesTypesAndMappingTypesAndMappingParamUploadOnly | None = None,
    ) -> DatatypesCombinedMap:
        """
        Returns all the data types extensions and their mappings

        Combines the datatype information from (/api/datatypes) and the mapping information from
        (/api/datatypes/mapping) into a single response.

        Args:
            extension_only (DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly | None)
                                     : Whether to return only the datatype's extension rather
                                       than the datatype's details
            upload_only (DatatypesTypesAndMappingTypesAndMappingParamUploadOnly | None)
                                     : Whether to return only datatypes which can be uploaded

        Returns:
            DatatypesCombinedMap: Dictionary to map data types with their classes

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/types_and_mapping"

        params: dict[str, Any] = {
            **({"extension_only": DataclassSerializer.serialize(extension_only)} if extension_only is not None else {}),
            **({"upload_only": DataclassSerializer.serialize(upload_only)} if upload_only is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesCombinedMap)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_types_and_mapping_types_and_mapping(
        self,
        extension_only: DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly | None = None,
        upload_only: DatatypesTypesAndMappingTypesAndMappingParamUploadOnly | None = None,
    ) -> DatatypesCombinedMap:
        """
        Returns all the data types extensions and their mappings

        Combines the datatype information from (/api/datatypes) and the mapping information from
        (/api/datatypes/mapping) into a single response.

        Args:
            extension_only (DatatypesTypesAndMappingTypesAndMappingParamExtensionOnly | None)
                                     : Whether to return only the datatype's extension rather
                                       than the datatype's details
            upload_only (DatatypesTypesAndMappingTypesAndMappingParamUploadOnly | None)
                                     : Whether to return only datatypes which can be uploaded

        Returns:
            DatatypesCombinedMap: Dictionary to map data types with their classes

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datatypes/types_and_mapping"

        params: dict[str, Any] = {
            **({"extension_only": DataclassSerializer.serialize(extension_only)} if extension_only is not None else {}),
            **({"upload_only": DataclassSerializer.serialize(upload_only)} if upload_only is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypesCombinedMap)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_show(
        self,
        datatype: str,
    ) -> dict[str, Any]:
        """
        Get details for a specific datatype

        Gets detailed information about a specific datatype.  Includes information about: -
        Basic properties (description, mime type, etc.) - Available converters - EDAM mappings -
        Preferred visualization

        Args:
            datatype (str)           : Datatype extension to get information for

        Returns:
            dict[str, Any]: Detailed information about a datatype

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        datatype = DataclassSerializer.serialize(datatype)

        url = f"{self.base_url}/api/datatypes/{datatype}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_show(
        self,
        datatype: str,
    ) -> dict[str, Any]:
        """
        Get details for a specific datatype

        Gets detailed information about a specific datatype.  Includes information about: -
        Basic properties (description, mime type, etc.) - Available converters - EDAM mappings -
        Preferred visualization

        Args:
            datatype (str)           : Datatype extension to get information for

        Returns:
            dict[str, Any]: Detailed information about a datatype

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        datatype = DataclassSerializer.serialize(datatype)

        url = f"{self.base_url}/api/datatypes/{datatype}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_visualizations_visualization_for_datatype(
        self,
        datatype: str,
    ) -> DatatypeVisualizationMappingsList:
        """
        Returns the visualization mapping for a specific datatype

        Gets the visualization mapping for a specific datatype.  Mappings are defined in the
        datatypes_conf.xml configuration file.

        Args:
            datatype (str)           : Datatype extension to get visualization mapping for

        Returns:
            DatatypeVisualizationMappingsList: Visualization mapping for the specified datatype

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        datatype = DataclassSerializer.serialize(datatype)

        url = f"{self.base_url}/api/datatypes/{datatype}/visualizations"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypeVisualizationMappingsList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datatypes_visualizations_visualization_for_datatype(
        self,
        datatype: str,
    ) -> DatatypeVisualizationMappingsList:
        """
        Returns the visualization mapping for a specific datatype

        Gets the visualization mapping for a specific datatype.  Mappings are defined in the
        datatypes_conf.xml configuration file.

        Args:
            datatype (str)           : Datatype extension to get visualization mapping for

        Returns:
            DatatypeVisualizationMappingsList: Visualization mapping for the specified datatype

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        datatype = DataclassSerializer.serialize(datatype)

        url = f"{self.base_url}/api/datatypes/{datatype}/visualizations"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatatypeVisualizationMappingsList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
