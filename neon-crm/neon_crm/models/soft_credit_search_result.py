from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.soft_credit import SoftCredit


T = TypeVar("T", bound="SoftCreditSearchResult")


@_attrs_define
class SoftCreditSearchResult:
    """
    Attributes:
        soft_credits (Union[Unset, list['SoftCredit']]):
        pagination (Union[Unset, Pagination]):
    """

    soft_credits: Union[Unset, list["SoftCredit"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        soft_credits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.soft_credits, Unset):
            soft_credits = []
            for soft_credits_item_data in self.soft_credits:
                soft_credits_item = soft_credits_item_data.to_dict()
                soft_credits.append(soft_credits_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if soft_credits is not UNSET:
            field_dict["softCredits"] = soft_credits
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.soft_credit import SoftCredit

        d = dict(src_dict)
        soft_credits = []
        _soft_credits = d.pop("softCredits", UNSET)
        for soft_credits_item_data in _soft_credits or []:
            soft_credits_item = SoftCredit.from_dict(soft_credits_item_data)

            soft_credits.append(soft_credits_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        soft_credit_search_result = cls(
            soft_credits=soft_credits,
            pagination=pagination,
        )

        soft_credit_search_result.additional_properties = d
        return soft_credit_search_result

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
