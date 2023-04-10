---
title: "HEPIX Spring 2011 – Day 3"
date: "2011-05-05"
categories: 
  - "it"
  - "storage"
tags: 
  - "adaptec"
  - "buffered-tape-marks"
  - "cern"
  - "cloud"
  - "ermm"
  - "errata"
  - "hepix"
  - "hepix-spring-2011"
  - "ibm"
  - "ioapps"
  - "ioreplay"
  - "ipv4"
  - "ipv6"
  - "lustre"
  - "oracle"
  - "scientific-linux"
  - "service-now"
  - "sl"
  - "strace"
  - "sun"
  - "t10000c"
  - "tape-drive"
  - "tsm"
---

Day 3 woop!

An evaluation of [gluster](http://www.gluster.org/ "gluster.org"): uses distributed metadata, so no bottleneck that comes with a metadata server, can or will do do some replication/snapshot.

Virtualization of mass storage (tapes). Using IBM's TSM (Tivoli Storage Manager) and [ERMM](http://www-935.ibm.com/services/de/igs/pdf/br-stor-enterprise-remove-mm-en.pdf "links to pdf on ibm.com"). Where ERMM manages the libraries, so that TSM only sees the link to the ERMM. No need to set up specific paths from each agent to each tape drive in each library. They were also using Oracle/SUN's T10000c tape drives that goes all the way up to 5TB - which is quite far ahead of LTO consortium's LTO-5 that only goes to 1.5/3TB per tape. Some talk about [buffered tape marks](http://publib.boulder.ibm.com/infocenter/zos/v1r10/index.jsp?topic=/com.ibm.zos.r10.idad500/buftms.htm "on boulder.ibm.com") which speeds up tape operations significantly.

Lustre success story at GSI. They have 105 servers that provide 1.2PB of storage and max throughput seen is 160Gb/s. Some problems with

**Adaptec 5401** – boots longer than entire linux. Not very nice to administrate. Controller complains about high temps – and missing fans of non-existing enclosures. Filter out e-mails with level “ERROR” and look at the ones with “WARNING” instead.

Benchmarking storage with trace/replay. Using strace (comes default with most Unixes) to record some operations and the [ioreplay](http://code.google.com/p/ioapps "ioapps on google code") to replay them. Proven to give very similar workloads. Especially great for when you have special applications.

IPv6 - [running out of](http://www.potaroo.net/tools/ipv4/ "clear") IPv4 addresses, when/will there be sites that are IPv6? Maybe if a new one comes up? What to do? Maybe collect/share IPv4 addresses?

Presentations about the evolve needed of two data centers to accomodate requirements of more resource/computing power.

Implementing ITIL with [Service-Now](http://www.service-now.com/ "service-now") (SNOW) at CERN.

[Scientific Linux](http://www.scientificlinux.org/ ".org") presentation. Live CD can be found here:

[www.livecd.ethz.ch](http://www.livecd.ethz.ch/). They might [port NFS 4.](http://pnfs.com/ "pnfs.com")1 that comes with Linux Kernel 2.6.38 to work with SL5. There aren't many differences between RHEL and SL but in SL there is a tool called [Revisor](https://www.scientificlinux.org/distributions/6x/build/sites "howto"), which can be used to create your own linux distributions/CDs quite easily.

 

Errata is a term - this means security fixes.

Dinner later today!

 

Next Days: [Day 5](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-5/ "day5") [Day 4](http://www.guldmyr.com/blog/hepix-spring-2011-day-4/ "day4")

Previous Days: [Day 2](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-2/ "day2") [Day 1](http://www.guldmyr.com/blog/hepix-spring-2011-day-1/ "day1")
