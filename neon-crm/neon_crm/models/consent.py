from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.consent_data_sharing import ConsentDataSharing
from ..models.consent_email import ConsentEmail
from ..models.consent_mail import ConsentMail
from ..models.consent_phone import ConsentPhone
from ..models.consent_sms import ConsentSms
from ..types import UNSET, Unset

T = TypeVar("T", bound="Consent")


@_attrs_define
class Consent:
    """
    Attributes:
        email (Union[Unset, ConsentEmail]):
        phone (Union[Unset, ConsentPhone]):
        mail (Union[Unset, ConsentMail]):
        sms (Union[Unset, ConsentSms]):
        data_sharing (Union[Unset, ConsentDataSharing]):
    """

    email: Union[Unset, ConsentEmail] = UNSET
    phone: Union[Unset, ConsentPhone] = UNSET
    mail: Union[Unset, ConsentMail] = UNSET
    sms: Union[Unset, ConsentSms] = UNSET
    data_sharing: Union[Unset, ConsentDataSharing] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: Union[Unset, str] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.value

        phone: Union[Unset, str] = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone.value

        mail: Union[Unset, str] = UNSET
        if not isinstance(self.mail, Unset):
            mail = self.mail.value

        sms: Union[Unset, str] = UNSET
        if not isinstance(self.sms, Unset):
            sms = self.sms.value

        data_sharing: Union[Unset, str] = UNSET
        if not isinstance(self.data_sharing, Unset):
            data_sharing = self.data_sharing.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if mail is not UNSET:
            field_dict["mail"] = mail
        if sms is not UNSET:
            field_dict["sms"] = sms
        if data_sharing is not UNSET:
            field_dict["dataSharing"] = data_sharing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _email = d.pop("email", UNSET)
        email: Union[Unset, ConsentEmail]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = ConsentEmail(_email)

        _phone = d.pop("phone", UNSET)
        phone: Union[Unset, ConsentPhone]
        if isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = ConsentPhone(_phone)

        _mail = d.pop("mail", UNSET)
        mail: Union[Unset, ConsentMail]
        if isinstance(_mail, Unset):
            mail = UNSET
        else:
            mail = ConsentMail(_mail)

        _sms = d.pop("sms", UNSET)
        sms: Union[Unset, ConsentSms]
        if isinstance(_sms, Unset):
            sms = UNSET
        else:
            sms = ConsentSms(_sms)

        _data_sharing = d.pop("dataSharing", UNSET)
        data_sharing: Union[Unset, ConsentDataSharing]
        if isinstance(_data_sharing, Unset):
            data_sharing = UNSET
        else:
            data_sharing = ConsentDataSharing(_data_sharing)

        consent = cls(
            email=email,
            phone=phone,
            mail=mail,
            sms=sms,
            data_sharing=data_sharing,
        )

        consent.additional_properties = d
        return consent

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
