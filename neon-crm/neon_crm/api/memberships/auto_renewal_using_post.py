from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.membership_auto_renewal import MembershipAutoRenewal
from ...models.response_entity import ResponseEntity
from ...types import Response


def _get_kwargs(
    membership_id: str,
    *,
    body: MembershipAutoRenewal,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/memberships/{membership_id}/autoRenewal",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ResponseEntity]]:
    if response.status_code == 200:
        response_200 = ResponseEntity.from_dict(response.json())

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
) -> Response[Union[Any, ResponseEntity]]:
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
    body: MembershipAutoRenewal,
) -> Response[Union[Any, ResponseEntity]]:
    """Edit auto-renewal for a membership

    Args:
        membership_id (str):
        body (MembershipAutoRenewal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ResponseEntity]]
    """

    kwargs = _get_kwargs(
        membership_id=membership_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    membership_id: str,
    *,
    client: AuthenticatedClient,
    body: MembershipAutoRenewal,
) -> Optional[Union[Any, ResponseEntity]]:
    """Edit auto-renewal for a membership

    Args:
        membership_id (str):
        body (MembershipAutoRenewal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ResponseEntity]
    """

    return sync_detailed(
        membership_id=membership_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    membership_id: str,
    *,
    client: AuthenticatedClient,
    body: MembershipAutoRenewal,
) -> Response[Union[Any, ResponseEntity]]:
    """Edit auto-renewal for a membership

    Args:
        membership_id (str):
        body (MembershipAutoRenewal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ResponseEntity]]
    """

    kwargs = _get_kwargs(
        membership_id=membership_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    membership_id: str,
    *,
    client: AuthenticatedClient,
    body: MembershipAutoRenewal,
) -> Optional[Union[Any, ResponseEntity]]:
    """Edit auto-renewal for a membership

    Args:
        membership_id (str):
        body (MembershipAutoRenewal):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ResponseEntity]
    """

    return (
        await asyncio_detailed(
            membership_id=membership_id,
            client=client,
            body=body,
        )
    ).parsed
