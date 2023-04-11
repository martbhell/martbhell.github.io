---
title: "Red Hat Certification – RHCE – Network Services – NTP"
date: "2012-06-08"
categories: 
  - "it"
tags: 
  - "centos"
  - "certification"
  - "file-transfer"
  - "linux"
  - "ntp"
  - "ntpd"
  - "ntpq"
  - "red-hat"
  - "rhce"
  - "studying"
  - "synchronization"
  - "tcpdump"
  - "time"
  - "time-sync"
  - "time-synchronizatino"
---

[1st post](http://www.guldmyr.com/blog/red-hat-certification-rhce-system-configuration-and-management-2/ "1st post") \- System Management and Configuration

[Objectives](https://www.redhat.com/training/courses/ex300/examobjective "on redhat.com")

# Network services

Network services are an important subset of the exam objectives. RHCE candidates should be capable of meeting the following objectives for each of the network services listed below:

- Install the packages needed to provide the service.
- Configure SELinux to support the service.
- Configure the service to start when the system is booted.
- Configure the service for basic operation.
- Configure host-based and user-based security for the service.

User should be able to do the following for all these services:

- [http/https](http://guldmyr.com/blog/red-hat-certification-rhce-network-services-httpd)
- [dns](http://guldmyr.com/blog/red-hat-certification-rhce-network-services-dns)
- [ftp](http://www.guldmyr.com/blog/red-hat-certification-rhce-network-services-ftp)
- [nfs](http://www.guldmyr.com/blog/red-hat-certification-rhce-network-services-nfs/)
- [smb](http://www.guldmyr.com/blog/red-hat-certification-rhce-network-services-smb/)
- [smtp](http://www.guldmyr.com/blog/red-hat-certification-rhce-network-services-e-mail/)
- [ssh](http://www.guldmyr.com/blog/red-hat-certification-rhce-network-services-ssh/)
- [ntp](http://www.guldmyr.com/blog/red-hat-certification-rhce-network-services-ntp/)

## NTP:

You could possibly test this from Windows as well.

On linux it's fairly straight-forward, you can use ntpd both as a client and as a server.

Check in /var/log/messages for details

The time-synchronization with ntpd is slow by design (to not overload or cause dramatic changes in the time set).

ntpdate is instant but it's not recommended to be used. For example with 'ntpdate -q'.

man ntp.conf this then points to : man ntp\_acc man ntp\_auth man ntp\_clock man ntp\_misc

- Install the packages needed to provide the service.

- yum install ntp

- Configure SELinux to support the service

- nothing to configure??

- Configure the service to start when the system is booted.

- chkconfig ntpd on

- Configure the service for basic operation.

- /etc/ntp.conf

- server ntp.server.com

- service ntpd start
- ntpq -p # to see status

- Configure host-based and user-based security for the service

- iptables

- port 123 (UDP)

## Enable ntpd as a client

What's a bit reverse for ntpd is that first you need to configure the server as a client

So that your local ntp-server gets good time from somewhere else. You can find a good time-server to use on www.pool.ntp.org

You only need to add one server line but for redundancy you should probably have more than one.

As an example with your client on 192.168.0.0/24 and server is on 192.168.1.0/24.

All you need to do is for the client part:

server ntp.example.com
service ntpd restart
ntpq -p

 

## Enable ntpd as a server

You need to add a restrict line in ntp.conf.

You also need to allow port 123 UDP in the firewall.

restrict 192.168.0.0 mask 255.255.255.0 nomodify notrap
service ntpd restart

## Client to use your ntp server

Basically the same as the above for client, but you specify the address to your NTP-server instead of one from pool.ntp.org.

## Extra

- Synchronize time using other NTP peers.

I believe this has been covered.

## More Extra

One extra thing you may want to check out is the 'tinker' command.

This is put on top of ntp.conf and more info are available in 'man ntp\_misc'.

However, most of the time you just need to wait a bit for the time change to come through.

## tcpdump

There's not much to go in logs on either server or client for ntpd. You'll get messages in /var/log/messages though that says "synchronized" and when the service is starting.

You can also use tcpdump on the server to see if there are any packets coming in.

tcpdump -i eth0 -w /tmp/tcmpdump.123 -s0 'udp port 123 and host NTP.CLIENT.IP'
# wait a while, restart ntpd on client
tcpdump -r /tmp/tcmpdump.123
# this will then show some packets if you have a working communication between server and client

## To test that it's working

Start with the server still connecting to an ntp-server with good time.

You could then set the date and time manually on the server to something else. For example, let's say the current time is 6 JUN 2012 17:15:00.

Set it to 15 minutes before:

date -s "6 JUN 2012 17:00:00"
service ntpd restart

Also restart ntpd on the client, then wait, this will probably take a bit longer than before.

If you set the time manually to something too big it won't work. You could then experiment with 'tinker panic 0'
