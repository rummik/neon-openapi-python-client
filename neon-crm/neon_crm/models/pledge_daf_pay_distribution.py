from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PledgeDafPayDistribution")


@_attrs_define
class PledgeDafPayDistribution:
    """
    Attributes:
        distribution_id (Union[Unset, str]):
        grant_id (Union[Unset, str]):
        total_fees (Union[Unset, float]):
        status (Union[Unset, str]):
        advisor (Union[Unset, str]):
        note (Union[Unset, str]):
    """

    distribution_id: Union[Unset, str] = UNSET
    grant_id: Union[Unset, str] = UNSET
    total_fees: Union[Unset, float] = UNSET
    status: Union[Unset, str] = UNSET
    advisor: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        distribution_id = self.distribution_id

        grant_id = self.grant_id

        total_fees = self.total_fees

        status = self.status

        advisor = self.advisor

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if distribution_id is not UNSET:
            field_dict["distributionId"] = distribution_id
        if grant_id is not UNSET:
            field_dict["grantId"] = grant_id
        if total_fees is not UNSET:
            field_dict["totalFees"] = total_fees
        if status is not UNSET:
            field_dict["status"] = status
        if advisor is not UNSET:
            field_dict["advisor"] = advisor
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        distribution_id = d.pop("distributionId", UNSET)

        grant_id = d.pop("grantId", UNSET)

        total_fees = d.pop("totalFees", UNSET)

        status = d.pop("status", UNSET)

        advisor = d.pop("advisor", UNSET)

        note = d.pop("note", UNSET)

        pledge_daf_pay_distribution = cls(
            distribution_id=distribution_id,
            grant_id=grant_id,
            total_fees=total_fees,
            status=status,
            advisor=advisor,
            note=note,
        )

        pledge_daf_pay_distribution.additional_properties = d
        return pledge_daf_pay_distribution

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
