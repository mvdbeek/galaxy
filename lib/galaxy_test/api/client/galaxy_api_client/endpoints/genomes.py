from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_89 import AnonymousArrayItem89
from ..models.genomes_index_param_run_as import GenomesIndexParamRunAs
from ..models.genomes_indexes_indexes_param_run_as import GenomesIndexesIndexesParamRunAs
from ..models.genomes_sequences_sequences_param_run_as import GenomesSequencesSequencesParamRunAs
from ..models.genomes_show_param_run_as import GenomesShowParamRunAs


@runtime_checkable
class GenomesClientProtocol(Protocol):
    """Protocol defining the interface of GenomesClient for dependency injection."""

    async def genomes_index(
        self,
        chrom_info: bool | None = None,
        run_as: GenomesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem89]: ...

    async def genomes_index(
        self,
        chrom_info: bool | None = None,
        run_as: GenomesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem89]: ...

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
    ) -> dict[str, Any]: ...

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
    ) -> dict[str, Any]: ...

    async def genomes_indexes_indexes(
        self,
        id_: str,
        type_: str | None = None,
        format_: str | None = None,
        run_as: GenomesIndexesIndexesParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def genomes_indexes_indexes(
        self,
        id_: str,
        type_: str | None = None,
        format_: str | None = None,
        run_as: GenomesIndexesIndexesParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def genomes_sequences_sequences(
        self,
        id_: str,
        reference: bool | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format_: str | None = None,
        run_as: GenomesSequencesSequencesParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def genomes_sequences_sequences(
        self,
        id_: str,
        reference: bool | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format_: str | None = None,
        run_as: GenomesSequencesSequencesParamRunAs | None = None,
    ) -> dict[str, Any]: ...


class GenomesClient(GenomesClientProtocol):
    """Client for genomes endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def genomes_index(
        self,
        chrom_info: bool | None = None,
        run_as: GenomesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem89]:
        """
        Return a list of installed genomes

        Args:
            chrom_info (bool | None) : If true, return genome keys with chromosome lengths
            run-as (GenomesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem89]: Installed genomes

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes"

        params: dict[str, Any] = {
            **({"chrom_info": DataclassSerializer.serialize(chrom_info)} if chrom_info is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem89])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def genomes_index(
        self,
        chrom_info: bool | None = None,
        run_as: GenomesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem89]:
        """
        Return a list of installed genomes

        Args:
            chrom_info (bool | None) : If true, return genome keys with chromosome lengths
            run-as (GenomesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem89]: Installed genomes

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes"

        params: dict[str, Any] = {
            **({"chrom_info": DataclassSerializer.serialize(chrom_info)} if chrom_info is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem89])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Return information about build <id>

        Args:
            id (str)                 : Genome ID
            reference (bool | None)  : If true, return reference data
            num (int | None)         : Limits size of returned data
            chrom (str | None)       : Limits size of returned data
            low (int | None)         : Limits size of returned data
            high (int | None)        : Limits size of returned data
            format (str | None)      : Format
            run-as (GenomesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Information about genome build <id>

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/genomes/{id_}"

        params: dict[str, Any] = {
            **({"reference": DataclassSerializer.serialize(reference)} if reference is not None else {}),
            **({"num": DataclassSerializer.serialize(num)} if num is not None else {}),
            **({"chrom": DataclassSerializer.serialize(chrom)} if chrom is not None else {}),
            **({"low": DataclassSerializer.serialize(low)} if low is not None else {}),
            **({"high": DataclassSerializer.serialize(high)} if high is not None else {}),
            **({"format": DataclassSerializer.serialize(format_)} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Return information about build <id>

        Args:
            id (str)                 : Genome ID
            reference (bool | None)  : If true, return reference data
            num (int | None)         : Limits size of returned data
            chrom (str | None)       : Limits size of returned data
            low (int | None)         : Limits size of returned data
            high (int | None)        : Limits size of returned data
            format (str | None)      : Format
            run-as (GenomesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Information about genome build <id>

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/genomes/{id_}"

        params: dict[str, Any] = {
            **({"reference": DataclassSerializer.serialize(reference)} if reference is not None else {}),
            **({"num": DataclassSerializer.serialize(num)} if num is not None else {}),
            **({"chrom": DataclassSerializer.serialize(chrom)} if chrom is not None else {}),
            **({"low": DataclassSerializer.serialize(low)} if low is not None else {}),
            **({"high": DataclassSerializer.serialize(high)} if high is not None else {}),
            **({"format": DataclassSerializer.serialize(format_)} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def genomes_indexes_indexes(
        self,
        id_: str,
        type_: str | None = None,
        format_: str | None = None,
        run_as: GenomesIndexesIndexesParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Return all available indexes for a genome id for provided type

        Args:
            id (str)                 : Genome ID
            type (str | None)        : Index type
            format (str | None)      : Format
            run-as (GenomesIndexesIndexesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Indexes for a genome id for provided type

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/genomes/{id_}/indexes"

        params: dict[str, Any] = {
            **({"type": DataclassSerializer.serialize(type_)} if type_ is not None else {}),
            **({"format": DataclassSerializer.serialize(format_)} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def genomes_indexes_indexes(
        self,
        id_: str,
        type_: str | None = None,
        format_: str | None = None,
        run_as: GenomesIndexesIndexesParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Return all available indexes for a genome id for provided type

        Args:
            id (str)                 : Genome ID
            type (str | None)        : Index type
            format (str | None)      : Format
            run-as (GenomesIndexesIndexesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Indexes for a genome id for provided type

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/genomes/{id_}/indexes"

        params: dict[str, Any] = {
            **({"type": DataclassSerializer.serialize(type_)} if type_ is not None else {}),
            **({"format": DataclassSerializer.serialize(format_)} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Return raw sequence data

        Args:
            id (str)                 : Genome ID
            reference (bool | None)  : If true, return reference data
            chrom (str | None)       : Limits size of returned data
            low (int | None)         : Limits size of returned data
            high (int | None)        : Limits size of returned data
            format (str | None)      : Format
            run-as (GenomesSequencesSequencesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Raw sequence data

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/genomes/{id_}/sequences"

        params: dict[str, Any] = {
            **({"reference": DataclassSerializer.serialize(reference)} if reference is not None else {}),
            **({"chrom": DataclassSerializer.serialize(chrom)} if chrom is not None else {}),
            **({"low": DataclassSerializer.serialize(low)} if low is not None else {}),
            **({"high": DataclassSerializer.serialize(high)} if high is not None else {}),
            **({"format": DataclassSerializer.serialize(format_)} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Return raw sequence data

        Args:
            id (str)                 : Genome ID
            reference (bool | None)  : If true, return reference data
            chrom (str | None)       : Limits size of returned data
            low (int | None)         : Limits size of returned data
            high (int | None)        : Limits size of returned data
            format (str | None)      : Format
            run-as (GenomesSequencesSequencesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Raw sequence data

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/genomes/{id_}/sequences"

        params: dict[str, Any] = {
            **({"reference": DataclassSerializer.serialize(reference)} if reference is not None else {}),
            **({"chrom": DataclassSerializer.serialize(chrom)} if chrom is not None else {}),
            **({"low": DataclassSerializer.serialize(low)} if low is not None else {}),
            **({"high": DataclassSerializer.serialize(high)} if high is not None else {}),
            **({"format": DataclassSerializer.serialize(format_)} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
