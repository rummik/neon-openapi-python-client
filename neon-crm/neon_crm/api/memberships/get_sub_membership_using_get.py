from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sub_membership import SubMembership
from ...types import UNSET, Response, Unset


def _get_kwargs(
    membership_id: str,
    *,
    is_current_employee: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["isCurrentEmployee"] = is_current_employee

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/memberships/{membership_id}/subMembers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["SubMembership"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SubMembership.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
) -> Response[Union[Any, list["SubMembership"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    membership_id: str,
    *,
    client: AuthenticatedClient,
    is_current_employee: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["SubMembership"]]]:
    """Get a list of sub-membership

    Args:
        membership_id (str):
        is_current_employee (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['SubMembership']]]
    """

    kwargs = _get_kwargs(
        membership_id=membership_id,
        is_current_employee=is_current_employee,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    membership_id: str,
    *,
    client: AuthenticatedClient,
    is_current_employee: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["SubMembership"]]]:
    """Get a list of sub-membership

    Args:
        membership_id (str):
        is_current_employee (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['SubMembership']]
    """

    return sync_detailed(
        membership_id=membership_id,
        client=client,
        is_current_employee=is_current_employee,
    ).parsed


async def asyncio_detailed(
    membership_id: str,
    *,
    client: AuthenticatedClient,
    is_current_employee: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["SubMembership"]]]:
    """Get a list of sub-membership

    Args:
        membership_id (str):
        is_current_employee (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['SubMembership']]]
    """

    kwargs = _get_kwargs(
        membership_id=membership_id,
        is_current_employee=is_current_employee,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    membership_id: str,
    *,
    client: AuthenticatedClient,
    is_current_employee: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["SubMembership"]]]:
    """Get a list of sub-membership

    Args:
        membership_id (str):
        is_current_employee (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['SubMembership']]
    """

    return (
        await asyncio_detailed(
            membership_id=membership_id,
            client=client,
            is_current_employee=is_current_employee,
        )
    ).parsed
