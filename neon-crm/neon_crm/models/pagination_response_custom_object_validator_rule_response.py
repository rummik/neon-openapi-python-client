from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_object_validator_rule_response import CustomObjectValidatorRuleResponse
    from ..models.pagination import Pagination


T = TypeVar("T", bound="PaginationResponseCustomObjectValidatorRuleResponse")


@_attrs_define
class PaginationResponseCustomObjectValidatorRuleResponse:
    """
    Attributes:
        results (Union[Unset, list['CustomObjectValidatorRuleResponse']]):
        pagination (Union[Unset, Pagination]):
    """

    results: Union[Unset, list["CustomObjectValidatorRuleResponse"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_object_validator_rule_response import CustomObjectValidatorRuleResponse
        from ..models.pagination import Pagination

        d = dict(src_dict)
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = CustomObjectValidatorRuleResponse.from_dict(results_item_data)

            results.append(results_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        pagination_response_custom_object_validator_rule_response = cls(
            results=results,
            pagination=pagination,
        )

        pagination_response_custom_object_validator_rule_response.additional_properties = d
        return pagination_response_custom_object_validator_rule_response

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
