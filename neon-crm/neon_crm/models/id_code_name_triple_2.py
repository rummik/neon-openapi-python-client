from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.id_code_name_triple_2_status import IdCodeNameTriple2Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdCodeNameTriple2")


@_attrs_define
class IdCodeNameTriple2:
    """
    Attributes:
        code (Union[Unset, str]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        status (Union[Unset, IdCodeNameTriple2Status]):
        is_default (Union[Unset, bool]):
    """

    code: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, IdCodeNameTriple2Status] = UNSET
    is_default: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        id = self.id

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IdCodeNameTriple2Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IdCodeNameTriple2Status(_status)

        is_default = d.pop("isDefault", UNSET)

        id_code_name_triple_2 = cls(
            code=code,
            id=id,
            name=name,
            status=status,
            is_default=is_default,
        )

        id_code_name_triple_2.additional_properties = d
        return id_code_name_triple_2

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
