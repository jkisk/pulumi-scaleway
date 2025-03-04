# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetInstanceVolumeResult',
    'AwaitableGetInstanceVolumeResult',
    'get_instance_volume',
    'get_instance_volume_output',
]

@pulumi.output_type
class GetInstanceVolumeResult:
    """
    A collection of values returned by getInstanceVolume.
    """
    def __init__(__self__, from_snapshot_id=None, from_volume_id=None, id=None, name=None, organization_id=None, project_id=None, server_id=None, size_in_gb=None, tags=None, type=None, volume_id=None, zone=None):
        if from_snapshot_id and not isinstance(from_snapshot_id, str):
            raise TypeError("Expected argument 'from_snapshot_id' to be a str")
        pulumi.set(__self__, "from_snapshot_id", from_snapshot_id)
        if from_volume_id and not isinstance(from_volume_id, str):
            raise TypeError("Expected argument 'from_volume_id' to be a str")
        pulumi.set(__self__, "from_volume_id", from_volume_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if server_id and not isinstance(server_id, str):
            raise TypeError("Expected argument 'server_id' to be a str")
        pulumi.set(__self__, "server_id", server_id)
        if size_in_gb and not isinstance(size_in_gb, int):
            raise TypeError("Expected argument 'size_in_gb' to be a int")
        pulumi.set(__self__, "size_in_gb", size_in_gb)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volume_id and not isinstance(volume_id, str):
            raise TypeError("Expected argument 'volume_id' to be a str")
        pulumi.set(__self__, "volume_id", volume_id)
        if zone and not isinstance(zone, str):
            raise TypeError("Expected argument 'zone' to be a str")
        pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="fromSnapshotId")
    def from_snapshot_id(self) -> str:
        return pulumi.get(self, "from_snapshot_id")

    @property
    @pulumi.getter(name="fromVolumeId")
    def from_volume_id(self) -> str:
        return pulumi.get(self, "from_volume_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> str:
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="sizeInGb")
    def size_in_gb(self) -> int:
        return pulumi.get(self, "size_in_gb")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[str]:
        return pulumi.get(self, "volume_id")

    @property
    @pulumi.getter
    def zone(self) -> Optional[str]:
        return pulumi.get(self, "zone")


class AwaitableGetInstanceVolumeResult(GetInstanceVolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceVolumeResult(
            from_snapshot_id=self.from_snapshot_id,
            from_volume_id=self.from_volume_id,
            id=self.id,
            name=self.name,
            organization_id=self.organization_id,
            project_id=self.project_id,
            server_id=self.server_id,
            size_in_gb=self.size_in_gb,
            tags=self.tags,
            type=self.type,
            volume_id=self.volume_id,
            zone=self.zone)


def get_instance_volume(name: Optional[str] = None,
                        volume_id: Optional[str] = None,
                        zone: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceVolumeResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['volumeId'] = volume_id
    __args__['zone'] = zone
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('scaleway:index/getInstanceVolume:getInstanceVolume', __args__, opts=opts, typ=GetInstanceVolumeResult).value

    return AwaitableGetInstanceVolumeResult(
        from_snapshot_id=__ret__.from_snapshot_id,
        from_volume_id=__ret__.from_volume_id,
        id=__ret__.id,
        name=__ret__.name,
        organization_id=__ret__.organization_id,
        project_id=__ret__.project_id,
        server_id=__ret__.server_id,
        size_in_gb=__ret__.size_in_gb,
        tags=__ret__.tags,
        type=__ret__.type,
        volume_id=__ret__.volume_id,
        zone=__ret__.zone)


@_utilities.lift_output_func(get_instance_volume)
def get_instance_volume_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                               volume_id: Optional[pulumi.Input[Optional[str]]] = None,
                               zone: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceVolumeResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
