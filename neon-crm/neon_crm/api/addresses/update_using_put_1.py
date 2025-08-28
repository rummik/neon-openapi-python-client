from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address import Address
from ...models.update_using_put1_response_200 import UpdateUsingPUT1Response200
from ...types import Response


def _get_kwargs(
    address_id: str,
    *,
    body: Address,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/addresses/{address_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateUsingPUT1Response200]]:
    if response.status_code == 200:
        response_200 = UpdateUsingPUT1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UpdateUsingPUT1Response200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address_id: str,
    *,
    client: AuthenticatedClient,
    body: Address,
) -> Response[Union[Any, UpdateUsingPUT1Response200]]:
    """Updates an address

    Args:
        address_id (str):
        body (Address):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateUsingPUT1Response200]]
    """

    kwargs = _get_kwargs(
        address_id=address_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address_id: str,
    *,
    client: AuthenticatedClient,
    body: Address,
) -> Optional[Union[Any, UpdateUsingPUT1Response200]]:
    """Updates an address

    Args:
        address_id (str):
        body (Address):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateUsingPUT1Response200]
    """

    return sync_detailed(
        address_id=address_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    address_id: str,
    *,
    client: AuthenticatedClient,
    body: Address,
) -> Response[Union[Any, UpdateUsingPUT1Response200]]:
    """Updates an address

    Args:
        address_id (str):
        body (Address):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateUsingPUT1Response200]]
    """

    kwargs = _get_kwargs(
        address_id=address_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address_id: str,
    *,
    client: AuthenticatedClient,
    body: Address,
) -> Optional[Union[Any, UpdateUsingPUT1Response200]]:
    """Updates an address

    Args:
        address_id (str):
        body (Address):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateUsingPUT1Response200]
    """

    return (
        await asyncio_detailed(
            address_id=address_id,
            client=client,
            body=body,
        )
    ).parsed
