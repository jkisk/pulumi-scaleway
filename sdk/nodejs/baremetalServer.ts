// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

export class BaremetalServer extends pulumi.CustomResource {
    /**
     * Get an existing BaremetalServer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BaremetalServerState, opts?: pulumi.CustomResourceOptions): BaremetalServer {
        return new BaremetalServer(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'scaleway:index/baremetalServer:BaremetalServer';

    /**
     * Returns true if the given object is an instance of BaremetalServer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BaremetalServer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BaremetalServer.__pulumiType;
    }

    /**
     * Some description to associate to the server, max 255 characters
     */
    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly domain!: pulumi.Output<string>;
    /**
     * Hostname of the server
     */
    public readonly hostname!: pulumi.Output<string | undefined>;
    public /*out*/ readonly ips!: pulumi.Output<outputs.BaremetalServerIp[]>;
    /**
     * Name of the server
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * ID or name of the server offer
     */
    public readonly offer!: pulumi.Output<string>;
    /**
     * ID of the server offer
     */
    public /*out*/ readonly offerId!: pulumi.Output<string>;
    /**
     * The organization_id you want to attach the resource to
     */
    public /*out*/ readonly organizationId!: pulumi.Output<string>;
    /**
     * The base image of the server
     */
    public readonly os!: pulumi.Output<string>;
    /**
     * The base image ID of the server
     */
    public /*out*/ readonly osId!: pulumi.Output<string>;
    /**
     * The project_id you want to attach the resource to
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Array of SSH key IDs allowed to SSH to the server
     */
    public readonly sshKeyIds!: pulumi.Output<string[]>;
    /**
     * Array of tags to associate with the server
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The zone you want to attach the resource to
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a BaremetalServer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BaremetalServerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BaremetalServerArgs | BaremetalServerState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as BaremetalServerState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["domain"] = state ? state.domain : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
            resourceInputs["ips"] = state ? state.ips : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["offer"] = state ? state.offer : undefined;
            resourceInputs["offerId"] = state ? state.offerId : undefined;
            resourceInputs["organizationId"] = state ? state.organizationId : undefined;
            resourceInputs["os"] = state ? state.os : undefined;
            resourceInputs["osId"] = state ? state.osId : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["sshKeyIds"] = state ? state.sshKeyIds : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as BaremetalServerArgs | undefined;
            if ((!args || args.offer === undefined) && !opts.urn) {
                throw new Error("Missing required property 'offer'");
            }
            if ((!args || args.os === undefined) && !opts.urn) {
                throw new Error("Missing required property 'os'");
            }
            if ((!args || args.sshKeyIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sshKeyIds'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["hostname"] = args ? args.hostname : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["offer"] = args ? args.offer : undefined;
            resourceInputs["os"] = args ? args.os : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["sshKeyIds"] = args ? args.sshKeyIds : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["zone"] = args ? args.zone : undefined;
            resourceInputs["domain"] = undefined /*out*/;
            resourceInputs["ips"] = undefined /*out*/;
            resourceInputs["offerId"] = undefined /*out*/;
            resourceInputs["organizationId"] = undefined /*out*/;
            resourceInputs["osId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(BaremetalServer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BaremetalServer resources.
 */
export interface BaremetalServerState {
    /**
     * Some description to associate to the server, max 255 characters
     */
    description?: pulumi.Input<string>;
    domain?: pulumi.Input<string>;
    /**
     * Hostname of the server
     */
    hostname?: pulumi.Input<string>;
    ips?: pulumi.Input<pulumi.Input<inputs.BaremetalServerIp>[]>;
    /**
     * Name of the server
     */
    name?: pulumi.Input<string>;
    /**
     * ID or name of the server offer
     */
    offer?: pulumi.Input<string>;
    /**
     * ID of the server offer
     */
    offerId?: pulumi.Input<string>;
    /**
     * The organization_id you want to attach the resource to
     */
    organizationId?: pulumi.Input<string>;
    /**
     * The base image of the server
     */
    os?: pulumi.Input<string>;
    /**
     * The base image ID of the server
     */
    osId?: pulumi.Input<string>;
    /**
     * The project_id you want to attach the resource to
     */
    projectId?: pulumi.Input<string>;
    /**
     * Array of SSH key IDs allowed to SSH to the server
     */
    sshKeyIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Array of tags to associate with the server
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The zone you want to attach the resource to
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a BaremetalServer resource.
 */
export interface BaremetalServerArgs {
    /**
     * Some description to associate to the server, max 255 characters
     */
    description?: pulumi.Input<string>;
    /**
     * Hostname of the server
     */
    hostname?: pulumi.Input<string>;
    /**
     * Name of the server
     */
    name?: pulumi.Input<string>;
    /**
     * ID or name of the server offer
     */
    offer: pulumi.Input<string>;
    /**
     * The base image of the server
     */
    os: pulumi.Input<string>;
    /**
     * The project_id you want to attach the resource to
     */
    projectId?: pulumi.Input<string>;
    /**
     * Array of SSH key IDs allowed to SSH to the server
     */
    sshKeyIds: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Array of tags to associate with the server
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The zone you want to attach the resource to
     */
    zone?: pulumi.Input<string>;
}
