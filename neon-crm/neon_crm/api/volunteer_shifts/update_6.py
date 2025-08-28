from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_message import APIMessage
from ...models.id_result import IdResult
from ...models.opportunity_shift import OpportunityShift
from ...types import Response


def _get_kwargs(
    opportunity_id: str,
    shift_id: str,
    *,
    body: OpportunityShift,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/opportunities/{opportunity_id}/shifts/{shift_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[IdResult, list["APIMessage"]]]:
    if response.status_code == 200:
        response_200 = IdResult.from_dict(response.json())

        return response_200
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
) -> Response[Union[IdResult, list["APIMessage"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    opportunity_id: str,
    shift_id: str,
    *,
    client: AuthenticatedClient,
    body: OpportunityShift,
) -> Response[Union[IdResult, list["APIMessage"]]]:
    """Update a volunteer shift

    Args:
        opportunity_id (str):
        shift_id (str):
        body (OpportunityShift):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IdResult, list['APIMessage']]]
    """

    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
        shift_id=shift_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    opportunity_id: str,
    shift_id: str,
    *,
    client: AuthenticatedClient,
    body: OpportunityShift,
) -> Optional[Union[IdResult, list["APIMessage"]]]:
    """Update a volunteer shift

    Args:
        opportunity_id (str):
        shift_id (str):
        body (OpportunityShift):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IdResult, list['APIMessage']]
    """

    return sync_detailed(
        opportunity_id=opportunity_id,
        shift_id=shift_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    opportunity_id: str,
    shift_id: str,
    *,
    client: AuthenticatedClient,
    body: OpportunityShift,
) -> Response[Union[IdResult, list["APIMessage"]]]:
    """Update a volunteer shift

    Args:
        opportunity_id (str):
        shift_id (str):
        body (OpportunityShift):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IdResult, list['APIMessage']]]
    """

    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
        shift_id=shift_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    opportunity_id: str,
    shift_id: str,
    *,
    client: AuthenticatedClient,
    body: OpportunityShift,
) -> Optional[Union[IdResult, list["APIMessage"]]]:
    """Update a volunteer shift

    Args:
        opportunity_id (str):
        shift_id (str):
        body (OpportunityShift):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IdResult, list['APIMessage']]
    """

    return (
        await asyncio_detailed(
            opportunity_id=opportunity_id,
            shift_id=shift_id,
            client=client,
            body=body,
        )
    ).parsed
