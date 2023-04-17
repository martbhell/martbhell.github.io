---
title: BCFD - CFD200 - Module 4 - SAN Software Features
date: 2012-01-15
category: storage
tags: bcfd, bcfp, brocade, brocade, certified, fabric, designer, certification, storage, storage, area, network, storage, network

[Overview](https://www.guldmyr.com/brocade-certification-bcfd-fabric-designer-preparation/ "overview") / Preparation

[Module 3](./bcfd-cfd200-module-3-san-infrastructure "module 3") / SAN Infrastructure

The idea for this is for me to write down the things I read about in the modules. As a way for me to learn what they're about and think about them other than just reading them and forgetting them. If I write it down here I need to try to explain it so that somebody else can understand it. But I also try to do it in a condense way and only write down what I feel is important, this is by no means intended to be used instead of the material.

Module 4 is about software features.

Discuss considerations for implementing:

## Fabric Routing

FSPF - fabric shortest path first, minimum cost paths, routing policies

Exchange (SID\_DID\_OXID), also called DPS. Requires DLS to be enabled. Choses a route for each exchange.

Port Based. Routes are allocated via round-robin. Each route is used until there is a fabric change /device offline.

**DLS:** If you have for example a 4G and an 8G link to the same switch the 8G will get more traffic with DLS enabled.

Over 4G Exchange Based is default. 1-2G only port-based. Different policy per switch. Some thing may require port-based. Document says port based is needed for HP EVA and HP CA for EVA, but this is not true anymore, CV 9.4 and XCS 09534000 works with exchange based.

But FICON requires it. See the [FICON Administrator's Guide](http://www.brocade.com/downloads/documents/product_manuals/B_SAN/FICON_AdminGd_v700.pdf "for 7.0.0 on brocade.com") for details. _"In all switches and directors that have FICON devices attached, or where FICON traffic will be carried, the port-based routing policy is required (set aptPolicy option 1). Exchange based routing (set aptPolicy option 3) is only supported when Lossless is specified. It is recommended that you enable Lossless, regardless of the routing policy"_

## Trunking

Combine two or more ISLs into a single logical link: reduce congestion and increase fault-tolerance. Requires a license. Same speed, port group, have trunking enabled, they form automatically, deskew cannot be too large. The port groups vary depending on the ASIC. 2-8 ISLs (2-4 for GoldenEye).

GoldenEye2: B200 Condor3: 16G

### Port Groups

Condor (4G): 0-7, 8-15, Condor2(8G): 0-7, 8-15, Condor3: 0-15, 16-31, 32-47, 48-64 (or 0-23, 24-47) GoldenEye (4G): 0-3, 4-7, 8-11, 12-15, GoldenEye2 (8G): 0-7, 8-15,

Grow existing trunk groups. Keep free ports in port groups (in case you need to add more ISLs). Consider splitting trunk between port blades.

The M-Series is called Open-Trunking

## Zoning

1 x Target 1 x Initiator per zone

Do some planning, which devices need to be connected? For example don't zone in a tape drive / library with devices that won't use them. Use alias/zone names that  help you.

1 x Inititator and Many x Targets can cause longer boot times.

A diagram might help. nszonemember, fcping, webtools, dcfm, san health. Configupload/download.

 

## Adaptive Networking

Optimization.

### TI - dedicate ISLs for specific hosts/targets

License needed for FOS <=6.

Via zoning. Done via a set of N\_ and E\_Ports. Attempts to exclude traffic not in the TI zone from using the E\_ports in that TI Zone. 4 and 8G. Doesn't alter FSPF rules. Dedicate an ISL to high prio traffic Force high-volume traffic into a path, so it doesn't affect other services. Ensure FCIP tape pipelining uses the same VE\_Port tunnel across fabrics. Dedicate bandwidth for replication.

### Ingress Rate Limiting - restrict speed from a device to the port

ASIC delays return of BB credits to device. Limits traffic from a device.

Requires license, only on 8G F\_ or FL\_ports. Avoid congestion (proactively and to remedy). Is enabled even if congestion occurs or not.

If you have another device that is slow at returning credits, then you can set IRL on the ports on one a device that communicate with this slow-drain device.

To enforce SLA:s.

### QoS (SID/DID) Prio - between host and target

Default = medium. Done via zoning. Condor2 or GE2 ASICs. License required. Brocade proprietary? FOS 6.0.0 or higher. Zones for QoS do both access and QoS.

30 (medium) / 10 (low) / 60 (high) %

If you want to make sure a certain application is always prioritized. Only in effect if there is need. If not all high priority VC are in use then medium priority traffic will use those.

### Top Talkers - determine highest flows

APM license required. FOS 6.0.x. Determine which SID/DID pair are major users of F\_Port bandwidth. Only on specific E\_ or F\_Ports. Condor, Condor2, GE2. Not on ports in AG.

Find which VM uses most bandwidth? Find flows that you can enable QoS, TI, etc, on.

## NPIV

virtual wwn zone to individual vm instead of to the host there are some restrictions to the amount of NPIVs per port / switch. Max is 255, 127 on FC\*-48 blades.

## AG

Doesn't use a DID. Focus is on connectivity, not bandwidth. No license. Can be used to connect switches of other vendors without changing the switch  interop mode? Or does it mean a Brocade switch in AG can be joined to another fabric, can other vendors do the same? Has as default port map, this can be altered. It maps which F\_port to which N\_port (which host to which "isl"). Each connection from an AG to a fabric can handle 255 devices. F\_Port trunking: Device PIDs do not change if a link fails in an F\_Port trunk. Similar requirements as a normal E\_port trunk.

## Port Fencing

Disable a port if it operates outside "normal operation". Uses Fabric Watch = requires license. Only through CLI. User intervention required to enable it. FW classes: Port, E\_, F\_ and FL\_. FW areas: link / sync loss, protocol error, invalid words/CRC.

'Only the FW "above" event will be monitored for Port Fencing'.

## Security

passwords (expire, history, strength, etc) authentication (radius/LDAP) - aaa, default accounts (root, factory, admin, user) roles (RBAC) - no need to set admin role on an account used for monitoring for example SCP (use instead of ftp) ACLs (which devices can join a fabric) ipfilters (deny telnet)

## Ficon

i/o protocol based on FC used with IBM mainframe/storage. FC layer 4 Successor of ESCON From late 90s.

Starting FICON Config Utility for a single fabric: (Fabric Manager, old displays, is worth to check how it's done now in new guides). Worth checking out the FICON Admin Guide anyway.

- Turns on insistent DID
- enabled port based routing
- disables DLS, enables IOD
- sets HIFS (high integrity fabric config) on seed/principal switch
    - Cascaded FICON?
- enable SCC policy in strict mode
- enable FMS (FICON Management Server) mode on switches.
- checks if there is a CUP license
- more in newer versions of DCFM/BNA?
