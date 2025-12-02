---
title: BCEFP 2015 – Studying for the exam - part 3
date: 2014-05-30
category: it
tags: brocade, brocade, certified, brocade, certified, ethernet, fabric, professional, certification
<!-- prettier-ignore -->
coverImage: "original.gif"
---

This third post  focuses on the remaining sources of information I had for studying for the BCEPF. At the time this post
is published I have taken the exam.

When I make comments to CLI commands I put them after a #.

This is part of a series of posts on the topic of studying for Brocade's Certified Ethernet Fabric Professional.

The two previous posts:
[Objectives and reading materials](https://www.guldmyr.com/brocade-certified-ethernet-fabric-professional-2015-beta-exam/),
[course and nutshell guide](https://www.guldmyr.com/bcefp-2015-studying-for-the-exam/)
and [NOS Admin Guide](https://www.guldmyr.com/bcefp-2015-studying-for-the-exam-part-2/)

## VDX Troubleshooting Course

The material available also feels very short, same as the beta material available for the CEF300 , like only the parts
of the slides that were updated for the BCEFP 2015 beta were included. When a slide says "(cont.)" but there was no
previous slides on this topic, that's a hint :) Take the (currently free) course on Brocade's SABA - it's under
Education on my.brocade.com. It has way more slides and info.

**Some notes from the course:**

Firmware Upgrade

- Can upgrade all/selected RBridges in a logical chassis: firmware download logical-chassis
- FTP/SCP/SFTP/USB(only local switch with USB)
- By default it stages firmware only - so no reboot or activate. By adding auto-activate it reboots all RBRidges at the
  same time, not recommended.

SNMP

- When BNA discovers a switch it automagically configures the switch to send traps (UDP 162) to the BNA server.

Fabric Formation:

- Requires: Licenses. Same VCS ID, unique RBridge ID and same VCS mode (Fabric Cluster or Logical Chassis)
- Check:
  - ISL ports are operational (show fabric islports)
  - Incompatible Firmware Levels

ISLs:

- no fabric isl enable # this disables ISL formation. This makes it an edge port
- CPU could be too busy to send ISL keepalives
- If ISL is segmented and interface is up/up - it's probably a config issue.

vLAGs:

- show running-config interface TenGigabitEthernet 1/0/2 _\# shows config_
  - no shutdown
  - channel-group $NUMBER mode active type standard _# active - LACP. Standard/Brocade proprietary._
- show interface TenGigabitEthernet 1/0/2 _\# shows status_
  - When counters are non-zero and looking for errors. Clear them and compare the delta.

Other:

- show interface stats brief _\# shows discards, errors and CRC_
- VRRP:
  - show vrrp detail
  - pre-empting : if a virtual router comes online with higher priority than the current it will take over
  - VRRPE: Can enable short-path-forwarding. If one of the backup virtual routers (that don't own the Virtual IP) can
    actually forward traffic if that is advantageous.

FCoE:

- show running-config zoning _\# show FCoE zoning_
- show fabric all #
  - RBRidge with this name: fcr_fd_160 # this comes online when fabrics are connected and Fibre Channel Routing is used.
  - RBRidge with this name: fcr_xd_4_100 # this comes online when devices across FC Fabrics can communicate. Don't see
    this? Check zoning.

iSCSI:

## BCEFP practice questions / answers

[http://community.brocade.com/t5/Certification/BCEFP-2013-Exam-150-180-Practice-Questions/ta-p/4099](http://community.brocade.com/t5/Certification/BCEFP-2013-Exam-150-180-Practice-Questions/ta-p/4099)

These are decent practice questions and is nice because the answers give some explanation to the answers too.

## Other

Intro to VCS Fabric Technology:
[http://www.brocade.com/downloads/documents/white_papers/intro-vcs-fabric-technology-wp.pdf](http://www.brocade.com/downloads/documents/white_papers/intro-vcs-fabric-technology-wp.pdf)

### **CFP- MSA CFP2 Hardweare Specs:**

- about the 40/100Gbps CFP2 SFP. MSA – multi-source agreement.
- CFP2 module shall support LC, MTP12 and MTP24 optical connector types. MPO

### **NOS 4.1.1 release notes (p4,10,28,50):**

- 4.1.0 and later support VRRP-E across VCS fabrics.
- 4.1.0 and later have vlag ignore split on by default
- clear mac-address-table can clear MAC addresses associated with vLAGs and on other switches
- Page 50 Has a table of scalability numbers for various features such as (6710 VCS, 6740 VCS, 8770 VCS):
  - max members of a LAG (8,16,8)
  - max switches in a fabric/logical cluster (24,32,32)
  - max ECMP paths (8,8,16)
  - max member ports in a vLAG (64)
  - max member of VMs (8k)
  - max ARP entries (8k,12,50k)

### **Network OS Command Reference v4.1.1** **_53-1003226-01_**

Pages 299, 1258-1260,1266,1297,1317,1318

- firmware download
- snmp-server user # access
- snmp-server v3host # trap recipients
- spanning-tree edgeport # quickly transitions to forwarding state: only for RSTP/MSTP. Portfast for STP.
- switchport access # only allows untagged and priority tagged
- switchport trunk allowed vlan ${rspan-vlan} # add allowed VLAN on trunks on L2 interfaces in trunk mode
- switchport trunk default-vlan # put all non-matching traffic into this VLAN

### Hardware reference manuals

**VDX 6740 Hardware Reference Manual** 53-1002829-02: Page 1

- 6470: 24 1/10GbE SFP+ ports.
- 6740T: 24 RJ-45
- 6740-1G: 48 RJ-45 Base-T. 10Gb with license.

**VDX 8770-4 / 8770-8 Hardware Reference Manual** 53-1002563-03:

- Chapter 1, Page 1:
  - Features CloudPlex.
  - Requires NOS 3.0.0 or greater.
  - 8770-8:
    - Up to 384 10GbE or 96 40GbE. Dual MM. 6 SFM. Max 8 PSU. 4 Fans. SX or LX 1Gbps SFP transceivers.
  - 8770-4:
- Chapter 3, Page 32
  - For copper connections to < 1Gbps BaseT switches a crossover cable is needed (but it might not be if MDI/MDIX
    works..).
  - LC connectors for fiber ports

**VDX 6730 Hardware Reference Manual** 53-1002389-06: Pages 1,2,15

- 6730-32: 32-ports. 6730-76: 76 ports. 8 or 16 x 8GB FC ports.

**Network OS Software Licensing Guide v4.1** 53-1003164-01

Pages 11-13

- All have FCoE license (except 6710).
- All have POD licenses (except 8770)
- 6740 have 10/40GbE port upgrades
- 8770 have L3 and Advanced Services

Notes:

- for multi-hop FCoE it is needed on each node
- L3: OSFP, VRRP, PIM-SM, Route-Maps, prefix list
- Advanced: FCoE and L3
- After installing a time-based license you cannot change system date or time. NTP is however not blocked. If you are
  using NTP, don't change system date/time when a time-based license is installed.
