// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupInstanceVolume(ctx *pulumi.Context, args *LookupInstanceVolumeArgs, opts ...pulumi.InvokeOption) (*LookupInstanceVolumeResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupInstanceVolumeResult
	err := ctx.Invoke("scaleway:index/getInstanceVolume:getInstanceVolume", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getInstanceVolume.
type LookupInstanceVolumeArgs struct {
	Name     *string `pulumi:"name"`
	VolumeId *string `pulumi:"volumeId"`
	Zone     *string `pulumi:"zone"`
}

// A collection of values returned by getInstanceVolume.
type LookupInstanceVolumeResult struct {
	FromSnapshotId string `pulumi:"fromSnapshotId"`
	FromVolumeId   string `pulumi:"fromVolumeId"`
	// The provider-assigned unique ID for this managed resource.
	Id             string   `pulumi:"id"`
	Name           *string  `pulumi:"name"`
	OrganizationId string   `pulumi:"organizationId"`
	ProjectId      string   `pulumi:"projectId"`
	ServerId       string   `pulumi:"serverId"`
	SizeInGb       int      `pulumi:"sizeInGb"`
	Tags           []string `pulumi:"tags"`
	Type           string   `pulumi:"type"`
	VolumeId       *string  `pulumi:"volumeId"`
	Zone           *string  `pulumi:"zone"`
}

func LookupInstanceVolumeOutput(ctx *pulumi.Context, args LookupInstanceVolumeOutputArgs, opts ...pulumi.InvokeOption) LookupInstanceVolumeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupInstanceVolumeResult, error) {
			args := v.(LookupInstanceVolumeArgs)
			r, err := LookupInstanceVolume(ctx, &args, opts...)
			var s LookupInstanceVolumeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupInstanceVolumeResultOutput)
}

// A collection of arguments for invoking getInstanceVolume.
type LookupInstanceVolumeOutputArgs struct {
	Name     pulumi.StringPtrInput `pulumi:"name"`
	VolumeId pulumi.StringPtrInput `pulumi:"volumeId"`
	Zone     pulumi.StringPtrInput `pulumi:"zone"`
}

func (LookupInstanceVolumeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceVolumeArgs)(nil)).Elem()
}

// A collection of values returned by getInstanceVolume.
type LookupInstanceVolumeResultOutput struct{ *pulumi.OutputState }

func (LookupInstanceVolumeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceVolumeResult)(nil)).Elem()
}

func (o LookupInstanceVolumeResultOutput) ToLookupInstanceVolumeResultOutput() LookupInstanceVolumeResultOutput {
	return o
}

func (o LookupInstanceVolumeResultOutput) ToLookupInstanceVolumeResultOutputWithContext(ctx context.Context) LookupInstanceVolumeResultOutput {
	return o
}

func (o LookupInstanceVolumeResultOutput) FromSnapshotId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) string { return v.FromSnapshotId }).(pulumi.StringOutput)
}

func (o LookupInstanceVolumeResultOutput) FromVolumeId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) string { return v.FromVolumeId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupInstanceVolumeResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupInstanceVolumeResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupInstanceVolumeResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

func (o LookupInstanceVolumeResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

func (o LookupInstanceVolumeResultOutput) ServerId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) string { return v.ServerId }).(pulumi.StringOutput)
}

func (o LookupInstanceVolumeResultOutput) SizeInGb() pulumi.IntOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) int { return v.SizeInGb }).(pulumi.IntOutput)
}

func (o LookupInstanceVolumeResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func (o LookupInstanceVolumeResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) string { return v.Type }).(pulumi.StringOutput)
}

func (o LookupInstanceVolumeResultOutput) VolumeId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) *string { return v.VolumeId }).(pulumi.StringPtrOutput)
}

func (o LookupInstanceVolumeResultOutput) Zone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupInstanceVolumeResult) *string { return v.Zone }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupInstanceVolumeResultOutput{})
}
