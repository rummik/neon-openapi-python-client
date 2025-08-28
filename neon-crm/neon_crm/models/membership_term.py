from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.membership_term_type import MembershipTermType
from ..models.membership_term_unit import MembershipTermUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cra_info import CraInfo
    from ..models.id_name_pair import IdNamePair
    from ..models.tax_deducible_info import TaxDeducibleInfo


T = TypeVar("T", bound="MembershipTerm")


@_attrs_define
class MembershipTerm:
    """
    Attributes:
        id (Union[Unset, int]):
        membership_level (Union[Unset, IdNamePair]):
        display (Union[Unset, str]):
        type_ (Union[Unset, MembershipTermType]):
        duration (Union[Unset, int]):
        unit (Union[Unset, MembershipTermUnit]):
        fee (Union[Unset, float]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
        child_terms (Union[Unset, list['MembershipTerm']]):
    """

    id: Union[Unset, int] = UNSET
    membership_level: Union[Unset, "IdNamePair"] = UNSET
    display: Union[Unset, str] = UNSET
    type_: Union[Unset, MembershipTermType] = UNSET
    duration: Union[Unset, int] = UNSET
    unit: Union[Unset, MembershipTermUnit] = UNSET
    fee: Union[Unset, float] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    child_terms: Union[Unset, list["MembershipTerm"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        membership_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.membership_level, Unset):
            membership_level = self.membership_level.to_dict()

        display = self.display

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        duration = self.duration

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        fee = self.fee

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        child_terms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.child_terms, Unset):
            child_terms = []
            for child_terms_item_data in self.child_terms:
                child_terms_item = child_terms_item_data.to_dict()
                child_terms.append(child_terms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if membership_level is not UNSET:
            field_dict["membershipLevel"] = membership_level
        if display is not UNSET:
            field_dict["display"] = display
        if type_ is not UNSET:
            field_dict["type"] = type_
        if duration is not UNSET:
            field_dict["duration"] = duration
        if unit is not UNSET:
            field_dict["unit"] = unit
        if fee is not UNSET:
            field_dict["fee"] = fee
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info
        if child_terms is not UNSET:
            field_dict["childTerms"] = child_terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cra_info import CraInfo
        from ..models.id_name_pair import IdNamePair
        from ..models.tax_deducible_info import TaxDeducibleInfo

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _membership_level = d.pop("membershipLevel", UNSET)
        membership_level: Union[Unset, IdNamePair]
        if isinstance(_membership_level, Unset):
            membership_level = UNSET
        else:
            membership_level = IdNamePair.from_dict(_membership_level)

        display = d.pop("display", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, MembershipTermType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MembershipTermType(_type_)

        duration = d.pop("duration", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, MembershipTermUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = MembershipTermUnit(_unit)

        fee = d.pop("fee", UNSET)

        _cra_info = d.pop("craInfo", UNSET)
        cra_info: Union[Unset, CraInfo]
        if isinstance(_cra_info, Unset):
            cra_info = UNSET
        else:
            cra_info = CraInfo.from_dict(_cra_info)

        _tax_deductible_info = d.pop("taxDeductibleInfo", UNSET)
        tax_deductible_info: Union[Unset, TaxDeducibleInfo]
        if isinstance(_tax_deductible_info, Unset):
            tax_deductible_info = UNSET
        else:
            tax_deductible_info = TaxDeducibleInfo.from_dict(_tax_deductible_info)

        child_terms = []
        _child_terms = d.pop("childTerms", UNSET)
        for child_terms_item_data in _child_terms or []:
            child_terms_item = MembershipTerm.from_dict(child_terms_item_data)

            child_terms.append(child_terms_item)

        membership_term = cls(
            id=id,
            membership_level=membership_level,
            display=display,
            type_=type_,
            duration=duration,
            unit=unit,
            fee=fee,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
            child_terms=child_terms,
        )

        membership_term.additional_properties = d
        return membership_term

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
