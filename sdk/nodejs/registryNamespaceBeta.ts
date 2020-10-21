// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Creates and manages Scaleway Container Registry. For more information see [the documentation](https://developers.scaleway.com/en/products/registry/api/).
 *
 * ## Examples
 *
 * ### Basic
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as scaleway from "@pulumi/scaleway";
 *
 * const main = new scaleway.RegistryNamespaceBeta("main", {
 *     description: "Main container registry",
 *     isPublic: false,
 * });
 * ```
 *
 * ## Attibutes Reference
 *
 * In addition to all arguments above, the following attibutes are exported:
 *
 * - `id` - The ID of the namespace
 * - `endpoint` - Endpoint reachable by docker.
 */
export class RegistryNamespaceBeta extends pulumi.CustomResource {
    /**
     * Get an existing RegistryNamespaceBeta resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegistryNamespaceBetaState, opts?: pulumi.CustomResourceOptions): RegistryNamespaceBeta {
        return new RegistryNamespaceBeta(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'scaleway:index/registryNamespaceBeta:RegistryNamespaceBeta';

    /**
     * Returns true if the given object is an instance of RegistryNamespaceBeta.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RegistryNamespaceBeta {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RegistryNamespaceBeta.__pulumiType;
    }

    /**
     * The description of the container registry namespace.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The endpoint reachable by docker
     */
    public /*out*/ readonly endpoint!: pulumi.Output<string>;
    /**
     * Whether or not the registry images stored in the namespace should be downloadable publicly (docker pull).
     */
    public readonly isPublic!: pulumi.Output<boolean | undefined>;
    /**
     * The unique name of the container registry namespace.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * `organizationId`) The ID of the organization the registry is associated with.
     */
    public readonly organizationId!: pulumi.Output<string>;
    /**
     * `region`). The region in which the container registry namespace should be created.
     */
    public readonly region!: pulumi.Output<string>;

    /**
     * Create a RegistryNamespaceBeta resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: RegistryNamespaceBetaArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RegistryNamespaceBetaArgs | RegistryNamespaceBetaState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RegistryNamespaceBetaState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["endpoint"] = state ? state.endpoint : undefined;
            inputs["isPublic"] = state ? state.isPublic : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["organizationId"] = state ? state.organizationId : undefined;
            inputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as RegistryNamespaceBetaArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["isPublic"] = args ? args.isPublic : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["organizationId"] = args ? args.organizationId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["endpoint"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RegistryNamespaceBeta.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RegistryNamespaceBeta resources.
 */
export interface RegistryNamespaceBetaState {
    /**
     * The description of the container registry namespace.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The endpoint reachable by docker
     */
    readonly endpoint?: pulumi.Input<string>;
    /**
     * Whether or not the registry images stored in the namespace should be downloadable publicly (docker pull).
     */
    readonly isPublic?: pulumi.Input<boolean>;
    /**
     * The unique name of the container registry namespace.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * `organizationId`) The ID of the organization the registry is associated with.
     */
    readonly organizationId?: pulumi.Input<string>;
    /**
     * `region`). The region in which the container registry namespace should be created.
     */
    readonly region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RegistryNamespaceBeta resource.
 */
export interface RegistryNamespaceBetaArgs {
    /**
     * The description of the container registry namespace.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Whether or not the registry images stored in the namespace should be downloadable publicly (docker pull).
     */
    readonly isPublic?: pulumi.Input<boolean>;
    /**
     * The unique name of the container registry namespace.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * `organizationId`) The ID of the organization the registry is associated with.
     */
    readonly organizationId?: pulumi.Input<string>;
    /**
     * `region`). The region in which the container registry namespace should be created.
     */
    readonly region?: pulumi.Input<string>;
}
