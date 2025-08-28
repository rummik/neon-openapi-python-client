import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipCalculateDatesResult")


@_attrs_define
class MembershipCalculateDatesResult:
    """
    Attributes:
        transaction_date (Union[Unset, datetime.datetime]):
        term_start_date (Union[Unset, datetime.datetime]):
        term_end_date (Union[Unset, datetime.datetime]):
    """

    transaction_date: Union[Unset, datetime.datetime] = UNSET
    term_start_date: Union[Unset, datetime.datetime] = UNSET
    term_end_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        term_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.term_start_date, Unset):
            term_start_date = self.term_start_date.isoformat()

        term_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.term_end_date, Unset):
            term_end_date = self.term_end_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_date is not UNSET:
            field_dict["transactionDate"] = transaction_date
        if term_start_date is not UNSET:
            field_dict["termStartDate"] = term_start_date
        if term_end_date is not UNSET:
            field_dict["termEndDate"] = term_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _transaction_date = d.pop("transactionDate", UNSET)
        transaction_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date, Unset):
            transaction_date = UNSET
        else:
            transaction_date = isoparse(_transaction_date)

        _term_start_date = d.pop("termStartDate", UNSET)
        term_start_date: Union[Unset, datetime.datetime]
        if isinstance(_term_start_date, Unset):
            term_start_date = UNSET
        else:
            term_start_date = isoparse(_term_start_date)

        _term_end_date = d.pop("termEndDate", UNSET)
        term_end_date: Union[Unset, datetime.datetime]
        if isinstance(_term_end_date, Unset):
            term_end_date = UNSET
        else:
            term_end_date = isoparse(_term_end_date)

        membership_calculate_dates_result = cls(
            transaction_date=transaction_date,
            term_start_date=term_start_date,
            term_end_date=term_end_date,
        )

        membership_calculate_dates_result.additional_properties = d
        return membership_calculate_dates_result

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
