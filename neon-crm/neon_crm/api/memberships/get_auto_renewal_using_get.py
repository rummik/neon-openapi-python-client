from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.membership_auto_renewal import MembershipAutoRenewal
from ...types import Response


def _get_kwargs(
    membership_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/memberships/{membership_id}/autoRenewal",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MembershipAutoRenewal]]:
    if response.status_code == 200:
        response_200 = MembershipAutoRenewal.from_dict(response.json())

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
) -> Response[Union[Any, MembershipAutoRenewal]]:
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
) -> Response[Union[Any, MembershipAutoRenewal]]:
    """Get auto-renewal of a membership

    Args:
        membership_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MembershipAutoRenewal]]
    """

    kwargs = _get_kwargs(
        membership_id=membership_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    membership_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, MembershipAutoRenewal]]:
    """Get auto-renewal of a membership

    Args:
        membership_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MembershipAutoRenewal]
    """

    return sync_detailed(
        membership_id=membership_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    membership_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, MembershipAutoRenewal]]:
    """Get auto-renewal of a membership

    Args:
        membership_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MembershipAutoRenewal]]
    """

    kwargs = _get_kwargs(
        membership_id=membership_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    membership_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, MembershipAutoRenewal]]:
    """Get auto-renewal of a membership

    Args:
        membership_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MembershipAutoRenewal]
    """

    return (
        await asyncio_detailed(
            membership_id=membership_id,
            client=client,
        )
    ).parsed
