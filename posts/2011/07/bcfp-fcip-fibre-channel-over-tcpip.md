---
title: "BCFP - FCIP - Fibre Channel over TCP/IP"
date: "2011-07-28"
categories: 
  - "storage"
tags: 
  - "bcfp"
  - "brocade"
  - "brocade-certified-professional"
  - "certification"
  - "circuits"
  - "extension"
  - "fcip"
  - "fibre-channel"
  - "fibre-channel-ip"
  - "gbe"
  - "ip"
  - "qos"
  - "routing"
  - "trunking"
  - "tunnels"
  - "ve_port"
  - "vex_port"
  - "virtual-fabric"
---

Still studying for Brocade's BCFP Exam. This post is to try to put light on some of the terms/technologies you'll be surrounded by when learning about FCIP.

Guides you should see are the "Fabric OS FCIP Administrator's Guide" and you should probably start with the material for BCFP - part 4 (theory) and 5 (administration).

Basically the FC frames will be encapsulated in packets over TCP/IP, making the TCP/IP part  invisible/irrelevant to the SAN fabric and the FC frames invisible/irrelevant to the TCP/IP. Except of course for the FC routers that bridge the networks. It is possible to run FCR over FCIP as well via the VEX ports (virtual EX\_port). Extension. This means that it's using TCP flow control, no BB credits.

## Terminology

### Tunnel (VE\_port) - are seen as VE\_ports in the fabric.

### Circuits (GbE ports) are inside a tunnel (VE\_port) Is a logical connection between two IP addresses.

Metric 0 - active (you can have several links at metric 0) Metric 1 - standby

FCIP tunnels support max two hops.

### Multi-Gigabit Circuits

On the FX8-24:

2x 10GbE 1x 10Gbe and 10x 1GbE 10x 1GbE Not,  all ports at the same time.

### FCIP Trunking

Basically adding more circuits to a tunnel, not recommended to set up several tunnels (limited anyway) but because ISL trunking is not supported on VE\_ports.

FICON timeout: 1s FC timeout: 4s Consider altering these depending on your setup/latencies.

### Virtual Fabric considerations

Define several logical switches inside a physical. You can with FOS 7.0.0 have a VE\_port (the GbE ports) defined in the base/default switch and then share it with other logical switches, giving you the possibility to extend/route the fabrics over a shared trunk while they are still isolated. You cannot mix dedicated (in an LS) and a shared (in default) in the same FCIP tunnel.

### QoS

Not enforced if there is no contention (there is free bandwidth)

VC0 (or F\_frames - fabric frames) - always first. QoS\_High: >50% : : 6 QoS\_Medium: >30% : 3 QoS\_low: >20% : 1

### DSCP (6 bits of priorities - 64 ) L2CoS (3 bits of priorities- 8 ) Priority is set in the TOS - in the header.

Compression

(four different ones, hardware, software, mix, auto)

### 10GbE

"lossless" failover only in FOS 7.0.0. (brocade chipset did not share ports) You cannot use both 10GbE and get 20GbE. You can have them active/standby or use both A/A and get 5Gbps on each. Disabling port != failover testing.  Can/will cause disruptions.

#### Crossport

Crossports are addresses and routes that belong to the other 10GbE (XGE) port’s DP or VE group.

The crossport for xge0 is xge1 and for xge1, the crossport is xge0. To use crossports, the port must be configured in 10 Gbps mode.

The crossport is the non-local XGE port for a VE\_Port group. In other words, for
VE ports 12 through 21, xge1 is the local XGE port and xge0 is the crossport. For VE ports 22
through 31, xge0 is the local XGE port and xge1 is the crossport.

### SACK

(selective acknoledgement - prevent that each lost packet requires an ack, bundles up several lost packets into one, default is **ON**)

### Adaptive Rate Limiting

Configure minimum and maximum rates on an FCIP circuit. Let's say you have one FCIP router with two circuits going to two independent IP-routers, these two share a link to another site. The idea is that then you can use ARL to configure minimum half of the shared link on each of the circuits from the FCIP router to the IP router, and a max of the whole one. So if one goes down, you're not stuck with half and you're not oversubscribing. There, easy to explain in words :d

## Hardware

### FX8-24

2 x 10GbE ports, 12 x 1GbE and 12 x FC8 [Link to hardware page on Brocade.](http://www.brocade.com/products/all/san-backbone-director-blades/product-details/FX8-24-extension-blade/specifications.page "on brocade.com")

### 7800

6 x 1GbE ports, 16 x FC8 [Link to hardware page on Brocade.](http://www.brocade.com/products/all/switches/product-details/7800-extension-switch/specifications.page "on brocade.com")

## Steps

1. What settings are you going to have on the ports/links/tunnels?
2. Configure hw ports (media type, mode etc)
3. Disable VE\_ports (Virtual FC E\_ports) with the tunnel (**portdisable**)
4. Create ip intf for each phy Ethernet port that's going to be used (**portcfg ipif**)
5. Config IP route for each port to specify an IP Gateway (not required; **portcfg iproute**)
6. Verify IP network between the two IP interfaces that will form the tunnel. (**portcmd --ping slot/port**)
7. Create an FCIP tunnel (circuit 0; **portcfg fciptunnel; portcfg fcipcircuit**)
8. Config FCIP Features (SACK, compression, etc)
9. Verify config, enable VE\_ports, verify that it's working
10. Add more circuits to the tunnel(s).
