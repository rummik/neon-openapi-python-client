from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_data_component import CustomFieldDataComponent
from ..models.custom_field_data_data_type import CustomFieldDataDataType
from ..models.custom_field_data_display_type import CustomFieldDataDisplayType
from ..models.custom_field_data_status import CustomFieldDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_custom_field_data import AccountCustomFieldData
    from ..models.custom_field_option import CustomFieldOption
    from ..models.event_custom_field_data import EventCustomFieldData
    from ..models.member_ship_custom_field_data import MemberShipCustomFieldData
    from ..models.product_custom_field_data import ProductCustomFieldData


T = TypeVar("T", bound="CustomFieldData")


@_attrs_define
class CustomFieldData:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        status (Union[Unset, CustomFieldDataStatus]):
        display_name (Union[Unset, str]):
        group_id (Union[Unset, str]):
        display_type (Union[Unset, CustomFieldDataDisplayType]):
        data_type (Union[Unset, CustomFieldDataDataType]):
        constituent_read_only (Union[Unset, bool]):
        component (Union[Unset, CustomFieldDataComponent]):
        option_values (Union[Unset, list['CustomFieldOption']]):
        account_settings (Union[Unset, AccountCustomFieldData]):
        event_settings (Union[Unset, EventCustomFieldData]):
        membership_settings (Union[Unset, MemberShipCustomFieldData]):
        product_settings (Union[Unset, ProductCustomFieldData]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, CustomFieldDataStatus] = UNSET
    display_name: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    display_type: Union[Unset, CustomFieldDataDisplayType] = UNSET
    data_type: Union[Unset, CustomFieldDataDataType] = UNSET
    constituent_read_only: Union[Unset, bool] = UNSET
    component: Union[Unset, CustomFieldDataComponent] = UNSET
    option_values: Union[Unset, list["CustomFieldOption"]] = UNSET
    account_settings: Union[Unset, "AccountCustomFieldData"] = UNSET
    event_settings: Union[Unset, "EventCustomFieldData"] = UNSET
    membership_settings: Union[Unset, "MemberShipCustomFieldData"] = UNSET
    product_settings: Union[Unset, "ProductCustomFieldData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        display_name = self.display_name

        group_id = self.group_id

        display_type: Union[Unset, str] = UNSET
        if not isinstance(self.display_type, Unset):
            display_type = self.display_type.value

        data_type: Union[Unset, str] = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        constituent_read_only = self.constituent_read_only

        component: Union[Unset, str] = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.value

        option_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.option_values, Unset):
            option_values = []
            for option_values_item_data in self.option_values:
                option_values_item = option_values_item_data.to_dict()
                option_values.append(option_values_item)

        account_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.account_settings, Unset):
            account_settings = self.account_settings.to_dict()

        event_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_settings, Unset):
            event_settings = self.event_settings.to_dict()

        membership_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.membership_settings, Unset):
            membership_settings = self.membership_settings.to_dict()

        product_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product_settings, Unset):
            product_settings = self.product_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if display_type is not UNSET:
            field_dict["displayType"] = display_type
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if constituent_read_only is not UNSET:
            field_dict["constituentReadOnly"] = constituent_read_only
        if component is not UNSET:
            field_dict["component"] = component
        if option_values is not UNSET:
            field_dict["optionValues"] = option_values
        if account_settings is not UNSET:
            field_dict["accountSettings"] = account_settings
        if event_settings is not UNSET:
            field_dict["eventSettings"] = event_settings
        if membership_settings is not UNSET:
            field_dict["membershipSettings"] = membership_settings
        if product_settings is not UNSET:
            field_dict["productSettings"] = product_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_custom_field_data import AccountCustomFieldData
        from ..models.custom_field_option import CustomFieldOption
        from ..models.event_custom_field_data import EventCustomFieldData
        from ..models.member_ship_custom_field_data import MemberShipCustomFieldData
        from ..models.product_custom_field_data import ProductCustomFieldData

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CustomFieldDataStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CustomFieldDataStatus(_status)

        display_name = d.pop("displayName", UNSET)

        group_id = d.pop("groupId", UNSET)

        _display_type = d.pop("displayType", UNSET)
        display_type: Union[Unset, CustomFieldDataDisplayType]
        if isinstance(_display_type, Unset):
            display_type = UNSET
        else:
            display_type = CustomFieldDataDisplayType(_display_type)

        _data_type = d.pop("dataType", UNSET)
        data_type: Union[Unset, CustomFieldDataDataType]
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = CustomFieldDataDataType(_data_type)

        constituent_read_only = d.pop("constituentReadOnly", UNSET)

        _component = d.pop("component", UNSET)
        component: Union[Unset, CustomFieldDataComponent]
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = CustomFieldDataComponent(_component)

        option_values = []
        _option_values = d.pop("optionValues", UNSET)
        for option_values_item_data in _option_values or []:
            option_values_item = CustomFieldOption.from_dict(option_values_item_data)

            option_values.append(option_values_item)

        _account_settings = d.pop("accountSettings", UNSET)
        account_settings: Union[Unset, AccountCustomFieldData]
        if isinstance(_account_settings, Unset):
            account_settings = UNSET
        else:
            account_settings = AccountCustomFieldData.from_dict(_account_settings)

        _event_settings = d.pop("eventSettings", UNSET)
        event_settings: Union[Unset, EventCustomFieldData]
        if isinstance(_event_settings, Unset):
            event_settings = UNSET
        else:
            event_settings = EventCustomFieldData.from_dict(_event_settings)

        _membership_settings = d.pop("membershipSettings", UNSET)
        membership_settings: Union[Unset, MemberShipCustomFieldData]
        if isinstance(_membership_settings, Unset):
            membership_settings = UNSET
        else:
            membership_settings = MemberShipCustomFieldData.from_dict(_membership_settings)

        _product_settings = d.pop("productSettings", UNSET)
        product_settings: Union[Unset, ProductCustomFieldData]
        if isinstance(_product_settings, Unset):
            product_settings = UNSET
        else:
            product_settings = ProductCustomFieldData.from_dict(_product_settings)

        custom_field_data = cls(
            id=id,
            name=name,
            status=status,
            display_name=display_name,
            group_id=group_id,
            display_type=display_type,
            data_type=data_type,
            constituent_read_only=constituent_read_only,
            component=component,
            option_values=option_values,
            account_settings=account_settings,
            event_settings=event_settings,
            membership_settings=membership_settings,
            product_settings=product_settings,
        )

        custom_field_data.additional_properties = d
        return custom_field_data

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
