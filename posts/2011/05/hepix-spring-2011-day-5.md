---
title: HEPIX Spring 2011 – Day 5
date: 2011-05-10
category: it, storage
tags: cern, cern, vm, fs, cloud, cloudbursting, cvmfs, cvs, distribution, git, hepix, hepix, spring, 2011, http, national, grid, service, cloud, software, squid, svn, version, control, virtual, machine, vm
<!-- prettier-ignore -->
---

What day it is can be told by all the suitcases around the room.

## Version Control

An overview of the version control used in CERN. Quite cool, they're not using Git yet but they are moving away from CVS
to SVN (subversion) which is not updated anymore. Apparently hard to migrate.

They use DNS load balancing

- Browse code / logging, revisions, branches: WEBSVN – on the fly tar creation.
- TRAC – web SVN browsing tool plus: ticketing system, wiki, plug-ins.
- SVNPlot – generate SVN statsw. No need to **checkout** source code (svnstats do 'co').

[Mercurial](http://mercurial.selenic.com/ "selenic.com") was also suggested at the side of
[Git](http://git-scm.com/ "git-scm.com") (which is founded by Linus Torvalds).

Cern - VM - FS

Cern-VM-FS (CVMFS) looked very promising. The last one is not intended at the moment for images but more for sending
applications around. It uses Squid proxy server and looked really excellent. Gives you a mount point like /cvmfs/ and
under there you have the softwares.

[http://twitter.com/cvmfs](http://twitter.com/cvmfs)

Requirements needed to set it up:

- Rpms: cvmfs, -init-scripts, -keys, -auto-setup (for tier-3 sites does some system configs), fuse, fuse-libs, autofs
- squid cache – you need to have one. Ideally two or more for resilience. Configured (at least) to accept traffic from
  your site to one or more cvmfs repository servers. You could use existing frontier-squids.

## National Grid Service Cloud

A Brittish cloud.

Good for teaching with a VM – if a machine is messed up it can be reinstalled.

Scalability **\-
'[cloudbursting](https://sites.google.com/site/cloudcomputingwiki/Home/cloud-computing-vocabulary "definition")' –**
users make use of their local systems/clusters – until they are full – and then if they need to they can do extra work
in the cloud. Scalability/cloudbursting is the key feature that users are looking for.

Easy way to test an application on a number of operating systems/platforms.

Two cases were not suitable. Intensive – with a lot of number crunching.

**Good:** you don't have to worry about physical assembly or housing. They do have to install the servers and networking
etc. Usually this is done by somebody else. Images are key to making this easier.

**Bad:** [Eucalyptus](http://www.eucalyptus.com/ ".com") stability – not so good. Bottlenecks: networking is important.
More is required to the whole physical server when it's running vms.

To put a 5GB vm on a machine you would need 10GB. 5 for the image and 5 for the actual machine. Some were intending to
develop the images locally on this cloud and then move it on to Amazon.

Previous Days: [Day 4](https://www.guldmyr.com/hepix-spring-2011-day-4/ "day4")
[Day 3](https://www.guldmyr.com/hepix-spring-2011-%e2%80%93-day-3/ "day3")
[Day 2](https://www.guldmyr.com/hepix-spring-2011-%e2%80%93-day-2/ "day2")
[Day 1](https://www.guldmyr.com/hepix-spring-2011-day-1/ "day1")
