---
title: "ESXi + VMWare Workstation + OpenIndiana"
date: 2012-02-18
category: it
tags: esx, esxi, openindiana, vmware, vmware, workstation

### Before

Register and download ESXi here https://www.vmware.com/tryvmware/

Free license can be found there as well.

Get ESXi and the vSphere Client.

Get an OS to install in a VM (I chose openindiana).

### Install ESXi in VMWare Workstation 8.

40G disk, 4GB RAM, 2 cores, enable Virtualization.

Very fast install.

Actually, in VMWare Workstation you can do 'connect to server'. So for this you do not need the vSphere Client? Looks like through VMWare Workstation there's a lot less options. Supposedly you can upload stuff to the datastore through the vSphere Client, and possibly more. Basically in VMWare Workstation you can just create a VM and make basically the same settings on it as you would on a normal VM.

Username: root. No password.

In the console, enable ssh and stuff. Then you can scp and ssh to the esxi host.

/vmfs/volumes/datastore is where you want to put isos.

you can also browse to the datastore via http!

### Install OpenIndiana in a VMWare Workstation VM running ESXi.

Connect to the ESXi server in VMWare Workstation (connect to server, put in the IP of the ESXi VM, the IP is in the console).

After it's there just create a new VM and select a 'remote location' of the iso when you look under CD. I'm went with [openindiana](http://openindiana.org/ "oi.org").

8G disk, 1GB RAM, 1 CPU, "VM Network" (I presume this means the same as the one where the VM is). Nothing else special during install.

Feels a bit slow, but that could be because of the 1GB RAM. But I increased this to 2GB and still the Grub menu was slow to load.

### Using OpenIndiana

In the console hit: 'pfexec su -' to get to the root shell.

From the start I can ping a DNS-host on the internets. Great success.

#### Static IP in OI

If you don't want to use nwam and you want to have a static IP you do [this in the console](http://wiki.openindiana.org/oi/4.+System+Administration "follow this guide on wiki.openindiana"):

- Find interface name with 'ifconfig -a' or 'dladm showphys'. If it's not visible with ifconfig, it's not plumbed, so ifconfig devname plumb. For this example, we'll use e1000g0
- Disable NWAM: svcadm disable svc:/network/physical:nwam
- Set IP address in /etc/hostname.e1000g0: echo 1.2.3.4 > /etc/hostname.e1000g0
- Set netmask in /etc/netmasks (there's an example in there)
- Set default gateway in /etc/defaultrouter: echo 1.2.3.1 > /etc/defaultrouter
- Set DNS servers in /etc/resolv.conf (example: printf "nameserver 1.2.3.4\\nnameserver 2.3.4.5\\n" > /etc/resolv.conf)
- Enable default: svcadm enable svc:/network/physical:default
- Restart networking: svcadm restart svc:/milestone/network:default

After this, restart the system (init 6) and see if the settings stick. (I had to restart the VM twice but the IP setting stuck). The OI VM stuck at boot a few times after this as well. poweroff/restart got it back without any issues though.

#### Packages in OI

this is how to update your OI (no questions asked, just update everything).

pkg install pkg:/package/pkg pkg update

You can of course do a lot more, see [http://wiki.openindiana.org/oi/3.+Installing+software+and+package+management](http://wiki.openindiana.org/oi/3.+Installing+software+and+package+management "http://wiki.openindiana.org/oi/3.+Installing+software+and+package+management")

#### Installing stuff

pkg install irssi

easy peasy, no problems at all (and screen is installed by default!).

JAVA is already installed by default (1.6.0.26).

java -version
