---
title: Red Hat Certification – RHCE – Network Services – FTP
date: 2012-05-12
category: it
tags: centos, certification, file, transfer, ftp, linux, red, hat, rhce, studying

[1st post](https://www.guldmyr.com/red-hat-certification-rhce-system-configuration-and-management-2/ "1st post") \- System Management and Configuration

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
- [ftp](https://www.guldmyr.com/red-hat-certification-rhce-network-services-ftp)
- nfs
- smb
- smtp
- ssh
- ntp

## FTP

An ftp-server is also quite easy to test. You can test it from many web-browsers, telnet, ftp, lftp or a myriad of other clients.

- Install the packages needed to provide the service.

- yum install vsftpd

- Configure SELinux to support the service

- this might be more interesting, you may need to do some magic here for sharing files
- getsebool -a|grep ftp

- Configure the service to start when the system is booted.

- chkconfig vsftpd on

- Configure the service for basic operation.

- for basic - only open firewall then start the service
- that is enough for anonymous read to /var/ftp/pub/

- cp /root/anaconda-ks.cfg /var/ftp/pub/
- chmod 755 /var/ftp/pub/anaconda-ks.cfg

- Configure host-based and user-based security for the service

- iptables to deny hosts
- you can deny users by putting them in /etc/vsftpd/ftp\_users and/or user\_list
- in vsftpd.conf there is a tcp\_wrappers variable

## Extra

- Configure anonymous-only download

- Deny all other users :)
