// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type LoadbalancerCertificate struct {
	pulumi.CustomResourceState

	// The main domain name of the certificate
	CommonName pulumi.StringOutput `pulumi:"commonName"`
	// The custom type certificate type configuration
	CustomCertificate LoadbalancerCertificateCustomCertificatePtrOutput `pulumi:"customCertificate"`
	// The identifier (SHA-1) of the certificate
	Fingerprint pulumi.StringOutput `pulumi:"fingerprint"`
	// The load-balancer ID
	LbId pulumi.StringOutput `pulumi:"lbId"`
	// The Let's Encrypt type certificate configuration
	Letsencrypt LoadbalancerCertificateLetsencryptPtrOutput `pulumi:"letsencrypt"`
	// The name of the load-balancer certificate
	Name pulumi.StringOutput `pulumi:"name"`
	// The not valid after validity bound timestamp
	NotValidAfter pulumi.StringOutput `pulumi:"notValidAfter"`
	// The not valid before validity bound timestamp
	NotValidBefore pulumi.StringOutput `pulumi:"notValidBefore"`
	// The status of certificate
	Status pulumi.StringOutput `pulumi:"status"`
	// The alternative domain names of the certificate
	SubjectAlternativeNames pulumi.StringArrayOutput `pulumi:"subjectAlternativeNames"`
}

// NewLoadbalancerCertificate registers a new resource with the given unique name, arguments, and options.
func NewLoadbalancerCertificate(ctx *pulumi.Context,
	name string, args *LoadbalancerCertificateArgs, opts ...pulumi.ResourceOption) (*LoadbalancerCertificate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.LbId == nil {
		return nil, errors.New("invalid value for required argument 'LbId'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource LoadbalancerCertificate
	err := ctx.RegisterResource("scaleway:index/loadbalancerCertificate:LoadbalancerCertificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLoadbalancerCertificate gets an existing LoadbalancerCertificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoadbalancerCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LoadbalancerCertificateState, opts ...pulumi.ResourceOption) (*LoadbalancerCertificate, error) {
	var resource LoadbalancerCertificate
	err := ctx.ReadResource("scaleway:index/loadbalancerCertificate:LoadbalancerCertificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LoadbalancerCertificate resources.
type loadbalancerCertificateState struct {
	// The main domain name of the certificate
	CommonName *string `pulumi:"commonName"`
	// The custom type certificate type configuration
	CustomCertificate *LoadbalancerCertificateCustomCertificate `pulumi:"customCertificate"`
	// The identifier (SHA-1) of the certificate
	Fingerprint *string `pulumi:"fingerprint"`
	// The load-balancer ID
	LbId *string `pulumi:"lbId"`
	// The Let's Encrypt type certificate configuration
	Letsencrypt *LoadbalancerCertificateLetsencrypt `pulumi:"letsencrypt"`
	// The name of the load-balancer certificate
	Name *string `pulumi:"name"`
	// The not valid after validity bound timestamp
	NotValidAfter *string `pulumi:"notValidAfter"`
	// The not valid before validity bound timestamp
	NotValidBefore *string `pulumi:"notValidBefore"`
	// The status of certificate
	Status *string `pulumi:"status"`
	// The alternative domain names of the certificate
	SubjectAlternativeNames []string `pulumi:"subjectAlternativeNames"`
}

type LoadbalancerCertificateState struct {
	// The main domain name of the certificate
	CommonName pulumi.StringPtrInput
	// The custom type certificate type configuration
	CustomCertificate LoadbalancerCertificateCustomCertificatePtrInput
	// The identifier (SHA-1) of the certificate
	Fingerprint pulumi.StringPtrInput
	// The load-balancer ID
	LbId pulumi.StringPtrInput
	// The Let's Encrypt type certificate configuration
	Letsencrypt LoadbalancerCertificateLetsencryptPtrInput
	// The name of the load-balancer certificate
	Name pulumi.StringPtrInput
	// The not valid after validity bound timestamp
	NotValidAfter pulumi.StringPtrInput
	// The not valid before validity bound timestamp
	NotValidBefore pulumi.StringPtrInput
	// The status of certificate
	Status pulumi.StringPtrInput
	// The alternative domain names of the certificate
	SubjectAlternativeNames pulumi.StringArrayInput
}

func (LoadbalancerCertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*loadbalancerCertificateState)(nil)).Elem()
}

type loadbalancerCertificateArgs struct {
	// The custom type certificate type configuration
	CustomCertificate *LoadbalancerCertificateCustomCertificate `pulumi:"customCertificate"`
	// The load-balancer ID
	LbId string `pulumi:"lbId"`
	// The Let's Encrypt type certificate configuration
	Letsencrypt *LoadbalancerCertificateLetsencrypt `pulumi:"letsencrypt"`
	// The name of the load-balancer certificate
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a LoadbalancerCertificate resource.
type LoadbalancerCertificateArgs struct {
	// The custom type certificate type configuration
	CustomCertificate LoadbalancerCertificateCustomCertificatePtrInput
	// The load-balancer ID
	LbId pulumi.StringInput
	// The Let's Encrypt type certificate configuration
	Letsencrypt LoadbalancerCertificateLetsencryptPtrInput
	// The name of the load-balancer certificate
	Name pulumi.StringPtrInput
}

func (LoadbalancerCertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*loadbalancerCertificateArgs)(nil)).Elem()
}

type LoadbalancerCertificateInput interface {
	pulumi.Input

	ToLoadbalancerCertificateOutput() LoadbalancerCertificateOutput
	ToLoadbalancerCertificateOutputWithContext(ctx context.Context) LoadbalancerCertificateOutput
}

func (*LoadbalancerCertificate) ElementType() reflect.Type {
	return reflect.TypeOf((**LoadbalancerCertificate)(nil)).Elem()
}

func (i *LoadbalancerCertificate) ToLoadbalancerCertificateOutput() LoadbalancerCertificateOutput {
	return i.ToLoadbalancerCertificateOutputWithContext(context.Background())
}

func (i *LoadbalancerCertificate) ToLoadbalancerCertificateOutputWithContext(ctx context.Context) LoadbalancerCertificateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LoadbalancerCertificateOutput)
}

type LoadbalancerCertificateOutput struct{ *pulumi.OutputState }

func (LoadbalancerCertificateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LoadbalancerCertificate)(nil)).Elem()
}

func (o LoadbalancerCertificateOutput) ToLoadbalancerCertificateOutput() LoadbalancerCertificateOutput {
	return o
}

func (o LoadbalancerCertificateOutput) ToLoadbalancerCertificateOutputWithContext(ctx context.Context) LoadbalancerCertificateOutput {
	return o
}

// The main domain name of the certificate
func (o LoadbalancerCertificateOutput) CommonName() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) pulumi.StringOutput { return v.CommonName }).(pulumi.StringOutput)
}

// The custom type certificate type configuration
func (o LoadbalancerCertificateOutput) CustomCertificate() LoadbalancerCertificateCustomCertificatePtrOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) LoadbalancerCertificateCustomCertificatePtrOutput {
		return v.CustomCertificate
	}).(LoadbalancerCertificateCustomCertificatePtrOutput)
}

// The identifier (SHA-1) of the certificate
func (o LoadbalancerCertificateOutput) Fingerprint() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) pulumi.StringOutput { return v.Fingerprint }).(pulumi.StringOutput)
}

// The load-balancer ID
func (o LoadbalancerCertificateOutput) LbId() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) pulumi.StringOutput { return v.LbId }).(pulumi.StringOutput)
}

// The Let's Encrypt type certificate configuration
func (o LoadbalancerCertificateOutput) Letsencrypt() LoadbalancerCertificateLetsencryptPtrOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) LoadbalancerCertificateLetsencryptPtrOutput { return v.Letsencrypt }).(LoadbalancerCertificateLetsencryptPtrOutput)
}

// The name of the load-balancer certificate
func (o LoadbalancerCertificateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The not valid after validity bound timestamp
func (o LoadbalancerCertificateOutput) NotValidAfter() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) pulumi.StringOutput { return v.NotValidAfter }).(pulumi.StringOutput)
}

// The not valid before validity bound timestamp
func (o LoadbalancerCertificateOutput) NotValidBefore() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) pulumi.StringOutput { return v.NotValidBefore }).(pulumi.StringOutput)
}

// The status of certificate
func (o LoadbalancerCertificateOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// The alternative domain names of the certificate
func (o LoadbalancerCertificateOutput) SubjectAlternativeNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *LoadbalancerCertificate) pulumi.StringArrayOutput { return v.SubjectAlternativeNames }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LoadbalancerCertificateInput)(nil)).Elem(), &LoadbalancerCertificate{})
	pulumi.RegisterOutputType(LoadbalancerCertificateOutput{})
}
