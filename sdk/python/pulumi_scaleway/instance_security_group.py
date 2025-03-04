# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['InstanceSecurityGroupArgs', 'InstanceSecurityGroup']

@pulumi.input_type
class InstanceSecurityGroupArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_default_security: Optional[pulumi.Input[bool]] = None,
                 external_rules: Optional[pulumi.Input[bool]] = None,
                 inbound_default_policy: Optional[pulumi.Input[str]] = None,
                 inbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupInboundRuleArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outbound_default_policy: Optional[pulumi.Input[str]] = None,
                 outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupOutboundRuleArgs']]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 stateful: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstanceSecurityGroup resource.
        :param pulumi.Input[str] description: The description of the security group
        :param pulumi.Input[bool] enable_default_security: Enable blocking of SMTP on IPv4 and IPv6
        :param pulumi.Input[str] inbound_default_policy: Default inbound traffic policy for this security group
        :param pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupInboundRuleArgs']]] inbound_rules: Inbound rules for this security group
        :param pulumi.Input[str] name: The name of the security group
        :param pulumi.Input[str] outbound_default_policy: Default outbound traffic policy for this security group
        :param pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupOutboundRuleArgs']]] outbound_rules: Outbound rules for this security group
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[bool] stateful: The stateful value of the security group
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the security group
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_default_security is not None:
            pulumi.set(__self__, "enable_default_security", enable_default_security)
        if external_rules is not None:
            pulumi.set(__self__, "external_rules", external_rules)
        if inbound_default_policy is not None:
            pulumi.set(__self__, "inbound_default_policy", inbound_default_policy)
        if inbound_rules is not None:
            pulumi.set(__self__, "inbound_rules", inbound_rules)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if outbound_default_policy is not None:
            pulumi.set(__self__, "outbound_default_policy", outbound_default_policy)
        if outbound_rules is not None:
            pulumi.set(__self__, "outbound_rules", outbound_rules)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if stateful is not None:
            pulumi.set(__self__, "stateful", stateful)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the security group
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableDefaultSecurity")
    def enable_default_security(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable blocking of SMTP on IPv4 and IPv6
        """
        return pulumi.get(self, "enable_default_security")

    @enable_default_security.setter
    def enable_default_security(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_default_security", value)

    @property
    @pulumi.getter(name="externalRules")
    def external_rules(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "external_rules")

    @external_rules.setter
    def external_rules(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "external_rules", value)

    @property
    @pulumi.getter(name="inboundDefaultPolicy")
    def inbound_default_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Default inbound traffic policy for this security group
        """
        return pulumi.get(self, "inbound_default_policy")

    @inbound_default_policy.setter
    def inbound_default_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inbound_default_policy", value)

    @property
    @pulumi.getter(name="inboundRules")
    def inbound_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupInboundRuleArgs']]]]:
        """
        Inbound rules for this security group
        """
        return pulumi.get(self, "inbound_rules")

    @inbound_rules.setter
    def inbound_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupInboundRuleArgs']]]]):
        pulumi.set(self, "inbound_rules", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the security group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="outboundDefaultPolicy")
    def outbound_default_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Default outbound traffic policy for this security group
        """
        return pulumi.get(self, "outbound_default_policy")

    @outbound_default_policy.setter
    def outbound_default_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outbound_default_policy", value)

    @property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupOutboundRuleArgs']]]]:
        """
        Outbound rules for this security group
        """
        return pulumi.get(self, "outbound_rules")

    @outbound_rules.setter
    def outbound_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupOutboundRuleArgs']]]]):
        pulumi.set(self, "outbound_rules", value)

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
    def stateful(self) -> Optional[pulumi.Input[bool]]:
        """
        The stateful value of the security group
        """
        return pulumi.get(self, "stateful")

    @stateful.setter
    def stateful(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "stateful", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags associated with the security group
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
class _InstanceSecurityGroupState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_default_security: Optional[pulumi.Input[bool]] = None,
                 external_rules: Optional[pulumi.Input[bool]] = None,
                 inbound_default_policy: Optional[pulumi.Input[str]] = None,
                 inbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupInboundRuleArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 outbound_default_policy: Optional[pulumi.Input[str]] = None,
                 outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupOutboundRuleArgs']]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 stateful: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstanceSecurityGroup resources.
        :param pulumi.Input[str] description: The description of the security group
        :param pulumi.Input[bool] enable_default_security: Enable blocking of SMTP on IPv4 and IPv6
        :param pulumi.Input[str] inbound_default_policy: Default inbound traffic policy for this security group
        :param pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupInboundRuleArgs']]] inbound_rules: Inbound rules for this security group
        :param pulumi.Input[str] name: The name of the security group
        :param pulumi.Input[str] organization_id: The organization_id you want to attach the resource to
        :param pulumi.Input[str] outbound_default_policy: Default outbound traffic policy for this security group
        :param pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupOutboundRuleArgs']]] outbound_rules: Outbound rules for this security group
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[bool] stateful: The stateful value of the security group
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the security group
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_default_security is not None:
            pulumi.set(__self__, "enable_default_security", enable_default_security)
        if external_rules is not None:
            pulumi.set(__self__, "external_rules", external_rules)
        if inbound_default_policy is not None:
            pulumi.set(__self__, "inbound_default_policy", inbound_default_policy)
        if inbound_rules is not None:
            pulumi.set(__self__, "inbound_rules", inbound_rules)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if outbound_default_policy is not None:
            pulumi.set(__self__, "outbound_default_policy", outbound_default_policy)
        if outbound_rules is not None:
            pulumi.set(__self__, "outbound_rules", outbound_rules)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if stateful is not None:
            pulumi.set(__self__, "stateful", stateful)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the security group
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableDefaultSecurity")
    def enable_default_security(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable blocking of SMTP on IPv4 and IPv6
        """
        return pulumi.get(self, "enable_default_security")

    @enable_default_security.setter
    def enable_default_security(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_default_security", value)

    @property
    @pulumi.getter(name="externalRules")
    def external_rules(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "external_rules")

    @external_rules.setter
    def external_rules(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "external_rules", value)

    @property
    @pulumi.getter(name="inboundDefaultPolicy")
    def inbound_default_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Default inbound traffic policy for this security group
        """
        return pulumi.get(self, "inbound_default_policy")

    @inbound_default_policy.setter
    def inbound_default_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inbound_default_policy", value)

    @property
    @pulumi.getter(name="inboundRules")
    def inbound_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupInboundRuleArgs']]]]:
        """
        Inbound rules for this security group
        """
        return pulumi.get(self, "inbound_rules")

    @inbound_rules.setter
    def inbound_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupInboundRuleArgs']]]]):
        pulumi.set(self, "inbound_rules", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the security group
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="outboundDefaultPolicy")
    def outbound_default_policy(self) -> Optional[pulumi.Input[str]]:
        """
        Default outbound traffic policy for this security group
        """
        return pulumi.get(self, "outbound_default_policy")

    @outbound_default_policy.setter
    def outbound_default_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outbound_default_policy", value)

    @property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupOutboundRuleArgs']]]]:
        """
        Outbound rules for this security group
        """
        return pulumi.get(self, "outbound_rules")

    @outbound_rules.setter
    def outbound_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceSecurityGroupOutboundRuleArgs']]]]):
        pulumi.set(self, "outbound_rules", value)

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
    def stateful(self) -> Optional[pulumi.Input[bool]]:
        """
        The stateful value of the security group
        """
        return pulumi.get(self, "stateful")

    @stateful.setter
    def stateful(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "stateful", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags associated with the security group
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


class InstanceSecurityGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_default_security: Optional[pulumi.Input[bool]] = None,
                 external_rules: Optional[pulumi.Input[bool]] = None,
                 inbound_default_policy: Optional[pulumi.Input[str]] = None,
                 inbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outbound_default_policy: Optional[pulumi.Input[str]] = None,
                 outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 stateful: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a InstanceSecurityGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the security group
        :param pulumi.Input[bool] enable_default_security: Enable blocking of SMTP on IPv4 and IPv6
        :param pulumi.Input[str] inbound_default_policy: Default inbound traffic policy for this security group
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]] inbound_rules: Inbound rules for this security group
        :param pulumi.Input[str] name: The name of the security group
        :param pulumi.Input[str] outbound_default_policy: Default outbound traffic policy for this security group
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]] outbound_rules: Outbound rules for this security group
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[bool] stateful: The stateful value of the security group
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the security group
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InstanceSecurityGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a InstanceSecurityGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InstanceSecurityGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceSecurityGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_default_security: Optional[pulumi.Input[bool]] = None,
                 external_rules: Optional[pulumi.Input[bool]] = None,
                 inbound_default_policy: Optional[pulumi.Input[str]] = None,
                 inbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outbound_default_policy: Optional[pulumi.Input[str]] = None,
                 outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 stateful: Optional[pulumi.Input[bool]] = None,
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
            __props__ = InstanceSecurityGroupArgs.__new__(InstanceSecurityGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enable_default_security"] = enable_default_security
            __props__.__dict__["external_rules"] = external_rules
            __props__.__dict__["inbound_default_policy"] = inbound_default_policy
            __props__.__dict__["inbound_rules"] = inbound_rules
            __props__.__dict__["name"] = name
            __props__.__dict__["outbound_default_policy"] = outbound_default_policy
            __props__.__dict__["outbound_rules"] = outbound_rules
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["stateful"] = stateful
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone"] = zone
            __props__.__dict__["organization_id"] = None
        super(InstanceSecurityGroup, __self__).__init__(
            'scaleway:index/instanceSecurityGroup:InstanceSecurityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            enable_default_security: Optional[pulumi.Input[bool]] = None,
            external_rules: Optional[pulumi.Input[bool]] = None,
            inbound_default_policy: Optional[pulumi.Input[str]] = None,
            inbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            outbound_default_policy: Optional[pulumi.Input[str]] = None,
            outbound_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            stateful: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'InstanceSecurityGroup':
        """
        Get an existing InstanceSecurityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the security group
        :param pulumi.Input[bool] enable_default_security: Enable blocking of SMTP on IPv4 and IPv6
        :param pulumi.Input[str] inbound_default_policy: Default inbound traffic policy for this security group
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupInboundRuleArgs']]]] inbound_rules: Inbound rules for this security group
        :param pulumi.Input[str] name: The name of the security group
        :param pulumi.Input[str] organization_id: The organization_id you want to attach the resource to
        :param pulumi.Input[str] outbound_default_policy: Default outbound traffic policy for this security group
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceSecurityGroupOutboundRuleArgs']]]] outbound_rules: Outbound rules for this security group
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[bool] stateful: The stateful value of the security group
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the security group
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceSecurityGroupState.__new__(_InstanceSecurityGroupState)

        __props__.__dict__["description"] = description
        __props__.__dict__["enable_default_security"] = enable_default_security
        __props__.__dict__["external_rules"] = external_rules
        __props__.__dict__["inbound_default_policy"] = inbound_default_policy
        __props__.__dict__["inbound_rules"] = inbound_rules
        __props__.__dict__["name"] = name
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["outbound_default_policy"] = outbound_default_policy
        __props__.__dict__["outbound_rules"] = outbound_rules
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["stateful"] = stateful
        __props__.__dict__["tags"] = tags
        __props__.__dict__["zone"] = zone
        return InstanceSecurityGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the security group
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableDefaultSecurity")
    def enable_default_security(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable blocking of SMTP on IPv4 and IPv6
        """
        return pulumi.get(self, "enable_default_security")

    @property
    @pulumi.getter(name="externalRules")
    def external_rules(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "external_rules")

    @property
    @pulumi.getter(name="inboundDefaultPolicy")
    def inbound_default_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Default inbound traffic policy for this security group
        """
        return pulumi.get(self, "inbound_default_policy")

    @property
    @pulumi.getter(name="inboundRules")
    def inbound_rules(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceSecurityGroupInboundRule']]]:
        """
        Inbound rules for this security group
        """
        return pulumi.get(self, "inbound_rules")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the security group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The organization_id you want to attach the resource to
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="outboundDefaultPolicy")
    def outbound_default_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Default outbound traffic policy for this security group
        """
        return pulumi.get(self, "outbound_default_policy")

    @property
    @pulumi.getter(name="outboundRules")
    def outbound_rules(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceSecurityGroupOutboundRule']]]:
        """
        Outbound rules for this security group
        """
        return pulumi.get(self, "outbound_rules")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project_id you want to attach the resource to
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def stateful(self) -> pulumi.Output[Optional[bool]]:
        """
        The stateful value of the security group
        """
        return pulumi.get(self, "stateful")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags associated with the security group
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The zone you want to attach the resource to
        """
        return pulumi.get(self, "zone")

