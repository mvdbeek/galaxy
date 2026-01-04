from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    force: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_force: bool | None | Unset
    if isinstance(force, Unset):
        json_force = UNSET
    else:
        json_force = force
    params["force"] = json_force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/histories/{history_id}/archive/restore".format(
            history_id=quote(str(history_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MessageExceptionModel | None:
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
) -> Response[MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    force: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Restore an archived history.

     Restores an archived history and returns it.

    Restoring an archived history will add it back to the list of active histories of the user (unless
    it was purged).

    **Warning**: Please note that histories that are associated with an archive export might be purged
    after export, so un-archiving them
    will not restore the datasets that were in the history before it was archived. You will need to
    import back the archive export
    record to restore the history and its datasets as a new copy. See `/api/histories/from_store_async`
    for more information.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        force (bool | None | Unset): If true, the history will be un-archived even if it has an
            associated archive export record and was purged.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        force=force,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    *,
    client: AuthenticatedClient,
    force: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Restore an archived history.

     Restores an archived history and returns it.

    Restoring an archived history will add it back to the list of active histories of the user (unless
    it was purged).

    **Warning**: Please note that histories that are associated with an archive export might be purged
    after export, so un-archiving them
    will not restore the datasets that were in the history before it was archived. You will need to
    import back the archive export
    record to restore the history and its datasets as a new copy. See `/api/histories/from_store_async`
    for more information.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        force (bool | None | Unset): If true, the history will be un-archived even if it has an
            associated archive export record and was purged.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        force=force,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    force: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[MessageExceptionModel]:
    """Restore an archived history.

     Restores an archived history and returns it.

    Restoring an archived history will add it back to the list of active histories of the user (unless
    it was purged).

    **Warning**: Please note that histories that are associated with an archive export might be purged
    after export, so un-archiving them
    will not restore the datasets that were in the history before it was archived. You will need to
    import back the archive export
    record to restore the history and its datasets as a new copy. See `/api/histories/from_store_async`
    for more information.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        force (bool | None | Unset): If true, the history will be un-archived even if it has an
            associated archive export record and was purged.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        force=force,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient,
    force: bool | None | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> MessageExceptionModel | None:
    """Restore an archived history.

     Restores an archived history and returns it.

    Restoring an archived history will add it back to the list of active histories of the user (unless
    it was purged).

    **Warning**: Please note that histories that are associated with an archive export might be purged
    after export, so un-archiving them
    will not restore the datasets that were in the history before it was archived. You will need to
    import back the archive export
    record to restore the history and its datasets as a new copy. See `/api/histories/from_store_async`
    for more information.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        force (bool | None | Unset): If true, the history will be un-archived even if it has an
            associated archive export record and was purged.
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            force=force,
            run_as=run_as,
        )
    ).parsed
