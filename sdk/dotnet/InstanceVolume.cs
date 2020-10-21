// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway
{
    /// <summary>
    /// Creates and manages Scaleway Compute Instance Volumes. For more information, see [the documentation](https://developers.scaleway.com/en/products/instance/api/#volumes-7e8a39).
    /// 
    /// ## Example
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Scaleway = Pulumi.Scaleway;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var serverVolume = new Scaleway.InstanceVolume("serverVolume", new Scaleway.InstanceVolumeArgs
    ///         {
    ///             SizeInGb = 20,
    ///             Type = "l_ssd",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class InstanceVolume : Pulumi.CustomResource
    {
        /// <summary>
        /// Create a volume based on a image
        /// </summary>
        [Output("fromSnapshotId")]
        public Output<string?> FromSnapshotId { get; private set; } = null!;

        /// <summary>
        /// If set, the new volume will be copied from this volume. Only one of `size_in_gb`, `from_volume_id` and `from_volume_id` should be specified.
        /// </summary>
        [Output("fromVolumeId")]
        public Output<string?> FromVolumeId { get; private set; } = null!;

        /// <summary>
        /// The name of the volume. If not provided it will be randomly generated.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// `organization_id`) The ID of the organization the volume is associated with.
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The id of the associated server.
        /// </summary>
        [Output("serverId")]
        public Output<string> ServerId { get; private set; } = null!;

        /// <summary>
        /// The size of the volume. Only one of `size_in_gb`, `from_volume_id` and `from_volume_id` should be specified.
        /// </summary>
        [Output("sizeInGb")]
        public Output<int> SizeInGb { get; private set; } = null!;

        /// <summary>
        /// The type of the volume. The possible values are: `b_ssd` (Block SSD), `l_ssd` (Local SSD).
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// `zone`) The zone in which the volume should be created.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a InstanceVolume resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstanceVolume(string name, InstanceVolumeArgs args, CustomResourceOptions? options = null)
            : base("scaleway:index/instanceVolume:InstanceVolume", name, args ?? new InstanceVolumeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstanceVolume(string name, Input<string> id, InstanceVolumeState? state = null, CustomResourceOptions? options = null)
            : base("scaleway:index/instanceVolume:InstanceVolume", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing InstanceVolume resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstanceVolume Get(string name, Input<string> id, InstanceVolumeState? state = null, CustomResourceOptions? options = null)
        {
            return new InstanceVolume(name, id, state, options);
        }
    }

    public sealed class InstanceVolumeArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Create a volume based on a image
        /// </summary>
        [Input("fromSnapshotId")]
        public Input<string>? FromSnapshotId { get; set; }

        /// <summary>
        /// If set, the new volume will be copied from this volume. Only one of `size_in_gb`, `from_volume_id` and `from_volume_id` should be specified.
        /// </summary>
        [Input("fromVolumeId")]
        public Input<string>? FromVolumeId { get; set; }

        /// <summary>
        /// The name of the volume. If not provided it will be randomly generated.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// `organization_id`) The ID of the organization the volume is associated with.
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The size of the volume. Only one of `size_in_gb`, `from_volume_id` and `from_volume_id` should be specified.
        /// </summary>
        [Input("sizeInGb")]
        public Input<int>? SizeInGb { get; set; }

        /// <summary>
        /// The type of the volume. The possible values are: `b_ssd` (Block SSD), `l_ssd` (Local SSD).
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// `zone`) The zone in which the volume should be created.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceVolumeArgs()
        {
        }
    }

    public sealed class InstanceVolumeState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Create a volume based on a image
        /// </summary>
        [Input("fromSnapshotId")]
        public Input<string>? FromSnapshotId { get; set; }

        /// <summary>
        /// If set, the new volume will be copied from this volume. Only one of `size_in_gb`, `from_volume_id` and `from_volume_id` should be specified.
        /// </summary>
        [Input("fromVolumeId")]
        public Input<string>? FromVolumeId { get; set; }

        /// <summary>
        /// The name of the volume. If not provided it will be randomly generated.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// `organization_id`) The ID of the organization the volume is associated with.
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The id of the associated server.
        /// </summary>
        [Input("serverId")]
        public Input<string>? ServerId { get; set; }

        /// <summary>
        /// The size of the volume. Only one of `size_in_gb`, `from_volume_id` and `from_volume_id` should be specified.
        /// </summary>
        [Input("sizeInGb")]
        public Input<int>? SizeInGb { get; set; }

        /// <summary>
        /// The type of the volume. The possible values are: `b_ssd` (Block SSD), `l_ssd` (Local SSD).
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// `zone`) The zone in which the volume should be created.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceVolumeState()
        {
        }
    }
}
