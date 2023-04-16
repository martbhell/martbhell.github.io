---
title: Red Hat Certification – RHCE – Network Services – SMB
date: 2012-05-14
category: it
tags: centos, certification, file, transfer, linux, red, hat, rhce, samba, smb, studying

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

- [http/https](http://guldmyr.com/red-hat-certification-rhce-network-services-httpd)
- [dns](http://guldmyr.com/red-hat-certification-rhce-network-services-dns)
- [ftp](http://www.guldmyr.com/red-hat-certification-rhce-network-services-ftp)
- [nfs](http://www.guldmyr.com/red-hat-certification-rhce-network-services-nfs/)
- [smb](http://www.guldmyr.com/red-hat-certification-rhce-network-services-smb/)
- smtp
- ssh
- ntp

## SMB:

Testing an SMB server may be quite easy from Windows, but from Linux I suppose it's a bit trickier.

The CLI client is called 'smbclient'

The tool to set passwords: 'smbpasswd'

You can also get some information with commands starting with 'net', for example 'net -U username session'

testparm is another tool you can use to test that the config file - smb.conf - is not missing anything structural or in syntax.

The server is called 'samba'.

There are more packages, for example 'samba-doc', samba4. You can find them by typing: 'yum install samba\*'

samba-doc installs lots of files in /usr/share/doc/samba\*

- Install the packages needed to provide the service.

- yum install samba

- Configure SELinux to support the service

- getsebool -a |grep smb; getsebool -a|grep samba
- /etc/samba/smb.conf # has some information about selinux

- Configure the service to start when the system is booted.

- chkconfig samba on

- Configure the service for basic operation.

- server#: open firewall (check man smb.conf, port 445 and 139 are mentioned)
- server#: mkdir /samba; chcon -t type\_in\_smb\_conf /samba
- server#: edit /etc/samba/smb.conf:

- copy an existing share - make it browseable and allow guest to access

- server#: service smb start
- server#: touch /samba/fileonshare
- client#: smbclient \\\\\\\\ip.to.smb.server\\\\share

- hit enter and it will attempt to log in as anonymous (guest)

- client#: get fileonehsare

- Configure host-based and user-based security for the service

- server#: check that 'security = user' in smb.conf.
- server#: add" writable = yes" or "read only = no" to the share in smb.conf
- server#: smbpasswd -a username
- server#: mkdir /samba/upload
- server#: chown username /samba/upload
- server#: chmod 777 /samba/upload
- client#: smbclient -U username \\\\\\\\ip.to.smb.server\\\\share
- client#: cd upload; mkdir newfolder; cd newfolder
- client#: put file

## Extra

- Provide network shares to specific clients.

- things you can set on the share:

- write list = +staff
- invalid users =
- valid users =
- hosts allow = 192.168.0.0/255.255.255.0
- hosts deny =

- Provide network shares suitable for group collaboration.

- groupadd staff
- usermod -a -G staff bosse
- chown root.staff /samba/upload
- chmod 775 /samba/upload
- connect with bosse - do things,
- connect with another user - can you do things?
