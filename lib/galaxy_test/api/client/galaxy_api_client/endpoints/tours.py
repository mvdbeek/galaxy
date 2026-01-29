from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.generate_tour_response import GenerateTourResponse
from ..models.tour_details import TourDetails
from ..models.tour_list import TourList
from ..models.tours_generate_generate_tour_param_run_as import ToursGenerateGenerateTourParamRunAs
from ..models.tours_update_tour_param_run_as import ToursUpdateTourParamRunAs


@runtime_checkable
class ToursClientProtocol(Protocol):
    """Protocol defining the interface of ToursClient for dependency injection."""

    async def tours_index(
        self,
    ) -> TourList: ...

    async def tours_index(
        self,
    ) -> TourList: ...

    async def tours_generate_generate_tour(
        self,
        tool_id: str,
        tool_version: str,
        performs_upload: bool | None = None,
        run_as: ToursGenerateGenerateTourParamRunAs | None = None,
    ) -> GenerateTourResponse: ...

    async def tours_generate_generate_tour(
        self,
        tool_id: str,
        tool_version: str,
        performs_upload: bool | None = None,
        run_as: ToursGenerateGenerateTourParamRunAs | None = None,
    ) -> GenerateTourResponse: ...

    async def tours_show(
        self,
        tour_id: str,
    ) -> TourDetails: ...

    async def tours_show(
        self,
        tour_id: str,
    ) -> TourDetails: ...

    async def tours_update_tour(
        self,
        tour_id: str,
        run_as: ToursUpdateTourParamRunAs | None = None,
    ) -> TourDetails: ...

    async def tours_update_tour(
        self,
        tour_id: str,
        run_as: ToursUpdateTourParamRunAs | None = None,
    ) -> TourDetails: ...


class ToursClient(ToursClientProtocol):
    """Client for tours endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def tours_index(
        self,
    ) -> TourList:
        """
        Index

        Return list of available tours.

        Returns:
            TourList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tours"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), TourList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tours_index(
        self,
    ) -> TourList:
        """
        Index

        Return list of available tours.

        Returns:
            TourList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tours"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), TourList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tours_generate_generate_tour(
        self,
        tool_id: str,
        tool_version: str,
        performs_upload: bool | None = None,
        run_as: ToursGenerateGenerateTourParamRunAs | None = None,
    ) -> GenerateTourResponse:
        """
        Generate Tour

        Generate a tour designed for the given tool.

        Args:
            tool_id (str)            :
            tool_version (str)       :
            performs_upload (bool | None)
                                     :
            run-as (ToursGenerateGenerateTourParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GenerateTourResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tours/generate"

        params: dict[str, Any] = {
            "tool_id": DataclassSerializer.serialize(tool_id),
            "tool_version": DataclassSerializer.serialize(tool_version),
            **(
                {"performs_upload": DataclassSerializer.serialize(performs_upload)}
                if performs_upload is not None
                else {}
            ),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GenerateTourResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tours_generate_generate_tour(
        self,
        tool_id: str,
        tool_version: str,
        performs_upload: bool | None = None,
        run_as: ToursGenerateGenerateTourParamRunAs | None = None,
    ) -> GenerateTourResponse:
        """
        Generate Tour

        Generate a tour designed for the given tool.

        Args:
            tool_id (str)            :
            tool_version (str)       :
            performs_upload (bool | None)
                                     :
            run-as (ToursGenerateGenerateTourParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            GenerateTourResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/tours/generate"

        params: dict[str, Any] = {
            "tool_id": DataclassSerializer.serialize(tool_id),
            "tool_version": DataclassSerializer.serialize(tool_version),
            **(
                {"performs_upload": DataclassSerializer.serialize(performs_upload)}
                if performs_upload is not None
                else {}
            ),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), GenerateTourResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tours_show(
        self,
        tour_id: str,
    ) -> TourDetails:
        """
        Show

        Return a tour definition.

        Args:
            tour_id (str)            :

        Returns:
            TourDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        tour_id = DataclassSerializer.serialize(tour_id)

        url = f"{self.base_url}/api/tours/{tour_id}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), TourDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tours_show(
        self,
        tour_id: str,
    ) -> TourDetails:
        """
        Show

        Return a tour definition.

        Args:
            tour_id (str)            :

        Returns:
            TourDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        tour_id = DataclassSerializer.serialize(tour_id)

        url = f"{self.base_url}/api/tours/{tour_id}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), TourDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tours_update_tour(
        self,
        tour_id: str,
        run_as: ToursUpdateTourParamRunAs | None = None,
    ) -> TourDetails:
        """
        Update Tour

        Return a tour definition.

        Args:
            tour_id (str)            :
            run-as (ToursUpdateTourParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            TourDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        tour_id = DataclassSerializer.serialize(tour_id)

        url = f"{self.base_url}/api/tours/{tour_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), TourDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def tours_update_tour(
        self,
        tour_id: str,
        run_as: ToursUpdateTourParamRunAs | None = None,
    ) -> TourDetails:
        """
        Update Tour

        Return a tour definition.

        Args:
            tour_id (str)            :
            run-as (ToursUpdateTourParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            TourDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        tour_id = DataclassSerializer.serialize(tour_id)

        url = f"{self.base_url}/api/tours/{tour_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), TourDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
