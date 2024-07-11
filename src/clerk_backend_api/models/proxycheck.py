"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import TypedDict


class ProxyCheckObject(str, Enum):
    PROXY_CHECK = "proxy_check"


class ProxyCheckTypedDict(TypedDict):
    object: ProxyCheckObject
    id: str
    domain_id: str
    last_run_at: int
    proxy_url: str
    successful: bool
    created_at: int
    updated_at: int
    

class ProxyCheck(BaseModel):
    object: ProxyCheckObject
    id: str
    domain_id: str
    last_run_at: int
    proxy_url: str
    successful: bool
    created_at: int
    updated_at: int
    
