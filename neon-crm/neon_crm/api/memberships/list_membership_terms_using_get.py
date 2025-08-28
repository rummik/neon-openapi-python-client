from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.membership_terms_response import MembershipTermsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    current_page: Union[Unset, int] = UNSET,
    level_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["currentPage"] = current_page

    params["levelId"] = level_id

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/memberships/terms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MembershipTermsResponse]]:
    if response.status_code == 200:
        response_200 = MembershipTermsResponse.from_dict(response.json())

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
) -> Response[Union[Any, MembershipTermsResponse]]:
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
    level_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[Any, MembershipTermsResponse]]:
    """Get a list of membership terms

    Args:
        current_page (Union[Unset, int]):
        level_id (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MembershipTermsResponse]]
    """

    kwargs = _get_kwargs(
        current_page=current_page,
        level_id=level_id,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    level_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, MembershipTermsResponse]]:
    """Get a list of membership terms

    Args:
        current_page (Union[Unset, int]):
        level_id (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MembershipTermsResponse]
    """

    return sync_detailed(
        client=client,
        current_page=current_page,
        level_id=level_id,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    level_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[Any, MembershipTermsResponse]]:
    """Get a list of membership terms

    Args:
        current_page (Union[Unset, int]):
        level_id (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MembershipTermsResponse]]
    """

    kwargs = _get_kwargs(
        current_page=current_page,
        level_id=level_id,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    level_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, MembershipTermsResponse]]:
    """Get a list of membership terms

    Args:
        current_page (Union[Unset, int]):
        level_id (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MembershipTermsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            current_page=current_page,
            level_id=level_id,
            page_size=page_size,
        )
    ).parsed
