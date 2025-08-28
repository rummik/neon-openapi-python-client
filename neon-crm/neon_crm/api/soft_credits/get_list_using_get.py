from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.soft_credit_search_result import SoftCreditSearchResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    donation_id: Union[Unset, str] = UNSET,
    event_registration_id: Union[Unset, str] = UNSET,
    membership_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params["currentPage"] = current_page

    params["donationId"] = donation_id

    params["eventRegistrationId"] = event_registration_id

    params["membershipId"] = membership_id

    params["orderId"] = order_id

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/softCredits",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SoftCreditSearchResult]]:
    if response.status_code == 200:
        response_200 = SoftCreditSearchResult.from_dict(response.json())

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
) -> Response[Union[Any, SoftCreditSearchResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    donation_id: Union[Unset, str] = UNSET,
    event_registration_id: Union[Unset, str] = UNSET,
    membership_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[Any, SoftCreditSearchResult]]:
    """Gets a list of soft credits

    Args:
        account_id (Union[Unset, str]):
        current_page (Union[Unset, int]):
        donation_id (Union[Unset, str]):
        event_registration_id (Union[Unset, str]):
        membership_id (Union[Unset, str]):
        order_id (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SoftCreditSearchResult]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        current_page=current_page,
        donation_id=donation_id,
        event_registration_id=event_registration_id,
        membership_id=membership_id,
        order_id=order_id,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    donation_id: Union[Unset, str] = UNSET,
    event_registration_id: Union[Unset, str] = UNSET,
    membership_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, SoftCreditSearchResult]]:
    """Gets a list of soft credits

    Args:
        account_id (Union[Unset, str]):
        current_page (Union[Unset, int]):
        donation_id (Union[Unset, str]):
        event_registration_id (Union[Unset, str]):
        membership_id (Union[Unset, str]):
        order_id (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SoftCreditSearchResult]
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        current_page=current_page,
        donation_id=donation_id,
        event_registration_id=event_registration_id,
        membership_id=membership_id,
        order_id=order_id,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    donation_id: Union[Unset, str] = UNSET,
    event_registration_id: Union[Unset, str] = UNSET,
    membership_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[Any, SoftCreditSearchResult]]:
    """Gets a list of soft credits

    Args:
        account_id (Union[Unset, str]):
        current_page (Union[Unset, int]):
        donation_id (Union[Unset, str]):
        event_registration_id (Union[Unset, str]):
        membership_id (Union[Unset, str]):
        order_id (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SoftCreditSearchResult]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        current_page=current_page,
        donation_id=donation_id,
        event_registration_id=event_registration_id,
        membership_id=membership_id,
        order_id=order_id,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    donation_id: Union[Unset, str] = UNSET,
    event_registration_id: Union[Unset, str] = UNSET,
    membership_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, SoftCreditSearchResult]]:
    """Gets a list of soft credits

    Args:
        account_id (Union[Unset, str]):
        current_page (Union[Unset, int]):
        donation_id (Union[Unset, str]):
        event_registration_id (Union[Unset, str]):
        membership_id (Union[Unset, str]):
        order_id (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SoftCreditSearchResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            current_page=current_page,
            donation_id=donation_id,
            event_registration_id=event_registration_id,
            membership_id=membership_id,
            order_id=order_id,
            page_size=page_size,
        )
    ).parsed
