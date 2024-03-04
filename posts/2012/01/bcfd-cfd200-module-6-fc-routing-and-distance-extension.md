---
title: BCFD – CFD200 – Module 6 – FC Routing and Distance Extension
date: 2012-01-17
category: storage
tags: bandwidth, bcfd, bcfp, brocade, brocade, certified, fabric, designer, buffers, certification, design, dwdm, fcip, fiber, latency, long, distance, mtu, packet, loss, routing, sfp, storage, storage, area, network, storage, network
<!-- prettier-ignore -->

Second Last module! But that's not the end of it, there are more admin guides, best practices to wade through :) This one is a bit more complicated though, a lot to think about when designing FCR and FCIP SAN networks.

# FC Routing

This is when you have SAN islands (isolated networks), but then after some time you find that you still have to share resources between the islands.

If you cannot merge (zoning db too big). SANs with different fabric.ops, different PIDs or overlapping DIDs. If they want to share devices for backups/dr. Autonomous SAN admin teams. Migrating data between fabrics.

To start routing you need: Physical Connection: FC Fabrics (`EX_Ports`) Logical Connection: LSAN Zones between devices. Zone in each autonomous fabric.

Greater resource utilization, scalability and long-distance extension.

Not as risky as merging fabrics. Interconnect heterogeneous SANs in different interop modes.

"Extended SAN". FCR is not a replacement for running dual fabrics, each edge fabric still need to be redundant by itself.

Oversubscription: Do check the bandwidth by the devices that will use the IFL and the size of the IFL(s).

## Availability

Same idea as in the previous module about the different availabilities:

Single BB, single FCR router: Not HA Single Extended SAN, multiple FCR routers: Not HA, because one fabric Two Extended SANs, each has a single FCR router: Highly Available. Two Extended SANs, multiple FCR: HA

Single BB (one physical router) and multiple edge fabrics. (OK for sharing, not redundant). Dual BB (two routers) and one or more edge fabrics. (gives redundancy, more bandwidth, is a core/edge style, scales well) "two routers" above is two hw routers, like 7500, or two IR enabled ports in two different blades/chassis.

## FID, FD and XD

Each edge and backbone get a unique Fabric ID. (max 128) `EX_Ports` are in the backbone (on the router or an Integrated Routing Port). On the edge fabric this is just an `E_port`. On each `EX_Port` there is an Front Domain. This domain is the link. When a device is exported (when it's online and zoned) an XD (translate domain) will appear on the `EX_Port` and that is where the device is. One XD for each edge fabric that exports devices.

Page 11 and 12 in the FC Routing part of this module has a good picture

## Implementation

Figure out meaningful names and assign FIDs (unique range for BB and a unique range for edge) Same with domain ids. Connect several IFL between FCR and edge fabric, trunking is nice and works the same here as without routing. Use single initiator zoning.

## Platforms

FR4-18i - bladed 7500 - Supported in DCX 8510 16G? Both give 2 x 1GbE for FCIP and up to 8 FCIP tunnels/port. 7500E - cheap one, two FC ports, limited to 50Mbps/GbE port. Can be upgraded. All ports on B5100, 5300 and any FC8-xx blades in DCX can be configured as `EX_Ports` == integrated routing. FOS 6.1. License required. Advice is to not have any backbone devices when using IR. Problematic when enabling. **Condor2/GE2 performs better than FR4-18i.** However, the FR4-18i does FCIP. There are other/lots of limitations:

- FR4-18i `EX_Port` and IR `EX_Port` - not in the same DCX, OK in same fabric though.
- FR4-18i `VEX_Port` and IR `EX_Port` - OK in the same DCX
- IR ports can be connected to FR4-18i in another fabric.
- Replacing FR4-18i with FC8-xx retains `EX_Port` config for the first 16 ports..

## Distance

Trunking works. If you're sharing devices with a smaller SAN, smaller switches on the smaller site will suffice.

## Consider

**Again, this is on FOS 6.3 and 8G platforms.**

No McData Max 128 `EX_Ports` SCC policy must include FD, but do not include XD) TI is OK after FOS 6.1.0. TI within Edge routes between real and proxy to an `EX_Port`. TI within BB lock down a route within BB based on `EX_Ports` and devices. Devices must also be in LSAN zones to enforce TI. Without TI, any traffic can use any ISL according to FSPF and exchange based routing. With TI, only TI zoned traffic uses the isolated route and all non-TI zoned traffic uses the rest of the routes.

# FCIP

interconnect FC switches over IP.

Merging: `VE_Port`. Does not support trunking, but they do support Exchange Based Routing.

7500 and FR4-18i SACK - 'selective acknowledgement'?

## Why FCIP?

need to connect sites that are longer than FC can handle. cheaper than FC no fibres available backup, consolidation, mirroring or dr routing (connect islands) FICON over long distance

Why not: performance, reliability (TCP/IP underlying protocol, not FC). Delays/packet loss, more complicated to troubleshoot.

## Performance

Use 'portcmd --ipperf' to check out Effective Bandwidth, Delay, Packet Loss. Also work with the WAN/Telco.

## Tools to improve performance

SACK, compression, jumbo frames, fastwrite and tape pipeline. FC frames max is 2148 bytes, larger than default Ethernet 1518 .

Fastwrite - improve synchronous SCSI writes over FCIP. When an initiator sends a SCSI write, the gateway sends an `XFR_RDY` immediately back to the initiator and then buffers. It always sends back `FCP_RSP` from target to initiator so the exchange is completed.

Tape Pipelining - improves sequential SCSI writes over FCIP to tapes. Auto-responds to each SCSI write with an `XFR_RDY`. Also auto-responds to the last data frame in each SCSI write request with an `FCP_RSP`. This means the initiator thinks that is complete and will continue to the next.

With fastwrite and/or tape pipelining you can only have one FCIP tunnel between switches or FDs. Not sharing buffers.

## Design Concepts

Connect a tunnel from each GbE port to each edge fabric - higher availability? Higher bandwidth?

No mix of VEX and VE per GbE Port. In the same tunnel group you can only route or merge.

If you have EX <> E and VEX <> E connections to the same fabric, only the EX <> E will show up, lower metric/link cost.

## Topologies

`VE_` - `VE_` (merge) `VEX_` - `VE_` (routing) `EX_` - `E_` (routing)

`E_Switch1` `<FC>` `EX_Router1` `VE_Router1` `<FCIP>` `VE_router2` `EX_Router2` `<FC>` `E_Switch2`

Red = Backbone Fabric Blue = Edge Fabrics

With this, any device can be shared with any device in any fabric.

---

`E_Switch3` `<FC>` `EX_Router3` `VEX_Router3` <> `VE_Router4` `E_Router4` `<FC>` `E_Switch4`

You can also make it like below, and you would have the same functionality, except that the router is in the same fabric as the  switches.

`E_Switch3` `<FC>` `E_Router3` `VEX_Router3` <> `VE_Router4` `E_Router4` `<FC>` `E_Switch4`

## nonos

1) make up your mind EX -> E and E -> E between two fabrics.

2) which is the edge/backbone? `EX_SW1` -> `E_SW2` `E_SW1` -> `EX_SW2`

3) a switch cannot be both edge and backbone `E_SW1` -> `EX_R1` `E_R1` -> `EX_R2`

You cannot share devices over more than one backbone fabric.

## Long Distance Connectivity Options

### Dark Fiber

fibre optic that is not used. Long Wavelength SFPs. Allocate extra buffers to the ports. **WDM - Transponder- or SFP-based**

several links on the same fibre optic (at different wave lengths). DWDM - full of win and expensive. CWDM - slower, shorter, less channels - lower cost.

Transponder based : 850nm or 1310nm. Using Optical-to-Electrical-to-Optical (OE-O). SFP based: uses switch equipment that has special WDM transcveivers (colored optics). Cheaper. CWDM SFPs are like a standard SFP in a FC switch, except they transmit on a particular CWDM frequency.

### TDM

Time Division Multiplexing takes many client-side data channels and map them onto a single higher-bit-rate channel for transmission on one wavelength. May requires special config on switches (IDLE primitives, `R_RDY` flow control)

### FC-SONET/SDH

Synchronous Optical Network and Synch. Digital Hierarchy. Often used across metropolitan networks. FC are mapped onto a SONET or SDH payload. Also special config.

**"Extended Distance Solutions"** Some  of these can participate in buffer-to-buffer flow control. Participate in `E_Port` initialization with an `FC_Switch` or "snoop" and that way get the **receive-buffer field** in the ELP. For these `R_RDY` needs to be enabled (`VC_RDY` is brocade proprietary?). The `R_RDY` are returned from the device to the switch in order to maintain performance over very long distances. Flow control and error correction between these extension solutions are not handled by the FC switches.

Consider bandwidth, delay/latency,packet loss (congestion), MTU sizes, etc.

Packet loss = congestion. When a router discards packets because it cannot store or pass them on.
