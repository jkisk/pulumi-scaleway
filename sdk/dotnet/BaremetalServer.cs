// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway
{
    [ScalewayResourceType("scaleway:index/baremetalServer:BaremetalServer")]
    public partial class BaremetalServer : Pulumi.CustomResource
    {
        /// <summary>
        /// Some description to associate to the server, max 255 characters
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("domain")]
        public Output<string> Domain { get; private set; } = null!;

        /// <summary>
        /// Hostname of the server
        /// </summary>
        [Output("hostname")]
        public Output<string?> Hostname { get; private set; } = null!;

        [Output("ips")]
        public Output<ImmutableArray<Outputs.BaremetalServerIp>> Ips { get; private set; } = null!;

        /// <summary>
        /// Name of the server
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// ID or name of the server offer
        /// </summary>
        [Output("offer")]
        public Output<string> Offer { get; private set; } = null!;

        /// <summary>
        /// ID of the server offer
        /// </summary>
        [Output("offerId")]
        public Output<string> OfferId { get; private set; } = null!;

        /// <summary>
        /// The organization_id you want to attach the resource to
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The base image of the server
        /// </summary>
        [Output("os")]
        public Output<string> Os { get; private set; } = null!;

        /// <summary>
        /// The base image ID of the server
        /// </summary>
        [Output("osId")]
        public Output<string> OsId { get; private set; } = null!;

        /// <summary>
        /// The project_id you want to attach the resource to
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// Array of SSH key IDs allowed to SSH to the server
        /// </summary>
        [Output("sshKeyIds")]
        public Output<ImmutableArray<string>> SshKeyIds { get; private set; } = null!;

        /// <summary>
        /// Array of tags to associate with the server
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a BaremetalServer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BaremetalServer(string name, BaremetalServerArgs args, CustomResourceOptions? options = null)
            : base("scaleway:index/baremetalServer:BaremetalServer", name, args ?? new BaremetalServerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BaremetalServer(string name, Input<string> id, BaremetalServerState? state = null, CustomResourceOptions? options = null)
            : base("scaleway:index/baremetalServer:BaremetalServer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing BaremetalServer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BaremetalServer Get(string name, Input<string> id, BaremetalServerState? state = null, CustomResourceOptions? options = null)
        {
            return new BaremetalServer(name, id, state, options);
        }
    }

    public sealed class BaremetalServerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Some description to associate to the server, max 255 characters
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Hostname of the server
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        /// <summary>
        /// Name of the server
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// ID or name of the server offer
        /// </summary>
        [Input("offer", required: true)]
        public Input<string> Offer { get; set; } = null!;

        /// <summary>
        /// The base image of the server
        /// </summary>
        [Input("os", required: true)]
        public Input<string> Os { get; set; } = null!;

        /// <summary>
        /// The project_id you want to attach the resource to
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        [Input("sshKeyIds", required: true)]
        private InputList<string>? _sshKeyIds;

        /// <summary>
        /// Array of SSH key IDs allowed to SSH to the server
        /// </summary>
        public InputList<string> SshKeyIds
        {
            get => _sshKeyIds ?? (_sshKeyIds = new InputList<string>());
            set => _sshKeyIds = value;
        }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Array of tags to associate with the server
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public BaremetalServerArgs()
        {
        }
    }

    public sealed class BaremetalServerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Some description to associate to the server, max 255 characters
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// Hostname of the server
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("ips")]
        private InputList<Inputs.BaremetalServerIpGetArgs>? _ips;
        public InputList<Inputs.BaremetalServerIpGetArgs> Ips
        {
            get => _ips ?? (_ips = new InputList<Inputs.BaremetalServerIpGetArgs>());
            set => _ips = value;
        }

        /// <summary>
        /// Name of the server
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// ID or name of the server offer
        /// </summary>
        [Input("offer")]
        public Input<string>? Offer { get; set; }

        /// <summary>
        /// ID of the server offer
        /// </summary>
        [Input("offerId")]
        public Input<string>? OfferId { get; set; }

        /// <summary>
        /// The organization_id you want to attach the resource to
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The base image of the server
        /// </summary>
        [Input("os")]
        public Input<string>? Os { get; set; }

        /// <summary>
        /// The base image ID of the server
        /// </summary>
        [Input("osId")]
        public Input<string>? OsId { get; set; }

        /// <summary>
        /// The project_id you want to attach the resource to
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        [Input("sshKeyIds")]
        private InputList<string>? _sshKeyIds;

        /// <summary>
        /// Array of SSH key IDs allowed to SSH to the server
        /// </summary>
        public InputList<string> SshKeyIds
        {
            get => _sshKeyIds ?? (_sshKeyIds = new InputList<string>());
            set => _sshKeyIds = value;
        }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Array of tags to associate with the server
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The zone you want to attach the resource to
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public BaremetalServerState()
        {
        }
    }
}
