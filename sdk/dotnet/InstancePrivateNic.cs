// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway
{
    [ScalewayResourceType("scaleway:index/instancePrivateNic:InstancePrivateNic")]
    public partial class InstancePrivateNic : Pulumi.CustomResource
    {
        /// <summary>
        /// MAC address of the NIC
        /// </summary>
        [Output("macAddress")]
        public Output<string> MacAddress { get; private set; } = null!;

        /// <summary>
        /// The private network ID
        /// </summary>
        [Output("privateNetworkId")]
        public Output<string> PrivateNetworkId { get; private set; } = null!;

        /// <summary>
        /// The server ID
        /// </summary>
        [Output("serverId")]
        public Output<string> ServerId { get; private set; } = null!;

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a InstancePrivateNic resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstancePrivateNic(string name, InstancePrivateNicArgs args, CustomResourceOptions? options = null)
            : base("scaleway:index/instancePrivateNic:InstancePrivateNic", name, args ?? new InstancePrivateNicArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstancePrivateNic(string name, Input<string> id, InstancePrivateNicState? state = null, CustomResourceOptions? options = null)
            : base("scaleway:index/instancePrivateNic:InstancePrivateNic", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/jaxxstorm/pulumi-scaleway/releases/download/${VERSION}",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing InstancePrivateNic resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstancePrivateNic Get(string name, Input<string> id, InstancePrivateNicState? state = null, CustomResourceOptions? options = null)
        {
            return new InstancePrivateNic(name, id, state, options);
        }
    }

    public sealed class InstancePrivateNicArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The private network ID
        /// </summary>
        [Input("privateNetworkId", required: true)]
        public Input<string> PrivateNetworkId { get; set; } = null!;

        /// <summary>
        /// The server ID
        /// </summary>
        [Input("serverId", required: true)]
        public Input<string> ServerId { get; set; } = null!;

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstancePrivateNicArgs()
        {
        }
    }

    public sealed class InstancePrivateNicState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// MAC address of the NIC
        /// </summary>
        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        /// <summary>
        /// The private network ID
        /// </summary>
        [Input("privateNetworkId")]
        public Input<string>? PrivateNetworkId { get; set; }

        /// <summary>
        /// The server ID
        /// </summary>
        [Input("serverId")]
        public Input<string>? ServerId { get; set; }

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstancePrivateNicState()
        {
        }
    }
}
