from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_role_api import AccountRoleApi
    from ..models.consent import Consent
    from ..models.contact import Contact
    from ..models.custom_field import CustomField
    from ..models.generosity_indicator import GenerosityIndicator
    from ..models.id_name_pair import IdNamePair
    from ..models.login import Login
    from ..models.origin import Origin
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="IndividualAccount")


@_attrs_define
class IndividualAccount:
    """
    Attributes:
        account_id (Union[Unset, str]):
        no_solicitation (Union[Unset, bool]):
        login (Union[Unset, Login]):
        url (Union[Unset, str]):
        timestamps (Union[Unset, Timestamps]):
        consent (Union[Unset, Consent]):
        account_custom_fields (Union[Unset, list['CustomField']]):
        source (Union[Unset, IdNamePair]):
        primary_contact (Union[Unset, Contact]):
        send_system_email (Union[Unset, bool]):
        email_1_opt_out (Union[Unset, bool]):
        origin (Union[Unset, Origin]):
        account_current_membership_status (Union[Unset, str]):
        generosity_indicator (Union[Unset, GenerosityIndicator]):
        send_text_opt_in (Union[Unset, bool]):
        sms_number (Union[Unset, str]):
        company (Union[Unset, IdNamePair]):
        facebook_page (Union[Unset, str]):
        twitter_page (Union[Unset, str]):
        individual_types (Union[Unset, list['IdNamePair']]):
        role_vo_list (Union[Unset, list['AccountRoleApi']]):
    """

    account_id: Union[Unset, str] = UNSET
    no_solicitation: Union[Unset, bool] = UNSET
    login: Union[Unset, "Login"] = UNSET
    url: Union[Unset, str] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    consent: Union[Unset, "Consent"] = UNSET
    account_custom_fields: Union[Unset, list["CustomField"]] = UNSET
    source: Union[Unset, "IdNamePair"] = UNSET
    primary_contact: Union[Unset, "Contact"] = UNSET
    send_system_email: Union[Unset, bool] = UNSET
    email_1_opt_out: Union[Unset, bool] = UNSET
    origin: Union[Unset, "Origin"] = UNSET
    account_current_membership_status: Union[Unset, str] = UNSET
    generosity_indicator: Union[Unset, "GenerosityIndicator"] = UNSET
    send_text_opt_in: Union[Unset, bool] = UNSET
    sms_number: Union[Unset, str] = UNSET
    company: Union[Unset, "IdNamePair"] = UNSET
    facebook_page: Union[Unset, str] = UNSET
    twitter_page: Union[Unset, str] = UNSET
    individual_types: Union[Unset, list["IdNamePair"]] = UNSET
    role_vo_list: Union[Unset, list["AccountRoleApi"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        no_solicitation = self.no_solicitation

        login: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.login, Unset):
            login = self.login.to_dict()

        url = self.url

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        consent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.consent, Unset):
            consent = self.consent.to_dict()

        account_custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_custom_fields, Unset):
            account_custom_fields = []
            for account_custom_fields_item_data in self.account_custom_fields:
                account_custom_fields_item = account_custom_fields_item_data.to_dict()
                account_custom_fields.append(account_custom_fields_item)

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        primary_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_contact, Unset):
            primary_contact = self.primary_contact.to_dict()

        send_system_email = self.send_system_email

        email_1_opt_out = self.email_1_opt_out

        origin: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        account_current_membership_status = self.account_current_membership_status

        generosity_indicator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.generosity_indicator, Unset):
            generosity_indicator = self.generosity_indicator.to_dict()

        send_text_opt_in = self.send_text_opt_in

        sms_number = self.sms_number

        company: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        facebook_page = self.facebook_page

        twitter_page = self.twitter_page

        individual_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.individual_types, Unset):
            individual_types = []
            for individual_types_item_data in self.individual_types:
                individual_types_item = individual_types_item_data.to_dict()
                individual_types.append(individual_types_item)

        role_vo_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.role_vo_list, Unset):
            role_vo_list = []
            for role_vo_list_item_data in self.role_vo_list:
                role_vo_list_item = role_vo_list_item_data.to_dict()
                role_vo_list.append(role_vo_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if no_solicitation is not UNSET:
            field_dict["noSolicitation"] = no_solicitation
        if login is not UNSET:
            field_dict["login"] = login
        if url is not UNSET:
            field_dict["url"] = url
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps
        if consent is not UNSET:
            field_dict["consent"] = consent
        if account_custom_fields is not UNSET:
            field_dict["accountCustomFields"] = account_custom_fields
        if source is not UNSET:
            field_dict["source"] = source
        if primary_contact is not UNSET:
            field_dict["primaryContact"] = primary_contact
        if send_system_email is not UNSET:
            field_dict["sendSystemEmail"] = send_system_email
        if email_1_opt_out is not UNSET:
            field_dict["email1OptOut"] = email_1_opt_out
        if origin is not UNSET:
            field_dict["origin"] = origin
        if account_current_membership_status is not UNSET:
            field_dict["accountCurrentMembershipStatus"] = account_current_membership_status
        if generosity_indicator is not UNSET:
            field_dict["generosityIndicator"] = generosity_indicator
        if send_text_opt_in is not UNSET:
            field_dict["sendTextOptIn"] = send_text_opt_in
        if sms_number is not UNSET:
            field_dict["smsNumber"] = sms_number
        if company is not UNSET:
            field_dict["company"] = company
        if facebook_page is not UNSET:
            field_dict["facebookPage"] = facebook_page
        if twitter_page is not UNSET:
            field_dict["twitterPage"] = twitter_page
        if individual_types is not UNSET:
            field_dict["individualTypes"] = individual_types
        if role_vo_list is not UNSET:
            field_dict["roleVoList"] = role_vo_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_role_api import AccountRoleApi
        from ..models.consent import Consent
        from ..models.contact import Contact
        from ..models.custom_field import CustomField
        from ..models.generosity_indicator import GenerosityIndicator
        from ..models.id_name_pair import IdNamePair
        from ..models.login import Login
        from ..models.origin import Origin
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        no_solicitation = d.pop("noSolicitation", UNSET)

        _login = d.pop("login", UNSET)
        login: Union[Unset, Login]
        if isinstance(_login, Unset):
            login = UNSET
        else:
            login = Login.from_dict(_login)

        url = d.pop("url", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        _consent = d.pop("consent", UNSET)
        consent: Union[Unset, Consent]
        if isinstance(_consent, Unset):
            consent = UNSET
        else:
            consent = Consent.from_dict(_consent)

        account_custom_fields = []
        _account_custom_fields = d.pop("accountCustomFields", UNSET)
        for account_custom_fields_item_data in _account_custom_fields or []:
            account_custom_fields_item = CustomField.from_dict(account_custom_fields_item_data)

            account_custom_fields.append(account_custom_fields_item)

        _source = d.pop("source", UNSET)
        source: Union[Unset, IdNamePair]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = IdNamePair.from_dict(_source)

        _primary_contact = d.pop("primaryContact", UNSET)
        primary_contact: Union[Unset, Contact]
        if isinstance(_primary_contact, Unset):
            primary_contact = UNSET
        else:
            primary_contact = Contact.from_dict(_primary_contact)

        send_system_email = d.pop("sendSystemEmail", UNSET)

        email_1_opt_out = d.pop("email1OptOut", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Origin]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = Origin.from_dict(_origin)

        account_current_membership_status = d.pop("accountCurrentMembershipStatus", UNSET)

        _generosity_indicator = d.pop("generosityIndicator", UNSET)
        generosity_indicator: Union[Unset, GenerosityIndicator]
        if isinstance(_generosity_indicator, Unset):
            generosity_indicator = UNSET
        else:
            generosity_indicator = GenerosityIndicator.from_dict(_generosity_indicator)

        send_text_opt_in = d.pop("sendTextOptIn", UNSET)

        sms_number = d.pop("smsNumber", UNSET)

        _company = d.pop("company", UNSET)
        company: Union[Unset, IdNamePair]
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = IdNamePair.from_dict(_company)

        facebook_page = d.pop("facebookPage", UNSET)

        twitter_page = d.pop("twitterPage", UNSET)

        individual_types = []
        _individual_types = d.pop("individualTypes", UNSET)
        for individual_types_item_data in _individual_types or []:
            individual_types_item = IdNamePair.from_dict(individual_types_item_data)

            individual_types.append(individual_types_item)

        role_vo_list = []
        _role_vo_list = d.pop("roleVoList", UNSET)
        for role_vo_list_item_data in _role_vo_list or []:
            role_vo_list_item = AccountRoleApi.from_dict(role_vo_list_item_data)

            role_vo_list.append(role_vo_list_item)

        individual_account = cls(
            account_id=account_id,
            no_solicitation=no_solicitation,
            login=login,
            url=url,
            timestamps=timestamps,
            consent=consent,
            account_custom_fields=account_custom_fields,
            source=source,
            primary_contact=primary_contact,
            send_system_email=send_system_email,
            email_1_opt_out=email_1_opt_out,
            origin=origin,
            account_current_membership_status=account_current_membership_status,
            generosity_indicator=generosity_indicator,
            send_text_opt_in=send_text_opt_in,
            sms_number=sms_number,
            company=company,
            facebook_page=facebook_page,
            twitter_page=twitter_page,
            individual_types=individual_types,
            role_vo_list=role_vo_list,
        )

        individual_account.additional_properties = d
        return individual_account

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
