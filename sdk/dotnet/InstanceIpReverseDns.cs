// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway
{
    [ScalewayResourceType("scaleway:index/instanceIpReverseDns:InstanceIpReverseDns")]
    public partial class InstanceIpReverseDns : Pulumi.CustomResource
    {
        /// <summary>
        /// The IP ID or IP address
        /// </summary>
        [Output("ipId")]
        public Output<string> IpId { get; private set; } = null!;

        /// <summary>
        /// The reverse DNS for this IP
        /// </summary>
        [Output("reverse")]
        public Output<string> Reverse { get; private set; } = null!;

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a InstanceIpReverseDns resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstanceIpReverseDns(string name, InstanceIpReverseDnsArgs args, CustomResourceOptions? options = null)
            : base("scaleway:index/instanceIpReverseDns:InstanceIpReverseDns", name, args ?? new InstanceIpReverseDnsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstanceIpReverseDns(string name, Input<string> id, InstanceIpReverseDnsState? state = null, CustomResourceOptions? options = null)
            : base("scaleway:index/instanceIpReverseDns:InstanceIpReverseDns", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing InstanceIpReverseDns resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstanceIpReverseDns Get(string name, Input<string> id, InstanceIpReverseDnsState? state = null, CustomResourceOptions? options = null)
        {
            return new InstanceIpReverseDns(name, id, state, options);
        }
    }

    public sealed class InstanceIpReverseDnsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP ID or IP address
        /// </summary>
        [Input("ipId", required: true)]
        public Input<string> IpId { get; set; } = null!;

        /// <summary>
        /// The reverse DNS for this IP
        /// </summary>
        [Input("reverse", required: true)]
        public Input<string> Reverse { get; set; } = null!;

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceIpReverseDnsArgs()
        {
        }
    }

    public sealed class InstanceIpReverseDnsState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP ID or IP address
        /// </summary>
        [Input("ipId")]
        public Input<string>? IpId { get; set; }

        /// <summary>
        /// The reverse DNS for this IP
        /// </summary>
        [Input("reverse")]
        public Input<string>? Reverse { get; set; }

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceIpReverseDnsState()
        {
        }
    }
}
