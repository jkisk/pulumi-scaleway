// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway.Inputs
{

    public sealed class IotDeviceMessageFiltersArgs : Pulumi.ResourceArgs
    {
        [Input("publish")]
        public Input<Inputs.IotDeviceMessageFiltersPublishArgs>? Publish { get; set; }

        [Input("subscribe")]
        public Input<Inputs.IotDeviceMessageFiltersSubscribeArgs>? Subscribe { get; set; }

        public IotDeviceMessageFiltersArgs()
        {
        }
    }
}
