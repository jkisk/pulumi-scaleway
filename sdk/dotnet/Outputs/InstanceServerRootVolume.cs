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
        public readonly bool? Boot;
        public readonly bool? DeleteOnTermination;
        public readonly int? SizeInGb;
        public readonly string? VolumeId;
        public readonly string? VolumeType;

        [OutputConstructor]
        private InstanceServerRootVolume(
            bool? boot,

            bool? deleteOnTermination,

            int? sizeInGb,

            string? volumeId,

            string? volumeType)
        {
            Boot = boot;
            DeleteOnTermination = deleteOnTermination;
            SizeInGb = sizeInGb;
            VolumeId = volumeId;
            VolumeType = volumeType;
        }
    }
}
