---
title: "Vyatta: a router/vpn/firewall in a VM"
date: 2013-08-26
categories: 
  - "it"
  - "storage"
tags: 
  - "bcvre"
  - "brocade"
  - "certified"
  - "exam"
  - "open-source"
  - "virtualization"
---

Brocade has a beta exam up for [BCVRE](http://community.brocade.com/docs/DOC-3336) - Certified vRouter Engineer - which is on the Vyatta software from the company with the same name that Brocade bought last year.

There is the free open source core. Download from here: [http://vyatta.org/downloads](http://vyatta.org/downloads?whence=) (no you don't have to register).  The evaluation/[subscriber](http://www.vyatta.com/product/vyatta-network-os/get-started) version has the API and web gui available, I'll probably check those out closer to the exam date.

I grabbed VC6.6 - Virtualization ISO. Use it in a VM and assign 5GB disk (install only requires 1G, or you could just run it on the iso, but then it doesn't keep state between reboots) and 1GB RAM. Two NICs: One NAT and one private. But to get more acquainted with it you'll likely have to do a bit more configuration on the hypervisor side. Such as turn off dhcpd in your virtual networks.

To install it to disk: hit "install system" at the CLI after it's booted.

More documentation: [http://docs.vyatta.com/current/wwhelp/wwhimpl/js/html/wwhelp.htm](http://docs.vyatta.com/current/wwhelp/wwhimpl/js/html/wwhelp.htm) - there are descriptions how to get for example ssh management working ( set service ssh ).

The server is basically Debian with a more recent kernel (6.6 has 3.3) and a shell to make it more switch-like. It actually uses the bash completion to make it look like this. Check out /etc/bash\_completion.d/vyatta-\*

To remove a setting use "delete" (comparable to no in other CLIs). There is a web interface, but this is only for subscribers. Core version allows SNMP though if you want to use that :)

[What to do with vyatta](http://www.vyatta.org/documentation)? A bunch of tutorials are here: [http://www.vyatta.org/documentation/tips-tricks](http://www.vyatta.org/documentation/tips-tricks)

- NAT
- VPN (for example connect private cloud <-> Amazon VPN)
- Firewall
- Routing (OSPF, BGP, etc)

But no SDN stuff (separate data and the control plane). It looks like it's not possible to modify the flow table of a switch via Vyatta. This looks like a software router/VPN/firewall with some extras added to it.
