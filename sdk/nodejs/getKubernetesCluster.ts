// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export function getKubernetesCluster(args?: GetKubernetesClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetKubernetesClusterResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("scaleway:index/getKubernetesCluster:getKubernetesCluster", {
        "clusterId": args.clusterId,
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getKubernetesCluster.
 */
export interface GetKubernetesClusterArgs {
    clusterId?: string;
    name?: string;
    region?: string;
}

/**
 * A collection of values returned by getKubernetesCluster.
 */
export interface GetKubernetesClusterResult {
    readonly admissionPlugins: string[];
    readonly apiserverCertSans: string[];
    readonly apiserverUrl: string;
    readonly autoUpgrades: outputs.GetKubernetesClusterAutoUpgrade[];
    readonly autoscalerConfigs: outputs.GetKubernetesClusterAutoscalerConfig[];
    readonly clusterId?: string;
    readonly cni: string;
    readonly createdAt: string;
    readonly description: string;
    readonly featureGates: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly kubeconfigs: outputs.GetKubernetesClusterKubeconfig[];
    readonly name?: string;
    readonly openIdConnectConfigs: outputs.GetKubernetesClusterOpenIdConnectConfig[];
    readonly organizationId: string;
    readonly projectId: string;
    readonly region?: string;
    readonly status: string;
    readonly tags: string[];
    readonly type: string;
    readonly updatedAt: string;
    readonly upgradeAvailable: boolean;
    readonly version: string;
    readonly wildcardDns: string;
}

export function getKubernetesClusterOutput(args?: GetKubernetesClusterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetKubernetesClusterResult> {
    return pulumi.output(args).apply(a => getKubernetesCluster(a, opts))
}

/**
 * A collection of arguments for invoking getKubernetesCluster.
 */
export interface GetKubernetesClusterOutputArgs {
    clusterId?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    region?: pulumi.Input<string>;
}
