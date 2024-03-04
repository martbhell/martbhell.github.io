---
title: Red Hat Certification – RHCE – Network Services – DNS
date: 2012-05-08
category: it
tags: centos, certification, dns, domain, name, linux, red, hat, rhce, studying
<!-- prettier-ignore -->
---

[1st post](https://www.guldmyr.com/red-hat-certification-rhce-system-configuration-and-management-2/ "1st post")
\- System Management and Configuration

[Objectives](https://www.redhat.com/training/courses/ex300/examobjective "on redhat.com")

## Network services

Network services are an important subset of the exam objectives. RHCE candidates
should be capable of meeting the following objectives for each of the network
services listed below:

- Install the packages needed to provide the service.
- Configure SELinux to support the service.
- Configure the service to start when the system is booted.
- Configure the service for basic operation.
- Configure host-based and user-based security for the service.

User should be able to do the following for all these services:

- [http/https](https://guldmyr.com/red-hat-certification-rhce-network-services-httpd)
- [dns](https://guldmyr.com/red-hat-certification-rhce-network-services-dns)
- ftp
- nfs
- smb
- smtp
- ssh
- ntp

### DNS

A DNS-server is quite easy to test as well, just point a client to the IP of
your local DNS server and check /var/log/messages on the DNS-server.

- Install the packages needed to provide the service.

- yum install bind

- Configure SELinux to support the service

- working from scratch, after adding new zones and things you may need to add
  correct context to the files

- Configure the service to start when the system is booted.

- chkconfig named on

- Configure the service for basic operation.

- /etc/named.conf

- after editing you need to restart named

- edit 'allow-query' and 'listen-on port 53' - update firewall, start named
- configure a client to use it with /etc/resolv.conf
- see examples in: /usr/share/doc/bind\*/

- Configure host-based and user-based security for the service

- host-based can be done via firewall (port 53 UDP and TCP)
- host-based: allow-query { localhost; };
- but user-based??

### Extra

- Configure a caching-only name server.

- This is what the default /etc/named.conf does it - (this is also stored in the
  /usr/shar/doc/bind\*/ - but, it a good thing to try would be to try to
  configure this from an empty named.conf

- Configure a caching-only name server to forward DNS queries.

- Almost same config as caching-only, except for the addition of two lines:

- forward only;
- forwarders  { dns.ip; dns.ip2 }

- Note: Candidates are not expected to configure master or slave name servers.
