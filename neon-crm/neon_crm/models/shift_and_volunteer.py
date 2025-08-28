from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShiftAndVolunteer")


@_attrs_define
class ShiftAndVolunteer:
    """
    Attributes:
        account_id (Union[Unset, str]):
        shift_ids (Union[Unset, list[str]]):
    """

    account_id: Union[Unset, str] = UNSET
    shift_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        shift_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shift_ids, Unset):
            shift_ids = self.shift_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if shift_ids is not UNSET:
            field_dict["shiftIds"] = shift_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        shift_ids = cast(list[str], d.pop("shiftIds", UNSET))

        shift_and_volunteer = cls(
            account_id=account_id,
            shift_ids=shift_ids,
        )

        shift_and_volunteer.additional_properties = d
        return shift_and_volunteer

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
