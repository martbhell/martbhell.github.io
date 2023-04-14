---
title: "Time Sync for Linux VMs in VMWare Workstation"
date: 2011-02-27
categories: 
  - "it"
tags: 
  - "10-10"
  - "linux"
  - "ntp"
  - "ntpd"
  - "red-hat-enterprise"
  - "rhel"
  - "time-servers"
  - "time-sync"
  - "ubuntu"
  - "vmware"
  - "vmware-workstation"
---

You may have seen in my [previous post about EyeO](http://www.guldmyr.com/blog/eyeos-cloud-desktop-in-your-browser-part-2/ "eyeos time sync")S that I tried many things to get time in sync on the virtual OS. It was drifting lots of time and after a few hours it was an hour behind. Google tells me this is quite common but I could not find anything that decidedly fixed it.

run ntpdate every hour. This is not advised, primarily because it will add a lot of extra load after a while to the public(free) time servers. Especially if I want to have several machines up to date. One thought then was to set up a local ntpd and let other guest OS sync time with that. But then I could not get that in sync so we were back to square one.

others mention using VMWare tools time sync.

### My setup:

Intel Quad Core i7-920 8GB RAM Corsair XMS3 DDR3 1333MHz 8GB CL9 Gigabyte GA-EX58-UD3R Windows 7 x64 Vmware Workstation 7.1.1

### What works for me

#### For **ubuntu 10.10** x64:

Make sure vmware tools is installed (type vmware and hit 'tab'). With a .txt editor open up "vmname.vmx" on your host OS. Set tools.syncTime = "FALSE" to "TRUE". Restart vm.

Now on this particular machine I've had ntpd installed, but it is now uninstalled.

#### For Red Hat Enterprise Linux  5 x64 - **RHEL 5**:

- Install vmware-tools (without make/gcc installed).
- Set tools.syncTime = "TRUE"
- Set up ntpd with the below from ntp.conf
- Restart ntpd by getting root shell with 'su -' and then '/etc/init.d/ntpd restart'

I filled out the ntp-information during installation and then after wards I added the "tinker panic 0" which should let the ntpd make 'big jumps' and by commenting the fudge-line I chose not to use the local clock because this is drifting so much. More than 24 hours after I installed the OS the driftfile is still 0.000.

**ntp.conf:**

`tinker panic 0 restrict default kod nomodify notrap nopeer noquery`

`restrict 127.0.0.1 restrict -6 ::1`

`# Hosts on local network are less restricted. #restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap`

`server 0.rhel.pool.ntp.org server 1.rhel.pool.ntp.org server 2.rhel.pool.ntp.org`

`# Undisciplined Local Clock. This is a fake driver intended for backup # and when no outside source of synchronized time is available. #fudge  127.127.1.0 stratum 10`

`driftfile /var/lib/ntp/drift keys /etc/ntp/keys restrict 0.rhel.pool.ntp.org mask 255.255.255.255 nomodify notrap noquery restrict 1.rhel.pool.ntp.org mask 255.255.255.255 nomodify notrap noquery restrict 2.rhel.pool.ntp.org mask 255.255.255.255 nomodify notrap noquery`
