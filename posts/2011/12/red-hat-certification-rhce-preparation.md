---
title: Red Hat Certification - RHCE - Preparation
date: 2011-12-18
category: it
tags: certification, linux, red, hat, rhcsa, studying

Wow, there's lots of it in there. Some of it is about networking and a lot about individual services. I haven't actually planned to go get the exam soon, but I think just going through these objectives will make me better at Linux. Anyway, if I pass the RHCE, that extends the RHCSA expiration automagically.

This is going to take a while to do. I will update this post as I progress through the sections.

This is a copy of the objectives from [https://www.redhat.com/certification/rhce/objectives/](https://www.redhat.com/certification/rhce/objectives/ "on redhat.com")

## System Configuration and Management

### Routing / NAT

- Route IP traffic and create static routes
- Use iptables to implement packet filtering and configure network address translation (NAT)

For the two above I think I need to use another machine. Maybe the IBM T40 could be of some use again. Install SLC via USB maybe! /2011 12 18: update: Nope, T40 didn't like booting like that. So, booting via DVD instead. But, maybe I can boot via the small CD and then load the files off of an NFS-server instead. Turns out the CPU in my laptop does not have PAE and thus cannot install anything after RHEL5(possibly) with the default isos. There is a guide on scientificlinux.com that tells you how to do it [via a fedora netinstall iso](http://scientificlinuxforum.org/index.php?showtopic=621 "http://scientificlinuxforum.org/index.php?showtopic=621").

### Other

- Use /proc/sys and sysctl to modify and set kernel run-time parameters
- Configure system to authenticate using Kerberos
- Configure a system as an iSCSI initiator that persistently mounts an iSCSI target
- Produce and deliver reports on system utilization (processor, memory, disk, and network)
- Use shell scripting to automate system maintenance tasks

### rsyslog

- Configure a system to log to a remote system
- Configure a system to accept logging from a remote system

## Network Services

Network services are an important subset of the exam objectives. RHCE candidates should be capable of meeting the following objectives for each of the network services listed below:

- Install the packages needed to provide the service
- Configure SELinux to support the service
- Configure the service to start when the system is booted
- Configure the service for basic operation
- Configure host-based and user-based security for the service

RHCE candidates should also be capable of meeting the following objectives associated with specific services:

## HTTP/HTTPS

- Configure a virtual host
- Configure private directories
- Deploy a basic CGI application
- Configure group-managed content

## DNS

- Configure a caching-only name server
- Configure a caching-only name server to forward DNS queries
- Note: Candidates are not expected to configure master or slave name servers

## FTP

- Configure anonymous-only download

## NFS

- Provide network shares to specific clients
- Provide network shares suitable for group collaboration

## SMB

- Provide network shares to specific clients
- Provide network shares suitable for group collaboration

## SMTP

- Configure a mail transfer agent (MTA) to accept inbound email from other systems
- Configure an MTA to forward (relay) email through a smart host

## SSH

- Configure key-based authentication
- Configure additional options described in documentation
