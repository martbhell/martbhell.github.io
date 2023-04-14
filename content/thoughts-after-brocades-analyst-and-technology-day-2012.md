---
title: "Thoughts after Brocade's Analyst and Technology Day 2012"
date: 2012-09-13
categories: 
  - "it"
  - "storage"
tags: 
  - "brcdtechday"
  - "bcefe"
  - "bcefp"
  - "brocade"
  - "certifications"
  - "dcx"
  - "ethernet-fabric-nvgre"
  - "frame-striping"
  - "juniper"
  - "mercury"
  - "oem"
  - "openflow"
  - "openstack"
  - "qfabric"
  - "sdn"
  - "trunks"
  - "vcs"
  - "vdx-8770"
  - "vxlan"
---

Thursday today, the day after the Day. It was a real long day, and to my surprise it said 'press' on my pass - so I had to try to ask some questions :)

Some things picked up:

**\* New [VDX 8770 product released](http://www.brocade.com/products/all/switches/product-details/vdx-8770-switch/index.page "on brocade.com")** \- a modular Ethernet switch. Room for 384 10GbE ports. 100GbE ready and also ready for SDN protocols like [VXLAN](http://www.vmware.com/solutions/datacenter/vxlan.html "on vmware.com") (vmware) and [NVGRE](http://technet.microsoft.com/en-us/library/jj134174.aspx "on microsoft.com") (windows 2012). The VDX 8770 chassi is called "Mercury" internally in Brocade. I found it very similar to the DCX chassis  except that the supervisor modules are half-height.

\* Today Brocade **opened up registrations** for the [BCEFP certification](http://community.brocade.com/docs/DOC-2814 "it's free!") - Brocade Certified Ethernet Fabric Professional (which include the VDX8770), It looks advanced and you probably want to take the previous exam - [BCEFE](http://www.brocade.com/education/certification-accreditation/certified-ethernet-fabric-engineer/index.page "on brocade.com") - before.

\* SDN - **storage-defined network was the main focus of the day**. Fibre Channel was barely mentioned at all. [Ken Cheng](http://www.brocade.com/company/about-brocade/executive-profiles.page "on brocade.com")'s (one of the VPs of Brocade) definition of SDN:

### _"A set of technologies which are focused on achieving three objectives: network virtualization (vxlan), programmatic control (openflow) and cloud orchestration (openstack)."_

It was quite obvious that Brocade's VCS is the technique/medium which they intend to enable these new technologies. SDN is still quite immature (even though internet2 are already using it in their production network) - so be prepared to wait if you want ready solutions.

\* **VCS seems quite similar to QLogic's/Juniper's [QFabric](http://www.juniper.net/us/en/dm/datacenter/details/ "link to juniper.net")**. They had a hands-on lab where we could connect four smaller vdx switches and a vdx8770 (4-slot version). The switches had only had a unique ID set on them and their were end-devices (web-servers, web cams and a tablet) on different IP subnets on each switch. All I needed to do to connect switches (and devices) was to connect two switches via a fibre pair. Quite easy. Almost too easy to be true. This is something I really enjoy that's part of Fibre Channel. The technology has quite a few features, self-forming trunks being one of them (with frames being striped over all members of a trunk). It also gets rid of spanning tree (so no more unused links).

\* Quite **soon we should see Brocade's OEMs release embedded VDX switches** for their blade chassis. No news yet about which but lately IBM have been quick to release new Brocade products. As a side note: Brocade from start only sold their gear through OEMs, this is no longer always the case and they are trying to communicate more directly with customers.

\* Cost per bit was really important to push down for internet exchanges.

\* It's a lot easier to write a blog post on my wordpress blog via Chrome (on android) than via the native browser. Using my asus transformer tf101 as a note taking device for the day worked out great. Success!
