from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gender_vo_status import GenderVOStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GenderVO")


@_attrs_define
class GenderVO:
    """
    Attributes:
        code (Union[Unset, str]):
        description (Union[Unset, str]):
        status (Union[Unset, GenderVOStatus]):
        position (Union[Unset, int]):
    """

    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, GenderVOStatus] = UNSET
    position: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        description = self.description

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GenderVOStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GenderVOStatus(_status)

        position = d.pop("position", UNSET)

        gender_vo = cls(
            code=code,
            description=description,
            status=status,
            position=position,
        )

        gender_vo.additional_properties = d
        return gender_vo

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
