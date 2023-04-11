---
title: "Ubuntu 10.10 + VMWare + Irssi"
date: "2011-02-10"
categories: 
  - "it"
tags: 
  - "10-10"
  - "apt-get"
  - "debian"
  - "debian-6"
  - "guide"
  - "irssi"
  - "it-2"
  - "kernel"
  - "linux"
  - "networking"
  - "ram"
  - "swap-space"
  - "ubuntu"
  - "virtual-kernel"
  - "vm"
  - "vmware"
  - "vmware-workstation"
---

How small VM can you make if you are only going to use it to run [Irssi](http://irssi.org/ "irssi.org") in a [screen](http://www.gnu.org/software/screen/ "screen")?

OS: Ubuntu 10.10 x64 Virtual Kernel Hypervisor: VMWare Workstation

Disk - no logs - 1.10GB is what my previous took, with samba, so probably less but 1.1 should be all right, don't want it to run out of space either. Should probably partition /var/log into its own so that if that fills up (maybe after bruteforce ssh logins) then it doesn't fill up the rest of /. RAM -

- turn off cron jobs
- install virtual kernel

about the cron jobs, I just installed a ubuntu virtual kernel and only cron job running (as seen in syslog) is this:

CRON\[9141\]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

### Test 1

1.2GB disk 64MB RAM

Kernel panic - not syncing: attempted to kill init! ctrl-alt-del in the VM doesn't work, had to hard kill it :p Reboot - same problem. It does this after selecting minimal virtual kernel and pressing install Ubuntu Server.

### Test2

Increased RAM to 96MB and now it passed. However, after selecting keyboard it still crashes. So 96 is also too little.

Googled around a little and found an [article on Ubuntu.com](https://help.ubuntu.com/community/Installation/LowMemorySystems "ubuntu install lowmemsystems") that gives some insight.

For example: if you run out of memory, then it will swap. So if you are not running out of memory then it's probably better to give it a little more to be on the safe side.

### Test 3

Increased RAM to 128MB Now it goes even longer.

Partitioning -> chose manual. There is a device there 'sda' -> SCSI3. Mark that and hit enter. Say yes to create new empty partition. Then it creates a new space pri/log. Create new partition.

As size, type in: 100MB Primary, beginning, default settings on the filesystem etc but mount point: /var/log. Then done setting up this partition.

Then we will create another partition for / (or the rest).

Like this:

\[caption id="attachment\_341" align="alignnone" width="150" caption="ubuntu\_partition right"\][![ubuntu_partition right](images/ubuntu_partition.png "ubuntu_partition right")](http://www.guldmyr.com/blog/wp-content/uploads/ubuntu_partition.png)\[/caption\]

The above does not include a swap space, and the installation complains that there is no swap space defined and that there may be problems if this is not configured during install.

Let's see :)

\*\* maybe Ubuntu is not the slimmest OS to install for this purpose. The guide I linked to above mentions a DSL - damn small linux. But we want a minimal server OS, not a desktop one. Maybe the new Debian 6 would be cool to try.

During install there was a dialogue about something being already on the disk.. and that this could cause issues. Maybe this was copied there from one of the previous tries with less amount of RAM. Went back and erazed this on each just to be on the safe side. Very slow though. About 1% / s. After this I went into each and set them to format instead. It mentions old installation files anyway. Proceeding. This happened twice? Three times now.. Maybe this is not going so well. Ok happened four times.

Hit Alt+F2 (and then enter to get the console) and then df -h. Nothing is over 20% except the SR0/cd-rom which is at 100%. Did a 'more /var/log/syslog' and at the end there are some 'Out of memory' things going on.

So there we go. 128MB is too little.

But [here](https://help.ubuntu.com/community/Installation/SystemRequirements#Ubuntu%20Server%20%28CLI%29%20Installation "ubuntu install reqs"):  it says that 128MB is the requirement..

### Test 4

I will try to install again and not mess up with the partitions. 1.2GB and 128MB again. Going pretty well, looks like it's stopped at 75% and "storing language". Patience. Ok, 10mins later still there. Nothing about out of memory in /var/syslog. The Guest was behaving a little slow though when working the console. Left it on over night and when I looked again the following day it was at the next step!

Installing openssh via the installation menu this time. Taking quite long time this time as well. Like hours. 2 hours now. Nothing happening in syslog. Think I'll give Debian a shot next Test.

In the meantime did Test 5. However 4 hours later, still configuring 'language-pack-en-base'.

Now, approximately lots of hours later. It is at configure grub.

And yay, it finally boots!

user@irssi:~$ df -h Filesystem            Size  Used Avail Use% Mounted on /dev/sda1             1.1G  430M  606M  42% / none                   54M  164K   54M   1% /dev none                   57M  4.0K   57M   1% /dev/shm none                   57M   36K   57M   1% /var/run none                   57M     0   57M   0% /var/lock none                  1.1G  430M  606M  42% /var/lib/ureadahead/debugfs /home/martbhell/.Private 1.1G  430M  606M  42% /home/martbhell

And the size of the folder in Windows: 750 MB (787 341 312 bytes)

With 128MB ram there is maybe 10MB free and it swaps a little (just a few kB so far).

### Test 5

debian-6.0.0-amd64-netinst Using Debian 5 64-bit.

1. graphical menu is seen, no advanced options used
2. chose languages - look a lot like Ubuntu but there are some differences:
3. After choosing a hostname it asks for domain. Put in WORKGROUP.
4. Set a root account password (so no more sudoing - probably just add my user to the wheel/root group).
5. and you have a few more options in the partitioning, like a separate /home partition
6. then you get to chose a debian mirror (becuase I use the netinst). ftp.fi.debian.org is the one I chose
7. you can participate in a "most used packages" survey
8. software selection: graphical desktop, web, dns, ssh, laptop, standard system utilities. I chose SSH and standard system utilities.
9. grub, then reboot and loading!

Internet works fine from the start. apt-get update; apt-get install irssi Remember, here you have to log in as root to run ifconfig or apt-get.

It's the same way in Debian as in Ubuntu to set static ip. Just edit /etc/network/interfaces / don't forget you can just restart the networking services by '/etc/init.d/networking start' instead of rebooting ;) Now, I actually forgot to set minimal ram/disk for this one. So we have to do this again ;)

### Test 6

debian-6.0.0-amd64-netinst Using Debian 5 64-bit. 128MB RAM

One thing that's cool about a VM is that you can resize the amount of RAM whenever (probably good to turn off the guest first). So how about just lowering it instead of installing a new one?

OK, so it now has 512MB. Going down to 64 in one go (listed as minimum in VMWare Workstation).

It's swapping after just a few minutes with screen+irssi.

_to sort by memory usage in top press SHIFT+m_

biggest memory hogs (all over 1% - figures in **bold**) are :

1474 user 20   0 23388 6220 1572 S  0.0 **11.2** 0:00.25 bash 1503 user 20   0 50084 5228 3824 S  0.0  **9.4** 0:00.06 irssi 1470 root      20   0 70488 3280 2584 S  0.0  **5.9** 0:00.03 sshd 913 root      20   0  117m 1788  904 S  0.0  **3.2** 0:00.01 rsyslogd 1473 user 20   0 70488 1680  964 S  0.0  **3.0** 0:00.06 sshd 1502 user 20   0 25184 1472  992 S  0.0  **2.6** 0:00.01 screen 1546 user 20   0 19040 1300 1004 R 99.9  **2.3** 0:00.01 top 985 root      20   0 22392  712  512 S  0.0  **1.3** 0:00.00 cron 1233 Debian-e  20   0 44140  660  392 S  0.0  **1.2** 0:00.00 exim4 1472 root      20   0  5928  620  520 S  0.0  **1.1** 0:00.00 getty 1 root      20   0  8352  616  560 S  0.0  **1.1** 0:01.42 init 1277 root      20   0 49168  544  428 S  0.0  **1.0** 0:00.00 sshd

What I might be able to get rid of is rsyslogd and cron. But then again, if I were to connect this to the internet so I could access it and resume the screen/irssi from anywhere, I would want to keep track of what is happening on the machine.

user@debian:/var/log$ df -h Filesystem            Size  Used Avail Use% Mounted on /dev/sda1             3.8G  638M  3.0G  18% / tmpfs                  28M     0   28M   0% /lib/init/rw udev                   23M  140K   23M   1% /dev tmpfs                  28M     0   28M   0% /dev/shm

Windows usage: 887 MB (930 816 000 bytes)

### Summary

The Ubuntu Server 10.10 with the minimal virtual kernel took forever to install (maybe it would have been faster to have more mem during install and then lower when it's done) and with 128MB it still swaps a little with only screen and irssi running. But it does use about 130MB or 200MB less space than the Debian6 guest.

The Debian 6 however runs OK with 64MB, swaps a little at that though so I would probably run this with 96 or 128MB just to be on the safe side if I were to run it.
