// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export function getDatabaseAcl(args: GetDatabaseAclArgs, opts?: pulumi.InvokeOptions): Promise<GetDatabaseAclResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("scaleway:index/getDatabaseAcl:getDatabaseAcl", {
        "instanceId": args.instanceId,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatabaseAcl.
 */
export interface GetDatabaseAclArgs {
    instanceId: string;
}

/**
 * A collection of values returned by getDatabaseAcl.
 */
export interface GetDatabaseAclResult {
    readonly aclRules: outputs.GetDatabaseAclAclRule[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly instanceId: string;
    readonly region: string;
}

export function getDatabaseAclOutput(args: GetDatabaseAclOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDatabaseAclResult> {
    return pulumi.output(args).apply(a => getDatabaseAcl(a, opts))
}

/**
 * A collection of arguments for invoking getDatabaseAcl.
 */
export interface GetDatabaseAclOutputArgs {
    instanceId: pulumi.Input<string>;
}
