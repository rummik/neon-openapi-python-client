from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_item import ProductItem


T = TypeVar("T", bound="ShippingMethodRequest")


@_attrs_define
class ShippingMethodRequest:
    """
    Attributes:
        country_id (str):
        zip_code (str):
        products (Union[Unset, list['ProductItem']]):
    """

    country_id: str
    zip_code: str
    products: Union[Unset, list["ProductItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_id = self.country_id

        zip_code = self.zip_code

        products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "countryId": country_id,
                "zipCode": zip_code,
            }
        )
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_item import ProductItem

        d = dict(src_dict)
        country_id = d.pop("countryId")

        zip_code = d.pop("zipCode")

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = ProductItem.from_dict(products_item_data)

            products.append(products_item)

        shipping_method_request = cls(
            country_id=country_id,
            zip_code=zip_code,
            products=products,
        )

        shipping_method_request.additional_properties = d
        return shipping_method_request

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
