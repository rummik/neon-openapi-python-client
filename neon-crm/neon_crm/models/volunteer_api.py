from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolunteerApi")


@_attrs_define
class VolunteerApi:
    """
    Attributes:
        account_id (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        sms_number (Union[Unset, str]):
        opportunity_ids (Union[Unset, list[str]]):
        shift_ids (Union[Unset, list[str]]):
        roles (Union[Unset, list[str]]):
        group_ids (Union[Unset, list[str]]):
        total_hours (Union[Unset, float]):
        total_expenses (Union[Unset, float]):
        total_mileages (Union[Unset, float]):
    """

    account_id: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    sms_number: Union[Unset, str] = UNSET
    opportunity_ids: Union[Unset, list[str]] = UNSET
    shift_ids: Union[Unset, list[str]] = UNSET
    roles: Union[Unset, list[str]] = UNSET
    group_ids: Union[Unset, list[str]] = UNSET
    total_hours: Union[Unset, float] = UNSET
    total_expenses: Union[Unset, float] = UNSET
    total_mileages: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone = self.phone

        sms_number = self.sms_number

        opportunity_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.opportunity_ids, Unset):
            opportunity_ids = self.opportunity_ids

        shift_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shift_ids, Unset):
            shift_ids = self.shift_ids

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        total_hours = self.total_hours

        total_expenses = self.total_expenses

        total_mileages = self.total_mileages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if sms_number is not UNSET:
            field_dict["smsNumber"] = sms_number
        if opportunity_ids is not UNSET:
            field_dict["opportunityIds"] = opportunity_ids
        if shift_ids is not UNSET:
            field_dict["shiftIds"] = shift_ids
        if roles is not UNSET:
            field_dict["roles"] = roles
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if total_hours is not UNSET:
            field_dict["totalHours"] = total_hours
        if total_expenses is not UNSET:
            field_dict["totalExpenses"] = total_expenses
        if total_mileages is not UNSET:
            field_dict["totalMileages"] = total_mileages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        sms_number = d.pop("smsNumber", UNSET)

        opportunity_ids = cast(list[str], d.pop("opportunityIds", UNSET))

        shift_ids = cast(list[str], d.pop("shiftIds", UNSET))

        roles = cast(list[str], d.pop("roles", UNSET))

        group_ids = cast(list[str], d.pop("groupIds", UNSET))

        total_hours = d.pop("totalHours", UNSET)

        total_expenses = d.pop("totalExpenses", UNSET)

        total_mileages = d.pop("totalMileages", UNSET)

        volunteer_api = cls(
            account_id=account_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            sms_number=sms_number,
            opportunity_ids=opportunity_ids,
            shift_ids=shift_ids,
            roles=roles,
            group_ids=group_ids,
            total_hours=total_hours,
            total_expenses=total_expenses,
            total_mileages=total_mileages,
        )

        volunteer_api.additional_properties = d
        return volunteer_api

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
