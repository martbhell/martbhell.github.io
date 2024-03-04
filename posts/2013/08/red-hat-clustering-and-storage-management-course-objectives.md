---
title: Red Hat - Clustering and Storage Management - Course Objectives
date: 2013-08-15
category: it, storage
tags: certification, cluster, iscsi, linux, lvm, openstack, red, hat, rhce, storage

Attending "Red Hat Enterprise Clustering and Storage Management" in August. Quite a few of these technologies I haven't touched upon before so probably best to go through them before the course.

Initially I wonder how many of these are Red Hat specific, or how many of these I can accomplish by using the free clones such as CentOS or Scientific Linux. We'll see :) At least a lot of Red Hat's guides will include their [Storage Server](http://www.redhat.com/products/storage-server/).

I used the course content summary as a template for this post, my notes are made within them.. below.

For future questions and trolls: this is not a how-to for lazy people who just want to copy and paste. There are plenty of other sites for that. This is just the basics and it might have some pointers so that I know which are the basic steps and names/commands for each task. That way I hope it's possible to figure out how to use the commands and such by RTFM.

## [Course content summary](http://www.redhat.com/training/courses/rh436/ "http://www.redhat.com/training/courses/rh436/")

### Clusters and storage

_Get an overview of storage and cluster technologies._

### ISCSI configuration

_Set up and manage iSCSI._

#### Step 1: Setup a server that can present iSCSI LUNs. A target

1. CentOS 6.4 - minimal. Set up basic stuff like networking, user account, yum update, ntp/time sync then make a clone of the VM.
2. Install some useful software like: yum install ntp parted man
3. Add a new disk to the VM

Step 2: Make nodes for the cluster.

1. yum install iscsi-initiator-utils

Step 3: Setup an iSCSI target on the iSCSI server.

[http://www.server-world.info/en/note?os=CentOS\_6&p=iscsi](http://www.server-world.info/en/note?os=CentOS_6&p=iscsi)

1. yum install scsi-target-utils
2. allow **port 3260**
3. edit /etc/tgt/target.conf
4. if you do comment out the ip range and authentication it's free-for-all

[http://www.server-world.info/en/note?os=CentOS\_6&p=iscsi&f=2](http://www.server-world.info/en/note?os=CentOS_6&p=iscsi&f=2)

Step 4: **Login** to the target from at least two nodes by running 'iscsiadm' commands.

Next step would be to put an appropriate file system on the LUN.

### UDEV

_Learn basic manipulation and creation of udev rules._

<http://www.reactivated.net/writing\_udev\_rules.html> is an old link but just change the commands to "udevadm" instead of "udev\*" and at least the sections I read worked the same.

udevadm info -a -n /dev/sdb

Above command helps you find properties which you can build rules from. Only use properties from one parent.

I have a USB key that I can pass through to my VM in VirtualBox, without any modifications it pops up as /dev/sdc.

By looking in the output of the above command I can create /etc/udev/rules.d/10-usb.rules that contains:

SUBSYSTEMS=="usb", ATTRS{serial}=="001CC0EC3450BB40E71401C9", NAME="my\_usb\_disk"

After "removing" the USB disk from the VM and adding it again the disk (and also all partitions!) will be called /dev/my\_usb\_disk. This is bad.

By using SYMLINK+="my\_usb\_disk" instead of NAME="my\_usb\_disk" all the /dev/sdc devices are kept and /dev/my\_usb\_disk points to /dev/sdc5. And on next boot it pointed to sdc6 (and before that sg3 and sdc7..). This is also bad.

To make one specific partition with a specific size be symlinked to /dev/my\_usb\_disk I could set this rule:

SUBSYSTEM=="block", ATTR{partition}=="5", ATTR{size}=="1933312", SYMLINK+="my\_usb\_disk"

You could do:

KERNEL=="sd\*" SUBSYSTEM=="block", ATTR{partition}=="5", ATTR{size}=="1933312", SYMLINK+="my\_usb\_disk%n"

Which will create /dev/my\_usb\_disk5 !

This would perhaps be acceptable, but if you ever want to re-partition the disk then you'd have to change the udev rules accordingly.

If you want to create symlinks for each partition (based on it being a usb, a disk and have the USB with specified serial number):

SUBSYSTEMS=="usb", KERNEL=="sd\*", ATTRS{serial}=="001CC0EC3450BB40E71401C9", SYMLINK+="my\_usb\_disk%n"

These things can be useful if you have several USB disks but you always want the disk to be called /dev/my\_usb\_disk and not sometimes /dev/sdb and sometimes /dev/sdc.

For testing one can use "udevadm test /sys/class/block/sdc"

### Multipathing

_Combine multiple paths to SAN devices into one fault-tolerant virtual device._

Ah, this one I've been in touch with before with fibrechannel, it also works with iSCSI. Multipath is the command and be wary of devices/multipaths vs default settings. Multipathd can be used in case there are actually multiple paths to a LUN (the target is perhaps available on two IP addresses/networks) but it can also be used to set a user\_friendly name to a disk, based on its wwid.

Some good commands:

service multipathd status
yum provides \*/multipath.conf # device-mapper-multipath is the package.
multipath -ll

Copy in default multipath.conf to /etc; reload and hit multipath -ll to see what it does. After that the [Fun](http://dwarffortresswiki.org/index.php/Fun) begins!

### Red Hat high-availability overview

_Learn the architecture and component technologies in the Red Hat® High Availability Add-On._

[https://access.redhat.com/site/documentation/en-US/Red\_Hat\_Enterprise\_Linux/6/html/High\_Availability\_Add-On\_Overview/index.html](https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/High_Availability_Add-On_Overview/index.html)

### Quorum

_Understand quorum and quorum calculations._

### Fencing

_Understand Fencing and fencing configuration._

### Resources and resource groups

_Understand rgmanager and the configuration of resources and resource groups._

[https://access.redhat.com/site/documentation/en-US/Red\_Hat\_Enterprise\_Linux/6/html/High\_Availability\_Add-On\_Overview/ch.gfscs.cluster-overview-rgmanager.html](https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/High_Availability_Add-On_Overview/ch.gfscs.cluster-overview-rgmanager.html)

### Advanced resource management

_Understand resource dependencies and complex resources._

### Two-node cluster issues

_Understand the use and limitations of 2-node clusters._

[http://en.wikipedia.org/wiki/Split-brain\_(computing)](http://en.wikipedia.org/wiki/Split-brain_(computing))

### LVM management

_Review LVM commands and Clustered LVM (clvm)._

#### Create **Normal LVM** and make a **snapshot**

[Tutonics](http://www.tutonics.com/2012/11/ubuntu-lvm-guide-part-1.html#.UgtWonUW1Ls) has a good "ubuntu" guide for LVMs, but at least the snapshot part works the same.

1. yum install lvm2
2. parted /dev/vda # create two primary large physical partitions. With a CentOS64 VM in openstack I had to reboot after this step.
3. pvcreate /dev/vda3 pvcreate /dev/vda4
4. vgcreate VG1 /dev/vda3 /dev/vda4
5. lvcreate -L 1G VG1 # create a smaller logical volume (to give room for snapshot volume)
6. mkfs.ext4 /dev/VG1/
7. mount /dev/VG1/lvol0 /mnt
8. date >> /mnt/datehere
9. lvcreate -L 1G -s -n snap\_lvol0 /dev/VG1/lvol0
10. date >> /mnt/datehere
11. mkdir /snapmount
12. mount /dev/VG1/snap\_lvol0 /snapmount # mount the snapshot :)
13. diff /snapmount/datehere /mnt/datehere

Revert a Logival Volume to the state of the snapshot:

1. umount /mnt /snapmount
2. lvconvert --merge /dev/VG1/snap\_lvol0 # this also removes the snapshot under /dev/VG1/
3. mount /mnt
4. cat /mnt/datehere

### XFS

_Explore the Features of the XFS® file system and tools required for creating, maintaining, and troubleshooting._

[https://access.redhat.com/site/documentation/en-US/Red\_Hat\_Enterprise\_Linux/6/html/Storage\_Administration\_Guide/xfsmain.html](https://access.redhat.com/site/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/xfsmain.html)

yum provides \*/mkfs.xfs

yum install quota

XFS Quotas:

mount with uquota for user quotas, mount with uqnoenforce for soft quotas. use xfs\_quota -x to set quotas help limit

To illustrate the quotas: set a limit for user "user":

xfs -x -c "limit bsoft=100m bhard=110m user"

Then create two 50M files. While writing the 3rd file the cp command will halt when it is at the hard limit:

\[user@rhce3 home\]$ cp 50M 50M\_2
cp: writing \`50M\_2': Disk quota exceeded
\[user@rhce3 home\]$ ls -l
total 112636
-rw-rw-r-- 1 user user 52428800 Aug 15 09:29 50M
-rw-rw-r-- 1 user user 52428800 Aug 15 09:29 50M\_1
-rw-rw-r-- 1 user user 10477568 Aug 15 09:29 50M\_2

### Red Hat Storage

_Work with Gluster to create and maintain a scale-out storage solution._

<http://chauhan-rhce.blogspot.fi/2013/04/gluster-file-system-configuration-steps.html>

<http://servicesblog.redhat.com/2012/07/31/updates-to-the-red-hat-enterprise-clustering-and-storage-management-course/>

### Comprehensive review

_Set up high-availability services and storage._
