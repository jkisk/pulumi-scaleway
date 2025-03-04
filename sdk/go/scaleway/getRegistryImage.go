// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetRegistryImage(ctx *pulumi.Context, args *GetRegistryImageArgs, opts ...pulumi.InvokeOption) (*GetRegistryImageResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetRegistryImageResult
	err := ctx.Invoke("scaleway:index/getRegistryImage:getRegistryImage", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRegistryImage.
type GetRegistryImageArgs struct {
	ImageId     *string  `pulumi:"imageId"`
	Name        *string  `pulumi:"name"`
	NamespaceId *string  `pulumi:"namespaceId"`
	ProjectId   *string  `pulumi:"projectId"`
	Region      *string  `pulumi:"region"`
	Tags        []string `pulumi:"tags"`
}

// A collection of values returned by getRegistryImage.
type GetRegistryImageResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id             string   `pulumi:"id"`
	ImageId        *string  `pulumi:"imageId"`
	Name           *string  `pulumi:"name"`
	NamespaceId    string   `pulumi:"namespaceId"`
	OrganizationId string   `pulumi:"organizationId"`
	ProjectId      string   `pulumi:"projectId"`
	Region         string   `pulumi:"region"`
	Size           int      `pulumi:"size"`
	Tags           []string `pulumi:"tags"`
	Visibility     string   `pulumi:"visibility"`
}

func GetRegistryImageOutput(ctx *pulumi.Context, args GetRegistryImageOutputArgs, opts ...pulumi.InvokeOption) GetRegistryImageResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetRegistryImageResult, error) {
			args := v.(GetRegistryImageArgs)
			r, err := GetRegistryImage(ctx, &args, opts...)
			var s GetRegistryImageResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetRegistryImageResultOutput)
}

// A collection of arguments for invoking getRegistryImage.
type GetRegistryImageOutputArgs struct {
	ImageId     pulumi.StringPtrInput   `pulumi:"imageId"`
	Name        pulumi.StringPtrInput   `pulumi:"name"`
	NamespaceId pulumi.StringPtrInput   `pulumi:"namespaceId"`
	ProjectId   pulumi.StringPtrInput   `pulumi:"projectId"`
	Region      pulumi.StringPtrInput   `pulumi:"region"`
	Tags        pulumi.StringArrayInput `pulumi:"tags"`
}

func (GetRegistryImageOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRegistryImageArgs)(nil)).Elem()
}

// A collection of values returned by getRegistryImage.
type GetRegistryImageResultOutput struct{ *pulumi.OutputState }

func (GetRegistryImageResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRegistryImageResult)(nil)).Elem()
}

func (o GetRegistryImageResultOutput) ToGetRegistryImageResultOutput() GetRegistryImageResultOutput {
	return o
}

func (o GetRegistryImageResultOutput) ToGetRegistryImageResultOutputWithContext(ctx context.Context) GetRegistryImageResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetRegistryImageResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistryImageResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetRegistryImageResultOutput) ImageId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetRegistryImageResult) *string { return v.ImageId }).(pulumi.StringPtrOutput)
}

func (o GetRegistryImageResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetRegistryImageResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o GetRegistryImageResultOutput) NamespaceId() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistryImageResult) string { return v.NamespaceId }).(pulumi.StringOutput)
}

func (o GetRegistryImageResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistryImageResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

func (o GetRegistryImageResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistryImageResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

func (o GetRegistryImageResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistryImageResult) string { return v.Region }).(pulumi.StringOutput)
}

func (o GetRegistryImageResultOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v GetRegistryImageResult) int { return v.Size }).(pulumi.IntOutput)
}

func (o GetRegistryImageResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetRegistryImageResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func (o GetRegistryImageResultOutput) Visibility() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegistryImageResult) string { return v.Visibility }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetRegistryImageResultOutput{})
}
