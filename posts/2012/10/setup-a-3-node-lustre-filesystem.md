---
title: Setup a 3 Node Lustre Filesystem
date: 2012-10-13
category: storage
tags: centos, cluster, filesystem, install, kernel, linux, lustre, mds, oss, ost, rhel, rpmbuild, san, storage, vmware, yum
<!-- prettier-ignore -->
---

# Introduction

Lustre is a filesystem often used by clusters because many computers can mount
the filesystem simultaneously.

This is a small log/instruction for how to setup
[Lustre](http://wiki.whamcloud.com/display/PUB/Documentation "whamcloud wiki")
in 3 virtualized machines (one metadata server, one object storage server and
one client).

Basic components:

- VMWare Workstation [3 x CentOS](http://www.nic.funet.fi "finnish mirror") 6.3
  VMs.
- Latest Lustre from
  [Whamcloud](http://www.whamcloud.com/ "http://www.whamcloud.com/")

To use Lustre your kernel needs to support it. There's a special one for server
and one for the client. Some packages are needed on both.

Besides lustre you'll need an updated version of e2fsprogs as well (because the
version that comes from RHEL6.3 does not support large partitions).

Starting with the MDS. When the basic OS setup is done will make a copy of that
to use for OSS and Client.

# Setup basic services

## Install an MDS

This will run the MDT - the metadata target.

- 2GB RAM, 10GB disk, bridged networking
- 500GB for /boot, rest for / (watch out, it may create a really large swap).

Minimal install.

Setup OS networking (static ip for servers, start on boot, open port 988 in
firewall, possibly some for outgoing if you decide to restrain that too), run
yum update and setup ntp.

Download latest lustre and e2fsprogs to /root/lustre-client, lustre-server and
e2fsprogs appropriately (x86_64).

Lustre also does not support selinux, so disable that.

- works fine with it in enforcing until time to create mds/mdt
- also fine with permissive until it's time to mount.

Put all hostnames into /etc/hosts. Poweroff and make two full clones. Set
hostname.

## Install an OSS

This will contain the OST (object storage target). This is where the data will
be stored.

- Networking may not work (maybe device name changed to eth1 or eth2).
- You may want to change this afterwards to get the interface back to be called
  (eth0).
- [A blog post](http://www.banym.de/linux/centos/change-network-device-name-from-eth1-back-to-eth0)
  about doing that.

## Install a client

This will access and use the filesystem.

Clone of the OSS before installing any lustre services or kernels.

# Install Lustre

Before you do this it may be wise to take a snapshot of each server. In case you
screw the VM up you can then go back :)

## Starting with the MDS

Installing e2fsprogs, kernel and lustre-modules.

Skipping debuginfo and devel packages, installing all the rest.

```bash
yum localinstall \
kernel-2.6.32-220.4.2.el6_lustre.x86_64.rpm kernel-firmware-2.6.32-220.4.2.el6_lustre.x86_64.rpm \
kernel-headers-2.6.32-220.4.2.el6_lustre.x86_64.rpm \
lustre-2.2.0-2.6.32_220.4.2.el6_lustre.x86_64.x86_64.rpm \
lustre-ldiskfs-3.3.0-2.6.32_220.4.2.el6_lustre.x86_64.x86_64.rpm \
lustre-modules-2.2.0-2.6.32_220.4.2.el6_lustre.x86_64.x86_64.rpm
```

The above was not the order they were installed. Yum changed the order so that
for example kernel-headers was last.

```bash
yum localinstall e2fsprogs-1.42.3.wc3-7.el6.x86_64.rpm \
e2fsprogs-debuginfo-1.42.3.wc3-7.el6.x86_64.rpm \
e2fsprogs-devel-1.42.3.wc3-7.el6.x86_64.rpm \
e2fsprogs-libs-1.42.3.wc3-7.el6.x86_64.rpm \
e2fsprogs-static-1.42.3.wc3-7.el6.x86_64.rpm \
libcom_err-1.42.3.wc3-7.el6.x86_64.rpm \
libcom_err-devel-1.42.3.wc3-7.el6.x86_64.rpm \
libss-1.42.3.wc3-7.el6.x86_64.rpm \
libss-devel-1.42.3.wc3-7.el6.x86_64.rpm
```

After boot, confirm that you have lustre kernel installed by typing:

`uname -av` and `mkfs.lustre --help`

to see if you have that and `rpm -qa 'e2fs*'` to see if that was installed
properly too.

By the way, you probably want to run this to exclude automatic yum kernel
updates:

`echo "exclude=kernel*" >> /etc/yum.conf`

After install and reboot into new kernel it's time to

1. `modprobe lustre`
1. start creating MDT, OST
1. then mount things!
1. But hold on to your horses, first we ned to install the client :)

## And then the Client

Install the e2fsprogs\*

We cannot just install the lustre-client packages, because we run a different
kernel than the ones that whamcloud have compiled the lustre-client against.

We can either back-pedal and install an older kernel. Or we can build (from
source / SRPMS) a lustre-client that works on a kernel of our choosing. The
later option seems like a better way, because we can then upgrade the kernel if
we want to.

### Build custom linux-client rpms

Because of [a bug](http://jira.whamcloud.com/browse/LU-1868) it appears that
some ext4 source packages are needed - while they are not. You need to add some
parameters to ./configure. This will be the topic of a future post.

The above rpmbuild should create rpms for the running kernel. If you want to
create rpms for a non-running kernel
[you are supposed to be able to run.](http://wiki.whamcloud.com/display/PUB/Rebuilding+the+Lustre-client+rpms+for+a+new+kernel "whamcloud wiki")

# Configure Lustre

[Whamcloud have good instructions](http://wiki.whamcloud.com/display/PUB/Create+and+Mount+a+Lustre+Filesystem).
Don't be afraid to check out their wiki or use google.

/var/log/messages is the place to look for more detailed errors.

## On the MDS

Because we do not have infiniband you want to change the parameters slightly for
lnet to include tcp(eth0). These changes are not reflected until reboot (quite
possibly something else) - but just editing a file under /etc/modprobe.d/ called
for example lustre.conf is not enough.

Added a 5GB disk to the mds.

```bash
fdisk -cu /dev/sdb; n, p, 1, (first-last)
modprobe lustre lnet
mkfs.lustre --mdt --mgs
mount
```

## On the OSS

Also add the parameters into modprobe.

`mkfs.lustre --ost` and `mount`

## On the client

Add things into modprobe.

mount!

Write something.

Then hit: `lfs df -h`

To see usage!

# Get it all working on boot

You want to start the MDS, then the OSS and last the client. But while it's
running you can restart any node and eventually it will start working again.

Fstab on **the client**: `ip@tcp:/fsname /mnt lustre defaults,_netdev 0 0`

Fstab on **the OSS and MDS**: `/dev/sdb1 /mnt/MDS lustre defaults,_netdev 0 0`

While it's running you can restart any node and eventually it will start working
again.
