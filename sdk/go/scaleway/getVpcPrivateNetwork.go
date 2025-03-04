// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupVpcPrivateNetwork(ctx *pulumi.Context, args *LookupVpcPrivateNetworkArgs, opts ...pulumi.InvokeOption) (*LookupVpcPrivateNetworkResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupVpcPrivateNetworkResult
	err := ctx.Invoke("scaleway:index/getVpcPrivateNetwork:getVpcPrivateNetwork", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVpcPrivateNetwork.
type LookupVpcPrivateNetworkArgs struct {
	Name             *string `pulumi:"name"`
	PrivateNetworkId *string `pulumi:"privateNetworkId"`
}

// A collection of values returned by getVpcPrivateNetwork.
type LookupVpcPrivateNetworkResult struct {
	CreatedAt string `pulumi:"createdAt"`
	// The provider-assigned unique ID for this managed resource.
	Id               string   `pulumi:"id"`
	Name             *string  `pulumi:"name"`
	OrganizationId   string   `pulumi:"organizationId"`
	PrivateNetworkId *string  `pulumi:"privateNetworkId"`
	ProjectId        string   `pulumi:"projectId"`
	Tags             []string `pulumi:"tags"`
	UpdatedAt        string   `pulumi:"updatedAt"`
	Zone             string   `pulumi:"zone"`
}

func LookupVpcPrivateNetworkOutput(ctx *pulumi.Context, args LookupVpcPrivateNetworkOutputArgs, opts ...pulumi.InvokeOption) LookupVpcPrivateNetworkResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVpcPrivateNetworkResult, error) {
			args := v.(LookupVpcPrivateNetworkArgs)
			r, err := LookupVpcPrivateNetwork(ctx, &args, opts...)
			var s LookupVpcPrivateNetworkResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVpcPrivateNetworkResultOutput)
}

// A collection of arguments for invoking getVpcPrivateNetwork.
type LookupVpcPrivateNetworkOutputArgs struct {
	Name             pulumi.StringPtrInput `pulumi:"name"`
	PrivateNetworkId pulumi.StringPtrInput `pulumi:"privateNetworkId"`
}

func (LookupVpcPrivateNetworkOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpcPrivateNetworkArgs)(nil)).Elem()
}

// A collection of values returned by getVpcPrivateNetwork.
type LookupVpcPrivateNetworkResultOutput struct{ *pulumi.OutputState }

func (LookupVpcPrivateNetworkResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpcPrivateNetworkResult)(nil)).Elem()
}

func (o LookupVpcPrivateNetworkResultOutput) ToLookupVpcPrivateNetworkResultOutput() LookupVpcPrivateNetworkResultOutput {
	return o
}

func (o LookupVpcPrivateNetworkResultOutput) ToLookupVpcPrivateNetworkResultOutputWithContext(ctx context.Context) LookupVpcPrivateNetworkResultOutput {
	return o
}

func (o LookupVpcPrivateNetworkResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupVpcPrivateNetworkResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupVpcPrivateNetworkResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupVpcPrivateNetworkResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

func (o LookupVpcPrivateNetworkResultOutput) PrivateNetworkId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) *string { return v.PrivateNetworkId }).(pulumi.StringPtrOutput)
}

func (o LookupVpcPrivateNetworkResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

func (o LookupVpcPrivateNetworkResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func (o LookupVpcPrivateNetworkResultOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) string { return v.UpdatedAt }).(pulumi.StringOutput)
}

func (o LookupVpcPrivateNetworkResultOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v LookupVpcPrivateNetworkResult) string { return v.Zone }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVpcPrivateNetworkResultOutput{})
}
