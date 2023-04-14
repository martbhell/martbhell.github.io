---
title: "Red Hat Certification - RHCSA - Preparation"
date: 2011-12-09
category: it
tags: boot, booting, certification, chcon, context, iso, kickstart, kvm, libvirt, linux, network, qemu, red, hat, rhcsa, selinux, studying, virt, manager

\[toc\]

[https://github.com/mconigliaro/RHCE-Cheat-Sheet](https://github.com/mconigliaro/RHCE-Cheat-Sheet "https://github.com/mconigliaro/RHCE-Cheat-Sheet")

Found this "cheat sheet" for RHCE. Sure it doesn't specifically say RHCSA but honestly there's a lot of good commands in there. Some things obviously might be too advanced for RHCSA, such configuring an dns/named service. But it might be good as a reference.

The objectives of the RHCSA exam: [https://www.redhat.com/certification/rhcsa/objectives/.](https://www.redhat.com/certification/rhcsa/objectives/ "https://www.redhat.com/certification/rhcsa/objectives/") I copied the ones I'm unsure about below.

I think definitely it would be a good idea to go through these objectives before taking the exam, and if you have time - do each step as well!

There's a bunch of things there that I'm not sure about or know how to do. I'm attending a five day RHCSA rapid track course, so we should be able to go through the stuff I don't know there, but doesn't hurt to do a little preparation!

This post is about: me going through each objective and trying to accomplish it. Writing it down is for you, but mostly for me :) If you have any questions there is the comment field below.

The lists are the objectives, first level is the actual objective while the sub-lists are commands, thoughts and comments.

I'm writing this and updating it as I go along. It's purpose is to prepare for the exam, without using any 'cheats' like trying to find out labs/questions that comes on the exam.

## Understand and Use Essential Tools

- Access remote systems using ssh and VNC

- In each VM's setting you can specify port etc to the VM.
- vnc client:

- Create hard and soft links

- ln -s file1 file2 #soft
- ln file1 file2 #hard
- ls -lia
- [wikipedia entry](http://en.wikipedia.org/wiki/Ln_%28Unix%29#Difference_b.2Fw_Hard_Link_and_Symbolic_.28soft.29_link "on wikipedia")

- adjust process priority with renice,

- renice
- nice
- top #to view, also in ps -fe -o pid,comm,nice
- /etc/security/limits.conf

- Access a virtual machine's console

- Open virt-manager and open the VM.

- Start and stop virtual machines

- Open virt-manager and stop/start there.
- CLI: virtsh.

### Add virtualization post-install.

To test: installing with only Desktop. Packages, modules, services?

After install 'lsmod|grep kvm' doesn't show anything. Went into Add/Remove Software and added stuff under 'Virtualization'. After install, just trying to start virt-manager doesn't work. It asks if libvirt service is running. 'service libvirtd start'. Then virt-manager starts and finds the qemu. No need to reboot as 'chkconfig --list|grep libv' shows that they start on boot. Booting a machine after this works.

## Configure Local Storage

- Create and configure LUKS-encrypted partitions and logical volumes to prompt for password and mount a decrypted file system at boot

- You can set this up while installing the system.
- /etc/crypttab
- /etc/fstab still necessary

- Configure systems to mount file systems at boot by Universally Unique ID (UUID) or label

- fstab: LABEL= and UUID=
- Find label/UUID with blkid, set label with e2label.

- Add new partitions, logical volumes and swap to a system non-destructively

- \# non-destructively? so without making the system unbootable?

You can format, partition a drive and encrypt it after install. In desktop you can go to places and find the drive in there, that will open a dialogue where you put in the password and tada. After that you can hit 'df -h' to get the UUID and mountpoint. This you then put in /etc/crypttab. Don't forget to add it to /etc/fsstab too. But, be careful here. I managed to screw it up so much that it wouldn't even boot anymore.

[This is a great guide for how to set up a LUKS partition and mount it on boot.](http://rhce.co/configure-systems-to-mount-ext4-luks-encrypted-and-network-file-systems-automatically.html "on rhce.co") Works for partitions created outside install.

When I did 'custom layout' in install and set up encryption, it appears to take a lot longer to encrypt/format. If doing this in the exam I'd consider making a small partition. Especially not a 16GB one. It took ~15minutes in comparison to 5s. It was however fast to create with cryptsetup post-install. If you do decide to split up the filesystem (perhaps one partition per VM) then you'll need to set appropriate selinux settings to make it work.

### Create LUKS partition to boot from post-install

During install:

vdisk in vmware of 20GB. One partition of 500MB for /boot One swap of 512MB One pg of 10GB, VG of the same, and lv for / Keeping available space of about 9GB.

After boot:

1. fdisk -c -u /dev/sda
2. n, p, 4, enter, enter, t, 4, 83, w

1. new partition, primary, partition 4, starting, end (space), set type, partition 4, type 83, write

4. some error, but fdisk -l shows the new partition /dev/sda4
5. rebooted (tool advised to)
6. cryptsetup luksFormat /dev/sda4
7. cryptsetup luksOpen /dev/sda4 luksdrive
8. ls /dev/mapper/ will show luksdrive in there.
9. mkfs.ext4 /dev/mapper/luksdrive
10. edit /etc/crypttab and add: /dev/mapper/luksdrive /dev/sda4

1. man crypttab

12. edit /etc/fstab and add: /dev/mapper/luksdrive /mnt/luksdrive ext4 defaults 1 2

1. man fstab

14. mkdir /mnt/luksdrive
15. mount -a
16. cd /mnt/luksdrive
17. try a reboot

### Mount filesystem based on UUID or label

**By UUID:** If you for example like above have created another partition and encrypted it and added it to fstab. You could just hit 'blkid' to get the UUID of the partition. Then you can change the /dev/mapper/luksdrive on the fstab into UUID=12354-515-51-5. To try it out, hit mount -a.

**By label:** set it with 'e2label /dev/mapper/luksdrive lukslabel'. Then in fstab add LABEL=lukslabel instead of /dev/mapper/luksdrive. To view label hit: blkid. If there is none set, it's not shown.

## Create and Configure File Systems

- Mount, unmount and use LUKS-encrypted file systems

- cryptsetup luksOpen /dev/sda4 luksdrivelabel
- mount -t filesystem /dev/mapper/luksdrivelabel /mnt/luksdrive
- touch /mnt/luksdrive
- umount /mn/luksdrive

- Mount and unmount CIFS and NFS network file systems

- mount -t nfs -o rw host:/remotedir /mnt/nfs
- mount -t cifs //server/share /mnt/cifs --verbose -o user=username
- umount /mnt/dir

- Extend existing unencrypted ext4-formatted logical volumes
- Create and configure set-GID directories for collaboration

- A chmod on a directory that changes group owner of all files under that directory, into the same as the directory.
- mkdir /share
- touch /share/1
- chgrp wheel/share
- chmod g+s /share
- touch /share/2
- ls -l /share/

- Create and manage Access Control Lists (ACLs)

- first you need to [add acl](http://rhce.co/create-and-manage-access-control-lists-acls.html "on rhce.co") on the file system in /etc/fstab
- getfacl
- setfacl -m g:wheel:rw /path/file

### Mount NFS file system

First, we need to [set up an nfs server](http://aaronwalrath.wordpress.com/2011/03/18/configure-nfs-server-v3-and-v4-on-scientific-linux-6-and-red-hat-enterprise-linux-rhel-6/ "aaronwalrath"), this is not part of RHCSA though.

**on server:** mkdir /nfs;chmod a+w /nfs Make sure nfs-utils and rpcbind are installed. chkconfig --list  # check nfs, nfslock and rpcbind are on edit /etc/export # /nfs IP/netmask(rw,sync,no\_root\_squash) setsebool -P nfs\_export\_all\_rw check /etc/hosts.allow and .deny starts services

**on client:** mkdir /mnt/nfs mount.nfs 192.168.0.17:/nfs /mnt/nfs -v -w or mount -t nfs -o rw 192.168.0.17:/nfs /mnt/nfs

### ACL on filesystem

- mount # see options on your filesystem
- vi /etc/fstab # change 'defaults' to the what you saw in 'mount' and add acl, comma separated
- mount -o remount / # use this to remount /. Or you could reboot. Hard to unmount / if you are using it.
- mount # now it has rw,acl
- getfacl /root/install.log
- setfacl -m g:wheel:rw /root/install.log
- getafcl /root/install.log

### Extend existing unencrypted ext4-formatted logical volumes

## Deploy, Configure and Maintain Systems

- Configure systems to boot into a specific runlevel automatically

- /etc/inittab

- Install Red Hat Enterprise Linux automatically using Kickstart
- Configure a physical machine to host virtual guests
- Install Red Hat Enterprise Linux systems as virtual guests
- Configure systems to launch virtual machines at boot

Installed SLC6.1 in a VM. This time I chose both Virtual Host and Desktop Environment and X11 for packages. In VMWare Workstation 8 and the settings for the VM, do enable 'virtualization' in the processor options or you cannot virtualize inside the VM. It's a lot easier to setup/install VM if you have a desktop GUI. Especially the part about you getting access to the console.

Post-install there is a GUI tool in the menu that you can use to install a VM and configure VM-stuff.

By default the virtual machine starts on boot. In chkconfig --list. There is an entry called 'libvirt-guests'. This is a fairly complex script that looks where the VMs are installed and boots them. You can go into the settings of the VM in the GUI and enable it to boot when the host boots. _By the way, if there are issues during boot, see /var/log/boot.log_

### Install a VM via an http server.

yum install php

This installs httpd with php-support.

### firewall

Add port 80 in the firewall: iptables-save > fwrules. Copy the one with port 22, paste and add port 80. iptables-restore < fwrules.

To keep the rules on reboot:

/etc/init.d/iptables save

### Copy DVD into your web root:

This assumes that the DVD is mounted automagically which it does for me.

sudo mkdir /var/www/html/SL6; sudo cp -pR /media/nameofdisk/\* /var/www/html/SL6

If you use the -p that means it preserves the read/write permissions on the files, beceause it's mounted as a CD/DVD that means the files are read-only. If you want to do changes don't use the -p or you'll have to change that stuff later.

### To set SELINUX context:

chcon -R --reference=/var/www /var/www/html/SL6.

### Install from HTTP

Launch the virtualization manager. Create new VM. Name and network transfer, point to your httpd. RAM, disk space. Chose network interface - I only had NAT. (if you follow my guide below you'll need to set static IP settings). After that the machine boots and you get a console. It starts graphical and then install continues as usual. If you want to see which IP your VM in the VM gets you can look in the access\_log in /var/log. By default it got an address in 192.168.122.\* range. If you set too little memory you cannot get the kdump.

### Bridged networking

follow [this guide](http://www.techotopia.com/index.php/Creating_an_RHEL_6_KVM_Networked_Bridge_Interface "on techotopia") (incomplete) or one on [linuxtopia](http://linuxtopia.org/online_books/rhel6/rhel_6_virtualization/rhel_6_virtualization_sect-Virtualization-Network_Configuration-Bridged_networking_with_libvirt.html "linuxtopia") or on [libvirt wiki](http://wiki.libvirt.org/page/Networking#Bridged_networking_.28aka_.22shared_physical_device.22.29 "libvirt")

1. ifdown eth0
2. cd /etc/sysconfig/network-scripts
3. cp ifcfg-eth0 ifcfg-bridge0
4. edit ifcfg-eth0 and add 'BRIDGE="bridge0" '
5. edit ifcfg-bridge0 and set 'DEVICE="bridge0" ', 'TYPE="Bridge" ', 'DELAY="0" '
6. TYPE needs to be Bridge, capital B.
7. ifup eth0
8. ifup bridge0
9. ifconfig bridge0 192.168.0.17
10. add a rule similar to -A INPUT -i bridge0 -j ACCEPT in the iptables (don't forget to save/restart iptables)
11. edit /etc/resolv.conf with 'nameserver ip.ip.ip.ip'.
12. /etc/sysctl.conf and enable ip\_forwarding. Reboot or sysctl -p /etc/sysctl.conf
13. consider adding static IP addresses in ifcfg-bridge0. My DHCP didn't work, probably because of some configration in VMWare Workstation. BOOTPROTO="static", IPADDR, NETMASK, GATEWAY, NM\_CONTROLLED="no", ONBOOT="yes".

### Installing with the help of kickstart

First, copy the /root/anaconda-ks.cfg to /var/www/html/SL6/ks.cfg. Also set permissions to the file as appropriate. Then open that file in system-config-kickstart. You probably want to change some stuff. For HTTP server install set server to: 192.168.0.17 and path to SL6. That's if your path is . And of course add the whole URL to the ks.cfg. Remove virtualization packets. Change hdd layout stuff, you probably have less space available this time. Change URL to repository. Mine was still set to CD/ROM so had to manually set that during boot. Got two questions during the install: do you want to overwrite what's on the disk? And, reboot? at the end of install. Consider removing these to speed up install. Also, I could not log on after first reboot. Even though I kept the root password as is.

In system-config-kickstart: Set it to clear MBR, initialize labels and also to autoreboot upon completion. For root password you need to manually enter, you can set it to plaintext. Set setupagent to disabled for a completely automatic install. Repository you cannot change in system-config-kickstart. Manually edit the ks.cfg.

repo --name --baseurl=http://192.168.0.17/SL6 user --name user --plaintext --password 112233

Last one creates a user called user with pw 112233.

### How-to Boot into CD in VM in qemu

Download the .iso. Add new storage hardware, make it an IDE CD-ROM, hit add existing storage and select the .iso, set type to 'raw'. Change boot order.

## Manage Users and Groups

- adjust password aging for local user accounts

- chage

- Set enforcing and permissive modes for SELinux

- sestatus to see current setting
- /etc/selinux/config # for settings
- Command to set it 'on the fly':

- List and identify SELinux file and process context

- files: ls -Z
- processes: ps -e fZ

- Restore default file contexts

- chcon -R --reference=/var/www/html /var/www/html/SL6
- chon -t usr\_t /var/www/html/SL6
- restorecon -v /var/www/html/SL6

- Use boolean settings to modify system SELinux settings

- setsebool
- to find the available settings: getsebool -a

- Diagnose and address routine SELinux policy violations

- Tool 'sealert'. Logs are in /var/log/audit
- There is also a GUI tool.
