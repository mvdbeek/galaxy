from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.license_metadata_model import LicenseMetadataModel


@runtime_checkable
class LicensesClientProtocol(Protocol):
    """Protocol defining the interface of LicensesClient for dependency injection."""

    async def licenses_index(
        self,
    ) -> list[LicenseMetadataModel]: ...

    async def licenses_index(
        self,
    ) -> list[LicenseMetadataModel]: ...

    async def licenses_get(
        self,
        id_: dict[str, Any],
    ) -> LicenseMetadataModel: ...

    async def licenses_get(
        self,
        id_: dict[str, Any],
    ) -> LicenseMetadataModel: ...


class LicensesClient(LicensesClientProtocol):
    """Client for licenses endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def licenses_index(
        self,
    ) -> list[LicenseMetadataModel]:
        """
        Lists all available SPDX licenses

        Returns an index with all the available [SPDX licenses](https://spdx.org/licenses/).

        Returns:
            List[LicenseMetadataModel]: List of SPDX licenses

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/licenses"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[LicenseMetadataModel])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def licenses_index(
        self,
    ) -> list[LicenseMetadataModel]:
        """
        Lists all available SPDX licenses

        Returns an index with all the available [SPDX licenses](https://spdx.org/licenses/).

        Returns:
            List[LicenseMetadataModel]: List of SPDX licenses

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/licenses"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[LicenseMetadataModel])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def licenses_get(
        self,
        id_: dict[str, Any],
    ) -> LicenseMetadataModel:
        """
        Gets the SPDX license metadata associated with the short identifier

        Returns the license metadata associated with the given [SPDX license short
        ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/).

        Args:
            id (dict[str, Any])      : The [SPDX license short
                                       identifier](https://spdx.github.io/spdx-spec/appendix-I-
                                       SPDX-license-list/)

        Returns:
            LicenseMetadataModel: SPDX license metadata

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/licenses/{id_}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LicenseMetadataModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def licenses_get(
        self,
        id_: dict[str, Any],
    ) -> LicenseMetadataModel:
        """
        Gets the SPDX license metadata associated with the short identifier

        Returns the license metadata associated with the given [SPDX license short
        ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/).

        Args:
            id (dict[str, Any])      : The [SPDX license short
                                       identifier](https://spdx.github.io/spdx-spec/appendix-I-
                                       SPDX-license-list/)

        Returns:
            LicenseMetadataModel: SPDX license metadata

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/licenses/{id_}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LicenseMetadataModel)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
