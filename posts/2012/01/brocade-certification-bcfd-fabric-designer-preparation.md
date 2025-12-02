---
title: Brocade Certification - BCFD - Fabric Designer - Preparation
date: 2012-01-13
category: storage
tags: bcfp, brocade, brocade, certified, fabric, designer, certification, storage, storage, area, network, storage, network
<!-- prettier-ignore -->
---

BCFD exam is going into Beta testing in January as well!

This post will be updated as I move along through the different objectives / documents.

// Update 2012-01-15: Added the Knowledge Assessment Test. // Update 2012-01-28: Went through each .pdf and updated some
in here.

The link to the Brocade page where it tells you how to register and where to get the
material: <http://community.brocade.com/docs/DOC-2379>

\# Note: This link no longer works

When are these available? On Thursday 12/01/2012 at 0728 EET it was not available. On Thursay 12/01/2012 at 0803 EET it
was available.

So, that would indicate that the time Pearson follows is GMT-6 or Central Time.

On top of that the only available dates for me was 23rd and 24th of January :( Time to study! // update, that was
changed, it was a mistake so now I get some more time to study :)

## Exam Study Resources (page numbers are document page numbers, NOT the PDF page)

As I see it, the importance of each document could be arranged like this:

1. CFD 200 Modules 3-7
2. SAN Design Best Practices
3. FOS Administrator's Guide
4. The rest.

With 1/2 sharing the top spot. I haven't gone through the modules yet but I presume they all complement each other. The
reason for them sharing the top spot is because for this Beta Exam, the CFD200 material is for 8Gbps (and it has quite a
lot of details about the M-series McData switches, which the 16Gbps BCFD did not include).

There is also a Knowledge Assessment on my.brocade.com 'education' page. It's called "CFD 201 8 Gbit/sec BCFD Knowledge
Assessment". Again, this is for 8G so beware that some stuff may not be up to date if you are doing the Beta for BCFD
16G. But, the actual type of questions is something that is useful. It mentions EFCM or Fabric Manager some times (this
is the previous names of DCFM or what's now called Brocade Network Advisor).

There is a nutshell guide for BCFD, but this is from November 2008 making it possibly even more outdated than the CFD200
material. But, because most of the topics are still valid it would still work as a refresher, but you can't use it for
anything specific.

I am doubtful that the M-series will be included in the BCFD 16G exam but as it's still in the objectives for the 8G
it's probably wise to not skip that part completely. For that 1.5 years (half 2009 and 2010) when I did SAN support I
only had one call about a McData switch.

## Exam Study Resources with my comments

### CFD 200 BCFD Design Course Modules 3-7

- Obviously these are the most important. I'll go through these at a later stage.

### Brocade DCX 8510 Backbone Family Datasheet

(GA-DS-1564-01)

- Lots of details about the system specs.

### SAN Design Best Practices

(GA-BP-329-02-02)

- **Pages** 2,5-16,19-26,31,32-36,40-45,51-53,55,58-62,66,67,72

### Fabric OS Administrators Guide v7.0

(53-1002148-03)

- **Pages** 37,43,66-70,102,142,151,153,157,196,199,241,273-286,301,314,315,320,372,383,395-398,402-406,414,417,425,429,437,438-443,449,454-461,464,503,504
  - topics
    - 256-area addressing
    - WWN-based PID assignment
    - enabling/disabling a port and port decommissioning
    - gateway links, ICL,
    - RADIUS/LDAP authentication
    - fddcfg / DCC/SCC policies
    - device authentication
    - ipfilter
    - firmwaredownload
    - advanced zoning (regular, broadcast, frame redirection, lsan, qos, ti)
    - traffic isolation zoning (and VF considerations for TI zones)
    - bottleneck detection
    - in-flight encryption and compression (technologies, enabling/disabling)
    - licensing (enable 10GbE, 7800, QoS, FCIP Extension, FICON acceleration, etc, etc, etc)
    - advanced performance monitoring (top talker, frame monitor, end-to-end)
    - adaptive networking (ingress rate limiting)
    - QoS prioritization (SID/DID or CS_CTL - class specific control)
    - trunking (ISL, ICL, EX_Port, F_Port)
    - Long Distance (buffer credit allocation, max distance, credit recovery)
    - FC-FC Routing (support platforms)
    - interopability (FOS vs M-EOS)

## Fabric OS Command Reference v7.0

(53-1002147-01)

- **Pages** 302,695,716,721,957,
  - commands
    - fcrconfigure  /  fcredgeshow
    - portcfgspeed
    - portdportest
    - portfencing
      - Why is the test for "Invalid Word Transmission" called ITW?
      - Ah, on portThConfig it is called "Invalid Transmission Word".
    - supportshow

### Fabric OS FCIP Administrators Guide v7.0

(53-1002155-01)

- **Pages** 1,6
- topics
  - FCIP platforms and supported features
    - 7800, FX8-24 and FR4-18i
    - FCIP Trunking
    - Adaptive Rate Limiting
    - 10GbE
    - 8G FC Ports
    - Compression (LZ and Deflate)
    - Acceleration (FCIP Fastwrite, OSTP)
    - QoS
    - VLAN Tagging
    - FICON
    - IPSEC
    - VEX
    - IPv6
    - Jumo Frames
  - 7800 switch hardware overview
  - FX8-24 has support for all features above, except: Jumbo frames (only FR4-18i supports those), IPv6 addresses for
    FCIP tunnels or IPsec, or 3rd WAN optimization hardware (the other do support this pre FOS 7)

## Monitoring and Diagnostic Testing in Today's High Speed High Density Networks

- **Pages** 2-4
  - topics
    - powerpoint presentation of four pages in total
    - fc cable lengths
    - measuring loss
    - embedded diagnostics (bottleneck detection, fabric watch, frame monitoring, port fencing)
      - **fmmonitor** is a CLI that you can use to set up frame monitoring, for example SCSI reservations and aborts.

## Brocade Network Advisor SAN User Manual

(53-1002355-01)

- **Pages** 12,164,186,255,596,770,794,796
  - topics
    - "Connectivity Map Toolbar" & "Product List"
    - Call Home Feature
    - Copying and Deleting Views
    - SAN Device Configuration (configuration repository management)
    - LSAN Zoning
    - Performance Overview
    - Bottleneck detection

## Why dB Loss Matters for Building Reliable Stable Networks

GA-TN-048-01

- **Pages** 2,3
  - topics
    - total 8 pages
    - link lengths and link loss budgets

### Brocade 6505 Hardware Reference

(53-1002449-01)

- **Pages** 13,15
  - topics
    - ISL trunking
    - switchstatuspoolicy
    - fos native and AG modes

### Brocade Access Gateway Administrator’s Guide

(53-1002156-01)

- **Pages** xiv,72,
  - topics
    - supported hardware and software (which switches and FOS)
    - enabling NPIV on M-EOS and Cisco switches
      - CISCO: config t; npiv enable
      - MEOS:
    - new features -F_Port static mapping, APM, B6510, Target Aggregation, Direct target attachment, N_Port monitoring

> "You can run the agshow command to display Access Gateway information registered with the fabric. When an Access
> Gateway is exclusively connected to non-Fabric-OS-based switches, it will not show up in the agshow output on other
> Brocade switches in the fabric."

### [CEE Admin Guide 53 1002163-02](http://www.brocade.com/downloads/documents/product_manuals/B_SAN/CEE_AdminGd_v700.pdf "this is not in the resource list on community.brocade.com")

- **Page** xviii
  - topics
    - Supported Hardware: Standalone switch B8000 and the blade FCOE10-24
    - IGMP configuring (IGMP is used in multicast, ethernet)
    - Replacing the B8000
      - configdownload
      - and copy running config and stuff! Looks very similar to the Cisco CLI.

### Brocade Adaptors Admin Guide

(53-1002143-01)

- **Pages** 3,13,
  - topics
    - AnyIO technology on the 1860 Fabric Adapter, just change the SFP and set the mode with **bcu port --mode** or
      **bcu adapter --mode**.
      - HBA or FC mode (FC)
      - Ethernet or NIC mode (GbE)
      - CNA mode (FCoE)
    - Adapter Support (OS + description of adapters)

### The New Data Center 1st Edition

ISBN: 978-1-4507-0195-2

- **Pages** 65,66,78
  - topics
    - Fabric Based Disaster Recovery (64-67)
      - An overview of some of the extension technologies and reasons behind them.
    - Network Security (77) + Power, Space and Cooling Efficiency (78)
      - Network Security is not FC related.
