"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .identificationlink import IdentificationLink, IdentificationLinkTypedDict
from clerk_backend_api.types import BaseModel, Nullable
from enum import Enum
from pydantic import model_serializer
from typing import List, Optional, TypedDict, Union
from typing_extensions import NotRequired


class EmailAddressObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    EMAIL_ADDRESS = "email_address"


class OauthVerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"
    TRANSFERABLE = "transferable"


class OauthVerificationStrategy(str, Enum):
    OAUTH_GOOGLE = "oauth_google"
    OAUTH_MOCK = "oauth_mock"
    FROM_OAUTH_DISCORD = "from_oauth_discord"
    FROM_OAUTH_GOOGLE = "from_oauth_google"


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
    

class OauthTypedDict(TypedDict):
    status: OauthVerificationStatus
    strategy: OauthVerificationStrategy
    expire_at: Nullable[int]
    external_verification_redirect_url: NotRequired[str]
    error: NotRequired[Nullable[ErrorTypedDict]]
    attempts: NotRequired[Nullable[int]]
    

class Oauth(BaseModel):
    status: OauthVerificationStatus
    strategy: OauthVerificationStrategy
    expire_at: Nullable[int]
    external_verification_redirect_url: Optional[str] = None
    error: Optional[Nullable[Error]] = None
    attempts: Optional[Nullable[int]] = None
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["external_verification_redirect_url", "error", "attempts"]
        nullable_fields = ["expire_at", "error", "attempts"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        

class AdminVerificationStatus(str, Enum):
    VERIFIED = "verified"


class VerificationStrategy(str, Enum):
    ADMIN = "admin"
    FROM_OAUTH_DISCORD = "from_oauth_discord"


class AdminTypedDict(TypedDict):
    status: AdminVerificationStatus
    strategy: VerificationStrategy
    attempts: NotRequired[Nullable[int]]
    expire_at: NotRequired[Nullable[int]]
    

class Admin(BaseModel):
    status: AdminVerificationStatus
    strategy: VerificationStrategy
    attempts: Optional[Nullable[int]] = None
    expire_at: Optional[Nullable[int]] = None
    
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

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        

class VerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"


class Strategy(str, Enum):
    PHONE_CODE = "phone_code"
    EMAIL_CODE = "email_code"
    RESET_PASSWORD_EMAIL_CODE = "reset_password_email_code"
    FROM_OAUTH_DISCORD = "from_oauth_discord"


class OtpTypedDict(TypedDict):
    status: VerificationStatus
    strategy: Strategy
    attempts: Nullable[int]
    expire_at: Nullable[int]
    

class Otp(BaseModel):
    status: VerificationStatus
    strategy: Strategy
    attempts: Nullable[int]
    expire_at: Nullable[int]
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["attempts", "expire_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        

class EmailAddressTypedDict(TypedDict):
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
    object: EmailAddressObject
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

            if val is not None:
                m[k] = val
            elif not k in optional_fields or (
                    k in optional_fields
                    and k in nullable_fields
                    and (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member
                ):
                m[k] = val

        return m
        

ErrorTypedDict = Union[ErrorClerkErrorTypedDict]


Error = Union[ErrorClerkError]


VerificationTypedDict = Union[OtpTypedDict, AdminTypedDict, OauthTypedDict]


Verification = Union[Otp, Admin, Oauth]

