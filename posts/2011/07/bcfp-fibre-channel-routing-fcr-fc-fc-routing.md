---
title: BCFP - Fibre Channel Routing - FCR - FC-FC Routing
date: 2011-07-26
category: storage
tags: bcfp, brocade, brocade, certified, fabric, professional, fc, fc, routing, fcr, fibre, channel, fibre, channel, routing, san, network, storage
<!-- prettier-ignore -->
---

FCR; Fibre Channel Routing; FC-FC Routing; etc; etc.

This has many names. FC-FC Routing service provides FCR (fibre channel routing).
Basically what it does is that it lets you zone devices in two separate fabrics
without merging them. These two separate fabrics are called 'edge fabrics' in
Brocade lingo, they are otherwise known as SAN islands. The edge fabric is
connected to a backbone fabric (an FC router or at least an EX_Port).

Integrated Routing - is a licensed feature that lets you run FCR on a port that
is in a normal port in a normal switch or port blade (so not in a dedicated
router switch or router blade).

## There's a few things required to set up FCR

1. Verify that you have the proper setup (required licenses/hardware)
2. Assign backbone FIDs (**switchdisable; fosConfig --disable fcr; fcrconfigure;
   fosconfig --enable; switchenable**)
3. Configure FCIP tunnel (not required but: **portcfg fciptunnel 8/ge0 create 2
   1.1.1.1 1.1.2.1 0 -v 100 -p 3 -P 7** . Remote IP first, tunnel ID, vlan,
   Classes for layer2 control and data traffic)
4. Configure IFLs - inter fabric links - links between edge and backbone fabrics
   (portcfgvexport, **portcfgexport 7 -a 1 -f 30** . port 7, enable, fabric
   id 30)
5. Modify cost on the EX_ports (not required; **portdisable; portcfgexport 7 -a
   1; fcrrouterportcost 7 10000**; for default, set it to 0; **fcrRouteShow**
   also shows cost)
6. Connect cables (if you do it before and they are configured as E_port you may
   get segmentation).
7. Configure trunking on EX_ports (not required but if you have more than one
   link, please do, same commands as for E_port trunking)
8. Configure LSAN zones (same as normal zoning; **zonecreate "lsan_zone_fabric",
   "wwn; wwn2; wwn3"; cfgadd "zone_cfg", "lsan_zone_fabric"; cfgenable
   "zone_cfg"**). Use **lsanzoneshow -s**. Shows
   imported/exist/configured/initializing. **fcrphydevshow, fcrproxydevshow**
   are also useful.
9. Confirm that it's working (**fcrfabricshow, switchshow, portcfgshow,
   portexport 7, portshow 7**)

So what you have to do is: assign FIDs, configure IFLs and LSAN zones.

## A little theory

Phantom domains.

**Front domains** -> always there

**Translate domains** (also xlate domains...).  -> only there when devices are
online and zoned

The FC router has a pool of wwns and proxy ids that it assigns to devices.
Basically a host that wants to communicate with a target in another fabric
communicates with a proxy WWN in its own fabric (so the FC router is like a
middle man that passes frames back n forth).

## A little more information

When a PLOGI, PDISC, ADISC frame arrives at the FC router, SID and DID are
checked. If they are zoned in both SID and DID edge fabrics (islands), the frame
is forwarded to DID. If not, only PLOGI is dropped; edge fabrics' zoning
enforcement takes care of the rest.

I found
[this document](http://education.emc.com/main/common/documents/ks_articles/brocade_fibre_channel_routing.pdf "on emc.com and it's a pdf")
on EMC's webpage (it's from 2007 so a bit outdated and it has EMC's names of the
Brocade products) but it explains the concept pretty nicely.

Also, this post is for me to study for the BCFP, I find that I learn better when
I write things down with a keyboard ;) There may be mistakes in here but that's
just how it is, I tried to keep it as factual as possible and used several
sources. There will most likely be more of these posts coming up.
