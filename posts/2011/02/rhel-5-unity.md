---
title: RHEL 5 + Unity
date: 2011-02-22
category: it
tags: depositories, fedora, linux, red, hat, rhel, unity, vmware, workstation

See my [previous post](http://www.guldmyr.com/red-hat-enterprise-linuxrhel-in-vmware-workstation/) for how to install it.

A couple of days later and the [time is still in synch](http://www.guldmyr.com/time-sync-for-linux-vms-in-vmware-workstation/ "rhel synch vmware workstation"). When I logged on there was a pop-up saying there were some updates. Put in root password and you get to see which are updates, the ones with a symbol next to them requires a reboot (kernel update in my case).

The VNC that was installed was a VNC client, not the server. There aren't that many packages by default - this is probably because all depositories are not enabled and that this is not Fedora.

After installing vmware-tools, a reboot or two and the resolution can be changed to larger than 800x600. And Unity works as well!
