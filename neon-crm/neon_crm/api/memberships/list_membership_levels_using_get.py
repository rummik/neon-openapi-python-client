from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_membership_levels_using_get_status import ListMembershipLevelsUsingGETStatus
from ...models.membership_levels_response import MembershipLevelsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListMembershipLevelsUsingGETStatus] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["currentPage"] = current_page

    params["pageSize"] = page_size

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/memberships/levels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MembershipLevelsResponse]]:
    if response.status_code == 200:
        response_200 = MembershipLevelsResponse.from_dict(response.json())

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
) -> Response[Union[Any, MembershipLevelsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListMembershipLevelsUsingGETStatus] = UNSET,
) -> Response[Union[Any, MembershipLevelsResponse]]:
    """Get a list of membership levels

    Args:
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        status (Union[Unset, ListMembershipLevelsUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MembershipLevelsResponse]]
    """

    kwargs = _get_kwargs(
        current_page=current_page,
        page_size=page_size,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListMembershipLevelsUsingGETStatus] = UNSET,
) -> Optional[Union[Any, MembershipLevelsResponse]]:
    """Get a list of membership levels

    Args:
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        status (Union[Unset, ListMembershipLevelsUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MembershipLevelsResponse]
    """

    return sync_detailed(
        client=client,
        current_page=current_page,
        page_size=page_size,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListMembershipLevelsUsingGETStatus] = UNSET,
) -> Response[Union[Any, MembershipLevelsResponse]]:
    """Get a list of membership levels

    Args:
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        status (Union[Unset, ListMembershipLevelsUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MembershipLevelsResponse]]
    """

    kwargs = _get_kwargs(
        current_page=current_page,
        page_size=page_size,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListMembershipLevelsUsingGETStatus] = UNSET,
) -> Optional[Union[Any, MembershipLevelsResponse]]:
    """Get a list of membership levels

    Args:
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        status (Union[Unset, ListMembershipLevelsUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MembershipLevelsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            current_page=current_page,
            page_size=page_size,
            status=status,
        )
    ).parsed
