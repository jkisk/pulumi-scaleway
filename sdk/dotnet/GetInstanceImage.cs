// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway
{
    public static class GetInstanceImage
    {
        public static Task<GetInstanceImageResult> InvokeAsync(GetInstanceImageArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetInstanceImageResult>("scaleway:index/getInstanceImage:getInstanceImage", args ?? new GetInstanceImageArgs(), options.WithDefaults());

        public static Output<GetInstanceImageResult> Invoke(GetInstanceImageInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetInstanceImageResult>("scaleway:index/getInstanceImage:getInstanceImage", args ?? new GetInstanceImageInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInstanceImageArgs : Pulumi.InvokeArgs
    {
        [Input("architecture")]
        public string? Architecture { get; set; }

        [Input("imageId")]
        public string? ImageId { get; set; }

        [Input("latest")]
        public bool? Latest { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        [Input("projectId")]
        public string? ProjectId { get; set; }

        [Input("zone")]
        public string? Zone { get; set; }

        public GetInstanceImageArgs()
        {
        }
    }

    public sealed class GetInstanceImageInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("architecture")]
        public Input<string>? Architecture { get; set; }

        [Input("imageId")]
        public Input<string>? ImageId { get; set; }

        [Input("latest")]
        public Input<bool>? Latest { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public GetInstanceImageInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetInstanceImageResult
    {
        public readonly ImmutableArray<string> AdditionalVolumeIds;
        public readonly string? Architecture;
        public readonly string CreationDate;
        public readonly string DefaultBootscriptId;
        public readonly string FromServerId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? ImageId;
        public readonly bool? Latest;
        public readonly string ModificationDate;
        public readonly string? Name;
        public readonly string OrganizationId;
        public readonly string ProjectId;
        public readonly bool Public;
        public readonly string RootVolumeId;
        public readonly string State;
        public readonly string Zone;

        [OutputConstructor]
        private GetInstanceImageResult(
            ImmutableArray<string> additionalVolumeIds,

            string? architecture,

            string creationDate,

            string defaultBootscriptId,

            string fromServerId,

            string id,

            string? imageId,

            bool? latest,

            string modificationDate,

            string? name,

            string organizationId,

            string projectId,

            bool @public,

            string rootVolumeId,

            string state,

            string zone)
        {
            AdditionalVolumeIds = additionalVolumeIds;
            Architecture = architecture;
            CreationDate = creationDate;
            DefaultBootscriptId = defaultBootscriptId;
            FromServerId = fromServerId;
            Id = id;
            ImageId = imageId;
            Latest = latest;
            ModificationDate = modificationDate;
            Name = name;
            OrganizationId = organizationId;
            ProjectId = projectId;
            Public = @public;
            RootVolumeId = rootVolumeId;
            State = state;
            Zone = zone;
        }
    }
}
