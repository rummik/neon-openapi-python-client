from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="HouseHoldContactDto")


@_attrs_define
class HouseHoldContactDto:
    """
    Attributes:
        account_id (str):
        relation_type (IdNamePair):
        is_primary_house_hold_contact (Union[Unset, bool]):  Default: False.
        confirm_delete (Union[Unset, bool]): This field is only applicable to the update household interface and will be
            ignored by the create household interface. Default: False.
    """

    account_id: str
    relation_type: "IdNamePair"
    is_primary_house_hold_contact: Union[Unset, bool] = False
    confirm_delete: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        relation_type = self.relation_type.to_dict()

        is_primary_house_hold_contact = self.is_primary_house_hold_contact

        confirm_delete = self.confirm_delete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "relationType": relation_type,
            }
        )
        if is_primary_house_hold_contact is not UNSET:
            field_dict["isPrimaryHouseHoldContact"] = is_primary_house_hold_contact
        if confirm_delete is not UNSET:
            field_dict["confirmDelete"] = confirm_delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        account_id = d.pop("accountId")

        relation_type = IdNamePair.from_dict(d.pop("relationType"))

        is_primary_house_hold_contact = d.pop("isPrimaryHouseHoldContact", UNSET)

        confirm_delete = d.pop("confirmDelete", UNSET)

        house_hold_contact_dto = cls(
            account_id=account_id,
            relation_type=relation_type,
            is_primary_house_hold_contact=is_primary_house_hold_contact,
            confirm_delete=confirm_delete,
        )

        house_hold_contact_dto.additional_properties = d
        return house_hold_contact_dto

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
