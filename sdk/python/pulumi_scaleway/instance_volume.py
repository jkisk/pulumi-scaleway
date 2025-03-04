# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['InstanceVolumeArgs', 'InstanceVolume']

@pulumi.input_type
class InstanceVolumeArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 from_snapshot_id: Optional[pulumi.Input[str]] = None,
                 from_volume_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 size_in_gb: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstanceVolume resource.
        :param pulumi.Input[str] type: The volume type
        :param pulumi.Input[str] from_snapshot_id: Create a volume based on a image
        :param pulumi.Input[str] from_volume_id: Create a copy of an existing volume
        :param pulumi.Input[str] name: The name of the volume
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[int] size_in_gb: The size of the volume in gigabyte
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the volume
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        pulumi.set(__self__, "type", type)
        if from_snapshot_id is not None:
            pulumi.set(__self__, "from_snapshot_id", from_snapshot_id)
        if from_volume_id is not None:
            pulumi.set(__self__, "from_volume_id", from_volume_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if size_in_gb is not None:
            pulumi.set(__self__, "size_in_gb", size_in_gb)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The volume type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="fromSnapshotId")
    def from_snapshot_id(self) -> Optional[pulumi.Input[str]]:
        """
        Create a volume based on a image
        """
        return pulumi.get(self, "from_snapshot_id")

    @from_snapshot_id.setter
    def from_snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "from_snapshot_id", value)

    @property
    @pulumi.getter(name="fromVolumeId")
    def from_volume_id(self) -> Optional[pulumi.Input[str]]:
        """
        Create a copy of an existing volume
        """
        return pulumi.get(self, "from_volume_id")

    @from_volume_id.setter
    def from_volume_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "from_volume_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the volume
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="sizeInGb")
    def size_in_gb(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the volume in gigabyte
        """
        return pulumi.get(self, "size_in_gb")

    @size_in_gb.setter
    def size_in_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size_in_gb", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags associated with the volume
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
class _InstanceVolumeState:
    def __init__(__self__, *,
                 from_snapshot_id: Optional[pulumi.Input[str]] = None,
                 from_volume_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 size_in_gb: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstanceVolume resources.
        :param pulumi.Input[str] from_snapshot_id: Create a volume based on a image
        :param pulumi.Input[str] from_volume_id: Create a copy of an existing volume
        :param pulumi.Input[str] name: The name of the volume
        :param pulumi.Input[str] organization_id: The organization_id you want to attach the resource to
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[str] server_id: The server associated with this volume
        :param pulumi.Input[int] size_in_gb: The size of the volume in gigabyte
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the volume
        :param pulumi.Input[str] type: The volume type
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        if from_snapshot_id is not None:
            pulumi.set(__self__, "from_snapshot_id", from_snapshot_id)
        if from_volume_id is not None:
            pulumi.set(__self__, "from_volume_id", from_volume_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if size_in_gb is not None:
            pulumi.set(__self__, "size_in_gb", size_in_gb)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="fromSnapshotId")
    def from_snapshot_id(self) -> Optional[pulumi.Input[str]]:
        """
        Create a volume based on a image
        """
        return pulumi.get(self, "from_snapshot_id")

    @from_snapshot_id.setter
    def from_snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "from_snapshot_id", value)

    @property
    @pulumi.getter(name="fromVolumeId")
    def from_volume_id(self) -> Optional[pulumi.Input[str]]:
        """
        Create a copy of an existing volume
        """
        return pulumi.get(self, "from_volume_id")

    @from_volume_id.setter
    def from_volume_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "from_volume_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the volume
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
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        The server associated with this volume
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="sizeInGb")
    def size_in_gb(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the volume in gigabyte
        """
        return pulumi.get(self, "size_in_gb")

    @size_in_gb.setter
    def size_in_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size_in_gb", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags associated with the volume
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The volume type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

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


class InstanceVolume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 from_snapshot_id: Optional[pulumi.Input[str]] = None,
                 from_volume_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 size_in_gb: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a InstanceVolume resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] from_snapshot_id: Create a volume based on a image
        :param pulumi.Input[str] from_volume_id: Create a copy of an existing volume
        :param pulumi.Input[str] name: The name of the volume
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[int] size_in_gb: The size of the volume in gigabyte
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the volume
        :param pulumi.Input[str] type: The volume type
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceVolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a InstanceVolume resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param InstanceVolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceVolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 from_snapshot_id: Optional[pulumi.Input[str]] = None,
                 from_volume_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 size_in_gb: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
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
            __props__ = InstanceVolumeArgs.__new__(InstanceVolumeArgs)

            __props__.__dict__["from_snapshot_id"] = from_snapshot_id
            __props__.__dict__["from_volume_id"] = from_volume_id
            __props__.__dict__["name"] = name
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["size_in_gb"] = size_in_gb
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["zone"] = zone
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["server_id"] = None
        super(InstanceVolume, __self__).__init__(
            'scaleway:index/instanceVolume:InstanceVolume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            from_snapshot_id: Optional[pulumi.Input[str]] = None,
            from_volume_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            size_in_gb: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'InstanceVolume':
        """
        Get an existing InstanceVolume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] from_snapshot_id: Create a volume based on a image
        :param pulumi.Input[str] from_volume_id: Create a copy of an existing volume
        :param pulumi.Input[str] name: The name of the volume
        :param pulumi.Input[str] organization_id: The organization_id you want to attach the resource to
        :param pulumi.Input[str] project_id: The project_id you want to attach the resource to
        :param pulumi.Input[str] server_id: The server associated with this volume
        :param pulumi.Input[int] size_in_gb: The size of the volume in gigabyte
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the volume
        :param pulumi.Input[str] type: The volume type
        :param pulumi.Input[str] zone: The zone you want to attach the resource to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceVolumeState.__new__(_InstanceVolumeState)

        __props__.__dict__["from_snapshot_id"] = from_snapshot_id
        __props__.__dict__["from_volume_id"] = from_volume_id
        __props__.__dict__["name"] = name
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["size_in_gb"] = size_in_gb
        __props__.__dict__["tags"] = tags
        __props__.__dict__["type"] = type
        __props__.__dict__["zone"] = zone
        return InstanceVolume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="fromSnapshotId")
    def from_snapshot_id(self) -> pulumi.Output[Optional[str]]:
        """
        Create a volume based on a image
        """
        return pulumi.get(self, "from_snapshot_id")

    @property
    @pulumi.getter(name="fromVolumeId")
    def from_volume_id(self) -> pulumi.Output[Optional[str]]:
        """
        Create a copy of an existing volume
        """
        return pulumi.get(self, "from_volume_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the volume
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
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project_id you want to attach the resource to
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        The server associated with this volume
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="sizeInGb")
    def size_in_gb(self) -> pulumi.Output[Optional[int]]:
        """
        The size of the volume in gigabyte
        """
        return pulumi.get(self, "size_in_gb")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags associated with the volume
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The volume type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        The zone you want to attach the resource to
        """
        return pulumi.get(self, "zone")

