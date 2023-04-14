---
title: "Install FreeBSD in VirtualBox"
date: 2011-11-24
categories: 
  - "it"
tags: 
  - "bash"
  - "freebsd"
  - "install"
  - "operatingsystem"
  - "os"
  - "ports"
  - "virtualbox"
  - "virtualization"
---

## The Past

I used to run FreeBSD 5 and 6 about eight years ago on a Pentium III 900MHz machine with maybe 768MB RAM. It was very slow but after a lot of tinkering with the kernel I got it to boot and run very nicely.

Fluxbox was the window manager I used then together with Eterm and pico :)

## The Install

Installing it $today in a VirtualBox 4.1.6 on an IBM T40 running RHEL 6 x64.

I used the 'disc1' .iso of FreeBSD 8.2. Give it enough of RAM and bridged networking is probably what you want. If you have it set to NAT and then want to change you can do that 'online' while the virtual machine is online. Might be good to run another dhcp discover after though. And also don't forget to remove default route before that. (route del default).

Defaults are pretty OK I suppose on a VM. No need to mess around with the partitions or labels.

It's all done in the console menus and you can go back and forth between the menus. You probably want to enter the 'post-install' section to set ip, password, chose to install sshd. Add a new user and add it to the group 'wheel'. That way you can hit 'su -' to get root access.

## Using FreeBSD

After it's up you probably want to get root access: 'su -' Run 'dhclient INTERFACE' to get a dhcp ip. Find the interface name via ifconfig.

### Install Bash

If you chose to install [Ports](http://www.freebsd.org/ports/ "link to ports on freebsd.org") during install, you can go to /usr/ports and hit 'make search name="bash". You can use this to search for packages called bash. Then cd /usr/ports/shells/bash; make; make install; make clean

Then 'chsh' and change to /usr/local/bin/bash. Vi-syntax works so press i to insert, r to replace, x to remove or :wq! to write and quit.

### Update and use ports.

You can also search on freshports.org.

csup is a tool that you use to update the ports collection. Another is [portsnap](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/ports-using.html "to the handbook"). Portsnap appears to be a bit simpler and it came by default when I installed it.

portsnap fetch; portsnap extract; port portsnap update

Basically Ports consists of softwares' make files and some files pointing where to download the softwares when you decide to install them. You only need to run the portsnap extract the first time. Rest of the times fetch and update should do it. Or 'portsnap cron' if you do it in the scheduler/crontab.

Portaudit is a tool that checks for vulnerabilities in the softwares you use. This was very quick to install though. To see if you have any issues, hit 'portaudit -Fda'.

Each port or software should have a file called pkg-descr, you can use this to see what it does.

portsearch is one that you can use to search for ports instead of the 'make search'.

### sshd

You can ssh into the machine directly after installing, as long as it has IP connectivity (if you can ping it). You also cannot ssh in as root by default.

### firewalling

the firewall is 'ipfw'. This is not enabled by default. To enable it set firewall\_enable to YES in /etc/rc.conf. Make sure you add some good fw rules first. Or you can set firewall\_type="open" in rc.conf and then firewall\_script="/etc/ipfw.rules".

See [http://www.freebsd.org/doc/handbook/firewalls-ipfw.html](http://www.freebsd.org/doc/handbook/firewalls-ipfw.html) . There is a sample called 'inclusive ruleset'. This one you can paste into /etc/ipfw.rules , edit to your liking (change your public interface name, add dns-servers, comment out services you don't need (like port 80 if you for example do not have a web-server). You could then edit this script to have a

$cmd 00411 allow tcp from 192.168.0.0/24 to me 22 in via $pif setup limit src-addr 2

This would allow only addresses from the 192.168.0.0/24 network to ssh into your machine if you comment the rule that allows incoming on port 22 from anywhere.

ipfw list # to see the current firewall

## Conclusion

FreeBSD is special compared to a few other operating systems because you get to compile all the software. You can of course get binaries if you want and install via pkg\_add. But that's not so cool right? It's also a good idea to tweak the kernel, especially if you have a little slower system and want some better performance. If you have a slower system (like in a virtual machine), it could be painfully slow to install something. For example bash took what felt like forever to install for me.

This means a bit more patience is required with FreeBSD, but on the other hand maybe this way there will much be less crap installed.

Apparently FreeBSD 8.2 is not so cool because there is a [9 in beta](http://www.freebsd.org/where.html#helptest "where to get latest-latest release") or [PC-BSD](http://www.pcbsd.org/ "pcbsd.org"). If you want you can even get a 'snapshot' in the CURRENT subset, which is basically as new as it gets.
