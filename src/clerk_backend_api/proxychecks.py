"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from clerk_backend_api import models
from clerk_backend_api._hooks import HookContext
from clerk_backend_api.types import Nullable, UNSET
import clerk_backend_api.utils as utils
from typing import Optional

class ProxyChecks(BaseSDK):
    
    
    def verify(
        self, *,
        domain_id: Optional[str] = None,
        proxy_url: Optional[str] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.ProxyCheck:
        r"""Verify the proxy configuration for your domain

        This endpoint can be used to validate that a proxy-enabled domain is operational.
        It tries to verify that the proxy URL provided in the parameters maps to a functional proxy that can reach the Clerk Frontend API.

        You can use this endpoint before you set a proxy URL for a domain. This way you can ensure that switching to proxy-based
        configuration will not lead to downtime for your instance.

        The `proxy_url` parameter allows for testing proxy configurations for domains that don't have a proxy URL yet, or operate on
        a different proxy URL than the one provided. It can also be used to re-validate a domain that is already configured to work with a proxy.

        :param domain_id: The ID of the domain that will be updated.
        :param proxy_url: The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. e.g. https://example.com/__clerk
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.VerifyDomainProxyRequestBody(
            domain_id=domain_id,
            proxy_url=proxy_url,
        )
        
        req = self.build_request(
            method="POST",
            path="/proxy_checks",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[models.VerifyDomainProxyRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="VerifyDomainProxy", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProxyCheck])
        if utils.match_response(http_res, ["400","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def verify_async(
        self, *,
        domain_id: Optional[str] = None,
        proxy_url: Optional[str] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.ProxyCheck:
        r"""Verify the proxy configuration for your domain

        This endpoint can be used to validate that a proxy-enabled domain is operational.
        It tries to verify that the proxy URL provided in the parameters maps to a functional proxy that can reach the Clerk Frontend API.

        You can use this endpoint before you set a proxy URL for a domain. This way you can ensure that switching to proxy-based
        configuration will not lead to downtime for your instance.

        The `proxy_url` parameter allows for testing proxy configurations for domains that don't have a proxy URL yet, or operate on
        a different proxy URL than the one provided. It can also be used to re-validate a domain that is already configured to work with a proxy.

        :param domain_id: The ID of the domain that will be updated.
        :param proxy_url: The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. e.g. https://example.com/__clerk
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.VerifyDomainProxyRequestBody(
            domain_id=domain_id,
            proxy_url=proxy_url,
        )
        
        req = self.build_request(
            method="POST",
            path="/proxy_checks",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[models.VerifyDomainProxyRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="VerifyDomainProxy", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ProxyCheck])
        if utils.match_response(http_res, ["400","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
