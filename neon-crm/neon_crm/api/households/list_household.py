from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_message import APIMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    household_id: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["householdId"] = household_id

    params["accountId"] = account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/households/listHouseholds",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["APIMessage"]]:
    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = APIMessage.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400
    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = APIMessage.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404
    if response.status_code == 415:
        response_415 = []
        _response_415 = response.json()
        for response_415_item_data in _response_415:
            response_415_item = APIMessage.from_dict(response_415_item_data)

            response_415.append(response_415_item)

        return response_415
    if response.status_code == 500:
        response_500 = []
        _response_500 = response.json()
        for response_500_item_data in _response_500:
            response_500_item = APIMessage.from_dict(response_500_item_data)

            response_500.append(response_500_item)

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["APIMessage"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    household_id: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Response[list["APIMessage"]]:
    """List households

    Args:
        household_id (Union[Unset, str]):
        account_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['APIMessage']]
    """

    kwargs = _get_kwargs(
        household_id=household_id,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    household_id: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Optional[list["APIMessage"]]:
    """List households

    Args:
        household_id (Union[Unset, str]):
        account_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['APIMessage']
    """

    return sync_detailed(
        client=client,
        household_id=household_id,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    household_id: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Response[list["APIMessage"]]:
    """List households

    Args:
        household_id (Union[Unset, str]):
        account_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['APIMessage']]
    """

    kwargs = _get_kwargs(
        household_id=household_id,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    household_id: Union[Unset, str] = UNSET,
    account_id: Union[Unset, str] = UNSET,
) -> Optional[list["APIMessage"]]:
    """List households

    Args:
        household_id (Union[Unset, str]):
        account_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['APIMessage']
    """

    return (
        await asyncio_detailed(
            client=client,
            household_id=household_id,
            account_id=account_id,
        )
    ).parsed
