# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['KubernetesClusterBeta']


class KubernetesClusterBeta(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admission_plugins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 auto_upgrade: Optional[pulumi.Input[pulumi.InputType['KubernetesClusterBetaAutoUpgradeArgs']]] = None,
                 autoscaler_config: Optional[pulumi.Input[pulumi.InputType['KubernetesClusterBetaAutoscalerConfigArgs']]] = None,
                 cni: Optional[pulumi.Input[str]] = None,
                 default_pool: Optional[pulumi.Input[pulumi.InputType['KubernetesClusterBetaDefaultPoolArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_dashboard: Optional[pulumi.Input[bool]] = None,
                 feature_gates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ingress: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a KubernetesClusterBeta resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] admission_plugins: The list of [admission plugins](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) to enable on the cluster.
        :param pulumi.Input[pulumi.InputType['KubernetesClusterBetaAutoUpgradeArgs']] auto_upgrade: The auto upgrade configuration.
        :param pulumi.Input[pulumi.InputType['KubernetesClusterBetaAutoscalerConfigArgs']] autoscaler_config: The configuration options for the [Kubernetes cluster autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler).
        :param pulumi.Input[str] cni: The Container Network Interface (CNI) for the Kubernetes cluster.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[pulumi.InputType['KubernetesClusterBetaDefaultPoolArgs']] default_pool: See below.
        :param pulumi.Input[str] description: A description for the Kubernetes cluster.
        :param pulumi.Input[bool] enable_dashboard: Enables the [Kubernetes dashboard](https://github.com/kubernetes/dashboard) for the Kubernetes cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] feature_gates: The list of [feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) to enable on the cluster.
        :param pulumi.Input[str] ingress: The [ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) to be deployed on the Kubernetes cluster.
        :param pulumi.Input[str] name: The name for the Kubernetes cluster.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the organization the cluster is associated with.
        :param pulumi.Input[str] region: `region`) The region in which the cluster should be created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the Kubernetes cluster.
        :param pulumi.Input[str] version: The version of the Kubernetes cluster.
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

            __props__['admission_plugins'] = admission_plugins
            __props__['auto_upgrade'] = auto_upgrade
            __props__['autoscaler_config'] = autoscaler_config
            if cni is None:
                raise TypeError("Missing required property 'cni'")
            __props__['cni'] = cni
            if default_pool is not None:
                warnings.warn("This fields is deprecated and will be removed in the next major version, please use scaleway_k8s_pool_beta instead.", DeprecationWarning)
                pulumi.log.warn("default_pool is deprecated: This fields is deprecated and will be removed in the next major version, please use scaleway_k8s_pool_beta instead.")
            __props__['default_pool'] = default_pool
            __props__['description'] = description
            __props__['enable_dashboard'] = enable_dashboard
            __props__['feature_gates'] = feature_gates
            __props__['ingress'] = ingress
            __props__['name'] = name
            __props__['organization_id'] = organization_id
            __props__['region'] = region
            __props__['tags'] = tags
            if version is None:
                raise TypeError("Missing required property 'version'")
            __props__['version'] = version
            __props__['apiserver_url'] = None
            __props__['created_at'] = None
            __props__['kubeconfig'] = None
            __props__['status'] = None
            __props__['updated_at'] = None
            __props__['upgrade_available'] = None
            __props__['wildcard_dns'] = None
        super(KubernetesClusterBeta, __self__).__init__(
            'scaleway:index/kubernetesClusterBeta:KubernetesClusterBeta',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admission_plugins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            apiserver_url: Optional[pulumi.Input[str]] = None,
            auto_upgrade: Optional[pulumi.Input[pulumi.InputType['KubernetesClusterBetaAutoUpgradeArgs']]] = None,
            autoscaler_config: Optional[pulumi.Input[pulumi.InputType['KubernetesClusterBetaAutoscalerConfigArgs']]] = None,
            cni: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            default_pool: Optional[pulumi.Input[pulumi.InputType['KubernetesClusterBetaDefaultPoolArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enable_dashboard: Optional[pulumi.Input[bool]] = None,
            feature_gates: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ingress: Optional[pulumi.Input[str]] = None,
            kubeconfig: Optional[pulumi.Input[pulumi.InputType['KubernetesClusterBetaKubeconfigArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            updated_at: Optional[pulumi.Input[str]] = None,
            upgrade_available: Optional[pulumi.Input[bool]] = None,
            version: Optional[pulumi.Input[str]] = None,
            wildcard_dns: Optional[pulumi.Input[str]] = None) -> 'KubernetesClusterBeta':
        """
        Get an existing KubernetesClusterBeta resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] admission_plugins: The list of [admission plugins](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) to enable on the cluster.
        :param pulumi.Input[str] apiserver_url: The URL of the Kubernetes API server.
        :param pulumi.Input[pulumi.InputType['KubernetesClusterBetaAutoUpgradeArgs']] auto_upgrade: The auto upgrade configuration.
        :param pulumi.Input[pulumi.InputType['KubernetesClusterBetaAutoscalerConfigArgs']] autoscaler_config: The configuration options for the [Kubernetes cluster autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler).
        :param pulumi.Input[str] cni: The Container Network Interface (CNI) for the Kubernetes cluster.
               > **Important:** Updates to this field will recreate a new resource.
        :param pulumi.Input[str] created_at: The creation date of the cluster.
        :param pulumi.Input[pulumi.InputType['KubernetesClusterBetaDefaultPoolArgs']] default_pool: See below.
        :param pulumi.Input[str] description: A description for the Kubernetes cluster.
        :param pulumi.Input[bool] enable_dashboard: Enables the [Kubernetes dashboard](https://github.com/kubernetes/dashboard) for the Kubernetes cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] feature_gates: The list of [feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) to enable on the cluster.
        :param pulumi.Input[str] ingress: The [ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) to be deployed on the Kubernetes cluster.
        :param pulumi.Input[pulumi.InputType['KubernetesClusterBetaKubeconfigArgs']] kubeconfig: The kubeconfig configuration file of the Kubernetes cluster
        :param pulumi.Input[str] name: The name for the Kubernetes cluster.
        :param pulumi.Input[str] organization_id: `organization_id`) The ID of the organization the cluster is associated with.
        :param pulumi.Input[str] region: `region`) The region in which the cluster should be created.
        :param pulumi.Input[str] status: The status of the Kubernetes cluster.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags associated with the Kubernetes cluster.
        :param pulumi.Input[str] updated_at: The last update date of the cluster.
        :param pulumi.Input[bool] upgrade_available: Set to `true` if a newer Kubernetes version is available.
        :param pulumi.Input[str] version: The version of the Kubernetes cluster.
        :param pulumi.Input[str] wildcard_dns: The DNS wildcard that points to all ready nodes.
               - `kubeconfig`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admission_plugins"] = admission_plugins
        __props__["apiserver_url"] = apiserver_url
        __props__["auto_upgrade"] = auto_upgrade
        __props__["autoscaler_config"] = autoscaler_config
        __props__["cni"] = cni
        __props__["created_at"] = created_at
        __props__["default_pool"] = default_pool
        __props__["description"] = description
        __props__["enable_dashboard"] = enable_dashboard
        __props__["feature_gates"] = feature_gates
        __props__["ingress"] = ingress
        __props__["kubeconfig"] = kubeconfig
        __props__["name"] = name
        __props__["organization_id"] = organization_id
        __props__["region"] = region
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["updated_at"] = updated_at
        __props__["upgrade_available"] = upgrade_available
        __props__["version"] = version
        __props__["wildcard_dns"] = wildcard_dns
        return KubernetesClusterBeta(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="admissionPlugins")
    def admission_plugins(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of [admission plugins](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) to enable on the cluster.
        """
        return pulumi.get(self, "admission_plugins")

    @property
    @pulumi.getter(name="apiserverUrl")
    def apiserver_url(self) -> pulumi.Output[str]:
        """
        The URL of the Kubernetes API server.
        """
        return pulumi.get(self, "apiserver_url")

    @property
    @pulumi.getter(name="autoUpgrade")
    def auto_upgrade(self) -> pulumi.Output['outputs.KubernetesClusterBetaAutoUpgrade']:
        """
        The auto upgrade configuration.
        """
        return pulumi.get(self, "auto_upgrade")

    @property
    @pulumi.getter(name="autoscalerConfig")
    def autoscaler_config(self) -> pulumi.Output['outputs.KubernetesClusterBetaAutoscalerConfig']:
        """
        The configuration options for the [Kubernetes cluster autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler).
        """
        return pulumi.get(self, "autoscaler_config")

    @property
    @pulumi.getter
    def cni(self) -> pulumi.Output[str]:
        """
        The Container Network Interface (CNI) for the Kubernetes cluster.
        > **Important:** Updates to this field will recreate a new resource.
        """
        return pulumi.get(self, "cni")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The creation date of the cluster.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="defaultPool")
    def default_pool(self) -> pulumi.Output[Optional['outputs.KubernetesClusterBetaDefaultPool']]:
        """
        See below.
        """
        return pulumi.get(self, "default_pool")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the Kubernetes cluster.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableDashboard")
    def enable_dashboard(self) -> pulumi.Output[Optional[bool]]:
        """
        Enables the [Kubernetes dashboard](https://github.com/kubernetes/dashboard) for the Kubernetes cluster.
        """
        return pulumi.get(self, "enable_dashboard")

    @property
    @pulumi.getter(name="featureGates")
    def feature_gates(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of [feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) to enable on the cluster.
        """
        return pulumi.get(self, "feature_gates")

    @property
    @pulumi.getter
    def ingress(self) -> pulumi.Output[Optional[str]]:
        """
        The [ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) to be deployed on the Kubernetes cluster.
        """
        return pulumi.get(self, "ingress")

    @property
    @pulumi.getter
    def kubeconfig(self) -> pulumi.Output['outputs.KubernetesClusterBetaKubeconfig']:
        """
        The kubeconfig configuration file of the Kubernetes cluster
        """
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for the Kubernetes cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        `organization_id`) The ID of the organization the cluster is associated with.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        `region`) The region in which the cluster should be created.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Kubernetes cluster.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags associated with the Kubernetes cluster.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The last update date of the cluster.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="upgradeAvailable")
    def upgrade_available(self) -> pulumi.Output[bool]:
        """
        Set to `true` if a newer Kubernetes version is available.
        """
        return pulumi.get(self, "upgrade_available")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the Kubernetes cluster.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="wildcardDns")
    def wildcard_dns(self) -> pulumi.Output[str]:
        """
        The DNS wildcard that points to all ready nodes.
        - `kubeconfig`
        """
        return pulumi.get(self, "wildcard_dns")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

