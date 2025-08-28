from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opportunity_shift import OpportunityShift
    from ..models.pagination import Pagination


T = TypeVar("T", bound="OpportunityShiftSearchResult")


@_attrs_define
class OpportunityShiftSearchResult:
    """
    Attributes:
        opportunity_shift_list (Union[Unset, list['OpportunityShift']]):
        pagination (Union[Unset, Pagination]):
    """

    opportunity_shift_list: Union[Unset, list["OpportunityShift"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        opportunity_shift_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.opportunity_shift_list, Unset):
            opportunity_shift_list = []
            for opportunity_shift_list_item_data in self.opportunity_shift_list:
                opportunity_shift_list_item = opportunity_shift_list_item_data.to_dict()
                opportunity_shift_list.append(opportunity_shift_list_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opportunity_shift_list is not UNSET:
            field_dict["opportunityShiftList"] = opportunity_shift_list
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opportunity_shift import OpportunityShift
        from ..models.pagination import Pagination

        d = dict(src_dict)
        opportunity_shift_list = []
        _opportunity_shift_list = d.pop("opportunityShiftList", UNSET)
        for opportunity_shift_list_item_data in _opportunity_shift_list or []:
            opportunity_shift_list_item = OpportunityShift.from_dict(opportunity_shift_list_item_data)

            opportunity_shift_list.append(opportunity_shift_list_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        opportunity_shift_search_result = cls(
            opportunity_shift_list=opportunity_shift_list,
            pagination=pagination,
        )

        opportunity_shift_search_result.additional_properties = d
        return opportunity_shift_search_result

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
