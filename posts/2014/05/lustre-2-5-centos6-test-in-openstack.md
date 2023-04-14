---
title: "Lustre 2.5 + CentOS6 Test in OpenStack"
date: 2014-05-30
category: storage
tags: centos, linux, lustre, openstack

Reason: Testing to Lustre 2.5 from a clean CentOS 6.5 install in an openstack.

Three VMs: two servers, one MDS, one OSS and one Client. CentOS65 on all. An open internal ethernet network for the lustre traffic (don't forget firewalls). Yum updated to latest kernel. Two volumes presented to the lustreserver and lustreoss for MDT + OST, both are at /dev/vdc. Hostnames set. /etc/hosts updated with three IPs: lustreserver,  lustreoss and lustreclient.

With 2.6.32-431.17.1.el6.x86\_64 there's some issues at the moment for building the server components. One needs to use the latest branch for 2.5 so the instructions are [https://wiki.hpdd.intel.com/pages/viewpage.action?pageId=8126821](https://wiki.hpdd.intel.com/pages/viewpage.action?pageId=8126821 "https://wiki.hpdd.intel.com/pages/viewpage.action?pageId=8126821")

## Server side

**MDT/OST:** Install e2fsprogs and reboot after yum update (to run the latest kernel kernel).

yum localinstall all files from: http://downloads.whamcloud.com/public/e2fsprogs/1.42.9.wc1/el6/RPMS/x86\_64/

Next is to rebuild lustre kernels to work with the kernel you are running and the one you have installed for next boot: [https://wiki.hpdd.intel.com/display/PUB/Rebuilding+the+Lustre-client+rpms+for+a+new+kernel](https://wiki.hpdd.intel.com/display/PUB/Rebuilding+the+Lustre-client+rpms+for+a+new+kernel)

RPMS are here: http://downloads.whamcloud.com/public/lustre/latest-feature-release/el6/server/SRPMS/

For rebuilding these are also needed:

yum -y install kernel-devel\* kernel-debug\* rpm-build make libselinux-devel gcc

basically:

- git clone -b b2\_5 git://git.whamcloud.com/fs/lustre-release.git
- autogen
- install kernel.src from redhat (puts tar.gz in /root/rpmbuild/SOURCES/)
- if rpmbuilding as user build, then copy files from /root/rpmbuild into /home/build/rpmbuild..
- rebuilding kernel requires quite a bit of hard disk space, as I only had 10G for / then I made symlinks under $HOME to the $HOME/kernel and $HOME/lustre-release

yum -y install expect and install the new kernel with lustre patches and the lustre and lustre modules.

Not important?: WARNING: /lib/modules/2.6.32-431.17.1.el6.x86\_64/weak-updates/kernel/fs/lustre/fsfilt\_ldiskfs.ko needs unknown symbol ldiskfs\_free\_blocks

/sbin/new-kernel-pkg --package kernel --mkinitrd --dracut --depmod --install 2.6.32.431.17.1.el6\_lustre

chkconfig lustre on

edit /etc/modprobe.d/lustre.conf and add the lnet parameters

modprobe lnet lctl network up # lctl list\_nids

creating MDT: mkfs.lustre --mdt --mgs --index=0 --fsname=wrk /dev/vdc1 mounting MDT: mkdir /mnt/MDT; mount.lustre /dev/vdc1 /mnt/MDT

creating OST: mkfs.lustre --ost --index=0 --fsname=wrk --mgsnode=lustreserver /dev/vdc1 mounting OST: mkdir /mnt/OST1; mount -t lustre /dev/vdc1 /mnt/OST1

## Client Side

rpmbuild --rebuild --without servers

cd /root/rpmbuild/RPMS/x86\_64 rpm -Uvh lustre-client\*

add modprobe.d/lustre.conf modprobe lnet lctl network up lctl list\_nids

mount.lustre lustreserver@tcp:/wrk /wrk

lfs df!
