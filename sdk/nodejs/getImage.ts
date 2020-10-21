// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
 * Please use `scaleway.getInstanceImage` instead or `scaleway.getMarketplaceImageBeta` depending on your usage.
 *
 * Use this data source to get the ID of a registered Image for use with the
 * `scaleway.Server` resource.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as scaleway from "@pulumi/scaleway";
 *
 * const ubuntu = scaleway.getImage({
 *     architecture: "arm",
 *     name: "Ubuntu Precise",
 * });
 * const base = new scaleway.Server("base", {
 *     image: ubuntu.then(ubuntu => ubuntu.id),
 *     type: "C1",
 * });
 * ```
 */
export function getImage(args: GetImageArgs, opts?: pulumi.InvokeOptions): Promise<GetImageResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("scaleway:index/getImage:getImage", {
        "architecture": args.architecture,
        "mostRecent": args.mostRecent,
        "name": args.name,
        "nameFilter": args.nameFilter,
    }, opts);
}

/**
 * A collection of arguments for invoking getImage.
 */
export interface GetImageArgs {
    /**
     * any supported Scaleway architecture, e.g. `x8664`, `arm`
     */
    readonly architecture: string;
    /**
     * Return most recent image if multiple exist. Can not be used together with name_filter.
     */
    readonly mostRecent?: boolean;
    /**
     * Exact name of desired Image
     */
    readonly name?: string;
    /**
     * Regexp to match Image name by
     */
    readonly nameFilter?: string;
}

/**
 * A collection of values returned by getImage.
 */
export interface GetImageResult {
    /**
     * architecture of the Image, e.g. `arm` or `x8664`
     */
    readonly architecture: string;
    /**
     * date when image was created
     */
    readonly creationDate: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly mostRecent?: boolean;
    readonly name: string;
    readonly nameFilter?: string;
    /**
     * uuid of the organization owning this Image
     */
    readonly organization: string;
    /**
     * is this a public image
     */
    readonly public: boolean;
}
