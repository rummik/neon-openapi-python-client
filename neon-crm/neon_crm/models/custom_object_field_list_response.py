from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_object_field_list_response_field_data_type import CustomObjectFieldListResponseFieldDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomObjectFieldListResponse")


@_attrs_define
class CustomObjectFieldListResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        field_label (Union[Unset, str]):
        api_name (Union[Unset, str]):
        field_data_type (Union[Unset, CustomObjectFieldListResponseFieldDataType]):
        field_description (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    field_label: Union[Unset, str] = UNSET
    api_name: Union[Unset, str] = UNSET
    field_data_type: Union[Unset, CustomObjectFieldListResponseFieldDataType] = UNSET
    field_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_label = self.field_label

        api_name = self.api_name

        field_data_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_data_type, Unset):
            field_data_type = self.field_data_type.value

        field_description = self.field_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if field_label is not UNSET:
            field_dict["fieldLabel"] = field_label
        if api_name is not UNSET:
            field_dict["apiName"] = api_name
        if field_data_type is not UNSET:
            field_dict["fieldDataType"] = field_data_type
        if field_description is not UNSET:
            field_dict["fieldDescription"] = field_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        field_label = d.pop("fieldLabel", UNSET)

        api_name = d.pop("apiName", UNSET)

        _field_data_type = d.pop("fieldDataType", UNSET)
        field_data_type: Union[Unset, CustomObjectFieldListResponseFieldDataType]
        if isinstance(_field_data_type, Unset):
            field_data_type = UNSET
        else:
            field_data_type = CustomObjectFieldListResponseFieldDataType(_field_data_type)

        field_description = d.pop("fieldDescription", UNSET)

        custom_object_field_list_response = cls(
            id=id,
            field_label=field_label,
            api_name=api_name,
            field_data_type=field_data_type,
            field_description=field_description,
        )

        custom_object_field_list_response.additional_properties = d
        return custom_object_field_list_response

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
