---
title: BCFD – CFD200 – Module 7 – Integration/Migration and Interopability
date: 2012-01-18
category: storage
tags: bcfd, bcfp, brocade, brocade, certified, fabric, designer, certification, storage, storage, area, network, storage, network
<!-- prettier-ignore -->
---

# Fabric migration planning and implementation

Why: faster, better scaling (less switches to manage), running out of ports, hardware refresh, new features.

Most of the time is spent assessing, determining strategy, development planning and site preparation. Only 20% is for deployment and validation.

**_The first page describes the order as above, but the order in the slides are different with strategies coming after the planning._**

## Assessment

Which connections are needed - which hosts and targets need to communicate. Any applications that need to be moved together. Maintenance windows. Coordinate with other groups (servers, disk arrays, OS, services, etc) Compatibility Matrix (HBA model, driver, firmware and FC OS, storage firmware) Risk

## Plan Development

Build a plan based on current and future requirements for:

- Port Count
- HA
- Power, cooling, space limitations

But also current and future technologies like: high bandwidth, server/storage virtualization and improved power/cooling efficiencies. Is the availability of the data center acceptable?

## Strategies

Most common ones:

### Replacement of existing switches

### Integration or consolidation of fabrics

Existing fabrics have new switches added. Hosts and targets are migrated to the new switches over time and eventually old switches are removed. Means new and old switches need to be compatible. Means upgrade firmwares or interopabilitiy modes. But, you can move storage first and then move hosts, you don't have to coordinate downtime for both. One fabric at a time, possibly most disruptive (DID, PID, FOS compatibility). Greater risk. Good because old/existing equipment can be used. No need to redo zoning. Means most effort and most scheduling. Hard to test architecture before implementing it. Loss of B-series features - if interopability mode or too old switches. Hard to schedule downtime for one fabric?

#### Merge Fabric Considerations

Before merging check for: Duplicate DID, incompatible fabric.ops, zoning mismatch, SCC policies.

### Dual fabrics (rip-and-replace)

Two new fabrics are created (not merged, so re-create zoning db). New hosts are moved over time. Means having devices on more fabrics (four) at the same time, especially for hosts with only two host ports this limits redundancy and possibly bandwidth reduction for targets. Might be necessary to move hosts and targets at the same time. No compatibility concerns between switches. Needs careful planning. Can test before deploying. Less planning needed. Cables moved more often. More power / cooling requirements. Changes might be required on hosts when storage moves.

### Dual fabrics and FC routing

Same as dual fabrics, but you can then use routing to interconnect devices during the transition period. Meaning you don't have to move hosts and targets at the same time.

No interopability needed, fabrics are kept isolated. During transition the devices can access eachother via IFLs. NSPOF. Works for hosts with single HBA. Reduce maintenance window? Might still need to change some hosts when storage moves. Best and with less impact. Can roll back if it doesn't work.

Use two routers for redundancy. LSAN zoning used to connect hosts between fabrics. This is also a way to migrate data off arrays.

#### Migration Steps

1. Create two new fabrics
2. Configure EX\_Ports
3. Attach routers to old and new fabrics
4. Verify connectivity
5. Create LSANs in old and new fabrics
6. Move host cables from old fabric to the new one
7. Verify connectivity
8. Repeat per fabric and for rest of storage and hosts
9. Remove routers

#### verify devices after they are moved

migrate one device at a time, after it's migrated confirm connectivity with 'nsshow, fcrproxydevshow, fcrphydevshow'. Record and track FID, PID and WWN. lsanshow -s.

# Interopability between B- and M-series SAN

M- to B-Series migration: for non-disruptive migration redundant fabrics are required. New FOS fabric should also be redundant. Postmigration you will have two SANs of identical topology. Using routers and the 'dual fabrics'.

Setting up a whole new SAN is good because you don't have to mess with interopability.

[Domain ID offset](http://community.brocade.com/docs/DOC-1639 "more details about IM") - is used in interopmode by default and makes the DID range from 1-31 or 97-127

The document above says "**Chapter 4 - Interop-Mode is Obsolete in FOS 7** Since Brocade announce and released as GA Fabric Operating System Release 7.x, Interop-Mode is not longer in use."

In the FOS 7.x admin guide it says **that the only way to mix FOS and M-EOS is via an FC Router.** Portcfgexport PORT -m "interopmode"

FOS 7.x a switch has to be in interopmode 0.

When you do routing between a B- and M-series the FD DID needs to be in the range of the M-EOS fabric (DID offset).

# Considerations when migration from 4G to 8G

Why: new features and more credits/channels/ports per ASIC. More bandwidth in the ISL ("optimum use of fabric resources"). If your SAN is high performing, you can implement services with both high and lower performance requirements.

## Put DCX in Core

Put DCX in Core and move 48k to the edge. Higher speed and denser core. 8G ISL are possible with 8G blades in the 48k, so 8G blades for ISL and keep the 4G for ports. FC10-6 could be used, but no trunking. On the 8G blades you could put hosts and storage on the same blade - local switching - means more chassi-backplane bandwidth available for other stuff.

## NPIV

Could increase need for high-speed capability in the SAN (well, better usage on a per server basis). A single server could exceed 4Gbps.

# Migrating from low port count switches to directors

structured - time phased integration manageable - interopable migration

## technology refresh

\- amount of ports - amount of rack space

Is there a single director that can accomodate all the ports? Replace existing hardware. Maybe that single director by itself is smaller (less U). No ISL, no oversubscription etc. If there are more ports, consider ICL. Nohops = nice.

## fabric expansion

you have to switches that are connected, you are running out of ports. put a DCX in the middle

# Interopability modes

Interop 0: Brocade Native. Interop 2: McData - M-EOS 9.6.2+ in **Fabric Mode** Interop 3: McData - M-EOS 9.6.2+ in **Open Fabric Mode**

0: default on brocade. Most features. Should always be set in pure Brocade environments. 2: can zone from both B- and M-series. Most FOS features. Good for adding B-switches to an M-series SAN. Cannot work with interop mode 1 (FOS 5.x). Supports FICON. 3: zoning done on M-series. Some features not available. Good for adding B-series switches. Not OK with interop 1. Only B- and M-series, nobody else.

Worry about:

- does the hardware support this
- any features unsupported
- restrictions for configuration
- upgrade/downgrade
- zone management
- moving from B- to M-series.

Basically you're not missing anything vital in interopmode, only special features. In IM3: FICON, TI Zones, Frame Redirection and SCC policies. Both miss out on: DCC policies, broadcast zoning, APM - top talkers, QoS, IRL, Alias Server, "Domain Offset"

Port and Exchange based can be mixed freely between any mode and B- or M-series.

## Zoning

IM3: only zone on WWpN. FOS zone confdigs are not supported IM2: WWpN and D,I zoning. No port number greater than 255, on any switch in the fabric, neither in fabric or in CLI/WebTOols. Safe Zoning must be disabled after joining.

FOS switches have 3 zoning databases:

**transaction** -  work area (cfgtransabort to abort)

**defined** - saved (cfgsave). Does not push to other switches.

**effective** - enabled (cfgenable). Does not push defined config.

There are limitations when in the IM modes:

FOS 6.1.x and higher -> IM2/3: 2048 devices and 31 DIDs
