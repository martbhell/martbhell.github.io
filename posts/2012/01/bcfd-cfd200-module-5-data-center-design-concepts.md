---
title: "BCFD – CFD200 – Module 5 – Data Center Design Concepts"
date: 2012-01-16
category: storage
tags: bcfd, bcfp, brocade, brocade, certified, fabric, designer, certification, storage, storage, area, network, storage, network

**Objectives:** Discuss general considerations such as attachment, availability, performance and scalability. But also solutions for needs: replication, tape backup, application and databases.

This module is quite long.

# Topologies and Topology Considerations

## Single Switch

Simplest: one switch. HA: use two. Pro: 0 hops. Con: no redundancy. Starting point. Management becomes difficult if you keep each switch isolated when the fabric expands.

What are the long-term management costs associated with more than one switch in a small SAN?

## Cascaded

Serial connection. Pro: Low port count for ISLs. Con: low perf/avail/scal. Good when most/all traffic is local.

## Ring

Better perf and avail than Cascade but scalability is not so great. ISLs are however still oversubscribed. Local traffic or suffer poor performance for non-local traffic.

## Full Mesh

All switches connect to all. Pro: great reliability and max one hop while all switches are operational. Con: Does not scale well, uses lots of ISLs. When setting up, leave free ports for ISL or be prepared to step away from the full-mesh. Or, if SAN will never grow, this is also good.

## Core to Edge

Core switches only connect switches. Edge switches connect devices. For example, Directors as cores and B5300 as edge switches. Brocade pictures this with two directors in the core (so four for 2 fabrics.. expensive). Pro: Scales well. Because there is always the same amount of hops to another switch, load balancing will use all paths. Con: Expensive.

## Single / Dual Fabric

Simplest: only one. HA: need two. Pro: HA, easier migrations. Con: Cost, footprint, more to manage

## Techniques

Check how much oversubscription, how many ports are available for servers, enough bandwidth. Core/Edge is da bomb, especially if you're planning for growth. Two directors are OK as well.

For **inter** **site** connections consider putting switches on remote site, less cables. One idea is to have a third site where the Core layer (and arrays/libraries) is.

## Locality / Attachment

If you put devices in the Core in a Core/Edge fabric then they will have a greater locality compared to having initiators and targets on different switches.

On Cascade/Ring locality is almost a must. Full Mesh: preferred. In any design, locality is full of win. But might be hard to accomplish if your targets are shared between many devices. In that case, achieve locality between high bandwidth flows. For this reason, a tiered design is better if it's a larger SAN. A pure Core/Edge can be very horizontal.

On directors, spread devices between port blades. Attach them in groups. First x ports for ISLs etc? Attachment in groups makes for better cabling etc. Attaching ports randomly is perhaps good when the SAN is expanding very quickly.

 

# Availability

## Four levels:

**1)** Single fabric, not resilient: Not HA. For example: a Core switch with three edge switches, one fabric. SPOFs all over the place.

**2)** Single fabric, resilient: Not HA. Example: 2x cores, each edge connects to each core, one fabric. Why not HA? Only one port per server? Some upgrades / replacement might require downtime.

**3)** Two Fabrics, non-resilient: HA. Example: two fabrics and each device connects to both. But individually each fabric is non-resilient.

**4)** Two Fabrics, resilient: HA. Example: no spofs. Two fabrics and each fabric is resilient. This is better than 3) because it leaves the fabric to handle the failure of a switch instead of the multipathing in the server. Default multipath timeout on Windows is 60 seconds, how fast is FSPF?

## Data Replication

Is the data critical in the event of a catastrophic failure? Consider remote replication. Expensive.

 

# Performance

ISL Oversubscription: bandwidth by devices:ISLs or # of devices:ISLs. Fan-out: HBA\_port\_rates:storage\_port\_rates Fan-in: storage\_port\_rates:HBA\_port\_rates # of hba\_ports:# of ISL  -- only good if all connections are of the same speed.

_Most common is to use an oversubscription of 7:1 and keep an extra 3:1._ **Is this different with faster switches?**

See the whole path.

How fast does Condor ASICs route frames? Condor: 800ns Condor2: 700ns Condor3:

## Trunking

Max 64Gbps - On 8G. 200E - 4 port port groups Condor/C2/GE2 - 8 port port groups Condor3 -

Check deskew and bandwidth requirements. Use Exchange based routing (DPS).

NPIV - good shiet. As you put more VMs behind one FC HBA you get better utilization of the HBA than if the VMs were physical hosts.

No FSPF routing update if one ISL in a trunk is lost.

Multiple trunks (several port blades): can lose a port blade (FSPF routing update will happen).

### Individual ISLs

This is with for example connecting two switches but the ports are in different port groups. If one ISL is lost, an FSPF routing update occurs.

## 8/16G technologies

ICL - no hops, no user ports, heaps of bandwidth. When connecting directors: prefer two 2xISL trunks to one 4xISL.

## Measurement

**bandwidth:** good for "large block size" applications, backups, large files. on SAN with: 'portperfshow'. **IOPS:** "small block size" apps, sql/transaction or file servers, with host and storage based tools. Is the number of consecutive I/O's per second that the HBA/storage can drive. **latency:** switch latency: <=2 mys and cable latency 5ns/m. Good for long distance. Doesn't include latencies in initiators/targets **response time:** total time to fetch data to a user. SAN latency+latency in server, storage, os, distance and application. Good for "small block size" apps. For example you want to see how long it takes for a user to get the response of a small/quick SQL query.

Tools: DCFM/BNA, APM, SAN Health, Web Tools and SNMP. Portperfshow, Fabric Watch thresholds and "performance view" in Web Tools.

# Scalability

Minimize / eliminate cable changes and device relocations. Non-disruptive.

Scale it by adding/replacing switches/blades. Scale performance by adding ISLs or core switches.

Vendors have guidelines.

In full mesh the amount of ports lost to scaling (connecting switches) increases rapidly with the amount of switches in the mesh.

For core/edge recommended to only use 2 ISLs per switch?

Requirements may change over time - so might need more than two ISLs/switch. Dual fabrics makes it easier to change topology.

There are limits that needs to be observed, for example:

**These are on 8G and FOS 6.3 Platform. Need to confirm if there are new/higher limits in FOS 6.4.x, 7.x or 16G.**

- max amount of domains in a fabric (56 in native or 31 in McData).
- device connections (2560, 4090 (48k+DCX+5300 . core/edge) or 6000 DCX/5300 only. 2048 in McData.
- max logged in devices per fabric with Management Server enabled???
- max NPIV devices per port (255, or 127 for FC8-48, same for 64?)
- max devices per switch (1000, 2048 (48k+DCX+5300), 4096 (DCX+5300))
- max NPIV per switch (same as device connections in fabric)
- unique zone members (varies with 2 or 16 per zone, 1MB in total, depends if you use alias or not)
- max number of zones and zone sets
- SCC/DCC policies (2560/6000/14000 - tested/supported/theoretical end device WWNs or 56 switch WWNs)
- max admin domains
- max hops from source to destination (7 or 19 if using routing)
- max ISLs per switch: unlimited, could be all ports
- AG per fabric: 50/300/NA (tested/supported/theoretical)
- Max F\_Ports mapped to single N\_Port (40/100/255)
- Max N\_Ports per AG (8)
- Max N\_ports (connected to AGs) per hosting switch : 60/max switch port count
