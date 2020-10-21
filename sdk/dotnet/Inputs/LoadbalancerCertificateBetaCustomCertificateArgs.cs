// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway.Inputs
{

    public sealed class LoadbalancerCertificateBetaCustomCertificateArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Full PEM-formatted certificate chain.
        /// </summary>
        [Input("certificateChain", required: true)]
        public Input<string> CertificateChain { get; set; } = null!;

        public LoadbalancerCertificateBetaCustomCertificateArgs()
        {
        }
    }
}
