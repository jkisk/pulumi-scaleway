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
    public sealed class IotRouteRest
    {
        public readonly ImmutableDictionary<string, string> Headers;
        public readonly string Uri;
        public readonly string Verb;

        [OutputConstructor]
        private IotRouteRest(
            ImmutableDictionary<string, string> headers,

            string uri,

            string verb)
        {
            Headers = headers;
            Uri = uri;
            Verb = verb;
        }
    }
}
