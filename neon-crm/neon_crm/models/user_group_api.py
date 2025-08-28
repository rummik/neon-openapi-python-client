from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGroupApi")


@_attrs_define
class UserGroupApi:
    """
    Attributes:
        name (str):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        total_volunteers (Union[Unset, int]):
        hours (Union[Unset, float]):
        expenses (Union[Unset, float]):
        mileages (Union[Unset, float]):
    """

    name: str
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    total_volunteers: Union[Unset, int] = UNSET
    hours: Union[Unset, float] = UNSET
    expenses: Union[Unset, float] = UNSET
    mileages: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        description = self.description

        total_volunteers = self.total_volunteers

        hours = self.hours

        expenses = self.expenses

        mileages = self.mileages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if total_volunteers is not UNSET:
            field_dict["totalVolunteers"] = total_volunteers
        if hours is not UNSET:
            field_dict["hours"] = hours
        if expenses is not UNSET:
            field_dict["expenses"] = expenses
        if mileages is not UNSET:
            field_dict["mileages"] = mileages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        total_volunteers = d.pop("totalVolunteers", UNSET)

        hours = d.pop("hours", UNSET)

        expenses = d.pop("expenses", UNSET)

        mileages = d.pop("mileages", UNSET)

        user_group_api = cls(
            name=name,
            id=id,
            description=description,
            total_volunteers=total_volunteers,
            hours=hours,
            expenses=expenses,
            mileages=mileages,
        )

        user_group_api.additional_properties = d
        return user_group_api

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
