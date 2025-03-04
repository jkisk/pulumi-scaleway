// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway
{
    [ScalewayResourceType("scaleway:index/loadbalancerIp:LoadbalancerIp")]
    public partial class LoadbalancerIp : Pulumi.CustomResource
    {
        /// <summary>
        /// The load-balancer public IP address
        /// </summary>
        [Output("ipAddress")]
        public Output<string> IpAddress { get; private set; } = null!;

        /// <summary>
        /// The ID of the load balancer attached to this IP, if any
        /// </summary>
        [Output("lbId")]
        public Output<string> LbId { get; private set; } = null!;

        /// <summary>
        /// The organization_id you want to attach the resource to
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The project_id you want to attach the resource to
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// The region of the resource
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The reverse domain name for this IP
        /// </summary>
        [Output("reverse")]
        public Output<string> Reverse { get; private set; } = null!;

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a LoadbalancerIp resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LoadbalancerIp(string name, LoadbalancerIpArgs? args = null, CustomResourceOptions? options = null)
            : base("scaleway:index/loadbalancerIp:LoadbalancerIp", name, args ?? new LoadbalancerIpArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LoadbalancerIp(string name, Input<string> id, LoadbalancerIpState? state = null, CustomResourceOptions? options = null)
            : base("scaleway:index/loadbalancerIp:LoadbalancerIp", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing LoadbalancerIp resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LoadbalancerIp Get(string name, Input<string> id, LoadbalancerIpState? state = null, CustomResourceOptions? options = null)
        {
            return new LoadbalancerIp(name, id, state, options);
        }
    }

    public sealed class LoadbalancerIpArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The project_id you want to attach the resource to
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The reverse domain name for this IP
        /// </summary>
        [Input("reverse")]
        public Input<string>? Reverse { get; set; }

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public LoadbalancerIpArgs()
        {
        }
    }

    public sealed class LoadbalancerIpState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The load-balancer public IP address
        /// </summary>
        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        /// <summary>
        /// The ID of the load balancer attached to this IP, if any
        /// </summary>
        [Input("lbId")]
        public Input<string>? LbId { get; set; }

        /// <summary>
        /// The organization_id you want to attach the resource to
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The project_id you want to attach the resource to
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The region of the resource
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The reverse domain name for this IP
        /// </summary>
        [Input("reverse")]
        public Input<string>? Reverse { get; set; }

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public LoadbalancerIpState()
        {
        }
    }
}
