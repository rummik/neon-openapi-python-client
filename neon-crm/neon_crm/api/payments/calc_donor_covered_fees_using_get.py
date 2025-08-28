from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.donor_covered_fees import DonorCoveredFees
from ...types import UNSET, Response


def _get_kwargs(
    *,
    transaction_amount: float,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["transactionAmount"] = transaction_amount

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/payments/donorCoveredFees",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DonorCoveredFees]]:
    if response.status_code == 200:
        response_200 = DonorCoveredFees.from_dict(response.json())

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
) -> Response[Union[Any, DonorCoveredFees]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    transaction_amount: float,
) -> Response[Union[Any, DonorCoveredFees]]:
    """Calculate the donor covered fee according to the transaction amount

    Args:
        transaction_amount (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DonorCoveredFees]]
    """

    kwargs = _get_kwargs(
        transaction_amount=transaction_amount,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    transaction_amount: float,
) -> Optional[Union[Any, DonorCoveredFees]]:
    """Calculate the donor covered fee according to the transaction amount

    Args:
        transaction_amount (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DonorCoveredFees]
    """

    return sync_detailed(
        client=client,
        transaction_amount=transaction_amount,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    transaction_amount: float,
) -> Response[Union[Any, DonorCoveredFees]]:
    """Calculate the donor covered fee according to the transaction amount

    Args:
        transaction_amount (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DonorCoveredFees]]
    """

    kwargs = _get_kwargs(
        transaction_amount=transaction_amount,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    transaction_amount: float,
) -> Optional[Union[Any, DonorCoveredFees]]:
    """Calculate the donor covered fee according to the transaction amount

    Args:
        transaction_amount (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DonorCoveredFees]
    """

    return (
        await asyncio_detailed(
            client=client,
            transaction_amount=transaction_amount,
        )
    ).parsed
