"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .identificationlink import IdentificationLink, IdentificationLinkTypedDict
from clerk_backend_api import utils
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from clerk_backend_api.utils import validate_open_enum
from enum import Enum
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class EmailAddressObject(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""String representing the object's type. Objects of the same type share the same value."""

    EMAIL_ADDRESS = "email_address"


class OauthVerificationStatus(str, Enum, metaclass=utils.OpenEnumMeta):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"
    TRANSFERABLE = "transferable"


class OauthVerificationStrategy(str, Enum, metaclass=utils.OpenEnumMeta):
    OAUTH_GOOGLE = "oauth_google"
    OAUTH_MOCK = "oauth_mock"
    FROM_OAUTH_GOOGLE = "from_oauth_google"
    FROM_OAUTH_DISCORD = "from_oauth_discord"
    FROM_OAUTH_MICROSOFT = "from_oauth_microsoft"
    OAUTH_APPLE = "oauth_apple"
    OAUTH_MICROSOFT = "oauth_microsoft"
    OAUTH_GITHUB = "oauth_github"
    EMAIL_LINK = "email_link"


class ErrorMetaTypedDict(TypedDict):
    pass


class ErrorMeta(BaseModel):
    pass


class ErrorClerkErrorTypedDict(TypedDict):
    message: str
    long_message: str
    code: str
    meta: NotRequired[ErrorMetaTypedDict]
    clerk_trace_id: NotRequired[str]


class ErrorClerkError(BaseModel):
    message: str

    long_message: str

    code: str

    meta: Optional[ErrorMeta] = None

    clerk_trace_id: Optional[str] = None


ErrorTypedDict = ErrorClerkErrorTypedDict


Error = ErrorClerkError


class OauthTypedDict(TypedDict):
    status: OauthVerificationStatus
    strategy: OauthVerificationStrategy
    expire_at: int
    external_verification_redirect_url: NotRequired[str]
    error: NotRequired[Nullable[ErrorTypedDict]]
    attempts: NotRequired[Nullable[int]]


class Oauth(BaseModel):
    status: Annotated[
        OauthVerificationStatus, PlainValidator(validate_open_enum(False))
    ]

    strategy: Annotated[
        OauthVerificationStrategy, PlainValidator(validate_open_enum(False))
    ]

    expire_at: int

    external_verification_redirect_url: Optional[str] = None

    error: OptionalNullable[Error] = UNSET

    attempts: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["external_verification_redirect_url", "error", "attempts"]
        nullable_fields = ["error", "attempts"]
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


class AdminVerificationStatus(str, Enum):
    VERIFIED = "verified"


class VerificationStrategy(str, Enum, metaclass=utils.OpenEnumMeta):
    ADMIN = "admin"


class AdminTypedDict(TypedDict):
    status: AdminVerificationStatus
    strategy: VerificationStrategy
    attempts: NotRequired[Nullable[int]]
    expire_at: NotRequired[Nullable[int]]


class Admin(BaseModel):
    status: AdminVerificationStatus

    strategy: Annotated[VerificationStrategy, PlainValidator(validate_open_enum(False))]

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


class VerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"


class Strategy(str, Enum, metaclass=utils.OpenEnumMeta):
    PHONE_CODE = "phone_code"
    EMAIL_CODE = "email_code"
    EMAIL_LINK = "email_link"
    RESET_PASSWORD_EMAIL_CODE = "reset_password_email_code"
    FROM_OAUTH_DISCORD = "from_oauth_discord"
    FROM_OAUTH_GOOGLE = "from_oauth_google"
    FROM_OAUTH_APPLE = "from_oauth_apple"
    FROM_OAUTH_MICROSOFT = "from_oauth_microsoft"
    FROM_OAUTH_GITHUB = "from_oauth_github"


class OtpTypedDict(TypedDict):
    status: VerificationStatus
    strategy: Strategy
    attempts: int
    expire_at: int


class Otp(BaseModel):
    status: VerificationStatus

    strategy: Annotated[Strategy, PlainValidator(validate_open_enum(False))]

    attempts: int

    expire_at: int


VerificationTypedDict = Union[OtpTypedDict, AdminTypedDict, OauthTypedDict]


Verification = Union[Otp, Admin, Oauth]


class EmailAddressTypedDict(TypedDict):
    r"""Success"""

    object: EmailAddressObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    email_address: str
    reserved: bool
    verification: Nullable[VerificationTypedDict]
    linked_to: List[IdentificationLinkTypedDict]
    created_at: int
    r"""Unix timestamp of creation

    """
    updated_at: int
    r"""Unix timestamp of creation

    """
    id: NotRequired[str]


class EmailAddress(BaseModel):
    r"""Success"""

    object: Annotated[EmailAddressObject, PlainValidator(validate_open_enum(False))]
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    email_address: str

    reserved: bool

    verification: Nullable[Verification]

    linked_to: List[IdentificationLink]

    created_at: int
    r"""Unix timestamp of creation

    """

    updated_at: int
    r"""Unix timestamp of creation

    """

    id: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id"]
        nullable_fields = ["verification"]
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
