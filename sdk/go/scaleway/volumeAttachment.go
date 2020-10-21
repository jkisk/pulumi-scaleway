// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// **DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
// Please use `scaleway_instance_server.additional_volumes` instead.
//
// This allows volumes to be attached to servers.
//
// > **Warning:** Attaching volumes requires the servers to be powered off. This will lead to downtime if the server is already in use.
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
// 		testServer, err := scaleway.NewServer(ctx, "testServer", &scaleway.ServerArgs{
// 			Image: pulumi.String("aecaed73-51a5-4439-a127-6d8229847145"),
// 			Type:  pulumi.String("C2S"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testVolume, err := scaleway.NewVolume(ctx, "testVolume", &scaleway.VolumeArgs{
// 			SizeInGb: pulumi.Int(20),
// 			Type:     pulumi.String("l_ssd"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = scaleway.NewVolumeAttachment(ctx, "testVolumeAttachment", &scaleway.VolumeAttachmentArgs{
// 			Server: testServer.ID(),
// 			Volume: testVolume.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type VolumeAttachment struct {
	pulumi.CustomResourceState

	// id of the server
	Server pulumi.StringOutput `pulumi:"server"`
	// id of the volume to be attached
	Volume pulumi.StringOutput `pulumi:"volume"`
}

// NewVolumeAttachment registers a new resource with the given unique name, arguments, and options.
func NewVolumeAttachment(ctx *pulumi.Context,
	name string, args *VolumeAttachmentArgs, opts ...pulumi.ResourceOption) (*VolumeAttachment, error) {
	if args == nil || args.Server == nil {
		return nil, errors.New("missing required argument 'Server'")
	}
	if args == nil || args.Volume == nil {
		return nil, errors.New("missing required argument 'Volume'")
	}
	if args == nil {
		args = &VolumeAttachmentArgs{}
	}
	var resource VolumeAttachment
	err := ctx.RegisterResource("scaleway:index/volumeAttachment:VolumeAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVolumeAttachment gets an existing VolumeAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolumeAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VolumeAttachmentState, opts ...pulumi.ResourceOption) (*VolumeAttachment, error) {
	var resource VolumeAttachment
	err := ctx.ReadResource("scaleway:index/volumeAttachment:VolumeAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VolumeAttachment resources.
type volumeAttachmentState struct {
	// id of the server
	Server *string `pulumi:"server"`
	// id of the volume to be attached
	Volume *string `pulumi:"volume"`
}

type VolumeAttachmentState struct {
	// id of the server
	Server pulumi.StringPtrInput
	// id of the volume to be attached
	Volume pulumi.StringPtrInput
}

func (VolumeAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeAttachmentState)(nil)).Elem()
}

type volumeAttachmentArgs struct {
	// id of the server
	Server string `pulumi:"server"`
	// id of the volume to be attached
	Volume string `pulumi:"volume"`
}

// The set of arguments for constructing a VolumeAttachment resource.
type VolumeAttachmentArgs struct {
	// id of the server
	Server pulumi.StringInput
	// id of the volume to be attached
	Volume pulumi.StringInput
}

func (VolumeAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeAttachmentArgs)(nil)).Elem()
}
