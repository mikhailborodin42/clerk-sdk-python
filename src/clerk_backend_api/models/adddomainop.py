"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AddDomainRequestBodyTypedDict(TypedDict):
    name: str
    r"""The new domain name. Can contain the port for development instances."""
    is_satellite: bool
    r"""Marks the new domain as satellite. Only `true` is accepted at the moment."""
    proxy_url: NotRequired[str]
    r"""The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances."""


class AddDomainRequestBody(BaseModel):
    name: str
    r"""The new domain name. Can contain the port for development instances."""

    is_satellite: bool
    r"""Marks the new domain as satellite. Only `true` is accepted at the moment."""

    proxy_url: Optional[str] = None
    r"""The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances."""
