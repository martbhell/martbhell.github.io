---
title: pdsh - parallell distributed shell
date: 2012-11-10
category: it
tags: distributed, shell, hpc, pdsh, rpmforge, shell
<!-- prettier-ignore -->
---

[pdsh](https://code.google.com/p/pdsh/ "https://code.google.com/p/pdsh/")

This a software to run commands on a set of servers.

For example 'pdsh -a uname -av' will give you "uname -av" of all machines.

[http://techsnail.com/howtos-tutorials/installing-pdsh-on-hpc-cluster/](http://techsnail.com/howtos-tutorials/installing-pdsh-on-hpc-cluster/ "http://techsnail.com/howtos-tutorials/installing-pdsh-on-hpc-cluster/")

It can be installed from rpmforge.0

wget <http://packages.sw.be/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.x86\_64.rpm>
rpm -ivh rpm-release\*
yum install pdsh

after that you can immediately run "pdsh -w oss1,client1 uname -av" to run a command on a remote node.

It's possible to set up so that it executes on a pre-defined list. Check out /etc/machines.

Extremely useful if you want to save some time :)
