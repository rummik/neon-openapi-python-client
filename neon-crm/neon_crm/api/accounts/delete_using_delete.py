from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_id_result import AccountIdResult
from ...types import Response


def _get_kwargs(
    id: str,
    contact_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/accounts/{id}/contacts/{contact_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountIdResult, Any]]:
    if response.status_code == 200:
        response_200 = AccountIdResult.from_dict(response.json())

        return response_200
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 222:
        response_222 = AccountIdResult.from_dict(response.json())

        return response_222
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AccountIdResult, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    contact_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[AccountIdResult, Any]]:
    """Deletes an contact

    Args:
        id (str):
        contact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountIdResult, Any]]
    """

    kwargs = _get_kwargs(
        id=id,
        contact_id=contact_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    contact_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AccountIdResult, Any]]:
    """Deletes an contact

    Args:
        id (str):
        contact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountIdResult, Any]
    """

    return sync_detailed(
        id=id,
        contact_id=contact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    contact_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[AccountIdResult, Any]]:
    """Deletes an contact

    Args:
        id (str):
        contact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountIdResult, Any]]
    """

    kwargs = _get_kwargs(
        id=id,
        contact_id=contact_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    contact_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[AccountIdResult, Any]]:
    """Deletes an contact

    Args:
        id (str):
        contact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountIdResult, Any]
    """

    return (
        await asyncio_detailed(
            id=id,
            contact_id=contact_id,
            client=client,
        )
    ).parsed
