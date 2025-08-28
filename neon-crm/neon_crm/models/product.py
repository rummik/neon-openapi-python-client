import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.product_status import ProductStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog import Catalog
    from ..models.category import Category
    from ..models.cra_info import CraInfo
    from ..models.custom_field import CustomField
    from ..models.product_image import ProductImage
    from ..models.product_option import ProductOption
    from ..models.product_shipping import ProductShipping
    from ..models.tax_deducible_info import TaxDeducibleInfo


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """
    Attributes:
        catalogs (Union[Unset, list['Catalog']]):
        id (Union[Unset, str]):
        category (Union[Unset, Category]):
        name (Union[Unset, str]):
        code (Union[Unset, str]):
        status (Union[Unset, ProductStatus]):
        keyword (Union[Unset, str]):
        description (Union[Unset, str]):
        unit_price (Union[Unset, float]):
        download_url (Union[Unset, str]):
        is_apply_on_site_tax (Union[Unset, bool]):
        is_front_end_display (Union[Unset, bool]):
        shipping (Union[Unset, ProductShipping]):
        price_off_discount (Union[Unset, float]):
        is_discount_in_percentage (Union[Unset, bool]):
        has_options (Union[Unset, bool]):
        price_off_discount_start_date (Union[Unset, datetime.datetime]):
        price_off_discount_end_date (Union[Unset, datetime.datetime]):
        images (Union[Unset, list['ProductImage']]):
        options (Union[Unset, list['ProductOption']]):
        custom_fields (Union[Unset, list['CustomField']]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
    """

    catalogs: Union[Unset, list["Catalog"]] = UNSET
    id: Union[Unset, str] = UNSET
    category: Union[Unset, "Category"] = UNSET
    name: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    status: Union[Unset, ProductStatus] = UNSET
    keyword: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    download_url: Union[Unset, str] = UNSET
    is_apply_on_site_tax: Union[Unset, bool] = UNSET
    is_front_end_display: Union[Unset, bool] = UNSET
    shipping: Union[Unset, "ProductShipping"] = UNSET
    price_off_discount: Union[Unset, float] = UNSET
    is_discount_in_percentage: Union[Unset, bool] = UNSET
    has_options: Union[Unset, bool] = UNSET
    price_off_discount_start_date: Union[Unset, datetime.datetime] = UNSET
    price_off_discount_end_date: Union[Unset, datetime.datetime] = UNSET
    images: Union[Unset, list["ProductImage"]] = UNSET
    options: Union[Unset, list["ProductOption"]] = UNSET
    custom_fields: Union[Unset, list["CustomField"]] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalogs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.catalogs, Unset):
            catalogs = []
            for catalogs_item_data in self.catalogs:
                catalogs_item = catalogs_item_data.to_dict()
                catalogs.append(catalogs_item)

        id = self.id

        category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        name = self.name

        code = self.code

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        keyword = self.keyword

        description = self.description

        unit_price = self.unit_price

        download_url = self.download_url

        is_apply_on_site_tax = self.is_apply_on_site_tax

        is_front_end_display = self.is_front_end_display

        shipping: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shipping, Unset):
            shipping = self.shipping.to_dict()

        price_off_discount = self.price_off_discount

        is_discount_in_percentage = self.is_discount_in_percentage

        has_options = self.has_options

        price_off_discount_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.price_off_discount_start_date, Unset):
            price_off_discount_start_date = self.price_off_discount_start_date.isoformat()

        price_off_discount_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.price_off_discount_end_date, Unset):
            price_off_discount_end_date = self.price_off_discount_end_date.isoformat()

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalogs is not UNSET:
            field_dict["catalogs"] = catalogs
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if description is not UNSET:
            field_dict["description"] = description
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if download_url is not UNSET:
            field_dict["downloadURL"] = download_url
        if is_apply_on_site_tax is not UNSET:
            field_dict["isApplyOnSiteTax"] = is_apply_on_site_tax
        if is_front_end_display is not UNSET:
            field_dict["isFrontEndDisplay"] = is_front_end_display
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if price_off_discount is not UNSET:
            field_dict["priceOffDiscount"] = price_off_discount
        if is_discount_in_percentage is not UNSET:
            field_dict["isDiscountInPercentage"] = is_discount_in_percentage
        if has_options is not UNSET:
            field_dict["hasOptions"] = has_options
        if price_off_discount_start_date is not UNSET:
            field_dict["priceOffDiscountStartDate"] = price_off_discount_start_date
        if price_off_discount_end_date is not UNSET:
            field_dict["priceOffDiscountEndDate"] = price_off_discount_end_date
        if images is not UNSET:
            field_dict["images"] = images
        if options is not UNSET:
            field_dict["options"] = options
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog import Catalog
        from ..models.category import Category
        from ..models.cra_info import CraInfo
        from ..models.custom_field import CustomField
        from ..models.product_image import ProductImage
        from ..models.product_option import ProductOption
        from ..models.product_shipping import ProductShipping
        from ..models.tax_deducible_info import TaxDeducibleInfo

        d = dict(src_dict)
        catalogs = []
        _catalogs = d.pop("catalogs", UNSET)
        for catalogs_item_data in _catalogs or []:
            catalogs_item = Catalog.from_dict(catalogs_item_data)

            catalogs.append(catalogs_item)

        id = d.pop("id", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, Category]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Category.from_dict(_category)

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProductStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProductStatus(_status)

        keyword = d.pop("keyword", UNSET)

        description = d.pop("description", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        download_url = d.pop("downloadURL", UNSET)

        is_apply_on_site_tax = d.pop("isApplyOnSiteTax", UNSET)

        is_front_end_display = d.pop("isFrontEndDisplay", UNSET)

        _shipping = d.pop("shipping", UNSET)
        shipping: Union[Unset, ProductShipping]
        if isinstance(_shipping, Unset):
            shipping = UNSET
        else:
            shipping = ProductShipping.from_dict(_shipping)

        price_off_discount = d.pop("priceOffDiscount", UNSET)

        is_discount_in_percentage = d.pop("isDiscountInPercentage", UNSET)

        has_options = d.pop("hasOptions", UNSET)

        _price_off_discount_start_date = d.pop("priceOffDiscountStartDate", UNSET)
        price_off_discount_start_date: Union[Unset, datetime.datetime]
        if isinstance(_price_off_discount_start_date, Unset):
            price_off_discount_start_date = UNSET
        else:
            price_off_discount_start_date = isoparse(_price_off_discount_start_date)

        _price_off_discount_end_date = d.pop("priceOffDiscountEndDate", UNSET)
        price_off_discount_end_date: Union[Unset, datetime.datetime]
        if isinstance(_price_off_discount_end_date, Unset):
            price_off_discount_end_date = UNSET
        else:
            price_off_discount_end_date = isoparse(_price_off_discount_end_date)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ProductImage.from_dict(images_item_data)

            images.append(images_item)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = ProductOption.from_dict(options_item_data)

            options.append(options_item)

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CustomField.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

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

        product = cls(
            catalogs=catalogs,
            id=id,
            category=category,
            name=name,
            code=code,
            status=status,
            keyword=keyword,
            description=description,
            unit_price=unit_price,
            download_url=download_url,
            is_apply_on_site_tax=is_apply_on_site_tax,
            is_front_end_display=is_front_end_display,
            shipping=shipping,
            price_off_discount=price_off_discount,
            is_discount_in_percentage=is_discount_in_percentage,
            has_options=has_options,
            price_off_discount_start_date=price_off_discount_start_date,
            price_off_discount_end_date=price_off_discount_end_date,
            images=images,
            options=options,
            custom_fields=custom_fields,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
        )

        product.additional_properties = d
        return product

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
