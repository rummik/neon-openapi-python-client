from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.time_sheet_api import TimeSheetApi


T = TypeVar("T", bound="TimeSheetSearchResult")


@_attrs_define
class TimeSheetSearchResult:
    """
    Attributes:
        time_sheet_api_list (Union[Unset, list['TimeSheetApi']]):
        pagination (Union[Unset, Pagination]):
    """

    time_sheet_api_list: Union[Unset, list["TimeSheetApi"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_sheet_api_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.time_sheet_api_list, Unset):
            time_sheet_api_list = []
            for time_sheet_api_list_item_data in self.time_sheet_api_list:
                time_sheet_api_list_item = time_sheet_api_list_item_data.to_dict()
                time_sheet_api_list.append(time_sheet_api_list_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_sheet_api_list is not UNSET:
            field_dict["timeSheetApiList"] = time_sheet_api_list
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.time_sheet_api import TimeSheetApi

        d = dict(src_dict)
        time_sheet_api_list = []
        _time_sheet_api_list = d.pop("timeSheetApiList", UNSET)
        for time_sheet_api_list_item_data in _time_sheet_api_list or []:
            time_sheet_api_list_item = TimeSheetApi.from_dict(time_sheet_api_list_item_data)

            time_sheet_api_list.append(time_sheet_api_list_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        time_sheet_search_result = cls(
            time_sheet_api_list=time_sheet_api_list,
            pagination=pagination,
        )

        time_sheet_search_result.additional_properties = d
        return time_sheet_search_result

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
