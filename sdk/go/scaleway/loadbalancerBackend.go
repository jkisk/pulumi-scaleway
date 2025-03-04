// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package scaleway

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type LoadbalancerBackend struct {
	pulumi.CustomResourceState

	// User sessions will be forwarded to this port of backend servers
	ForwardPort pulumi.IntOutput `pulumi:"forwardPort"`
	// Load balancing algorithm
	ForwardPortAlgorithm pulumi.StringPtrOutput `pulumi:"forwardPortAlgorithm"`
	// Backend protocol
	ForwardProtocol pulumi.StringOutput `pulumi:"forwardProtocol"`
	// Interval between two HC requests
	HealthCheckDelay pulumi.StringPtrOutput                       `pulumi:"healthCheckDelay"`
	HealthCheckHttp  LoadbalancerBackendHealthCheckHttpPtrOutput  `pulumi:"healthCheckHttp"`
	HealthCheckHttps LoadbalancerBackendHealthCheckHttpsPtrOutput `pulumi:"healthCheckHttps"`
	// Number of allowed failed HC requests before the backend server is marked down
	HealthCheckMaxRetries pulumi.IntPtrOutput `pulumi:"healthCheckMaxRetries"`
	// Port the HC requests will be send to. Default to `forward_port`
	HealthCheckPort pulumi.IntOutput                        `pulumi:"healthCheckPort"`
	HealthCheckTcp  LoadbalancerBackendHealthCheckTcpOutput `pulumi:"healthCheckTcp"`
	// Timeout before we consider a HC request failed
	HealthCheckTimeout pulumi.StringPtrOutput `pulumi:"healthCheckTimeout"`
	// The load-balancer ID
	LbId pulumi.StringOutput `pulumi:"lbId"`
	// The name of the backend
	Name pulumi.StringOutput `pulumi:"name"`
	// Modify what occurs when a backend server is marked down
	OnMarkedDownAction pulumi.StringPtrOutput `pulumi:"onMarkedDownAction"`
	// Type of PROXY protocol to enable
	ProxyProtocol pulumi.StringPtrOutput `pulumi:"proxyProtocol"`
	// Enables PROXY protocol version 2
	//
	// Deprecated: Please use proxy_protocol instead
	SendProxyV2 pulumi.BoolPtrOutput `pulumi:"sendProxyV2"`
	// Backend server IP addresses list (IPv4 or IPv6)
	ServerIps pulumi.StringArrayOutput `pulumi:"serverIps"`
	// Load balancing algorithm
	StickySessions pulumi.StringPtrOutput `pulumi:"stickySessions"`
	// Cookie name for for sticky sessions
	StickySessionsCookieName pulumi.StringPtrOutput `pulumi:"stickySessionsCookieName"`
	// Maximum initial server connection establishment time
	TimeoutConnect pulumi.StringPtrOutput `pulumi:"timeoutConnect"`
	// Maximum server connection inactivity time
	TimeoutServer pulumi.StringPtrOutput `pulumi:"timeoutServer"`
	// Maximum tunnel inactivity time
	TimeoutTunnel pulumi.StringPtrOutput `pulumi:"timeoutTunnel"`
}

// NewLoadbalancerBackend registers a new resource with the given unique name, arguments, and options.
func NewLoadbalancerBackend(ctx *pulumi.Context,
	name string, args *LoadbalancerBackendArgs, opts ...pulumi.ResourceOption) (*LoadbalancerBackend, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ForwardPort == nil {
		return nil, errors.New("invalid value for required argument 'ForwardPort'")
	}
	if args.ForwardProtocol == nil {
		return nil, errors.New("invalid value for required argument 'ForwardProtocol'")
	}
	if args.LbId == nil {
		return nil, errors.New("invalid value for required argument 'LbId'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource LoadbalancerBackend
	err := ctx.RegisterResource("scaleway:index/loadbalancerBackend:LoadbalancerBackend", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLoadbalancerBackend gets an existing LoadbalancerBackend resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoadbalancerBackend(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LoadbalancerBackendState, opts ...pulumi.ResourceOption) (*LoadbalancerBackend, error) {
	var resource LoadbalancerBackend
	err := ctx.ReadResource("scaleway:index/loadbalancerBackend:LoadbalancerBackend", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LoadbalancerBackend resources.
type loadbalancerBackendState struct {
	// User sessions will be forwarded to this port of backend servers
	ForwardPort *int `pulumi:"forwardPort"`
	// Load balancing algorithm
	ForwardPortAlgorithm *string `pulumi:"forwardPortAlgorithm"`
	// Backend protocol
	ForwardProtocol *string `pulumi:"forwardProtocol"`
	// Interval between two HC requests
	HealthCheckDelay *string                              `pulumi:"healthCheckDelay"`
	HealthCheckHttp  *LoadbalancerBackendHealthCheckHttp  `pulumi:"healthCheckHttp"`
	HealthCheckHttps *LoadbalancerBackendHealthCheckHttps `pulumi:"healthCheckHttps"`
	// Number of allowed failed HC requests before the backend server is marked down
	HealthCheckMaxRetries *int `pulumi:"healthCheckMaxRetries"`
	// Port the HC requests will be send to. Default to `forward_port`
	HealthCheckPort *int                               `pulumi:"healthCheckPort"`
	HealthCheckTcp  *LoadbalancerBackendHealthCheckTcp `pulumi:"healthCheckTcp"`
	// Timeout before we consider a HC request failed
	HealthCheckTimeout *string `pulumi:"healthCheckTimeout"`
	// The load-balancer ID
	LbId *string `pulumi:"lbId"`
	// The name of the backend
	Name *string `pulumi:"name"`
	// Modify what occurs when a backend server is marked down
	OnMarkedDownAction *string `pulumi:"onMarkedDownAction"`
	// Type of PROXY protocol to enable
	ProxyProtocol *string `pulumi:"proxyProtocol"`
	// Enables PROXY protocol version 2
	//
	// Deprecated: Please use proxy_protocol instead
	SendProxyV2 *bool `pulumi:"sendProxyV2"`
	// Backend server IP addresses list (IPv4 or IPv6)
	ServerIps []string `pulumi:"serverIps"`
	// Load balancing algorithm
	StickySessions *string `pulumi:"stickySessions"`
	// Cookie name for for sticky sessions
	StickySessionsCookieName *string `pulumi:"stickySessionsCookieName"`
	// Maximum initial server connection establishment time
	TimeoutConnect *string `pulumi:"timeoutConnect"`
	// Maximum server connection inactivity time
	TimeoutServer *string `pulumi:"timeoutServer"`
	// Maximum tunnel inactivity time
	TimeoutTunnel *string `pulumi:"timeoutTunnel"`
}

type LoadbalancerBackendState struct {
	// User sessions will be forwarded to this port of backend servers
	ForwardPort pulumi.IntPtrInput
	// Load balancing algorithm
	ForwardPortAlgorithm pulumi.StringPtrInput
	// Backend protocol
	ForwardProtocol pulumi.StringPtrInput
	// Interval between two HC requests
	HealthCheckDelay pulumi.StringPtrInput
	HealthCheckHttp  LoadbalancerBackendHealthCheckHttpPtrInput
	HealthCheckHttps LoadbalancerBackendHealthCheckHttpsPtrInput
	// Number of allowed failed HC requests before the backend server is marked down
	HealthCheckMaxRetries pulumi.IntPtrInput
	// Port the HC requests will be send to. Default to `forward_port`
	HealthCheckPort pulumi.IntPtrInput
	HealthCheckTcp  LoadbalancerBackendHealthCheckTcpPtrInput
	// Timeout before we consider a HC request failed
	HealthCheckTimeout pulumi.StringPtrInput
	// The load-balancer ID
	LbId pulumi.StringPtrInput
	// The name of the backend
	Name pulumi.StringPtrInput
	// Modify what occurs when a backend server is marked down
	OnMarkedDownAction pulumi.StringPtrInput
	// Type of PROXY protocol to enable
	ProxyProtocol pulumi.StringPtrInput
	// Enables PROXY protocol version 2
	//
	// Deprecated: Please use proxy_protocol instead
	SendProxyV2 pulumi.BoolPtrInput
	// Backend server IP addresses list (IPv4 or IPv6)
	ServerIps pulumi.StringArrayInput
	// Load balancing algorithm
	StickySessions pulumi.StringPtrInput
	// Cookie name for for sticky sessions
	StickySessionsCookieName pulumi.StringPtrInput
	// Maximum initial server connection establishment time
	TimeoutConnect pulumi.StringPtrInput
	// Maximum server connection inactivity time
	TimeoutServer pulumi.StringPtrInput
	// Maximum tunnel inactivity time
	TimeoutTunnel pulumi.StringPtrInput
}

func (LoadbalancerBackendState) ElementType() reflect.Type {
	return reflect.TypeOf((*loadbalancerBackendState)(nil)).Elem()
}

type loadbalancerBackendArgs struct {
	// User sessions will be forwarded to this port of backend servers
	ForwardPort int `pulumi:"forwardPort"`
	// Load balancing algorithm
	ForwardPortAlgorithm *string `pulumi:"forwardPortAlgorithm"`
	// Backend protocol
	ForwardProtocol string `pulumi:"forwardProtocol"`
	// Interval between two HC requests
	HealthCheckDelay *string                              `pulumi:"healthCheckDelay"`
	HealthCheckHttp  *LoadbalancerBackendHealthCheckHttp  `pulumi:"healthCheckHttp"`
	HealthCheckHttps *LoadbalancerBackendHealthCheckHttps `pulumi:"healthCheckHttps"`
	// Number of allowed failed HC requests before the backend server is marked down
	HealthCheckMaxRetries *int `pulumi:"healthCheckMaxRetries"`
	// Port the HC requests will be send to. Default to `forward_port`
	HealthCheckPort *int                               `pulumi:"healthCheckPort"`
	HealthCheckTcp  *LoadbalancerBackendHealthCheckTcp `pulumi:"healthCheckTcp"`
	// Timeout before we consider a HC request failed
	HealthCheckTimeout *string `pulumi:"healthCheckTimeout"`
	// The load-balancer ID
	LbId string `pulumi:"lbId"`
	// The name of the backend
	Name *string `pulumi:"name"`
	// Modify what occurs when a backend server is marked down
	OnMarkedDownAction *string `pulumi:"onMarkedDownAction"`
	// Type of PROXY protocol to enable
	ProxyProtocol *string `pulumi:"proxyProtocol"`
	// Enables PROXY protocol version 2
	//
	// Deprecated: Please use proxy_protocol instead
	SendProxyV2 *bool `pulumi:"sendProxyV2"`
	// Backend server IP addresses list (IPv4 or IPv6)
	ServerIps []string `pulumi:"serverIps"`
	// Load balancing algorithm
	StickySessions *string `pulumi:"stickySessions"`
	// Cookie name for for sticky sessions
	StickySessionsCookieName *string `pulumi:"stickySessionsCookieName"`
	// Maximum initial server connection establishment time
	TimeoutConnect *string `pulumi:"timeoutConnect"`
	// Maximum server connection inactivity time
	TimeoutServer *string `pulumi:"timeoutServer"`
	// Maximum tunnel inactivity time
	TimeoutTunnel *string `pulumi:"timeoutTunnel"`
}

// The set of arguments for constructing a LoadbalancerBackend resource.
type LoadbalancerBackendArgs struct {
	// User sessions will be forwarded to this port of backend servers
	ForwardPort pulumi.IntInput
	// Load balancing algorithm
	ForwardPortAlgorithm pulumi.StringPtrInput
	// Backend protocol
	ForwardProtocol pulumi.StringInput
	// Interval between two HC requests
	HealthCheckDelay pulumi.StringPtrInput
	HealthCheckHttp  LoadbalancerBackendHealthCheckHttpPtrInput
	HealthCheckHttps LoadbalancerBackendHealthCheckHttpsPtrInput
	// Number of allowed failed HC requests before the backend server is marked down
	HealthCheckMaxRetries pulumi.IntPtrInput
	// Port the HC requests will be send to. Default to `forward_port`
	HealthCheckPort pulumi.IntPtrInput
	HealthCheckTcp  LoadbalancerBackendHealthCheckTcpPtrInput
	// Timeout before we consider a HC request failed
	HealthCheckTimeout pulumi.StringPtrInput
	// The load-balancer ID
	LbId pulumi.StringInput
	// The name of the backend
	Name pulumi.StringPtrInput
	// Modify what occurs when a backend server is marked down
	OnMarkedDownAction pulumi.StringPtrInput
	// Type of PROXY protocol to enable
	ProxyProtocol pulumi.StringPtrInput
	// Enables PROXY protocol version 2
	//
	// Deprecated: Please use proxy_protocol instead
	SendProxyV2 pulumi.BoolPtrInput
	// Backend server IP addresses list (IPv4 or IPv6)
	ServerIps pulumi.StringArrayInput
	// Load balancing algorithm
	StickySessions pulumi.StringPtrInput
	// Cookie name for for sticky sessions
	StickySessionsCookieName pulumi.StringPtrInput
	// Maximum initial server connection establishment time
	TimeoutConnect pulumi.StringPtrInput
	// Maximum server connection inactivity time
	TimeoutServer pulumi.StringPtrInput
	// Maximum tunnel inactivity time
	TimeoutTunnel pulumi.StringPtrInput
}

func (LoadbalancerBackendArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*loadbalancerBackendArgs)(nil)).Elem()
}

type LoadbalancerBackendInput interface {
	pulumi.Input

	ToLoadbalancerBackendOutput() LoadbalancerBackendOutput
	ToLoadbalancerBackendOutputWithContext(ctx context.Context) LoadbalancerBackendOutput
}

func (*LoadbalancerBackend) ElementType() reflect.Type {
	return reflect.TypeOf((**LoadbalancerBackend)(nil)).Elem()
}

func (i *LoadbalancerBackend) ToLoadbalancerBackendOutput() LoadbalancerBackendOutput {
	return i.ToLoadbalancerBackendOutputWithContext(context.Background())
}

func (i *LoadbalancerBackend) ToLoadbalancerBackendOutputWithContext(ctx context.Context) LoadbalancerBackendOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LoadbalancerBackendOutput)
}

type LoadbalancerBackendOutput struct{ *pulumi.OutputState }

func (LoadbalancerBackendOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LoadbalancerBackend)(nil)).Elem()
}

func (o LoadbalancerBackendOutput) ToLoadbalancerBackendOutput() LoadbalancerBackendOutput {
	return o
}

func (o LoadbalancerBackendOutput) ToLoadbalancerBackendOutputWithContext(ctx context.Context) LoadbalancerBackendOutput {
	return o
}

// User sessions will be forwarded to this port of backend servers
func (o LoadbalancerBackendOutput) ForwardPort() pulumi.IntOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.IntOutput { return v.ForwardPort }).(pulumi.IntOutput)
}

// Load balancing algorithm
func (o LoadbalancerBackendOutput) ForwardPortAlgorithm() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.ForwardPortAlgorithm }).(pulumi.StringPtrOutput)
}

// Backend protocol
func (o LoadbalancerBackendOutput) ForwardProtocol() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringOutput { return v.ForwardProtocol }).(pulumi.StringOutput)
}

// Interval between two HC requests
func (o LoadbalancerBackendOutput) HealthCheckDelay() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.HealthCheckDelay }).(pulumi.StringPtrOutput)
}

func (o LoadbalancerBackendOutput) HealthCheckHttp() LoadbalancerBackendHealthCheckHttpPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) LoadbalancerBackendHealthCheckHttpPtrOutput { return v.HealthCheckHttp }).(LoadbalancerBackendHealthCheckHttpPtrOutput)
}

func (o LoadbalancerBackendOutput) HealthCheckHttps() LoadbalancerBackendHealthCheckHttpsPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) LoadbalancerBackendHealthCheckHttpsPtrOutput { return v.HealthCheckHttps }).(LoadbalancerBackendHealthCheckHttpsPtrOutput)
}

// Number of allowed failed HC requests before the backend server is marked down
func (o LoadbalancerBackendOutput) HealthCheckMaxRetries() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.IntPtrOutput { return v.HealthCheckMaxRetries }).(pulumi.IntPtrOutput)
}

// Port the HC requests will be send to. Default to `forward_port`
func (o LoadbalancerBackendOutput) HealthCheckPort() pulumi.IntOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.IntOutput { return v.HealthCheckPort }).(pulumi.IntOutput)
}

func (o LoadbalancerBackendOutput) HealthCheckTcp() LoadbalancerBackendHealthCheckTcpOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) LoadbalancerBackendHealthCheckTcpOutput { return v.HealthCheckTcp }).(LoadbalancerBackendHealthCheckTcpOutput)
}

// Timeout before we consider a HC request failed
func (o LoadbalancerBackendOutput) HealthCheckTimeout() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.HealthCheckTimeout }).(pulumi.StringPtrOutput)
}

// The load-balancer ID
func (o LoadbalancerBackendOutput) LbId() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringOutput { return v.LbId }).(pulumi.StringOutput)
}

// The name of the backend
func (o LoadbalancerBackendOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Modify what occurs when a backend server is marked down
func (o LoadbalancerBackendOutput) OnMarkedDownAction() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.OnMarkedDownAction }).(pulumi.StringPtrOutput)
}

// Type of PROXY protocol to enable
func (o LoadbalancerBackendOutput) ProxyProtocol() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.ProxyProtocol }).(pulumi.StringPtrOutput)
}

// Enables PROXY protocol version 2
//
// Deprecated: Please use proxy_protocol instead
func (o LoadbalancerBackendOutput) SendProxyV2() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.BoolPtrOutput { return v.SendProxyV2 }).(pulumi.BoolPtrOutput)
}

// Backend server IP addresses list (IPv4 or IPv6)
func (o LoadbalancerBackendOutput) ServerIps() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringArrayOutput { return v.ServerIps }).(pulumi.StringArrayOutput)
}

// Load balancing algorithm
func (o LoadbalancerBackendOutput) StickySessions() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.StickySessions }).(pulumi.StringPtrOutput)
}

// Cookie name for for sticky sessions
func (o LoadbalancerBackendOutput) StickySessionsCookieName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.StickySessionsCookieName }).(pulumi.StringPtrOutput)
}

// Maximum initial server connection establishment time
func (o LoadbalancerBackendOutput) TimeoutConnect() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.TimeoutConnect }).(pulumi.StringPtrOutput)
}

// Maximum server connection inactivity time
func (o LoadbalancerBackendOutput) TimeoutServer() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.TimeoutServer }).(pulumi.StringPtrOutput)
}

// Maximum tunnel inactivity time
func (o LoadbalancerBackendOutput) TimeoutTunnel() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LoadbalancerBackend) pulumi.StringPtrOutput { return v.TimeoutTunnel }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LoadbalancerBackendInput)(nil)).Elem(), &LoadbalancerBackend{})
	pulumi.RegisterOutputType(LoadbalancerBackendOutput{})
}
