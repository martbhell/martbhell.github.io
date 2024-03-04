---
title: Factory reset of a Brocade SAN switch
date: 2013-07-18
category: storage
tags: access, gateway, ag, brocade, factory, reset, licenses
<!-- prettier-ignore -->
---

Ever wondered which is the easiest way?

Using the "configDefault --all" does not clear everything, for example it doesn't clear: system name, zoning, etc.

Setting the switch to AG mode (Access Gateway) - will clear more things as it basically dumbs down the switch, it does not remove the licenses, IP and password.

ag --modeenable
ag --modedisable

The 'ag --modedisable' (puts switch back in normal switch mode) command sets the default zones access to No Access, so if you want to merge this switch into a fabric you'll most likely need to change that and disable/enable the E\_Ports.

Quite often there are some good tips on the Brocade's [community forum](http://community.brocade.com/ "http://community.brocade.com/").
