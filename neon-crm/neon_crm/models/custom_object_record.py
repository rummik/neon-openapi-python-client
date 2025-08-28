from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_data import RecordData


T = TypeVar("T", bound="CustomObjectRecord")


@_attrs_define
class CustomObjectRecord:
    """
    Attributes:
        name_value_pair (Union[Unset, list['RecordData']]):
    """

    name_value_pair: Union[Unset, list["RecordData"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_value_pair: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.name_value_pair, Unset):
            name_value_pair = []
            for name_value_pair_item_data in self.name_value_pair:
                name_value_pair_item = name_value_pair_item_data.to_dict()
                name_value_pair.append(name_value_pair_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_value_pair is not UNSET:
            field_dict["nameValuePair"] = name_value_pair

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_data import RecordData

        d = dict(src_dict)
        name_value_pair = []
        _name_value_pair = d.pop("nameValuePair", UNSET)
        for name_value_pair_item_data in _name_value_pair or []:
            name_value_pair_item = RecordData.from_dict(name_value_pair_item_data)

            name_value_pair.append(name_value_pair_item)

        custom_object_record = cls(
            name_value_pair=name_value_pair,
        )

        custom_object_record.additional_properties = d
        return custom_object_record

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
