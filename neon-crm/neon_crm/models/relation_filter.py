from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_criteria import FilterCriteria


T = TypeVar("T", bound="RelationFilter")


@_attrs_define
class RelationFilter:
    """
    Attributes:
        active (Union[Unset, bool]):
        error_message (Union[Unset, str]):
        lookup_window_text (Union[Unset, str]):
        filter_criteria (Union[Unset, list['FilterCriteria']]):
    """

    active: Union[Unset, bool] = UNSET
    error_message: Union[Unset, str] = UNSET
    lookup_window_text: Union[Unset, str] = UNSET
    filter_criteria: Union[Unset, list["FilterCriteria"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        error_message = self.error_message

        lookup_window_text = self.lookup_window_text

        filter_criteria: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filter_criteria, Unset):
            filter_criteria = []
            for filter_criteria_item_data in self.filter_criteria:
                filter_criteria_item = filter_criteria_item_data.to_dict()
                filter_criteria.append(filter_criteria_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if lookup_window_text is not UNSET:
            field_dict["lookupWindowText"] = lookup_window_text
        if filter_criteria is not UNSET:
            field_dict["filterCriteria"] = filter_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_criteria import FilterCriteria

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        lookup_window_text = d.pop("lookupWindowText", UNSET)

        filter_criteria = []
        _filter_criteria = d.pop("filterCriteria", UNSET)
        for filter_criteria_item_data in _filter_criteria or []:
            filter_criteria_item = FilterCriteria.from_dict(filter_criteria_item_data)

            filter_criteria.append(filter_criteria_item)

        relation_filter = cls(
            active=active,
            error_message=error_message,
            lookup_window_text=lookup_window_text,
            filter_criteria=filter_criteria,
        )

        relation_filter.additional_properties = d
        return relation_filter

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
