from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.license_metadata_model import LicenseMetadataModel


class LicensesClient:
    """Client for licenses endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def licenses_index_2_2(
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
                return cast(list[LicenseMetadataModel], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def licenses_index_2_2(
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
                return cast(list[LicenseMetadataModel], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def licenses_get_2_2(
        self,
        id_: Any,
    ) -> LicenseMetadataModel:
        """
        Gets the SPDX license metadata associated with the short identifier

        Returns the license metadata associated with the given [SPDX license short
        ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/).

        Args:
            id (Any)                 : The [SPDX license short
                                       identifier](https://spdx.github.io/spdx-spec/appendix-I-
                                       SPDX-license-list/)

        Returns:
            LicenseMetadataModel: SPDX license metadata

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/licenses/{id_}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LicenseMetadataModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def licenses_get_2_2(
        self,
        id_: Any,
    ) -> LicenseMetadataModel:
        """
        Gets the SPDX license metadata associated with the short identifier

        Returns the license metadata associated with the given [SPDX license short
        ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/).

        Args:
            id (Any)                 : The [SPDX license short
                                       identifier](https://spdx.github.io/spdx-spec/appendix-I-
                                       SPDX-license-list/)

        Returns:
            LicenseMetadataModel: SPDX license metadata

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/licenses/{id_}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LicenseMetadataModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
