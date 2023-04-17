---
title: Red Hat Certification – RHCE – Network Services – NFS
date: 2012-05-14
category: it
tags: centos, certification, file, transfer, linux, nfs, red, hat, rhce, studying

[1st post](http://www.guldmyr.com/red-hat-certification-rhce-system-configuration-and-management-2/ "1st post") \- System Management and Configuration

[Objectives](https://www.redhat.com/training/courses/ex300/examobjective "on redhat.com")

# Network services

Network services are an important subset of the exam objectives. RHCE candidates should be capable of meeting the following objectives for each of the network services listed below:

- Install the packages needed to provide the service.
- Configure SELinux to support the service.
- Configure the service to start when the system is booted.
- Configure the service for basic operation.
- Configure host-based and user-based security for the service.

User should be able to do the following for all these services:

- [http/https](https://guldmyr.com/red-hat-certification-rhce-network-services-httpd)
- [dns](https://guldmyr.com/red-hat-certification-rhce-network-services-dns)
- [ftp](http://www.guldmyr.com/red-hat-certification-rhce-network-services-ftp)
- [nfs](http://www.guldmyr.com/red-hat-certification-rhce-network-services-nfs/)
- smb
- smtp
- ssh
- ntp

## NFS:

Testing an NFS server is generally easier from another linux-server.

- Install the packages needed to provide the service.

- yum install nfs ?? (already installed on mine)

- Configure SELinux to support the service

- getsebool -a |grep nfs

- Configure the service to start when the system is booted.

- chkconfig nfs on
- edit /etc/fstab on the client to mount on boot

- Configure the service for basic operation.

- server#: mkdir /foo
- server#: vi /etc/exports

- /foo          192.168.0.0/24(rw)

- server#: iptables - port 2049 tcp and udp
- server#: service nfs start
- client#: mount -t nfs IP:/foo /mnt
- server#: mkdir /foo/upload
- server#: chown username.username /foo/upload
- server#: chmod 777 /foo/upload
- client#: touch /mnt/upload/file2
- server#: cd /net/ip.to.server/foo

- Configure host-based and user-based security for the service

- iptables to deny hosts
- add permissions appropriately in /etc/exports

- man exports

## Extra

- Provide network shares to specific clients.

- Add a new folder / line in /etc/exports and only allow certain clients to connect to it

- Provide network shares suitable for group collaboration.

- With the help of permissions. Use unix group ID number or names.
