// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type DomainRecord struct {
	pulumi.CustomResourceState

	// The data of the record
	Data pulumi.StringOutput `pulumi:"data"`
	// The zone you want to add the record in
	DnsZone pulumi.StringOutput `pulumi:"dnsZone"`
	// Return record based on client localisation
	GeoIp DomainRecordGeoIpPtrOutput `pulumi:"geoIp"`
	// Return record based on client localisation
	HttpService DomainRecordHttpServicePtrOutput `pulumi:"httpService"`
	// When destroy a resource record, if a zone have only NS, delete the zone
	KeepEmptyZone pulumi.BoolPtrOutput `pulumi:"keepEmptyZone"`
	// The name of the record
	Name pulumi.StringOutput `pulumi:"name"`
	// The priority of the record
	Priority pulumi.IntOutput `pulumi:"priority"`
	// The project_id you want to attach the resource to
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Does the DNS zone is the root zone or not
	RootZone pulumi.BoolOutput `pulumi:"rootZone"`
	// The ttl of the record
	Ttl pulumi.IntPtrOutput `pulumi:"ttl"`
	// The type of the record
	Type pulumi.StringOutput `pulumi:"type"`
	// Return record based on client subnet
	Views DomainRecordViewArrayOutput `pulumi:"views"`
	// Return record based on weight
	Weighteds DomainRecordWeightedArrayOutput `pulumi:"weighteds"`
}

// NewDomainRecord registers a new resource with the given unique name, arguments, and options.
func NewDomainRecord(ctx *pulumi.Context,
	name string, args *DomainRecordArgs, opts ...pulumi.ResourceOption) (*DomainRecord, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Data == nil {
		return nil, errors.New("invalid value for required argument 'Data'")
	}
	if args.DnsZone == nil {
		return nil, errors.New("invalid value for required argument 'DnsZone'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource DomainRecord
	err := ctx.RegisterResource("scaleway:index/domainRecord:DomainRecord", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomainRecord gets an existing DomainRecord resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomainRecord(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainRecordState, opts ...pulumi.ResourceOption) (*DomainRecord, error) {
	var resource DomainRecord
	err := ctx.ReadResource("scaleway:index/domainRecord:DomainRecord", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DomainRecord resources.
type domainRecordState struct {
	// The data of the record
	Data *string `pulumi:"data"`
	// The zone you want to add the record in
	DnsZone *string `pulumi:"dnsZone"`
	// Return record based on client localisation
	GeoIp *DomainRecordGeoIp `pulumi:"geoIp"`
	// Return record based on client localisation
	HttpService *DomainRecordHttpService `pulumi:"httpService"`
	// When destroy a resource record, if a zone have only NS, delete the zone
	KeepEmptyZone *bool `pulumi:"keepEmptyZone"`
	// The name of the record
	Name *string `pulumi:"name"`
	// The priority of the record
	Priority *int `pulumi:"priority"`
	// The project_id you want to attach the resource to
	ProjectId *string `pulumi:"projectId"`
	// Does the DNS zone is the root zone or not
	RootZone *bool `pulumi:"rootZone"`
	// The ttl of the record
	Ttl *int `pulumi:"ttl"`
	// The type of the record
	Type *string `pulumi:"type"`
	// Return record based on client subnet
	Views []DomainRecordView `pulumi:"views"`
	// Return record based on weight
	Weighteds []DomainRecordWeighted `pulumi:"weighteds"`
}

type DomainRecordState struct {
	// The data of the record
	Data pulumi.StringPtrInput
	// The zone you want to add the record in
	DnsZone pulumi.StringPtrInput
	// Return record based on client localisation
	GeoIp DomainRecordGeoIpPtrInput
	// Return record based on client localisation
	HttpService DomainRecordHttpServicePtrInput
	// When destroy a resource record, if a zone have only NS, delete the zone
	KeepEmptyZone pulumi.BoolPtrInput
	// The name of the record
	Name pulumi.StringPtrInput
	// The priority of the record
	Priority pulumi.IntPtrInput
	// The project_id you want to attach the resource to
	ProjectId pulumi.StringPtrInput
	// Does the DNS zone is the root zone or not
	RootZone pulumi.BoolPtrInput
	// The ttl of the record
	Ttl pulumi.IntPtrInput
	// The type of the record
	Type pulumi.StringPtrInput
	// Return record based on client subnet
	Views DomainRecordViewArrayInput
	// Return record based on weight
	Weighteds DomainRecordWeightedArrayInput
}

func (DomainRecordState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainRecordState)(nil)).Elem()
}

type domainRecordArgs struct {
	// The data of the record
	Data string `pulumi:"data"`
	// The zone you want to add the record in
	DnsZone string `pulumi:"dnsZone"`
	// Return record based on client localisation
	GeoIp *DomainRecordGeoIp `pulumi:"geoIp"`
	// Return record based on client localisation
	HttpService *DomainRecordHttpService `pulumi:"httpService"`
	// When destroy a resource record, if a zone have only NS, delete the zone
	KeepEmptyZone *bool `pulumi:"keepEmptyZone"`
	// The name of the record
	Name *string `pulumi:"name"`
	// The priority of the record
	Priority *int `pulumi:"priority"`
	// The project_id you want to attach the resource to
	ProjectId *string `pulumi:"projectId"`
	// The ttl of the record
	Ttl *int `pulumi:"ttl"`
	// The type of the record
	Type string `pulumi:"type"`
	// Return record based on client subnet
	Views []DomainRecordView `pulumi:"views"`
	// Return record based on weight
	Weighteds []DomainRecordWeighted `pulumi:"weighteds"`
}

// The set of arguments for constructing a DomainRecord resource.
type DomainRecordArgs struct {
	// The data of the record
	Data pulumi.StringInput
	// The zone you want to add the record in
	DnsZone pulumi.StringInput
	// Return record based on client localisation
	GeoIp DomainRecordGeoIpPtrInput
	// Return record based on client localisation
	HttpService DomainRecordHttpServicePtrInput
	// When destroy a resource record, if a zone have only NS, delete the zone
	KeepEmptyZone pulumi.BoolPtrInput
	// The name of the record
	Name pulumi.StringPtrInput
	// The priority of the record
	Priority pulumi.IntPtrInput
	// The project_id you want to attach the resource to
	ProjectId pulumi.StringPtrInput
	// The ttl of the record
	Ttl pulumi.IntPtrInput
	// The type of the record
	Type pulumi.StringInput
	// Return record based on client subnet
	Views DomainRecordViewArrayInput
	// Return record based on weight
	Weighteds DomainRecordWeightedArrayInput
}

func (DomainRecordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainRecordArgs)(nil)).Elem()
}

type DomainRecordInput interface {
	pulumi.Input

	ToDomainRecordOutput() DomainRecordOutput
	ToDomainRecordOutputWithContext(ctx context.Context) DomainRecordOutput
}

func (*DomainRecord) ElementType() reflect.Type {
	return reflect.TypeOf((**DomainRecord)(nil)).Elem()
}

func (i *DomainRecord) ToDomainRecordOutput() DomainRecordOutput {
	return i.ToDomainRecordOutputWithContext(context.Background())
}

func (i *DomainRecord) ToDomainRecordOutputWithContext(ctx context.Context) DomainRecordOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainRecordOutput)
}

type DomainRecordOutput struct{ *pulumi.OutputState }

func (DomainRecordOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DomainRecord)(nil)).Elem()
}

func (o DomainRecordOutput) ToDomainRecordOutput() DomainRecordOutput {
	return o
}

func (o DomainRecordOutput) ToDomainRecordOutputWithContext(ctx context.Context) DomainRecordOutput {
	return o
}

// The data of the record
func (o DomainRecordOutput) Data() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.StringOutput { return v.Data }).(pulumi.StringOutput)
}

// The zone you want to add the record in
func (o DomainRecordOutput) DnsZone() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.StringOutput { return v.DnsZone }).(pulumi.StringOutput)
}

// Return record based on client localisation
func (o DomainRecordOutput) GeoIp() DomainRecordGeoIpPtrOutput {
	return o.ApplyT(func(v *DomainRecord) DomainRecordGeoIpPtrOutput { return v.GeoIp }).(DomainRecordGeoIpPtrOutput)
}

// Return record based on client localisation
func (o DomainRecordOutput) HttpService() DomainRecordHttpServicePtrOutput {
	return o.ApplyT(func(v *DomainRecord) DomainRecordHttpServicePtrOutput { return v.HttpService }).(DomainRecordHttpServicePtrOutput)
}

// When destroy a resource record, if a zone have only NS, delete the zone
func (o DomainRecordOutput) KeepEmptyZone() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.BoolPtrOutput { return v.KeepEmptyZone }).(pulumi.BoolPtrOutput)
}

// The name of the record
func (o DomainRecordOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The priority of the record
func (o DomainRecordOutput) Priority() pulumi.IntOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.IntOutput { return v.Priority }).(pulumi.IntOutput)
}

// The project_id you want to attach the resource to
func (o DomainRecordOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// Does the DNS zone is the root zone or not
func (o DomainRecordOutput) RootZone() pulumi.BoolOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.BoolOutput { return v.RootZone }).(pulumi.BoolOutput)
}

// The ttl of the record
func (o DomainRecordOutput) Ttl() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.IntPtrOutput { return v.Ttl }).(pulumi.IntPtrOutput)
}

// The type of the record
func (o DomainRecordOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *DomainRecord) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// Return record based on client subnet
func (o DomainRecordOutput) Views() DomainRecordViewArrayOutput {
	return o.ApplyT(func(v *DomainRecord) DomainRecordViewArrayOutput { return v.Views }).(DomainRecordViewArrayOutput)
}

// Return record based on weight
func (o DomainRecordOutput) Weighteds() DomainRecordWeightedArrayOutput {
	return o.ApplyT(func(v *DomainRecord) DomainRecordWeightedArrayOutput { return v.Weighteds }).(DomainRecordWeightedArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DomainRecordInput)(nil)).Elem(), &DomainRecord{})
	pulumi.RegisterOutputType(DomainRecordOutput{})
}
