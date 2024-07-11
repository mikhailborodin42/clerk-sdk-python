"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class OrganizationSettingsObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""
    ORGANIZATION_SETTINGS = "organization_settings"


class DomainsEnrollmentModes(str, Enum):
    MANUAL_INVITATION = "manual_invitation"
    AUTOMATIC_INVITATION = "automatic_invitation"
    AUTOMATIC_SUGGESTION = "automatic_suggestion"


class OrganizationSettingsTypedDict(TypedDict):
    object: OrganizationSettingsObject
    r"""String representing the object's type. Objects of the same type share the same value."""
    enabled: bool
    max_allowed_memberships: int
    creator_role: str
    r"""The role key that a user will be assigned after creating an organization."""
    admin_delete_enabled: bool
    r"""The default for whether an admin can delete an organization with the Frontend API."""
    domains_enabled: bool
    domains_enrollment_modes: List[DomainsEnrollmentModes]
    domains_default_role: str
    r"""The role key that it will be used in order to create an organization invitation or suggestion."""
    max_allowed_roles: NotRequired[int]
    max_allowed_permissions: NotRequired[int]
    

class OrganizationSettings(BaseModel):
    object: OrganizationSettingsObject
    r"""String representing the object's type. Objects of the same type share the same value."""
    enabled: bool
    max_allowed_memberships: int
    creator_role: str
    r"""The role key that a user will be assigned after creating an organization."""
    admin_delete_enabled: bool
    r"""The default for whether an admin can delete an organization with the Frontend API."""
    domains_enabled: bool
    domains_enrollment_modes: List[DomainsEnrollmentModes]
    domains_default_role: str
    r"""The role key that it will be used in order to create an organization invitation or suggestion."""
    max_allowed_roles: Optional[int] = None
    max_allowed_permissions: Optional[int] = None
    
