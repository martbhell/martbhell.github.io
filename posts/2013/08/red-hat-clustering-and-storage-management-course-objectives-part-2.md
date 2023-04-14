---
title: "Red Hat – Clustering and Storage Management – Course Objectives - part 2"
date: 2013-08-21
categories: 
  - "it"
tags: 
  - "certification"
  - "cluster"
  - "iscsi"
  - "linux"
  - "lvm"
  - "openstack"
  - "red-hat"
  - "rhce"
  - "storage"
---

Post 1 - [http://www.guldmyr.com/blog/red-hat-clustering-and-storage-management-course-objectives/](http://www.guldmyr.com/blog/red-hat-clustering-and-storage-management-course-objectives/) Where I checked out udev, multipathing, iscsi, LVM and xfs.

**This** post is about getting using luci/ricci to get a Red Hat cluster working, but not on a RHEL machine because sadly I do not have one available for practice purposes. So CentOS64 it is. Using openstack for virtualization.

Topology: Four hosts on all three networks, -a, -b and internal. Three cluster nodes and one management node.

Get the basic cluster going:

- image four identical nodes
- ssh-key is distributed
- /etc/hosts file has all hosts, IPs and networks
    - network interfaces are configured -
    - set a gateway in /etc/sysconfig/network
- firewall
    - all traffic allowed from -a and -b networks
    - at a minimum allow traffic from the network that the hostname corresponds to that you enter in luci
- dns (PEERDNS=no is good with several dhcp interfaces)
- timesync with ntpd
- luci installed on mgmt-node # ricci is a web gui
- ricci installed on all cluster nodes # this is the service talks with corosync
    - password set for user ricci on cluster nodes
- create cluster in luci
    - multicast perhaps doesn't work so well in openstack ?
    - on cluster nodes this runs "yum -y install cman rgmanager lvm2-cluster sg3\_utils gfs2-utils" if shared storage is selected, probably less if not.
- fencing is really important, how to do it in openstack would require a bit of work though. Not as easy as with kvm/xvm to send a destroy domain message.

Tests:

- Update and distribute cluster.conf
- Have a service run on a node on the cluster (doesn't have to have a shared storage for this).
- Commands:
    - clustat
    - cman\_tool
    - rg\_test test /etc/cluster/cluster.conf start service name-of-service
    - ccs\_config\_validate

 

Share an iSCSI target between all nodes:

- Using management node to share the iSCSI LUN.
- tgtd, multipath
- clvmd running on all nodes
- lvmconf - make sure locking is set correctly
- create vg with clustering
- partprobe; multipath -r # do this often
- vgs/lvs and make sure all nodes see the clusterd lv
- minimum GFS filesystem is around 128M - you didn't use all the vg right? =)
    - for testing/small cluster lowering the journal size is goodness
- mount!
