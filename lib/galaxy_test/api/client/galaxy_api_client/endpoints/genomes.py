from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.anonymous_array_item_133 import AnonymousArrayItem133
from ..models.genomes_index_param_run_as import GenomesIndexParamRunAs
from ..models.genomes_indexes_indexes_param_run_as import GenomesIndexesIndexesParamRunAs
from ..models.genomes_sequences_sequences_param_run_as import GenomesSequencesSequencesParamRunAs
from ..models.genomes_show_param_run_as import GenomesShowParamRunAs


class GenomesClient:
    """Client for genomes endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def genomes_index_2_2(
        self,
        chrom_info: bool | None = None,
        run_as: GenomesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem133]:
        """
        Return a list of installed genomes

        Args:
            chrom_info (Optional[bool])
                                     : If true, return genome keys with chromosome lengths
            run-as (Optional[GenomesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem133]: Installed genomes

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes"

        params: dict[str, Any] = {
            **({"chrom_info": chrom_info} if chrom_info is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem133], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def genomes_index_2_2(
        self,
        chrom_info: bool | None = None,
        run_as: GenomesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem133]:
        """
        Return a list of installed genomes

        Args:
            chrom_info (Optional[bool])
                                     : If true, return genome keys with chromosome lengths
            run-as (Optional[GenomesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem133]: Installed genomes

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes"

        params: dict[str, Any] = {
            **({"chrom_info": chrom_info} if chrom_info is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem133], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def genomes_show_2_2(
        self,
        id_: str,
        reference: bool | None = None,
        num: int | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format_: str | None = None,
        run_as: GenomesShowParamRunAs | None = None,
    ) -> Any:
        """
        Return information about build <id>

        Args:
            id (str)                 : Genome ID
            reference (Optional[bool]): If true, return reference data
            num (Optional[int])      : Limits size of returned data
            chrom (Optional[str])    : Limits size of returned data
            low (Optional[int])      : Limits size of returned data
            high (Optional[int])     : Limits size of returned data
            format (Optional[str])   : Format
            run-as (Optional[GenomesShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Information about genome build <id>

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes/{id_}"

        params: dict[str, Any] = {
            **({"reference": reference} if reference is not None else {}),
            **({"num": num} if num is not None else {}),
            **({"chrom": chrom} if chrom is not None else {}),
            **({"low": low} if low is not None else {}),
            **({"high": high} if high is not None else {}),
            **({"format": format_} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def genomes_show_2_2(
        self,
        id_: str,
        reference: bool | None = None,
        num: int | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format_: str | None = None,
        run_as: GenomesShowParamRunAs | None = None,
    ) -> Any:
        """
        Return information about build <id>

        Args:
            id (str)                 : Genome ID
            reference (Optional[bool]): If true, return reference data
            num (Optional[int])      : Limits size of returned data
            chrom (Optional[str])    : Limits size of returned data
            low (Optional[int])      : Limits size of returned data
            high (Optional[int])     : Limits size of returned data
            format (Optional[str])   : Format
            run-as (Optional[GenomesShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Information about genome build <id>

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes/{id_}"

        params: dict[str, Any] = {
            **({"reference": reference} if reference is not None else {}),
            **({"num": num} if num is not None else {}),
            **({"chrom": chrom} if chrom is not None else {}),
            **({"low": low} if low is not None else {}),
            **({"high": high} if high is not None else {}),
            **({"format": format_} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def genomes_indexes_indexes_2_2(
        self,
        id_: str,
        type_: str | None = "fasta_indexes",
        format_: str | None = None,
        run_as: GenomesIndexesIndexesParamRunAs | None = None,
    ) -> Any:
        """
        Return all available indexes for a genome id for provided type

        Args:
            id (str)                 : Genome ID
            type (Optional[str])     : Index type
            format (Optional[str])   : Format
            run-as (Optional[GenomesIndexesIndexesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Indexes for a genome id for provided type

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes/{id_}/indexes"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"format": format_} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def genomes_indexes_indexes_2_2(
        self,
        id_: str,
        type_: str | None = "fasta_indexes",
        format_: str | None = None,
        run_as: GenomesIndexesIndexesParamRunAs | None = None,
    ) -> Any:
        """
        Return all available indexes for a genome id for provided type

        Args:
            id (str)                 : Genome ID
            type (Optional[str])     : Index type
            format (Optional[str])   : Format
            run-as (Optional[GenomesIndexesIndexesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Indexes for a genome id for provided type

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes/{id_}/indexes"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"format": format_} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def genomes_sequences_sequences_2_2(
        self,
        id_: str,
        reference: bool | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format_: str | None = None,
        run_as: GenomesSequencesSequencesParamRunAs | None = None,
    ) -> Any:
        """
        Return raw sequence data

        Args:
            id (str)                 : Genome ID
            reference (Optional[bool]): If true, return reference data
            chrom (Optional[str])    : Limits size of returned data
            low (Optional[int])      : Limits size of returned data
            high (Optional[int])     : Limits size of returned data
            format (Optional[str])   : Format
            run-as (Optional[GenomesSequencesSequencesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Raw sequence data

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes/{id_}/sequences"

        params: dict[str, Any] = {
            **({"reference": reference} if reference is not None else {}),
            **({"chrom": chrom} if chrom is not None else {}),
            **({"low": low} if low is not None else {}),
            **({"high": high} if high is not None else {}),
            **({"format": format_} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def genomes_sequences_sequences_2_2(
        self,
        id_: str,
        reference: bool | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format_: str | None = None,
        run_as: GenomesSequencesSequencesParamRunAs | None = None,
    ) -> Any:
        """
        Return raw sequence data

        Args:
            id (str)                 : Genome ID
            reference (Optional[bool]): If true, return reference data
            chrom (Optional[str])    : Limits size of returned data
            low (Optional[int])      : Limits size of returned data
            high (Optional[int])     : Limits size of returned data
            format (Optional[str])   : Format
            run-as (Optional[GenomesSequencesSequencesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Raw sequence data

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/genomes/{id_}/sequences"

        params: dict[str, Any] = {
            **({"reference": reference} if reference is not None else {}),
            **({"chrom": chrom} if chrom is not None else {}),
            **({"low": low} if low is not None else {}),
            **({"high": high} if high is not None else {}),
            **({"format": format_} if format_ is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
