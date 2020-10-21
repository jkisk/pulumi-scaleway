// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Creates and manages Scaleway Compute Baremetal servers. For more information, see [the documentation](https://developers.scaleway.com/en/products/baremetal/api).
//
// ## Examples
//
// ### Basic
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
// 		opt0 := "main"
// 		main, err := scaleway.LookupAccountSshKey(ctx, &scaleway.LookupAccountSshKeyArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = scaleway.NewBaremetalServer(ctx, "base", &scaleway.BaremetalServerArgs{
// 			Zone:  pulumi.String("fr-par-2"),
// 			Offer: pulumi.String("GP-BM1-M"),
// 			Os:    pulumi.String("d17d6872-0412-45d9-a198-af82c34d3c5c"),
// 			SshKeyIds: pulumi.StringArray{
// 				scaleway.LookupAccountSshKeyResult(main),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type BaremetalServer struct {
	pulumi.CustomResourceState

	// A description for the server.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The domain of the server.
	Domain pulumi.StringOutput `pulumi:"domain"`
	// The hostname of the server.
	Hostname pulumi.StringPtrOutput `pulumi:"hostname"`
	// (List of) The IPs of the server.
	Ips BaremetalServerIpArrayOutput `pulumi:"ips"`
	// The name of the server.
	Name pulumi.StringOutput `pulumi:"name"`
	// The offer name or UUID of the baremetal server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-334154) to find the right offer.
	Offer pulumi.StringOutput `pulumi:"offer"`
	// The ID of the offer.
	OfferId pulumi.StringOutput `pulumi:"offerId"`
	// `organizationId`) The ID of the organization the server is associated with.
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The UUID of the os to install on the server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-87598a) to find the right OS ID.
	Os pulumi.StringOutput `pulumi:"os"`
	// The ID of the os.
	OsId pulumi.StringOutput `pulumi:"osId"`
	// List of SSH keys allowed to connect to the server.
	SshKeyIds pulumi.StringArrayOutput `pulumi:"sshKeyIds"`
	// The tags associated with the server.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// `zone`) The zone in which the server should be created.
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewBaremetalServer registers a new resource with the given unique name, arguments, and options.
func NewBaremetalServer(ctx *pulumi.Context,
	name string, args *BaremetalServerArgs, opts ...pulumi.ResourceOption) (*BaremetalServer, error) {
	if args == nil || args.Offer == nil {
		return nil, errors.New("missing required argument 'Offer'")
	}
	if args == nil || args.Os == nil {
		return nil, errors.New("missing required argument 'Os'")
	}
	if args == nil || args.SshKeyIds == nil {
		return nil, errors.New("missing required argument 'SshKeyIds'")
	}
	if args == nil {
		args = &BaremetalServerArgs{}
	}
	var resource BaremetalServer
	err := ctx.RegisterResource("scaleway:index/baremetalServer:BaremetalServer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBaremetalServer gets an existing BaremetalServer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBaremetalServer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BaremetalServerState, opts ...pulumi.ResourceOption) (*BaremetalServer, error) {
	var resource BaremetalServer
	err := ctx.ReadResource("scaleway:index/baremetalServer:BaremetalServer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BaremetalServer resources.
type baremetalServerState struct {
	// A description for the server.
	Description *string `pulumi:"description"`
	// The domain of the server.
	Domain *string `pulumi:"domain"`
	// The hostname of the server.
	Hostname *string `pulumi:"hostname"`
	// (List of) The IPs of the server.
	Ips []BaremetalServerIp `pulumi:"ips"`
	// The name of the server.
	Name *string `pulumi:"name"`
	// The offer name or UUID of the baremetal server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-334154) to find the right offer.
	Offer *string `pulumi:"offer"`
	// The ID of the offer.
	OfferId *string `pulumi:"offerId"`
	// `organizationId`) The ID of the organization the server is associated with.
	OrganizationId *string `pulumi:"organizationId"`
	// The UUID of the os to install on the server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-87598a) to find the right OS ID.
	Os *string `pulumi:"os"`
	// The ID of the os.
	OsId *string `pulumi:"osId"`
	// List of SSH keys allowed to connect to the server.
	SshKeyIds []string `pulumi:"sshKeyIds"`
	// The tags associated with the server.
	Tags []string `pulumi:"tags"`
	// `zone`) The zone in which the server should be created.
	Zone *string `pulumi:"zone"`
}

type BaremetalServerState struct {
	// A description for the server.
	Description pulumi.StringPtrInput
	// The domain of the server.
	Domain pulumi.StringPtrInput
	// The hostname of the server.
	Hostname pulumi.StringPtrInput
	// (List of) The IPs of the server.
	Ips BaremetalServerIpArrayInput
	// The name of the server.
	Name pulumi.StringPtrInput
	// The offer name or UUID of the baremetal server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-334154) to find the right offer.
	Offer pulumi.StringPtrInput
	// The ID of the offer.
	OfferId pulumi.StringPtrInput
	// `organizationId`) The ID of the organization the server is associated with.
	OrganizationId pulumi.StringPtrInput
	// The UUID of the os to install on the server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-87598a) to find the right OS ID.
	Os pulumi.StringPtrInput
	// The ID of the os.
	OsId pulumi.StringPtrInput
	// List of SSH keys allowed to connect to the server.
	SshKeyIds pulumi.StringArrayInput
	// The tags associated with the server.
	Tags pulumi.StringArrayInput
	// `zone`) The zone in which the server should be created.
	Zone pulumi.StringPtrInput
}

func (BaremetalServerState) ElementType() reflect.Type {
	return reflect.TypeOf((*baremetalServerState)(nil)).Elem()
}

type baremetalServerArgs struct {
	// A description for the server.
	Description *string `pulumi:"description"`
	// The hostname of the server.
	Hostname *string `pulumi:"hostname"`
	// The name of the server.
	Name *string `pulumi:"name"`
	// The offer name or UUID of the baremetal server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-334154) to find the right offer.
	Offer string `pulumi:"offer"`
	// `organizationId`) The ID of the organization the server is associated with.
	OrganizationId *string `pulumi:"organizationId"`
	// The UUID of the os to install on the server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-87598a) to find the right OS ID.
	Os string `pulumi:"os"`
	// List of SSH keys allowed to connect to the server.
	SshKeyIds []string `pulumi:"sshKeyIds"`
	// The tags associated with the server.
	Tags []string `pulumi:"tags"`
	// `zone`) The zone in which the server should be created.
	Zone *string `pulumi:"zone"`
}

// The set of arguments for constructing a BaremetalServer resource.
type BaremetalServerArgs struct {
	// A description for the server.
	Description pulumi.StringPtrInput
	// The hostname of the server.
	Hostname pulumi.StringPtrInput
	// The name of the server.
	Name pulumi.StringPtrInput
	// The offer name or UUID of the baremetal server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-334154) to find the right offer.
	Offer pulumi.StringInput
	// `organizationId`) The ID of the organization the server is associated with.
	OrganizationId pulumi.StringPtrInput
	// The UUID of the os to install on the server.
	// Use [this endpoint](https://developers.scaleway.com/en/products/baremetal/api/#get-87598a) to find the right OS ID.
	Os pulumi.StringInput
	// List of SSH keys allowed to connect to the server.
	SshKeyIds pulumi.StringArrayInput
	// The tags associated with the server.
	Tags pulumi.StringArrayInput
	// `zone`) The zone in which the server should be created.
	Zone pulumi.StringPtrInput
}

func (BaremetalServerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*baremetalServerArgs)(nil)).Elem()
}
