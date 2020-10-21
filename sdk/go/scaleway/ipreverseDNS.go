// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
// Please use `InstanceIP` instead.
//
// Provides reverse DNS settings for IPs.
// For additional details please refer to [API documentation](https://developer.scaleway.com/#ips).
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-scaleway/sdk/go/scaleway"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		testService, err := scaleway.NewIP(ctx, "testService", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = scaleway.NewIPReverseDNS(ctx, "google", &scaleway.IPReverseDNSArgs{
// 			Ip:      testService.ID(),
// 			Reverse: pulumi.String("test_service.awesome-corp.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type IPReverseDNS struct {
	pulumi.CustomResourceState

	// ID or Address of IP
	Ip pulumi.StringOutput `pulumi:"ip"`
	// Reverse DNS of the IP
	Reverse pulumi.StringOutput `pulumi:"reverse"`
}

// NewIPReverseDNS registers a new resource with the given unique name, arguments, and options.
func NewIPReverseDNS(ctx *pulumi.Context,
	name string, args *IPReverseDNSArgs, opts ...pulumi.ResourceOption) (*IPReverseDNS, error) {
	if args == nil || args.Ip == nil {
		return nil, errors.New("missing required argument 'Ip'")
	}
	if args == nil || args.Reverse == nil {
		return nil, errors.New("missing required argument 'Reverse'")
	}
	if args == nil {
		args = &IPReverseDNSArgs{}
	}
	var resource IPReverseDNS
	err := ctx.RegisterResource("scaleway:index/iPReverseDNS:IPReverseDNS", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIPReverseDNS gets an existing IPReverseDNS resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIPReverseDNS(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IPReverseDNSState, opts ...pulumi.ResourceOption) (*IPReverseDNS, error) {
	var resource IPReverseDNS
	err := ctx.ReadResource("scaleway:index/iPReverseDNS:IPReverseDNS", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IPReverseDNS resources.
type ipreverseDNSState struct {
	// ID or Address of IP
	Ip *string `pulumi:"ip"`
	// Reverse DNS of the IP
	Reverse *string `pulumi:"reverse"`
}

type IPReverseDNSState struct {
	// ID or Address of IP
	Ip pulumi.StringPtrInput
	// Reverse DNS of the IP
	Reverse pulumi.StringPtrInput
}

func (IPReverseDNSState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipreverseDNSState)(nil)).Elem()
}

type ipreverseDNSArgs struct {
	// ID or Address of IP
	Ip string `pulumi:"ip"`
	// Reverse DNS of the IP
	Reverse string `pulumi:"reverse"`
}

// The set of arguments for constructing a IPReverseDNS resource.
type IPReverseDNSArgs struct {
	// ID or Address of IP
	Ip pulumi.StringInput
	// Reverse DNS of the IP
	Reverse pulumi.StringInput
}

func (IPReverseDNSArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipreverseDNSArgs)(nil)).Elem()
}
