---
title: Red Hat Certification – RHCE – Network Services – ssh
date: 2012-06-06
category: it
tags: centos, certification, file, transfer, linux, openssh, red, hat, rhce, ssh, sshd, studying, tcp, wrapper

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
- [nfs](https://www.guldmyr.com/red-hat-certification-rhce-network-services-nfs/)
- [smb](https://www.guldmyr.com/red-hat-certification-rhce-network-services-smb/)
- [smtp](https://www.guldmyr.com/red-hat-certification-rhce-network-services-e-mail/)
- [ssh](https://www.guldmyr.com/red-hat-certification-rhce-network-services-ssh/)
- ntp

## SSH

To test from windows you can use putty.

But in linux you just need ssh for client and sshd for server.

man 5 sshd\_config and [this blogpost](http://www.aboutlinux.info/2005/10/using-tcp-wrappers-to-secure-linux.html "on aboutlinux.info") has an overview.

- Install the packages needed to provide the service.

- yum install openssh

- Configure SELinux to support the service

- getsebool -a|grep ssh

- Configure the service to start when the system is booted.

- chkconfig sshd on

- Configure the service for basic operation.

- /etc/ssh/sshd\_config

- Configure host-based and user-based security for the service

- iptables

- port 22 (TCP)

- tcp.wrapper

### TCP Wrapper

More info in man tcpd and man 5 hosts\_access

Check that your daemon supports it:

which sshd
ldd /usr/sbin/sshd|grep wrap

For this test, let's say that the server you are configuring has IP/netmask 192.168.1.1/24 and that you have a client on 192.168.0.0/24

cat /etc/hosts.allow

sshd: 192.168.0.0/255.255.255.0
sshd: ALL : twist /bin/echo DEATH

The last row sends a special message to a client connecting from a non-allowed network.

cat /etc/hosts.deny

ALL: ALL

If you on the server with these settings try to do "ssh -v root@localhost" or "ssh -v root@192.168.1.1" you'll get the message from twist.

If you in hosts.allow add:

sshd: KNOWN

You can log on to the localhost, but not if you add "LOCAL".

If you add

sshd: 192.168.1.

you can log on from localhost to the public IP of the server.

## Extra

- Configure key-based authentication.

- ssh-keygen
- ssh-copy-id user@host
- ssh user@host
- set PasswordAuthentication to no in sshd\_config
- service sshd restart

- Configure additional options described in documentation.

- many things can be done, see "man 5 sshd\_config"
- chrootdirectory looks quite cool but requires a bit of work
