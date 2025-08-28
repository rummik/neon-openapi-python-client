from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_value_pair import NameValuePair


T = TypeVar("T", bound="RecordResponse")


@_attrs_define
class RecordResponse:
    """
    Attributes:
        record_id (Union[Unset, int]):
        record_data (Union[Unset, list['NameValuePair']]):
    """

    record_id: Union[Unset, int] = UNSET
    record_data: Union[Unset, list["NameValuePair"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        record_data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.record_data, Unset):
            record_data = []
            for record_data_item_data in self.record_data:
                record_data_item = record_data_item_data.to_dict()
                record_data.append(record_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if record_data is not UNSET:
            field_dict["recordData"] = record_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.name_value_pair import NameValuePair

        d = dict(src_dict)
        record_id = d.pop("recordId", UNSET)

        record_data = []
        _record_data = d.pop("recordData", UNSET)
        for record_data_item_data in _record_data or []:
            record_data_item = NameValuePair.from_dict(record_data_item_data)

            record_data.append(record_data_item)

        record_response = cls(
            record_id=record_id,
            record_data=record_data,
        )

        record_response.additional_properties = d
        return record_response

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
