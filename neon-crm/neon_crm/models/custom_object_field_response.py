from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_object_field_response_field_data_type import CustomObjectFieldResponseFieldDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_attribute import FieldAttribute


T = TypeVar("T", bound="CustomObjectFieldResponse")


@_attrs_define
class CustomObjectFieldResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        field_label (Union[Unset, str]):
        api_name (Union[Unset, str]):
        field_data_type (Union[Unset, CustomObjectFieldResponseFieldDataType]):
        field_description (Union[Unset, str]):
        field_help_text (Union[Unset, str]):
        is_internal (Union[Unset, bool]):
        attribute (Union[Unset, FieldAttribute]):
    """

    id: Union[Unset, str] = UNSET
    field_label: Union[Unset, str] = UNSET
    api_name: Union[Unset, str] = UNSET
    field_data_type: Union[Unset, CustomObjectFieldResponseFieldDataType] = UNSET
    field_description: Union[Unset, str] = UNSET
    field_help_text: Union[Unset, str] = UNSET
    is_internal: Union[Unset, bool] = UNSET
    attribute: Union[Unset, "FieldAttribute"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_label = self.field_label

        api_name = self.api_name

        field_data_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_data_type, Unset):
            field_data_type = self.field_data_type.value

        field_description = self.field_description

        field_help_text = self.field_help_text

        is_internal = self.is_internal

        attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute, Unset):
            attribute = self.attribute.to_dict()

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
        if field_help_text is not UNSET:
            field_dict["fieldHelpText"] = field_help_text
        if is_internal is not UNSET:
            field_dict["isInternal"] = is_internal
        if attribute is not UNSET:
            field_dict["attribute"] = attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field_attribute import FieldAttribute

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        field_label = d.pop("fieldLabel", UNSET)

        api_name = d.pop("apiName", UNSET)

        _field_data_type = d.pop("fieldDataType", UNSET)
        field_data_type: Union[Unset, CustomObjectFieldResponseFieldDataType]
        if isinstance(_field_data_type, Unset):
            field_data_type = UNSET
        else:
            field_data_type = CustomObjectFieldResponseFieldDataType(_field_data_type)

        field_description = d.pop("fieldDescription", UNSET)

        field_help_text = d.pop("fieldHelpText", UNSET)

        is_internal = d.pop("isInternal", UNSET)

        _attribute = d.pop("attribute", UNSET)
        attribute: Union[Unset, FieldAttribute]
        if isinstance(_attribute, Unset):
            attribute = UNSET
        else:
            attribute = FieldAttribute.from_dict(_attribute)

        custom_object_field_response = cls(
            id=id,
            field_label=field_label,
            api_name=api_name,
            field_data_type=field_data_type,
            field_description=field_description,
            field_help_text=field_help_text,
            is_internal=is_internal,
            attribute=attribute,
        )

        custom_object_field_response.additional_properties = d
        return custom_object_field_response

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
