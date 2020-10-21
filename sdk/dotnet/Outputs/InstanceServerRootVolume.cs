// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway.Outputs
{

    [OutputType]
    public sealed class InstanceServerRootVolume
    {
        /// <summary>
        /// Forces deletion of the root volume on instance termination.
        /// </summary>
        public readonly bool? DeleteOnTermination;
        /// <summary>
        /// Size of the root volume in gigabytes.
        /// To find the right size use [this endpoint](https://api.scaleway.com/instance/v1/zones/fr-par-1/products/servers) and
        /// check the `volumes_constraint.{min|max}_size` (in bytes) for your `commercial_type`.
        /// Updates to this field will recreate a new resource.
        /// </summary>
        public readonly int? SizeInGb;
        /// <summary>
        /// The volume ID of the root volume of the server.
        /// </summary>
        public readonly string? VolumeId;

        [OutputConstructor]
        private InstanceServerRootVolume(
            bool? deleteOnTermination,

            int? sizeInGb,

            string? volumeId)
        {
            DeleteOnTermination = deleteOnTermination;
            SizeInGb = sizeInGb;
            VolumeId = volumeId;
        }
    }
}
