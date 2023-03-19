---
title: "Dragonfly - Testing another OS"
date: "2012-02-27"
categories: 
  - "it"
tags: 
  - "bsd"
  - "dragonfly"
  - "freebsd"
  - "operating-system"
  - "os"
  - "vmware"
  - "vmware-workstation"
---

# [http://www.dragonflybsd.org/](http://www.dragonflybsd.org/ "http://www.dragonflybsd.org/")

## Install

It's based on ... BSD! (FreeBSD 4.8 is apparently what dragonfly span off from)

What's weird is that while VMWare Workstation scans the iso (to find which OS it is) it stops responding (other VMs are unaffected). It finds FreeBSD 64-bit.

It has a 'hammer' filesystem. Apparently this is unsupported for FS under 10GB and not recommended for under 50G and will apparently require a lot of [things](http://leaf.dragonflybsd.org/cgi/web-man?command=newfs_hammer&section=8) (period clean-up job) occasionally.

     **HAMMER** file systems are designed for large storage systems, up to 1
     Exabyte, and will not operate efficiently on small storage systems.  The
     minimum recommended file system size is 50GB.  **HAMMER** must reserve 500MB
     to 1GB of its storage for reblocking and UNDO/REDO.  In addition, **HAMMER**
     file systems operating normally, with full history retention and daily
     snapshots, do not immediately reclaim space when files are deleted.  A
     regular system maintenance job runs once a day by [periodic(8)](http://leaf.dragonflybsd.org/cgi/web-man?command=periodic&section=8) to handle
     reclamation.

 

Nice and straight-forward console-based installation.

Quick and easy!

## Configure

As it's BSD, add the user to the 'wheel' group so that it can become super-user.

Guide to get sshd working (basically set PasswordAuthentication = yes). The guide mentions a lot of other things, but in 3.0.1 sshd is on by default and the keys have been generated.

## Install  software

Edit /usr/pkg/etc/pkgin/repositories.conf and add the URL to a repository near you.

pkgin update

pkgin full-update

pkgin search packagename

pkgin install bash

This installs bash to /usr/pkg/bin/bash

It's not enough to just edit /etc/passwd to get the new shell, you need to edit it via 'chsh'.

To install screen you need to

ln -s /usr/lib/libcrypt.so.4 /usr/lib/libcrypt.so.3

or it will complain that libcrypt.so.3 doesn't exist.

## The HAMMER filesystem

All commands start with 'hammer'. Like 'hammer info'.

 

## Conclusion

While looking at it from the above angle (quite distant) - this doesn't appear to be very different from other bsd/unix/linux distributions, a bit different commands to do some things but that's not so odd in itself.

Personally I like the name, maybe that's enough to use it? =)
