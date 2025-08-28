from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.neon_pay_setting import NeonPaySetting


T = TypeVar("T", bound="ProcessorSettings")


@_attrs_define
class ProcessorSettings:
    """
    Attributes:
        neon_pay_setting (Union[Unset, NeonPaySetting]):
    """

    neon_pay_setting: Union[Unset, "NeonPaySetting"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        neon_pay_setting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.neon_pay_setting, Unset):
            neon_pay_setting = self.neon_pay_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if neon_pay_setting is not UNSET:
            field_dict["neonPaySetting"] = neon_pay_setting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.neon_pay_setting import NeonPaySetting

        d = dict(src_dict)
        _neon_pay_setting = d.pop("neonPaySetting", UNSET)
        neon_pay_setting: Union[Unset, NeonPaySetting]
        if isinstance(_neon_pay_setting, Unset):
            neon_pay_setting = UNSET
        else:
            neon_pay_setting = NeonPaySetting.from_dict(_neon_pay_setting)

        processor_settings = cls(
            neon_pay_setting=neon_pay_setting,
        )

        processor_settings.additional_properties = d
        return processor_settings

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
