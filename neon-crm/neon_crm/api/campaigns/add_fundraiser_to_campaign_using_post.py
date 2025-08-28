from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_fundraiser_to_campaign_using_post_response_200 import AddFundraiserToCampaignUsingPOSTResponse200
from ...models.campaign_fundraiser import CampaignFundraiser
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: CampaignFundraiser,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/campaigns/{id}/p2p",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]]:
    if response.status_code == 200:
        response_200 = AddFundraiserToCampaignUsingPOSTResponse200.from_dict(response.json())

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
) -> Response[Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CampaignFundraiser,
) -> Response[Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]]:
    """Add a fundraiser to a campaign

    Args:
        id (str):
        body (CampaignFundraiser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CampaignFundraiser,
) -> Optional[Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]]:
    """Add a fundraiser to a campaign

    Args:
        id (str):
        body (CampaignFundraiser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CampaignFundraiser,
) -> Response[Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]]:
    """Add a fundraiser to a campaign

    Args:
        id (str):
        body (CampaignFundraiser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CampaignFundraiser,
) -> Optional[Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]]:
    """Add a fundraiser to a campaign

    Args:
        id (str):
        body (CampaignFundraiser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddFundraiserToCampaignUsingPOSTResponse200, Any]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
