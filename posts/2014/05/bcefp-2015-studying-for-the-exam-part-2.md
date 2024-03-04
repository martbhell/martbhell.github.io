---
title: BCEFP 2015 – Studying for the exam - part 2
date: 2014-05-21
category: it
tags: brocade, brocade, certified, brocade, certified, ethernet, fabric, professional, certification
<!-- prettier-ignore -->
coverImage: "original.gif"
---

This second post  focuses on the NOS Admin Guide.

When I make comments to CLI commands I put them after a #.

This is part of a series of posts on the topic of studying for Brocade's
Certified Ethernet Fabric Professional.

The two previous
posts:
 [Objectives and reading materials](https://www.guldmyr.com/brocade-certified-ethernet-fabric-professional-2015-beta-exam/)
 and [course and nutshell guide](https://www.guldmyr.com/bcefp-2015-studying-for-the-exam/)

## The NOS 4.1.1 Admin Guide

I've been reading the pages on paper (together with a highlighter :) that I
printed with the help of my script below and there is lots of goodness in there.
For sure some topics are brought up without any preamble so for these I just
make a note in the paper that I need to check out this other thing later.
Especially the Fibre Channel things take up quite a lot of pages. I thought in
these devices FC would not be with so much focus but it seems like they do
re-use a lot of the things in FC that works.

Notes and acronyms (page in NOS Admin Guide):

- DCB - lossless. Able to allocate bandwidth on links.
- TRILL - transparent interconnections of lots of links.
- RBridge - Routing Bridge. Lowest WWN or priority.
- Looks like on p54 only the text about Logical Chassis cluster config is
  applicable.
- Trunking between VDX8770 and B8000 are not supported (B8000 is some early
  version of FCoE from Brocade, not visible on Brocade's
  [page](http://www.brocade.com/products/all/switches/index.page) where they
  list their switches)
- ECMP - Equal-cost multi-path routing (p149)
- AG - VCS must be enabled for Access Gateway
- AMPP - Automatic Migration of Port Profiles - some OK pictures around p375
- VRF - Virtual Routing and Forwarding

Questions:

- There is also a
  [Openstack Neutron Plugin](https://wiki.openstack.org/wiki/Brocade-neutron-plugin) (p29)
- Would be good to include also page 114 before page 115 to see what they mean
  with leaf/spine/core (p115)
- OOB access to console is via serial (p115)
- How to reload a group of switches? (p115)
  - reload system rbridge-id all
- Does trill use IS-IS type link-state? (p136)
  [Yes](<http://en.wikipedia.org/wiki/TRILL_(computing)> "on wikipedia")
- Can VF_Ports be anywhere in the fabric? (p202) Yes, they must be mapped to
  N_Ports.
- Is there no web interface on the VDX? (p269) Probably not, there are some
  "http server" and "ip http-server" commands.
- What are valid upgrade paths? Not so clear. 3.0.0 to 4.0.0 is not OK. 3.0.1 to
  4.0.0 is OK. (p341)
- What is this netinstall? (p371) - 10 hits on google: brocade "netinstall" vdx
- What does the asterisk mean in the output of "do show vcs" ? (p597) The one
  you are running the command on? Is not principal RBRidge, that is >.

Commands (# comments) (page):

- backup config: copy rbridge-running-config rbridge-id rbridge-id
  location_config
  - copy rbridge-running-config rbridge-id 2 scp://user:pw@host
- vcs
  - no vcs logical-chassis enable # remove a node from logical chassis cluster
    (p76)
  - vcs replace rbridge-id 3 # replace RBridge with id 3 (p77)
  - enable (p139)
  - virtual ip address 10.1.1.1 (p143)
- config terminal # to enter global exec mode (p94)
- firmware download (p119)
- logical-chassis principal-switchover (p138)
  - and logical-chassis principal-priority are the only logical-chassis commands
- disabling a port:
  - shutdown # on an ISL brings down link and FSPF adjacency.
  - no fabric isl enable #  link stays up, shorter reconvergence
- show
  - vcs virtual-ip (p143)
- vcenter/vnetwork # used to connect to a vcenter and to discover hosts. (p243)
- bind # create persistent binding between logical FCoE port and 10G/40G/LAG
  port. Port or MAC, not both. (p345)
- enable statistics direction # for VXLAN tunnels to enable statistics on VLANs.
  (p365)
- no spanning-tree shutdown # default for all VLANs - meaning it's enabled.
  (p381)
- lacp system-priority 25000 # For deciding which system is in charge of
  resolving LAG conflicts. (p437)
- nas server-ip IP/PREFIX # Set IPs for AutoQoS for NAS (p506)
- address-family ipv4 unicast # Used to enter IPv4 config in a VRF (p609)
- debug lacp pdu # turn on debug (p714)
  - terminal monitor # view debug messages in terminal

### Printing the NOS Admin Guide relevant pages

Because the slides for the BCEFP course were insufficient I would get a lot of
the basic information about the NOS from the NOS Admin Guide. In the materials
provided the NOS Admin Guide was separated into two documents. The guide is of
course available in one pdf. Go to the
[web version](http://www.brocade.com/downloads/documents/html_product_manuals/NOS_411_AG/index.html "html") and
click on the
[pdf icon](http://www.brocade.com/downloads/documents/product_manuals/B_VDX/NOS_AdminGuide_v411.pdf "http://www.brocade.com/downloads/documents/product_manuals/B_VDX/NOS_AdminGuide_v411.pdf").
This makes printing based on the numbers provided easier. However the NOS Admin
Guide for v4.1.1 referenced was one version below the one on the html version.

Now the numbers referenced are the numbers in the document, not the one told by
the pdf viewer. So actually page 11 is page 13. Page 135 is 137. 311 is 313. 425
is 427. 517 is 519. 661 is 663. 714 is 716. I checked a few to make sure there
were no major increase due to version difference or elsewhere. One could with
[a bit of scripting](https://guldmyr.com/scripts/increasevalueofeachentry.py "python script")
increase each number with two like:

1,13-22,28-33,56-58,77-79,96,117,121,137-146,151,152,193,203-205,212,245-249,255,263,271,313-316,323,324,340-347,363-387,402,405,408,427-435,439,467,485,497,506,508,519-523,543,561,565,567,585,595,596,599,605-611,663-665,670,678,684,688,716,717

Cover page added to make it look nicer when printing. Old numbers:

**Network OS Administrator’s Guide v4.1.1 *53-1003225-01***

Pages
11-20,26-31,54-56,75-77,94,115,119,135-144,149,150,191,201-203,210,243-247,253,261,269,311-314,321,322,338-345,361-385,400,403,406,425-433,437,465,483,495,504,506,517-521,541,559,563,565,583,593,594,597,603-609,661-663,668,676,682,686,714,715
