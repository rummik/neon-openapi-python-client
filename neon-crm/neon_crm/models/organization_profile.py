from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationProfile")


@_attrs_define
class OrganizationProfile:
    """
    Attributes:
        name (Union[Unset, str]):
        org_id (Union[Unset, str]):
        app_url (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    org_id: Union[Unset, str] = UNSET
    app_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        org_id = self.org_id

        app_url = self.app_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if app_url is not UNSET:
            field_dict["appUrl"] = app_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        org_id = d.pop("orgId", UNSET)

        app_url = d.pop("appUrl", UNSET)

        organization_profile = cls(
            name=name,
            org_id=org_id,
            app_url=app_url,
        )

        organization_profile.additional_properties = d
        return organization_profile

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
