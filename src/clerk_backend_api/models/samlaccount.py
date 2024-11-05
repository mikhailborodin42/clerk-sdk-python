"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing import Any, Dict, Optional, Union
from typing_extensions import NotRequired, TypedDict


class SAMLAccountObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    SAML_ACCOUNT = "saml_account"


class TicketVerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    EXPIRED = "expired"


class TicketVerificationStrategy(str, Enum):
    TICKET = "ticket"


class TicketTypedDict(TypedDict):
    status: TicketVerificationStatus
    strategy: TicketVerificationStrategy
    attempts: NotRequired[Nullable[int]]
    expire_at: NotRequired[Nullable[int]]


class Ticket(BaseModel):
    status: TicketVerificationStatus

    strategy: TicketVerificationStrategy

    attempts: OptionalNullable[int] = UNSET

    expire_at: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["attempts", "expire_at"]
        nullable_fields = ["attempts", "expire_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class SAMLVerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"
    TRANSFERABLE = "transferable"


class SAMLVerificationStrategy(str, Enum):
    SAML = "saml"


class ClerkErrorErrorMetaTypedDict(TypedDict):
    pass


class ClerkErrorErrorMeta(BaseModel):
    pass


class SAMLErrorClerkErrorTypedDict(TypedDict):
    message: str
    long_message: str
    code: str
    meta: NotRequired[ClerkErrorErrorMetaTypedDict]
    clerk_trace_id: NotRequired[str]


class SAMLErrorClerkError(BaseModel):
    message: str

    long_message: str

    code: str

    meta: Optional[ClerkErrorErrorMeta] = None

    clerk_trace_id: Optional[str] = None


VerificationErrorTypedDict = SAMLErrorClerkErrorTypedDict


VerificationError = SAMLErrorClerkError


class SamlTypedDict(TypedDict):
    status: SAMLVerificationStatus
    strategy: SAMLVerificationStrategy
    external_verification_redirect_url: Nullable[str]
    expire_at: int
    error: NotRequired[Nullable[VerificationErrorTypedDict]]
    attempts: NotRequired[Nullable[int]]


class Saml(BaseModel):
    status: SAMLVerificationStatus

    strategy: SAMLVerificationStrategy

    external_verification_redirect_url: Nullable[str]

    expire_at: int

    error: OptionalNullable[VerificationError] = UNSET

    attempts: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["error", "attempts"]
        nullable_fields = ["external_verification_redirect_url", "error", "attempts"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


SAMLAccountVerificationTypedDict = Union[TicketTypedDict, SamlTypedDict]


SAMLAccountVerification = Union[Ticket, Saml]


class SAMLConnectionSAMLConnectionTypedDict(TypedDict):
    id: str
    name: str
    domain: str
    active: bool
    provider: str
    sync_user_attributes: bool
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    allow_subdomains: NotRequired[bool]
    allow_idp_initiated: NotRequired[bool]
    disable_additional_identifications: NotRequired[bool]


class SAMLConnectionSAMLConnection(BaseModel):
    id: str

    name: str

    domain: str

    active: bool

    provider: str

    sync_user_attributes: bool

    created_at: int
    r"""Unix timestamp of creation.

    """

    updated_at: int
    r"""Unix timestamp of last update.

    """

    allow_subdomains: Optional[bool] = None

    allow_idp_initiated: Optional[bool] = None

    disable_additional_identifications: Optional[bool] = None


SamlConnectionTypedDict = SAMLConnectionSAMLConnectionTypedDict


SamlConnection = SAMLConnectionSAMLConnection


class SAMLAccountTypedDict(TypedDict):
    id: str
    object: SAMLAccountObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    provider: str
    active: bool
    email_address: str
    verification: Nullable[SAMLAccountVerificationTypedDict]
    first_name: NotRequired[Nullable[str]]
    last_name: NotRequired[Nullable[str]]
    provider_user_id: NotRequired[Nullable[str]]
    public_metadata: NotRequired[Dict[str, Any]]
    saml_connection: NotRequired[Nullable[SamlConnectionTypedDict]]


class SAMLAccount(BaseModel):
    id: str

    object: SAMLAccountObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    provider: str

    active: bool

    email_address: str

    verification: Nullable[SAMLAccountVerification]

    first_name: OptionalNullable[str] = UNSET

    last_name: OptionalNullable[str] = UNSET

    provider_user_id: OptionalNullable[str] = UNSET

    public_metadata: Optional[Dict[str, Any]] = None

    saml_connection: OptionalNullable[SamlConnection] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "first_name",
            "last_name",
            "provider_user_id",
            "public_metadata",
            "saml_connection",
        ]
        nullable_fields = [
            "verification",
            "first_name",
            "last_name",
            "provider_user_id",
            "saml_connection",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
