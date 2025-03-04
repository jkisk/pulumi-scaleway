# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VpcPublicGatewayIpArgs', 'VpcPublicGatewayIp']

@pulumi.input_type
class VpcPublicGatewayIpArgs:
    def __init__(__self__, *,
                 project_id: Optional[pulumi.Input[str]] = None,
                 reverse: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpcPublicGatewayIp resource.
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[str] reverse: reverse domain name for the IP address
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with public gateway IP
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if reverse is not None:
            pulumi.set(__self__, "reverse", reverse)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project_id you want to attach the resource to
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def reverse(self) -> Optional[pulumi.Input[str]]:
        """
        reverse domain name for the IP address
        """
        return pulumi.get(self, "reverse")

    @reverse.setter
    def reverse(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reverse", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags associated with public gateway IP
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone you want to attach the resource to
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class _VpcPublicGatewayIpState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 reverse: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpcPublicGatewayIp resources.
        :param pulumi.Input[str] address: the IP itself
        :param pulumi.Input[str] created_at: The date and time of the creation of the public gateway IP
        :param pulumi.Input[str] organization_id: The organization_id you want to attach the resource to
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[str] reverse: reverse domain name for the IP address
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with public gateway IP
        :param pulumi.Input[str] updated_at: The date and time of the last update of the public gateway IP
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if reverse is not None:
            pulumi.set(__self__, "reverse", reverse)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        the IP itself
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time of the creation of the public gateway IP
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The organization_id you want to attach the resource to
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project_id you want to attach the resource to
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def reverse(self) -> Optional[pulumi.Input[str]]:
        """
        reverse domain name for the IP address
        """
        return pulumi.get(self, "reverse")

    @reverse.setter
    def reverse(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reverse", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags associated with public gateway IP
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time of the last update of the public gateway IP
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The zone you want to attach the resource to
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class VpcPublicGatewayIp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 reverse: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a VpcPublicGatewayIp resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[str] reverse: reverse domain name for the IP address
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with public gateway IP
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VpcPublicGatewayIpArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a VpcPublicGatewayIp resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param VpcPublicGatewayIpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpcPublicGatewayIpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 reverse: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpcPublicGatewayIpArgs.__new__(VpcPublicGatewayIpArgs)

            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["reverse"] = reverse
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
            __props__.__dict__["address"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["updated_at"] = None
        super(VpcPublicGatewayIp, __self__).__init__(
            'scaleway:index/vpcPublicGatewayIp:VpcPublicGatewayIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            reverse: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'VpcPublicGatewayIp':
        """
        Get an existing VpcPublicGatewayIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: the IP itself
        :param pulumi.Input[str] created_at: The date and time of the creation of the public gateway IP
        :param pulumi.Input[str] organization_id: The organization_id you want to attach the resource to
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[str] reverse: reverse domain name for the IP address
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with public gateway IP
        :param pulumi.Input[str] updated_at: The date and time of the last update of the public gateway IP
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpcPublicGatewayIpState.__new__(_VpcPublicGatewayIpState)

        __props__.__dict__["address"] = address
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["reverse"] = reverse
        __props__.__dict__["tags"] = tags
        __props__.__dict__["updated_at"] = updated_at
        __props__.__dict__["zone"] = zone
        return VpcPublicGatewayIp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        the IP itself
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The date and time of the creation of the public gateway IP
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The organization_id you want to attach the resource to
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project_id you want to attach the resource to
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def reverse(self) -> pulumi.Output[str]:
        """
        reverse domain name for the IP address
        """
        return pulumi.get(self, "reverse")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags associated with public gateway IP
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The date and time of the last update of the public gateway IP
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The zone you want to attach the resource to
        """
        return pulumi.get(self, "zone")

