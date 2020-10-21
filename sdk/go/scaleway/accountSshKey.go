// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages user SSH keys to access servers provisioned on Scaleway.
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
// 		_, err := scaleway.NewAccountSshKey(ctx, "main", &scaleway.AccountSshKeyArgs{
// 			PublicKey: pulumi.String("<YOUR-PUBLIC-SSH-KEY>"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type AccountSshKey struct {
	pulumi.CustomResourceState

	// The name of the SSH key.
	Name pulumi.StringOutput `pulumi:"name"`
	// `organizationId`) The ID of the organization the IP is associated with.
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The public SSH key to be added.
	PublicKey pulumi.StringOutput `pulumi:"publicKey"`
}

// NewAccountSshKey registers a new resource with the given unique name, arguments, and options.
func NewAccountSshKey(ctx *pulumi.Context,
	name string, args *AccountSshKeyArgs, opts ...pulumi.ResourceOption) (*AccountSshKey, error) {
	if args == nil || args.PublicKey == nil {
		return nil, errors.New("missing required argument 'PublicKey'")
	}
	if args == nil {
		args = &AccountSshKeyArgs{}
	}
	var resource AccountSshKey
	err := ctx.RegisterResource("scaleway:index/accountSshKey:AccountSshKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccountSshKey gets an existing AccountSshKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccountSshKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccountSshKeyState, opts ...pulumi.ResourceOption) (*AccountSshKey, error) {
	var resource AccountSshKey
	err := ctx.ReadResource("scaleway:index/accountSshKey:AccountSshKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccountSshKey resources.
type accountSshKeyState struct {
	// The name of the SSH key.
	Name *string `pulumi:"name"`
	// `organizationId`) The ID of the organization the IP is associated with.
	OrganizationId *string `pulumi:"organizationId"`
	// The public SSH key to be added.
	PublicKey *string `pulumi:"publicKey"`
}

type AccountSshKeyState struct {
	// The name of the SSH key.
	Name pulumi.StringPtrInput
	// `organizationId`) The ID of the organization the IP is associated with.
	OrganizationId pulumi.StringPtrInput
	// The public SSH key to be added.
	PublicKey pulumi.StringPtrInput
}

func (AccountSshKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*accountSshKeyState)(nil)).Elem()
}

type accountSshKeyArgs struct {
	// The name of the SSH key.
	Name *string `pulumi:"name"`
	// `organizationId`) The ID of the organization the IP is associated with.
	OrganizationId *string `pulumi:"organizationId"`
	// The public SSH key to be added.
	PublicKey string `pulumi:"publicKey"`
}

// The set of arguments for constructing a AccountSshKey resource.
type AccountSshKeyArgs struct {
	// The name of the SSH key.
	Name pulumi.StringPtrInput
	// `organizationId`) The ID of the organization the IP is associated with.
	OrganizationId pulumi.StringPtrInput
	// The public SSH key to be added.
	PublicKey pulumi.StringInput
}

func (AccountSshKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accountSshKeyArgs)(nil)).Elem()
}
