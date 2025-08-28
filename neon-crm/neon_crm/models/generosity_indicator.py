from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerosityIndicator")


@_attrs_define
class GenerosityIndicator:
    """
    Attributes:
        indicator (Union[Unset, float]):
        affinity (Union[Unset, int]):
        recency (Union[Unset, int]):
        frequency (Union[Unset, int]):
        monetary_value (Union[Unset, int]):
    """

    indicator: Union[Unset, float] = UNSET
    affinity: Union[Unset, int] = UNSET
    recency: Union[Unset, int] = UNSET
    frequency: Union[Unset, int] = UNSET
    monetary_value: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indicator = self.indicator

        affinity = self.affinity

        recency = self.recency

        frequency = self.frequency

        monetary_value = self.monetary_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if indicator is not UNSET:
            field_dict["indicator"] = indicator
        if affinity is not UNSET:
            field_dict["affinity"] = affinity
        if recency is not UNSET:
            field_dict["recency"] = recency
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if monetary_value is not UNSET:
            field_dict["monetaryValue"] = monetary_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indicator = d.pop("indicator", UNSET)

        affinity = d.pop("affinity", UNSET)

        recency = d.pop("recency", UNSET)

        frequency = d.pop("frequency", UNSET)

        monetary_value = d.pop("monetaryValue", UNSET)

        generosity_indicator = cls(
            indicator=indicator,
            affinity=affinity,
            recency=recency,
            frequency=frequency,
            monetary_value=monetary_value,
        )

        generosity_indicator.additional_properties = d
        return generosity_indicator

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
