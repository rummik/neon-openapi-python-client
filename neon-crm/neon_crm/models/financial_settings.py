from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.financial_settings_fee_type import FinancialSettingsFeeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admission_fee import AdmissionFee
    from ..models.financial_settings_donations import FinancialSettingsDonations
    from ..models.id_name_pair import IdNamePair
    from ..models.tax_deductible_portion import TaxDeductiblePortion
    from ..models.tickets_per_registration import TicketsPerRegistration


T = TypeVar("T", bound="FinancialSettings")


@_attrs_define
class FinancialSettings:
    """
    Attributes:
        fee_type (Union[Unset, FinancialSettingsFeeType]):
        admission_fee (Union[Unset, AdmissionFee]):
        tickets_per_registration (Union[Unset, TicketsPerRegistration]):
        fund (Union[Unset, IdNamePair]):
        tax_deductible_portion (Union[Unset, TaxDeductiblePortion]):
        donations (Union[Unset, FinancialSettingsDonations]):
    """

    fee_type: Union[Unset, FinancialSettingsFeeType] = UNSET
    admission_fee: Union[Unset, "AdmissionFee"] = UNSET
    tickets_per_registration: Union[Unset, "TicketsPerRegistration"] = UNSET
    fund: Union[Unset, "IdNamePair"] = UNSET
    tax_deductible_portion: Union[Unset, "TaxDeductiblePortion"] = UNSET
    donations: Union[Unset, "FinancialSettingsDonations"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee_type: Union[Unset, str] = UNSET
        if not isinstance(self.fee_type, Unset):
            fee_type = self.fee_type.value

        admission_fee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.admission_fee, Unset):
            admission_fee = self.admission_fee.to_dict()

        tickets_per_registration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tickets_per_registration, Unset):
            tickets_per_registration = self.tickets_per_registration.to_dict()

        fund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fund, Unset):
            fund = self.fund.to_dict()

        tax_deductible_portion: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_portion, Unset):
            tax_deductible_portion = self.tax_deductible_portion.to_dict()

        donations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.donations, Unset):
            donations = self.donations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee_type is not UNSET:
            field_dict["feeType"] = fee_type
        if admission_fee is not UNSET:
            field_dict["admissionFee"] = admission_fee
        if tickets_per_registration is not UNSET:
            field_dict["ticketsPerRegistration"] = tickets_per_registration
        if fund is not UNSET:
            field_dict["fund"] = fund
        if tax_deductible_portion is not UNSET:
            field_dict["taxDeductiblePortion"] = tax_deductible_portion
        if donations is not UNSET:
            field_dict["donations"] = donations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admission_fee import AdmissionFee
        from ..models.financial_settings_donations import FinancialSettingsDonations
        from ..models.id_name_pair import IdNamePair
        from ..models.tax_deductible_portion import TaxDeductiblePortion
        from ..models.tickets_per_registration import TicketsPerRegistration

        d = dict(src_dict)
        _fee_type = d.pop("feeType", UNSET)
        fee_type: Union[Unset, FinancialSettingsFeeType]
        if isinstance(_fee_type, Unset):
            fee_type = UNSET
        else:
            fee_type = FinancialSettingsFeeType(_fee_type)

        _admission_fee = d.pop("admissionFee", UNSET)
        admission_fee: Union[Unset, AdmissionFee]
        if isinstance(_admission_fee, Unset):
            admission_fee = UNSET
        else:
            admission_fee = AdmissionFee.from_dict(_admission_fee)

        _tickets_per_registration = d.pop("ticketsPerRegistration", UNSET)
        tickets_per_registration: Union[Unset, TicketsPerRegistration]
        if isinstance(_tickets_per_registration, Unset):
            tickets_per_registration = UNSET
        else:
            tickets_per_registration = TicketsPerRegistration.from_dict(_tickets_per_registration)

        _fund = d.pop("fund", UNSET)
        fund: Union[Unset, IdNamePair]
        if isinstance(_fund, Unset):
            fund = UNSET
        else:
            fund = IdNamePair.from_dict(_fund)

        _tax_deductible_portion = d.pop("taxDeductiblePortion", UNSET)
        tax_deductible_portion: Union[Unset, TaxDeductiblePortion]
        if isinstance(_tax_deductible_portion, Unset):
            tax_deductible_portion = UNSET
        else:
            tax_deductible_portion = TaxDeductiblePortion.from_dict(_tax_deductible_portion)

        _donations = d.pop("donations", UNSET)
        donations: Union[Unset, FinancialSettingsDonations]
        if isinstance(_donations, Unset):
            donations = UNSET
        else:
            donations = FinancialSettingsDonations.from_dict(_donations)

        financial_settings = cls(
            fee_type=fee_type,
            admission_fee=admission_fee,
            tickets_per_registration=tickets_per_registration,
            fund=fund,
            tax_deductible_portion=tax_deductible_portion,
            donations=donations,
        )

        financial_settings.additional_properties = d
        return financial_settings

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
