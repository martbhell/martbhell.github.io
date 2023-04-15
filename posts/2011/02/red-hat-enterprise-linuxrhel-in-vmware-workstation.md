---
title: Red Hat Enterprise Linux(RHEL) in VMWare Workstation
date: 2011-02-21
category: it
tags: kernel, linux, red, hat, enterprise, rhel, ssh, subscription, number, ubuntu, vmware, workstation

## Test with Red Hat Enterprise Linux (RHEL).

Download: Sign up for an evaulation on [https://access.redhat.com/downloads/](https://access.redhat.com/downloads/ "red hat download")

rhel-server-5.6-x86\_64-disc1.iso

VMWare Workstation does find this in "easy install". Not doing that this time.

20GBdisk (default) and 1552MB RAM (default 1024MB)

1. install in either graphical or text mode, going with graphical. There are also special modes. Maybe something similar to Ubuntu's minimal virtual kernel is available?
2. test cd
3. Mouse works!
4. Get subscription number with the help of this: https://access.redhat.com/kb/docs/DOC-15404. Copy paste did not work.
5. Filesystem stuff. Modify or not. Encrypt or not. I went with default and encryption. For encryption you need to set a boot password (min 8 chars).
6. IP/Timezone settings.
7. root password (not min 8 chars)
8. software sets - software development, virtualization, web server. I went with the two last. You can also customize it deeper. Like: gnome/kde? Printing support? Samba? I chose web server but mysql was not selected, not the php-mysql plugin for apache either. Virtualization is Xen - openfabrics enterprise distribution for RDMA/infiniband stuff.
9. cool stuff found: iptraf, hwbrowser, vnc
10. /root/install.log for install .. log.
11. After this it says that it will require all cds.. but I want to download them instead. How? proceeding anyway, let's see what happens. Maybe it gives the opportunity to download instead. Googling in the meantime. [Doesn't look good](http://www.techotopia.com/index.php/Performing_an_RHEL_5_Network_Installation "rhel network instal"). One way to do it would be to put the CDS/dvd on a network/http server in your LAN. But it does not mention a public repository etc.
12. Formatting, then installing. It asks for CD2. No other buttons. Getting DVD instead. rhel-server-5.6-x86\_64-dvd.iso
13. DVD went fine, nothing after this, just reboot.

## Booting

1. Insert LUKS password - the encryption password you entered before.
2. IPv6 failed during first boot.
3. Also some kind of disk monitoring.
4. Then a little configuration! This is nice. In ubuntu/debian it just goes into the system with a bunch of default setings.
5. Like firewall, enabled/disabled. Trusted srevices.
6. SELinux - 'improved' security controls, enforced/permissive/disabled. Keeping default: enforced.
7. no kdump
8. NTP! Enabling this, using default ntp servers (0.rhel.pool.ntp.org) and disabling 'use local time source'. This part contacts the NTP server during install, which worked, so that looks good.
9. Connect to RHN. Said yes. Takes a long time to register? no contact. Trying [this](https://rhn.redhat.com/rhn/help/reference/rhn500/en/s1-registration-yum.jsp "RHN registration red hat") later.
10. Set up a new user. You can use kerberos or NIS too from here.
11. Insert additional CDS
12. Login prompt!

## After login

1. VM -> Install VMWare Tools - I want to use "Unity" in Red Hat. I've used it for Windows XP (had a guest os for work) and it was great.
2. Right-click the tarball and 'extract to'. You need to have root access when you run it. So open a terminal and type 'su -' - this will give you the root prompt.
3. Then go to where you extracted it. ./vmware-install.pl.
4. Gives message that I apparently am running a Xen kernel and that this is not supported. Trying anyway. Answering yes as default on the questions.
5. Install was successful, opening configuration tool. Some green 'OK' s.
6. Before we can compile we need to have make and gcc installed. It also asks for kernel headers that it couldn't find. Going with the default "" on that.
7. memory manager, vmhgfs (filesystem driver for shared folders), vmxnet (fast ethernet), vmblock (drag 'n' drop), communication service, vsock, vmxnet3 (virtual network card), pvscsi,  - not installed because no compilation software like make/gcc installed.
8. x configuration, host resolution found but vm resolutions max at 800x600!?
9. restarting and it said good stuff, but unity does not work and resolution cannot be changed above 800x600.
10. accessing via ssh works fine too
