from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="AccountRoleApi")


@_attrs_define
class AccountRoleApi:
    """
    Attributes:
        id (int):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        color (Union[Unset, IdNamePair]):
    """

    id: int
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    color: Union[Unset, "IdNamePair"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        color: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _color = d.pop("color", UNSET)
        color: Union[Unset, IdNamePair]
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = IdNamePair.from_dict(_color)

        account_role_api = cls(
            id=id,
            name=name,
            description=description,
            color=color,
        )

        account_role_api.additional_properties = d
        return account_role_api

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
