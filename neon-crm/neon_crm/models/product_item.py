from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cra_info import CraInfo
    from ..models.product_option_selection import ProductOptionSelection
    from ..models.tax_deducible_info import TaxDeducibleInfo


T = TypeVar("T", bound="ProductItem")


@_attrs_define
class ProductItem:
    """
    Attributes:
        product_id (str):
        unit_price (Union[Unset, float]):
        option_selections (Union[Unset, list['ProductOptionSelection']]): A maximum of three options are allowed
        quantity (Union[Unset, int]):
        send_acknowledge_email (Union[Unset, bool]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
    """

    product_id: str
    unit_price: Union[Unset, float] = UNSET
    option_selections: Union[Unset, list["ProductOptionSelection"]] = UNSET
    quantity: Union[Unset, int] = UNSET
    send_acknowledge_email: Union[Unset, bool] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        unit_price = self.unit_price

        option_selections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.option_selections, Unset):
            option_selections = []
            for option_selections_item_data in self.option_selections:
                option_selections_item = option_selections_item_data.to_dict()
                option_selections.append(option_selections_item)

        quantity = self.quantity

        send_acknowledge_email = self.send_acknowledge_email

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productId": product_id,
            }
        )
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if option_selections is not UNSET:
            field_dict["optionSelections"] = option_selections
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if send_acknowledge_email is not UNSET:
            field_dict["sendAcknowledgeEmail"] = send_acknowledge_email
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cra_info import CraInfo
        from ..models.product_option_selection import ProductOptionSelection
        from ..models.tax_deducible_info import TaxDeducibleInfo

        d = dict(src_dict)
        product_id = d.pop("productId")

        unit_price = d.pop("unitPrice", UNSET)

        option_selections = []
        _option_selections = d.pop("optionSelections", UNSET)
        for option_selections_item_data in _option_selections or []:
            option_selections_item = ProductOptionSelection.from_dict(option_selections_item_data)

            option_selections.append(option_selections_item)

        quantity = d.pop("quantity", UNSET)

        send_acknowledge_email = d.pop("sendAcknowledgeEmail", UNSET)

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

        product_item = cls(
            product_id=product_id,
            unit_price=unit_price,
            option_selections=option_selections,
            quantity=quantity,
            send_acknowledge_email=send_acknowledge_email,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
        )

        product_item.additional_properties = d
        return product_item

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
