# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['LoadbalancerBeta']


class LoadbalancerBeta(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a LoadbalancerBeta resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_id: The ID of the associated IP. See below.
        :param pulumi.Input[str] name: The name of the load-balancer.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the organization the load-balancer is associated with.
        :param pulumi.Input[str] region: `region`) The region in which the load-balancer should be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the load-balancers.
        :param pulumi.Input[str] type: The type of the load-balancer.  For now only `LB-S` is available
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if ip_id is None:
                raise TypeError("Missing required property 'ip_id'")
            __props__['ip_id'] = ip_id
            __props__['name'] = name
            __props__['organization_id'] = organization_id
            __props__['region'] = region
            __props__['tags'] = tags
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['ip_address'] = None
        super(LoadbalancerBeta, __self__).__init__(
            'scaleway:index/loadbalancerBeta:LoadbalancerBeta',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            ip_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'LoadbalancerBeta':
        """
        Get an existing LoadbalancerBeta resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_address: The load-balance public IP Address
        :param pulumi.Input[str] ip_id: The ID of the associated IP. See below.
        :param pulumi.Input[str] name: The name of the load-balancer.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the organization the load-balancer is associated with.
        :param pulumi.Input[str] region: `region`) The region in which the load-balancer should be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the load-balancers.
        :param pulumi.Input[str] type: The type of the load-balancer.  For now only `LB-S` is available
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["ip_address"] = ip_address
        __props__["ip_id"] = ip_id
        __props__["name"] = name
        __props__["organization_id"] = organization_id
        __props__["region"] = region
        __props__["tags"] = tags
        __props__["type"] = type
        return LoadbalancerBeta(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The load-balance public IP Address
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="ipId")
    def ip_id(self) -> pulumi.Output[str]:
        """
        The ID of the associated IP. See below.
        """
        return pulumi.get(self, "ip_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the load-balancer.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        `organization_id`) The ID of the organization the load-balancer is associated with.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        `region`) The region in which the load-balancer should be created.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags associated with the load-balancers.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the load-balancer.  For now only `LB-S` is available
        """
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

