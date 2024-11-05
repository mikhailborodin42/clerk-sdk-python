"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .schemas_samlconnection import (
    SchemasSAMLConnection,
    SchemasSAMLConnectionTypedDict,
)
from clerk_backend_api.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class SAMLConnectionsTypedDict(TypedDict):
    r"""A list of SAML Connections"""

    data: List[SchemasSAMLConnectionTypedDict]
    total_count: int
    r"""Total number of SAML Connections

    """


class SAMLConnections(BaseModel):
    r"""A list of SAML Connections"""

    data: List[SchemasSAMLConnection]

    total_count: int
    r"""Total number of SAML Connections

    """
