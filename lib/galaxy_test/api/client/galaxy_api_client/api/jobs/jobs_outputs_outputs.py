from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.job_output_association import JobOutputAssociation
from ...models.job_output_collection_association import JobOutputCollectionAssociation
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/jobs/{job_id}/outputs".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> JobOutputAssociation | JobOutputCollectionAssociation:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = JobOutputAssociation.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_1 = JobOutputCollectionAssociation.from_dict(data)

                return response_200_item_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if 400 <= response.status_code <= 499:
        response_4xx = MessageExceptionModel.from_dict(response.json())

        return response_4xx

    if 500 <= response.status_code <= 599:
        response_5xx = MessageExceptionModel.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation]]:
    """Returns output datasets created by a job.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation] | None:
    """Returns output datasets created by a job.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation]]:
    """Returns output datasets created by a job.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation] | None:
    """Returns output datasets created by a job.

    Args:
        job_id (str):  Example: 0123456789ABCDEF.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel | list[JobOutputAssociation | JobOutputCollectionAssociation]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            run_as=run_as,
        )
    ).parsed
