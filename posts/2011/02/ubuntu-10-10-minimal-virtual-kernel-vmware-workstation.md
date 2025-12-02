---
title: Ubuntu 10.10 Minimal Virtual Kernel + VMWare Workstation
date: 2011-02-07
category: it
tags: 10.10, apt, get, dns, finland, it, kernel, pico, time, servers, ubuntu, virtual, kernel, virtual, machine, vm, vmware, workstation
<!-- prettier-ignore -->
---

To install Ubuntu 10.10 with a virtual kernel instead of the normal one = good, less stuff installed that you may not
need.

1. When setting up the install, do not use the easy install. Chose to install an OS later. Set up bridged/nat depending
   on which one you want.
2. Add the install .iso to the CD-drive in the VM
3. Select a language
4. Press F4 (it didn't work in the first screen)
5. Chose - install a minimal virtual machine
6. Install Ubuntu Server
7. Chose language again
8. Chose key map - (I chose English and had to browse to Finland)
9. Asked to press some buttons, wanted Swedish (but have an English keyboard) so tried to press the right ones :p
10. Then time zone Helsinki/Finland was found.
11. Using default (whole disk, no encryption or lvm) for partitioning.
12. set up users
13. set up encryption on home dir
14. proxy setup
15. installing security updates automagically
16. any extra packages (DNS, LAMP, Mail, OpenSSH, etc)? - I chose no, want to chose this myself later.
17. yes I want grub (it finds only one OS on the virtual disk ;)

Then I see the login prompt! Obviously the easy-install in VMWare Workstation has a lot less steps :)

But on the other hand you could install OpenSSH directly through the install and then you do not have to log on to the
VM via VMWare Workstation, but can do it via your favorite ssh program instead.

## Post install

What I want installed every time after an uninstall. After install it is a very very small installation. Not even 'man'
is installed.

`sudo apt-get install openssh-server ntp nano`

- edit /etc/network/interfaces
- configure static ip
- edit /etc/ntp.conf
- add time servers
- edit ~/.bashrc
- change colors in the prompt and add color

Kernel difference you can see when running uname: 2.6.35-22-virtual in comparison to 2.6.35-22-generic

There!

Now you can set up whatever you want on it! Of course you may want to do more things, set up iptables or you could use
it like it is before the things I do after each install. You can use vi instead of nano/pico and use dhcp instead,
depends on what you are going to do with your VM.
