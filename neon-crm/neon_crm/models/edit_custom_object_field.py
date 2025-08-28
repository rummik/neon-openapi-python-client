from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_number import AutoNumber
    from ..models.basic_attribute import BasicAttribute
    from ..models.checkbox_single import CheckboxSingle
    from ..models.date import Date
    from ..models.file import File
    from ..models.formula import Formula
    from ..models.lookup import Lookup
    from ..models.master_detail import MasterDetail
    from ..models.number import Number
    from ..models.options_field import OptionsField
    from ..models.percent import Percent
    from ..models.text import Text
    from ..models.textarea import Textarea


T = TypeVar("T", bound="EditCustomObjectField")


@_attrs_define
class EditCustomObjectField:
    """
    Attributes:
        field_label (Union[Unset, str]):
        field_description (Union[Unset, str]):
        field_help_text (Union[Unset, str]):
        is_internal (Union[Unset, bool]):
        auto_number_attribute (Union[Unset, AutoNumber]):
        formula_attribute (Union[Unset, Formula]):
        master_detail_attribute (Union[Unset, MasterDetail]):
        lookup_attribute (Union[Unset, Lookup]):
        text_attribute (Union[Unset, Text]):
        number_attribute (Union[Unset, Number]):
        percent_attribute (Union[Unset, Percent]):
        email_attribute (Union[Unset, BasicAttribute]):
        phone_attribute (Union[Unset, BasicAttribute]):
        url_attribute (Union[Unset, BasicAttribute]):
        textarea_short_attribute (Union[Unset, Textarea]):
        textarea_attribute (Union[Unset, Textarea]):
        date_attribute (Union[Unset, Date]):
        date_time_attribute (Union[Unset, Date]):
        checkbox_single_attribute (Union[Unset, CheckboxSingle]):
        checkbox_attribute (Union[Unset, OptionsField]):
        dropdown_attribute (Union[Unset, OptionsField]):
        radio_attribute (Union[Unset, OptionsField]):
        file_attribute (Union[Unset, File]):
    """

    field_label: Union[Unset, str] = UNSET
    field_description: Union[Unset, str] = UNSET
    field_help_text: Union[Unset, str] = UNSET
    is_internal: Union[Unset, bool] = UNSET
    auto_number_attribute: Union[Unset, "AutoNumber"] = UNSET
    formula_attribute: Union[Unset, "Formula"] = UNSET
    master_detail_attribute: Union[Unset, "MasterDetail"] = UNSET
    lookup_attribute: Union[Unset, "Lookup"] = UNSET
    text_attribute: Union[Unset, "Text"] = UNSET
    number_attribute: Union[Unset, "Number"] = UNSET
    percent_attribute: Union[Unset, "Percent"] = UNSET
    email_attribute: Union[Unset, "BasicAttribute"] = UNSET
    phone_attribute: Union[Unset, "BasicAttribute"] = UNSET
    url_attribute: Union[Unset, "BasicAttribute"] = UNSET
    textarea_short_attribute: Union[Unset, "Textarea"] = UNSET
    textarea_attribute: Union[Unset, "Textarea"] = UNSET
    date_attribute: Union[Unset, "Date"] = UNSET
    date_time_attribute: Union[Unset, "Date"] = UNSET
    checkbox_single_attribute: Union[Unset, "CheckboxSingle"] = UNSET
    checkbox_attribute: Union[Unset, "OptionsField"] = UNSET
    dropdown_attribute: Union[Unset, "OptionsField"] = UNSET
    radio_attribute: Union[Unset, "OptionsField"] = UNSET
    file_attribute: Union[Unset, "File"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_label = self.field_label

        field_description = self.field_description

        field_help_text = self.field_help_text

        is_internal = self.is_internal

        auto_number_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auto_number_attribute, Unset):
            auto_number_attribute = self.auto_number_attribute.to_dict()

        formula_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.formula_attribute, Unset):
            formula_attribute = self.formula_attribute.to_dict()

        master_detail_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.master_detail_attribute, Unset):
            master_detail_attribute = self.master_detail_attribute.to_dict()

        lookup_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.lookup_attribute, Unset):
            lookup_attribute = self.lookup_attribute.to_dict()

        text_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.text_attribute, Unset):
            text_attribute = self.text_attribute.to_dict()

        number_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.number_attribute, Unset):
            number_attribute = self.number_attribute.to_dict()

        percent_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.percent_attribute, Unset):
            percent_attribute = self.percent_attribute.to_dict()

        email_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.email_attribute, Unset):
            email_attribute = self.email_attribute.to_dict()

        phone_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.phone_attribute, Unset):
            phone_attribute = self.phone_attribute.to_dict()

        url_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.url_attribute, Unset):
            url_attribute = self.url_attribute.to_dict()

        textarea_short_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.textarea_short_attribute, Unset):
            textarea_short_attribute = self.textarea_short_attribute.to_dict()

        textarea_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.textarea_attribute, Unset):
            textarea_attribute = self.textarea_attribute.to_dict()

        date_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.date_attribute, Unset):
            date_attribute = self.date_attribute.to_dict()

        date_time_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.date_time_attribute, Unset):
            date_time_attribute = self.date_time_attribute.to_dict()

        checkbox_single_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.checkbox_single_attribute, Unset):
            checkbox_single_attribute = self.checkbox_single_attribute.to_dict()

        checkbox_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.checkbox_attribute, Unset):
            checkbox_attribute = self.checkbox_attribute.to_dict()

        dropdown_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dropdown_attribute, Unset):
            dropdown_attribute = self.dropdown_attribute.to_dict()

        radio_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.radio_attribute, Unset):
            radio_attribute = self.radio_attribute.to_dict()

        file_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.file_attribute, Unset):
            file_attribute = self.file_attribute.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_label is not UNSET:
            field_dict["fieldLabel"] = field_label
        if field_description is not UNSET:
            field_dict["fieldDescription"] = field_description
        if field_help_text is not UNSET:
            field_dict["fieldHelpText"] = field_help_text
        if is_internal is not UNSET:
            field_dict["isInternal"] = is_internal
        if auto_number_attribute is not UNSET:
            field_dict["autoNumberAttribute"] = auto_number_attribute
        if formula_attribute is not UNSET:
            field_dict["formulaAttribute"] = formula_attribute
        if master_detail_attribute is not UNSET:
            field_dict["masterDetailAttribute"] = master_detail_attribute
        if lookup_attribute is not UNSET:
            field_dict["lookupAttribute"] = lookup_attribute
        if text_attribute is not UNSET:
            field_dict["textAttribute"] = text_attribute
        if number_attribute is not UNSET:
            field_dict["numberAttribute"] = number_attribute
        if percent_attribute is not UNSET:
            field_dict["percentAttribute"] = percent_attribute
        if email_attribute is not UNSET:
            field_dict["emailAttribute"] = email_attribute
        if phone_attribute is not UNSET:
            field_dict["phoneAttribute"] = phone_attribute
        if url_attribute is not UNSET:
            field_dict["urlAttribute"] = url_attribute
        if textarea_short_attribute is not UNSET:
            field_dict["textareaShortAttribute"] = textarea_short_attribute
        if textarea_attribute is not UNSET:
            field_dict["textareaAttribute"] = textarea_attribute
        if date_attribute is not UNSET:
            field_dict["dateAttribute"] = date_attribute
        if date_time_attribute is not UNSET:
            field_dict["dateTimeAttribute"] = date_time_attribute
        if checkbox_single_attribute is not UNSET:
            field_dict["checkboxSingleAttribute"] = checkbox_single_attribute
        if checkbox_attribute is not UNSET:
            field_dict["checkboxAttribute"] = checkbox_attribute
        if dropdown_attribute is not UNSET:
            field_dict["dropdownAttribute"] = dropdown_attribute
        if radio_attribute is not UNSET:
            field_dict["radioAttribute"] = radio_attribute
        if file_attribute is not UNSET:
            field_dict["fileAttribute"] = file_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_number import AutoNumber
        from ..models.basic_attribute import BasicAttribute
        from ..models.checkbox_single import CheckboxSingle
        from ..models.date import Date
        from ..models.file import File
        from ..models.formula import Formula
        from ..models.lookup import Lookup
        from ..models.master_detail import MasterDetail
        from ..models.number import Number
        from ..models.options_field import OptionsField
        from ..models.percent import Percent
        from ..models.text import Text
        from ..models.textarea import Textarea

        d = dict(src_dict)
        field_label = d.pop("fieldLabel", UNSET)

        field_description = d.pop("fieldDescription", UNSET)

        field_help_text = d.pop("fieldHelpText", UNSET)

        is_internal = d.pop("isInternal", UNSET)

        _auto_number_attribute = d.pop("autoNumberAttribute", UNSET)
        auto_number_attribute: Union[Unset, AutoNumber]
        if isinstance(_auto_number_attribute, Unset):
            auto_number_attribute = UNSET
        else:
            auto_number_attribute = AutoNumber.from_dict(_auto_number_attribute)

        _formula_attribute = d.pop("formulaAttribute", UNSET)
        formula_attribute: Union[Unset, Formula]
        if isinstance(_formula_attribute, Unset):
            formula_attribute = UNSET
        else:
            formula_attribute = Formula.from_dict(_formula_attribute)

        _master_detail_attribute = d.pop("masterDetailAttribute", UNSET)
        master_detail_attribute: Union[Unset, MasterDetail]
        if isinstance(_master_detail_attribute, Unset):
            master_detail_attribute = UNSET
        else:
            master_detail_attribute = MasterDetail.from_dict(_master_detail_attribute)

        _lookup_attribute = d.pop("lookupAttribute", UNSET)
        lookup_attribute: Union[Unset, Lookup]
        if isinstance(_lookup_attribute, Unset):
            lookup_attribute = UNSET
        else:
            lookup_attribute = Lookup.from_dict(_lookup_attribute)

        _text_attribute = d.pop("textAttribute", UNSET)
        text_attribute: Union[Unset, Text]
        if isinstance(_text_attribute, Unset):
            text_attribute = UNSET
        else:
            text_attribute = Text.from_dict(_text_attribute)

        _number_attribute = d.pop("numberAttribute", UNSET)
        number_attribute: Union[Unset, Number]
        if isinstance(_number_attribute, Unset):
            number_attribute = UNSET
        else:
            number_attribute = Number.from_dict(_number_attribute)

        _percent_attribute = d.pop("percentAttribute", UNSET)
        percent_attribute: Union[Unset, Percent]
        if isinstance(_percent_attribute, Unset):
            percent_attribute = UNSET
        else:
            percent_attribute = Percent.from_dict(_percent_attribute)

        _email_attribute = d.pop("emailAttribute", UNSET)
        email_attribute: Union[Unset, BasicAttribute]
        if isinstance(_email_attribute, Unset):
            email_attribute = UNSET
        else:
            email_attribute = BasicAttribute.from_dict(_email_attribute)

        _phone_attribute = d.pop("phoneAttribute", UNSET)
        phone_attribute: Union[Unset, BasicAttribute]
        if isinstance(_phone_attribute, Unset):
            phone_attribute = UNSET
        else:
            phone_attribute = BasicAttribute.from_dict(_phone_attribute)

        _url_attribute = d.pop("urlAttribute", UNSET)
        url_attribute: Union[Unset, BasicAttribute]
        if isinstance(_url_attribute, Unset):
            url_attribute = UNSET
        else:
            url_attribute = BasicAttribute.from_dict(_url_attribute)

        _textarea_short_attribute = d.pop("textareaShortAttribute", UNSET)
        textarea_short_attribute: Union[Unset, Textarea]
        if isinstance(_textarea_short_attribute, Unset):
            textarea_short_attribute = UNSET
        else:
            textarea_short_attribute = Textarea.from_dict(_textarea_short_attribute)

        _textarea_attribute = d.pop("textareaAttribute", UNSET)
        textarea_attribute: Union[Unset, Textarea]
        if isinstance(_textarea_attribute, Unset):
            textarea_attribute = UNSET
        else:
            textarea_attribute = Textarea.from_dict(_textarea_attribute)

        _date_attribute = d.pop("dateAttribute", UNSET)
        date_attribute: Union[Unset, Date]
        if isinstance(_date_attribute, Unset):
            date_attribute = UNSET
        else:
            date_attribute = Date.from_dict(_date_attribute)

        _date_time_attribute = d.pop("dateTimeAttribute", UNSET)
        date_time_attribute: Union[Unset, Date]
        if isinstance(_date_time_attribute, Unset):
            date_time_attribute = UNSET
        else:
            date_time_attribute = Date.from_dict(_date_time_attribute)

        _checkbox_single_attribute = d.pop("checkboxSingleAttribute", UNSET)
        checkbox_single_attribute: Union[Unset, CheckboxSingle]
        if isinstance(_checkbox_single_attribute, Unset):
            checkbox_single_attribute = UNSET
        else:
            checkbox_single_attribute = CheckboxSingle.from_dict(_checkbox_single_attribute)

        _checkbox_attribute = d.pop("checkboxAttribute", UNSET)
        checkbox_attribute: Union[Unset, OptionsField]
        if isinstance(_checkbox_attribute, Unset):
            checkbox_attribute = UNSET
        else:
            checkbox_attribute = OptionsField.from_dict(_checkbox_attribute)

        _dropdown_attribute = d.pop("dropdownAttribute", UNSET)
        dropdown_attribute: Union[Unset, OptionsField]
        if isinstance(_dropdown_attribute, Unset):
            dropdown_attribute = UNSET
        else:
            dropdown_attribute = OptionsField.from_dict(_dropdown_attribute)

        _radio_attribute = d.pop("radioAttribute", UNSET)
        radio_attribute: Union[Unset, OptionsField]
        if isinstance(_radio_attribute, Unset):
            radio_attribute = UNSET
        else:
            radio_attribute = OptionsField.from_dict(_radio_attribute)

        _file_attribute = d.pop("fileAttribute", UNSET)
        file_attribute: Union[Unset, File]
        if isinstance(_file_attribute, Unset):
            file_attribute = UNSET
        else:
            file_attribute = File.from_dict(_file_attribute)

        edit_custom_object_field = cls(
            field_label=field_label,
            field_description=field_description,
            field_help_text=field_help_text,
            is_internal=is_internal,
            auto_number_attribute=auto_number_attribute,
            formula_attribute=formula_attribute,
            master_detail_attribute=master_detail_attribute,
            lookup_attribute=lookup_attribute,
            text_attribute=text_attribute,
            number_attribute=number_attribute,
            percent_attribute=percent_attribute,
            email_attribute=email_attribute,
            phone_attribute=phone_attribute,
            url_attribute=url_attribute,
            textarea_short_attribute=textarea_short_attribute,
            textarea_attribute=textarea_attribute,
            date_attribute=date_attribute,
            date_time_attribute=date_time_attribute,
            checkbox_single_attribute=checkbox_single_attribute,
            checkbox_attribute=checkbox_attribute,
            dropdown_attribute=dropdown_attribute,
            radio_attribute=radio_attribute,
            file_attribute=file_attribute,
        )

        edit_custom_object_field.additional_properties = d
        return edit_custom_object_field

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
