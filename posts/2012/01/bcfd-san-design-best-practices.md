---
title: "BCFD - SAN Design Best Practices"
date: 2012-01-23
category: storage
tags: bcfd, best, practices, brocade, brocade, certified, fabric, designer, certification, design, san, design, storage, storage, area, network, storage, network

This is a post in series of me studying for the BCFD - Brocade Certified Fabric Designer and it's my comments on the document SAN Design Best Practices. Apparently this document is planned to be updated. The one I have is version 2.1. To find the latest go to My.brocade.com , documentation, Best Practices Guides. There's also a "SAN Migration" guide there, but it's from 2003 so irrelevant when it comes to anything specific, but ideas and reasons and methods might be valuable.

OK. I thought about doing something similar for this document as for the previous ones. But I just don't feel like that, it's basically just re-writing things in different wording so that it sticks in my brain. No instead I'll post the questions that popped into my brain while reading it.

For a starter, I printed this .pdf. OK it's not so environmentally friendly but it's nice to have a break. One thing though, it took me a lot longer to read this than the course modules for BCFD. The SAN Design Best Practices is a first class pdf. At least in my opinion. I mean it's general **and** specific. It needs to be general because there's a lot of reasons behind designing things. Also, I don't have any actual previous experience designing a SAN, so this is all new to me, and brings up a new side of Storage and Storage Networking that I just haven't bothered much with before. Hopefully I have and will be learning a lot.

## Links

This paper refers to a lot of documents.

The "[Brocade Scalability Guidelines](http://www.brocade.com/downloads/documents/matrices/Brocade_Scalability_Guidelines_100208.pdf)" is not updated with 16G products (Only goes to FOS 6.3.0).

## Latency

Page 10 it says "hop count is not a concern if the total switching latency is less than the disk I/O timeout value".

Every switch hop adds latency (frame needs to be put in ASIC, processed then sent on its way).

Switch latency is measured in microseconds. Disk I/O - is that the same as multipathing timeout? So 60 seconds for MPIO default in Windows?

How are these latencies measured?

## Redundancy Resiliency

Two fairly similar words. One indicates something has a replica or a duplicate to fall back on. The other indicates the strength, can it by itself handle a problem.

Core switches should be equal or higher perf compared to edge switches. Highest performing switch should be the principal switch. Redundant links should be placed on different blades/ASICs or at least different port groups.

## EHT - edge hold time

New timeout value that can discard blocked frames earlier than the 500ms default (down to 100ms). An I/O retry will still happen for each dropped frame.

Is a new features in FOS 7**(confirm)** and it is ASIC dependent. Meaning ports in another port group are not affected by the EHT in another port group.

EHT applies to all F\_Ports on a switch _and_ all the E\_ports that share ASIC with F\_Ports.

Intended for initiators only.

## ICL

Directors interconnected via ICL is not considered a hop in FICON, is it in Open Systems? Are the links uni-directional?

ICL cables should all have the same length. ISL can be a bit different, max 30m in difference. Don't have ISL and ICL to the same switch/domain.

## Links

Hyper-Scale Fabrics: Scale-out Architecture with Brocade DCX 8510 Feature Brief.

## Small Fabrics

Page 15: Brocade recommends core-edge as primary SAN design, or mesh for **small fabrics** (under 2000). !!! That's pretty big.. On page 16 it says use full-mesh under 1500 ports.

## Fan-In and Fan-Out and Oversubscription

Host ports to Target Ports

Device to ISL

Fan In : number of device ports that need to share a single port, be it target or ISL.

Consider: port queue depth, iops and throughput.

Example: If you have 4 devices with one 8G FC port each (32Gbps) and they are connecting over an ISL of 2x8G to another switch to a storage array that also have 2x8G then there is a 2:1 oversubscription, both on the ISL and on the target ports.

## Bottleneck Detection

BD consumes switch memory, don't monitor more than 100 ports on a 48k (no limit on DCX).

Start monitoring a small number of storage ports.

## Fabric Watch

Thresholds and actions are generally different between initiators and targets. Thus place these on different switches.

[FW Administrator's Guide 7.0.0](http://www.brocade.com/downloads/documents/product_manuals/B_SAN/FabricWatch_AdminGd_v700.pdf)

Monitor Class 3 frame discards (C3TX\_TO), they are an indicator of high-latency devices.

### Fabric Watch Classes

This is a wide grouping of similar devices. For example, temperature is a part of the class Environment.

## Long Distance

### Buffer Allocation

Number of credits: 6+ ((link speed Gb/s \* Distance in km) / frame size in KB)

On 8510 4K buffers are available per ASIC to drive 16Gbps to 500km at 2KB frame size. With credit linking, buffers can be borrowed from a neighboring ASIC to extend distance. Details about 'credit linking'? Not many hits about this on google.

You can connect DWDMs in pass-thru mode where the switch is providing all the buffering.

### FCIP

FCIP adds a small latency (35 micro seconds). This is without the underlying TCP/IP delays.

Use QoS to give FCIP traffic highest priority. Use CAR (committed access rate) to limit other traffic. Use ARL (adaptive rate limiting) and set the limit to the remaining bandwidth.

FCIP traffic believes it is the only one using the bandwidth it has available, other traffic will suffer if they if they are sharing.

Use rate limiting on the FCIP on the Brocade systems, don't limit it on the IP network.

### MLX

This is mentioned for when extending mainframe/FICON extension over FCIP.

[MLX is a Brocade Router.](http://www.brocade.com/products/all/routers/product-details/netiron-mlx-series/index.page "brocade.com")

### OC

OC1 =~ 52Mbps or without overhead ~50Mbps OC12 = 12\*52 or about 622Mbps OC48 = 48\*52 or about 2488Mbps

OC12 is recommended for Compression Mode 3 (GZIP/software only) OC48 is recommended for Compression Mode 2 (SW with HW assist)

Neither of those are recommended for synchronous replications. Mode 0 is recommended and that is HW only compression.

## Gaussian or Normal Distribution

[http://en.wikipedia.org/wiki/Normal\_distribution](http://en.wikipedia.org/wiki/Normal_distribution)

Have fun.

## Virtualization

There's quite a bit about new Virtualization Engines in this paper. It basically means a device that has other disk arrays behind it, and then this device presents disks to servers. The danger is told to be that the engine can send a lot of small control frames, using up the buffer credits without using all the available bandwidth.

**APM and Fabric Watch can apparently be used to monitor for excessive levels of SCSI reservations. How? -** No specific details found but it is apparently threshold configurable in  fabric watch.

## NPIV

Less domains equals to reduced:

- inter-switch zone transfers
- name server synchronizations
- RSCN processing

## Dynamic Fabric Provisioning (DFP)

Only on Brocade HBAs and 16G.

Dynamically provision switch-generated virtual WWN.

Can be user-generated as well.

WWN stays the same even after HBA replacement.

In practice this means you can zone, QoS even before the HBA is online and before you know what the WWN is of the new device.
