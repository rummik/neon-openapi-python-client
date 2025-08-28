from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Solicitor")


@_attrs_define
class Solicitor:
    """
    Attributes:
        account_id (Union[Unset, str]):
        solicitor_name (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    solicitor_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        solicitor_name = self.solicitor_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if solicitor_name is not UNSET:
            field_dict["solicitorName"] = solicitor_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        solicitor_name = d.pop("solicitorName", UNSET)

        solicitor = cls(
            account_id=account_id,
            solicitor_name=solicitor_name,
        )

        solicitor.additional_properties = d
        return solicitor

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
