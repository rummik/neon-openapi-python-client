from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cra_info import CraInfo
    from ..models.tax_deducible_info import TaxDeducibleInfo


T = TypeVar("T", bound="AdmissionFee")


@_attrs_define
class AdmissionFee:
    """
    Attributes:
        fee (Union[Unset, float]):
        tax_deductible_percent (Union[Unset, float]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
    """

    fee: Union[Unset, float] = UNSET
    tax_deductible_percent: Union[Unset, float] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee = self.fee

        tax_deductible_percent = self.tax_deductible_percent

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee is not UNSET:
            field_dict["fee"] = fee
        if tax_deductible_percent is not UNSET:
            field_dict["taxDeductiblePercent"] = tax_deductible_percent
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cra_info import CraInfo
        from ..models.tax_deducible_info import TaxDeducibleInfo

        d = dict(src_dict)
        fee = d.pop("fee", UNSET)

        tax_deductible_percent = d.pop("taxDeductiblePercent", UNSET)

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

        admission_fee = cls(
            fee=fee,
            tax_deductible_percent=tax_deductible_percent,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
        )

        admission_fee.additional_properties = d
        return admission_fee

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
