---
title: HEPIX Spring 2011 - Day 4
date: 2011-05-09
category: it, storage
tags: eofs, hepix, hepix, spring, 2011, iaas, lustre, öl, open, source, oracle, oracle, linux, virtual, machine, virtual, machine, image, virtualization, vm

Dinner on the 3rd night was amazing. It was at the hotel Weisse Schwan in Arheilgen outside Darmstadt and it was a nice reception hall with big round tables, waiters with lots of wine and great buffet food. A+

[Cloudy day](http://molnmolnmoln.se "moln@IDG")!

## Or - Infrastructure as a Service - IaaS

A few had the standpoint that the HEP community is not ready for cloud, not secure enough and we have something that's working. But maybe a mix period would work. At least for now it's quite awesome for non i/o intensive applications.

There were talks about virtual images and how to (securely) transfer them between sites. Several options about this, [stratuslab](https://twitter.com/#!/@StratusLab "on twitter") cloud distribution of images and cloudscheduler.

One great use case for running computing nodes in the cloud is at the moment for when the cluster is maxed out - then you can kick up some more vms in the cloud to help speed up the run. Or when running the jobs it keeps the VM running as long as jobs that require that kind of VMs are in the queue. Or for testing - quite easy to set up several VMs with different operating systems/platforms and then run testing on them. See [cloudscheduler.org](http://cloudscheduler.org/ "cloudscheduler")

[cloudscheduler](http://cloudscheduler.org/ "cloudscheduler")Infrastructure as a Code - IaaC - see [Opscode and Chef](http://www.opscode.com/chef/ "opscode.com"). A pretty interesting looking  configuration management system.

﻿Terms: fairshare [json](http://www.json.org/ ".org")

## Oracle

Maybe the most interesting presentation at the end of the day - and the debate following was maybe the most - it was the presentations from Oracle Linux and Oracle Open Source.

Before the presentation they had a nice slide stating that they don't make any promises based on the presentation. That presentation is not available but the [other one is](http://indico.cern.ch/getFile.py/access?contribId=27&sessionId=9&resId=0&materialId=slides&confId=118192 "slide2") - the one about Oracle and Open Source..

[Oracle Linux](http://oracle.com/linux "oracle.com") (OL) looks pretty good, it's free to download but if you want any updates you need to pay them. They have an upgrade thing so if you're on RHEL6 you can apparently update easily (changes some yum repos). A lot of advertisement - but it was a presentation about the distribution. It's based on RHEL, they take the updates from RHEL, then add their own magic to it. They have a boot setup so if you want to you can boot OL in Red Hat Compatibility mode. Apparently Oracle wants to put Red Hat out of business (after which they were asked: "Where will you get the kernel then?"). x86-64 only.

#### On the horizon:

- btrfs(fs that supports error detection, CoW, snapshots, ssd optimization, small files are put in metadata)
- vswitch(full network switch, set up virtual network in the OS, ACL, VLAN, QoS, flow monitoring with openFlow)
- Zcache(keep more pages of the fs page cache longer in main memory, more cache using LZO compression and thus fewer I/O operations - a lot faster to compress/uncompress than to access disk)
- storage connect
- linux containers (resource management, jails on bsd, zones on solaris, own apps/libs/root, runs on top of the kernel, not a virtualization).

## From the discussion

Pidgin – some wanted Video. Pidgin said: no way. This is how Oracle will run their open source projects like MySQL, Lustre.

_**“If you don't like how the project is going – fork.” - Gilles Gravier.**_

Two reasons to fork: proactively (worried) or because they are unhappy with how it's going (how it's going or not going).

\---

People in the audience are afraid that a lot of times a company acquires an open source project and then closes it down.

\---

_“When you acquire a company and it's the projects. You have two options if don't want the project. Drop it or kill it. Kill it does not work for open source.” - Gilles Gravier._

Openoffice is not dropped yet. Lots of other options. Fork and work on closed source (like Grid Engine). Drop it and stop working on it. Drop it and “talk to the community”. ---

No info about Lustre – when asked about it Oracle did not want to comment. Asked to e-mail [gilles.gravier@oracle.com](mailto:gilles.gravier@oracle.com) for more information. --- Will Oracle port debconf to Oracle Linux? Oracle will take a look. --- There was lot of angst against Oracle that surfaced, but Oracle handed it quite well and had good answers. --- From one of the Oracles: “Allow me to be a bit provocative: If Oracle's prices were lower; would you consider buying an Oracle product?” ---

_“It takes 25 years to make a good reputation, 5 minutes to loose it.”_ - CERN employee. _“SUN used to make hardware and give away software for free; Oracle is .. the other way around.”_ \- Lenz Grimmer _“Laughter”_ \- Audience.

## European Open File System SCE

- [http://www.eofs.org](http://www.eofs.org/)
- one repository of lustre
- hpcfs.org is another lustre open source – this will merge with opensfs.org. Both are American.
- Close work together with eofs.org – the two above have agreed on a set of improvements.
- 2.1 lustre will be released by Whamcloud in summer 2011.
- LUG – lustre user group – reports and interviews at [http://insidehpc.com](http://insidehpc.com/)

Next Day: [Day 5](https://www.guldmyr.com/hepix-spring-2011-%e2%80%93-day-5/ "day5")

Previous Days: [Day 3](https://www.guldmyr.com/hepix-spring-2011-%e2%80%93-day-3/ "day3") [Day 2](https://www.guldmyr.com/hepix-spring-2011-%e2%80%93-day-2/ "day2") [Day 1](https://www.guldmyr.com/hepix-spring-2011-day-1/ "day1")
