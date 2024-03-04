---
title: Access Gateway - NPV - TR
date: 2012-05-11
category: storage
tags:
  access, gateway, brocade, cisco, ipm, mds, npiv, npv, qlogic, san, storage,
  transparent, mode
---

## Say what??

[Access Gateway](http://www.brocade.com/solutions-technology/technology/platforms/fabric-os/access_gateway.page "link to brocade.com") -
Brocade

[NPV](http://datacenteroverlords.com/2012/05/08/npv-and-npiv/ "great discussion in the comments on this post by the way") (N_port
Virtualization (not NPIV) - Cisco

[Transparent Mode](http://community.brocade.com/thread/6267?start=0&tstart=0 "on brocade.com") -
QLogic

These are all names for the basic idea / functionality but as there's no
standard the vendors have made up their own names for it.

A switch in Access Gateway (AG) mode does not consume Domain IDs, you can do
port mapping, needs NPIV on the port in the switch that it connects to. AG
requires a switch / fabric to connect to as it doesn't run the normal fibre
channel services.

It is very useful in case you are going to mix vendors in your fabric. Meaning
you can populate the core with Brocade switches and then connect other vendors'
switches in the above modes to the Brocade switches.

On some QLogic switches you can also set a port into TR-mode,
see [this post](http://h30499.www3.hp.com/t5/Storage-Area-Networks-SAN-Small/Can-I-connect-HP-8-20q-to-HP-8-24c-via-TR-port/td-p/5723725#.UAfyrNIgcak "hp.com") on
HP's EBC forum about how to do it. It is not exactly the same as AG or NPV,
because you still need to do zoning on the QLogic switch.

There is also the IPM by Qlogic for IBM - it looks like a module that you cannot
switch between 'fabric' and 'IPM' mode. Which is what you can do on a Cisco or
on a Brocade switch.
