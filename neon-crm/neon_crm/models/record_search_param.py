from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_object_page_param import CustomObjectPageParam
    from ..models.record_search_criteria import RecordSearchCriteria


T = TypeVar("T", bound="RecordSearchParam")


@_attrs_define
class RecordSearchParam:
    """
    Attributes:
        search_criteria_list (Union[Unset, list['RecordSearchCriteria']]):
        output_column_list (Union[Unset, list[str]]):
        page_param (Union[Unset, CustomObjectPageParam]):
    """

    search_criteria_list: Union[Unset, list["RecordSearchCriteria"]] = UNSET
    output_column_list: Union[Unset, list[str]] = UNSET
    page_param: Union[Unset, "CustomObjectPageParam"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_criteria_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.search_criteria_list, Unset):
            search_criteria_list = []
            for search_criteria_list_item_data in self.search_criteria_list:
                search_criteria_list_item = search_criteria_list_item_data.to_dict()
                search_criteria_list.append(search_criteria_list_item)

        output_column_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.output_column_list, Unset):
            output_column_list = self.output_column_list

        page_param: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_param, Unset):
            page_param = self.page_param.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_criteria_list is not UNSET:
            field_dict["searchCriteriaList"] = search_criteria_list
        if output_column_list is not UNSET:
            field_dict["outputColumnList"] = output_column_list
        if page_param is not UNSET:
            field_dict["pageParam"] = page_param

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_object_page_param import CustomObjectPageParam
        from ..models.record_search_criteria import RecordSearchCriteria

        d = dict(src_dict)
        search_criteria_list = []
        _search_criteria_list = d.pop("searchCriteriaList", UNSET)
        for search_criteria_list_item_data in _search_criteria_list or []:
            search_criteria_list_item = RecordSearchCriteria.from_dict(search_criteria_list_item_data)

            search_criteria_list.append(search_criteria_list_item)

        output_column_list = cast(list[str], d.pop("outputColumnList", UNSET))

        _page_param = d.pop("pageParam", UNSET)
        page_param: Union[Unset, CustomObjectPageParam]
        if isinstance(_page_param, Unset):
            page_param = UNSET
        else:
            page_param = CustomObjectPageParam.from_dict(_page_param)

        record_search_param = cls(
            search_criteria_list=search_criteria_list,
            output_column_list=output_column_list,
            page_param=page_param,
        )

        record_search_param.additional_properties = d
        return record_search_param

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
