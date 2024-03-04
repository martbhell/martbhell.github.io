---
title: BCFD - CFD200 - Module 3 - SAN Infrastructure
date: 2012-01-14
category: storage
tags: bcfd, bcfp, brocade, brocade, certified, fabric, designer, certification, storage, storage, area, network, storage, network
<!-- prettier-ignore -->
---

This is a post in a series where I will go through the modules made available
for free by Brocade for the beta test of the BCFD 16Gbps exam. If there's any
objection to me writing about these in this detail here please let me know.

First module available (is the third module). Both for BCFA and BCFP 16 Beta the
module 1 was not available. Maybe that's just an introduction? I don't remember
from when I had access to the real material. This module is also shared top1 in
terms of size :)

The material could be found here: community.brocade.com/docs/DOC-2379

## Describe B- and M-Series infrastructure for a DCF

dcf - data center fabric?

Before designing, you need to find out what your resources / building blocks
are.

Most highly-used design is a Core/Edge SAN, this has:

- Core (connect edge switches)
- Edge switches (connect targets and inititators to the fabric)
- Backbone and extension (provide routing or FCIP)

Core/Edge can be switches/directors and the Backbone would need to be a device
that supports routing.

1. Level of availability required?
2. How many ports are required for this?
3. Estimated port growth rate?
4. What is most important: performance, cost, redundancy or all?
5. Do you need to micro-manage the SAN with Adaptive Networking or Routing?
6. open systems (Windows/Linux) or
   [FICON](http://en.wikipedia.org/wiki/FICON "on wikipedia") (mainframes such
   as IBM's z/ and high end disk arrays)?

## Discuss the hw technologies for B- and M-series switches, directors and backbone

### HW

There's quite a lot about harware in this module. This was in both BCFA and
BCFP, so if you've done them you gain a lot. A little repetition is in order
though. **Also this module does not have the 16G hardware or the FC8-64 blades.
It's quite old. Some stuff in these slides will not be in use anymore. I expect
that new features / hw we need to investigate ourselves and read about in the
manuals.**

8G Switches:
 [300](http://www.brocade.com/products/all/switches/product-details/300-switch/specifications.page)
 , [5100](http://www.brocade.com/products/all/switches/product-details/5100-switch/specifications.page),
 [5300](http://www.brocade.com/products/all/switches/product-details/5300-switch/specifications.page "brocade.com").

Standalone switches usually don't have all ports enabled when you get them
(unless you buy them that way), to enable all you buy POD (ports on demand)
licenses.

Directors: the routing blades (C**R**) are on the oute**R.** The control blades
(CP) are on the inner. The DCX (8G) only works with the FR4-18i and FA4-18
blades, the other 4G no. FC8-48 does not support FL\_ or FICON, higher
oversubscription and more ports = more ports that can lose connectivity.

The 10G ports on FC10-6 blade are nice if you don't have many fibres/links
available and if 16G is not possible because of distance limitations. However,
it does not trunk and proprietary. Because it uses 64b/66b encoding you gain a
lot compared to the 8/10. 8/10 you miss out on 20% due to encoding, crc, etc.
64/66 you miss about 3%. So out of 10G you miss out on 300Mbit.

### Technologies

**Oversubscription**: The 48k does 4 and 8 Gbps in ports in 8G port blades, but
it has 4G CP ASICs (Condor). Making it easier to oversubscribe, make sure to do
local switching as much as possible. Is good for long distance and ingress rate
limiting though. The directors can switch within a portgroup, this is when the
ports are handled by the same ASIC. FC8-16 - one local switching group. -32 has
two. -48 also has two.

**Buffer Credits**: Maximum amount available per port varies between the
switches. The 5100 has most, which means it can support longer distances.
Calculate with: #buffers per port group - 8(ports in port group). For blades the
credits are about the same for FC8 (**also same for FC8-64? they are about 1300
on DCX and 1400 on 48k..).**

### Why get a DCX?

lulz, all this has a nice marketing feeling to it. But I guess when you design
an IT infrastructure you need to wade through a lot of marketing.

Besides the obvious ones (DCX is awesome, it has features you need, you need
more ports) it's good to cope with faster FICON environments, encryption, CEE or
FCoE support when/if, integrated routing (in a normal FC port in a port blade),
more QoS features.

## Distinguish differences between Brocade hw platforms

### M-Series

In BCFA and BCFD there's been very **very** little focus on the M-series
equipment. It appears to be a bit more in the BCFD. But, as far as I can tell
they are not sold anymore so hopefully there's not much focus on them. Gamble:
should I just browse through the McData sections?

#### Mi10k

hardware partitioning with SAN LPARs, mix FICON/open system in separate LPARs.
1,2,4,10 Gbps FC. Max 256 ports. Comparable to the 48k.

#### M6140

Open Systems and FICON, 140 ports in 4-port increments (each module you add have
4 ports, except 10G that has 1), 1,2,4,10 Gbps FC. M-series Directors are End of
Sale.

### Fabric Routing and Extension

There was quite a lot about this in the BCFP course. I am not sure if BCFA ->
BCFP -> BCFD is the best order to do them in but it is starting to look that
way.

7500E (E - economy, less ports) and 7500. FCIP and FCR. FR4-18i : Blade version
of 7500. M3000: interconnect FC and FICON SANs over IP or ATM. Accelerate tape
with Tape Piplining. Accelerate disk with Fastwrite and XRC. USD-X: connects and
extends mainframe and open systems storage data replication apps for
disk/tape. OC-3 ATM and 10/100 and GbE and FC. The USD-X does the same as the
others but also does  FICON, ESCON, Bus-and-Tag or mixed environments.

M3000 and USD-X does not: HW encryption (IPSec), FCR, Call Home, SSH(SSL,
RADIUS), inband management via GbE or FastWrite over FC. They both also only
operate at 2G speed. This makes me believe they are not included in the 16G
BCFD, 2G is just too little?

Also integrated routing on the DCX, 5300 and 5100.

### 7600 and FA4-18

They are the same?

Allows "third party storage apps to run on top of FOS". Uses Brocade's SAS
(storage application services) for 'data movement' and 'offload server
resources'. EMC, Fujitsu and Brocade has softwares (possibly more now)

### HBA

815, 825, 415, 425.

### Embedded SAN modules

For blades:

Dell/Fujutsu: 4016 (10 internal, 6 external) IBM/Intel: 4020 (14 int, 6 ext) HP
p-class: 4012 (16 int, 4 ext) HP c-class/NEC: 4024 (16 int, 8 ext) HDS: 4016
(10,16) Huawei: 4018 (12 int, 6 ext) IBM:
