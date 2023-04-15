---
title: "Install Scientific Linux 6 in VMWare Workstation"
date: 2011-10-02
category: finland
tags: certification, kvm, learning, linux, red, hat, rhcsa, rhel, scientifix, linux, sl, studying, vmware, workstation

Time for some more Linux testing.

The reason for this is because I think I will go ahead and try to study for the [RHCSA](http://www.redhat.com/certification/rhcsa/ "on redhat.com") \- Red Hat Certified System Administrator. Work might send me to a course in December, probably wise to play around with it before this.

So here we go.

Scientific Linux (SL) is a free clone of Red Hat Enterprise Linux (RHEL). Historically it's been updated faster than CentOS. It's same as Enterprise Linux (EL) - it's re-compiled from source.

New VM, \\SL-61-x86\_64-2011-07-27-Install-DVD.iso, RHEL6 64-bit. 1 Core, 2G RAM, NAT, LSI Logic, New virtual disk, SCSI, 20G. Then boot the VM.

SL.org has this in pictures.

First thing you see is the Grub menu:

1. Install or Upgrade
2. Install with basic video driver
3. Rescue
4. Boot from local drive
5. Memtest (I like that memtest is pretty standard now)

Chose 1. Next screen is a graphical interface where you click and write, so you need keyboard/mouse. Next screen asks if you want local disks or external storage (fc, iSCSI, or zFCP - for system Z). Hostname: SL1.localdomain.

Create disks. **Custom/full size. xfs/encryption/lvm cannot be used for boot volumes.**

Role: Virtual Host (I want to try KVM). Enabling SL 6.1 and SL 6.1 Security Updates repositories.

Pinging to something on the Intertubes work from the start.

More posts coming with more fun stuff :)
