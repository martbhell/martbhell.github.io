---
title: Red Hat Certification – RHCE - Course Outline
date: 2012-06-13
category: it
tags: authconfig, centos, certification, encryption, firewall, gnupg, gpg, http, proxy, iptables, ipv6, ldap, linux, masquerade, nat, openssl, pam, pki, proxy, red, hat, rhce, routing, squid, ssh, keygen, sssd, studying, web, proxy

Howdy!

In case you saw my previous posts I've been prepping for a RHCE course the last couple of weeks.

Here are the posts based on the objectives:

- [http/https](http://guldmyr.com/red-hat-certification-rhce-network-services-httpd)
- [dns](http://guldmyr.com/red-hat-certification-rhce-network-services-dns)
- [ftp](http://www.guldmyr.com/red-hat-certification-rhce-network-services-ftp)
- [nfs](http://www.guldmyr.com/red-hat-certification-rhce-network-services-nfs/)
- [smb](http://www.guldmyr.com/red-hat-certification-rhce-network-services-smb/)
- [smtp](http://www.guldmyr.com/red-hat-certification-rhce-network-services-e-mail/)
- [ssh](http://www.guldmyr.com/red-hat-certification-rhce-network-services-ssh/)
- [ntp](http://www.guldmyr.com/red-hat-certification-rhce-network-services-ntp/)

Odds are quite high that I've missed something or not gone deep enough into some subjects and for the record some subjects I decided to skip.

I'm taking the course over at Tieturi here in Helsinki and they have published the schedule for the course, with quite [detailed o](http://www.tieturi.fi/kurssit/kurssi.html?course=83902366&category=RedHat%2BLinux&city=Helsinki&training=25.06.2012 "on tieturi.fi")utline.

This outline of the course can with benefit be used to see if you missed any terms or functions while going through the objectives.

I'll go through the ones I find more interesting below:

## Network Resource Access Controls

\-Internet Protocol and Routing

OK, well this is quite obvious, some commands:

ip addr
ip route
route add
netstat -rn

### IPv6

\-IPv6: Dynamic Interface Configuration -IPv6: StaticInterface Configuration -IPv6: Routing Configuration

You can add IPV6 specific lines in the ifcfg-device files in /etc/sysconfig/network-scripts/. See /usr/share/doc/initscripts\*/sysconfig

Some settings can also go into /etc/sysconfig/network

### iptables

\-[Netfilter](http://en.wikipedia.org/wiki/Netfilter "on wikipedia") Overview -Rules: General Considerations -[Connection Tracking](http://en.wikipedia.org/wiki/Netfilter#Connection_Tracking "on wikipedia") -Network Address Translation (NAT) -IPv6 and ip6tables

 

## Web Services

\-Squid Web Proxy Cache

On client check what IP you get:

curl --proxy squid-server.example.com:3128 www.guldmyr.com/ip.php

On server install and setup squid:

yum install squid
vi /etc/squid/squid.conf
#add this line in the right place:
acl localnet src 192.168.1.1/32
#allow port 3128 TCP in the firewall (use very strict access here)
service squid start

On client:

curl --proxy squid-server.example.com:3128 www.guldmyr.com/ip.php

Beware that this is unsecure. Very unsecure. You should at least set up a password for the proxy, change the default port and have as limited firewall rules as possible.

## E-mail Services

\-Simple Mail Transport Protocol -Sendmail SMTP Restrictions -Sendmail Operation

 

## Securing Data

### \-The Need For Encryption

[\-Symmetric Encryption](http://support.microsoft.com/kb/246071 "on microsoft.com :)")

Symmetric uses a secret/password to encrypt and decrypt a message. You can use GnuPG (cli command is 'gpg') to encrypt and decrypt a file symmetrically. Arguments:

\--symmetric/-c == symmetric cipher (CAST5 by default) --force-mdc == if you don't have this you'll get "message was not integrity protected"

There are many more things you can specify.

echo "awesome secret message" > /tmp/file
gpg --symmetric --force-mdc /tmp/file
#(enter password)
#this creates a /tmp/file.gpg
#beware that /tmp/file still exists
#to decrypt:
gpg --decrypt /tmp/file.gpg
gpg: 3DES encrypted data
gpg: encrypted with 1 passphrase
awesome secret message

 

### \-Asymmetric Encryption

Uses a key-pair. A public key and a private key. A message **encrypted with the public key** can only be decrypted with the **private key**. A message encrypted with the **private key** can only be decrypted with the **public key**.

GnuPG can let you handle this.

Login with a user called 'labber':

gpg --gen-key
# in this interactive dialog enter username: labber, e-mail and password
# this doesn't always work, might take \_long\_time\_, eventually I just tried on another machine
echo "secret message" > /tmp/file
gpg -e -r labber /tmp/file
# enter password
gpg --decrypt /tmp/file
# enter password

To export the public key in ASCII format you can:

gpg --armor --output "key.txt" --export "labber"

However, how to encrypt a file with somebody else's public key?

### \-Public Key Infrastructures - PKI

Consists of:

- CA - certificate authority - issues and verifies digital certiciates
- RA - registration authoriy - verifies user identity requesting info from the CA
- central directory - used to store and index keys

\-Digital Certificates

A certificate has user details and the public key.

## Account Management

\-Account Management -Account Information (Name Service) -[Name Service Switch](http://en.wikipedia.org/wiki/Name_Service_Switch "on wikipedia") (NSS) -[Pluggable Authentication Modules](http://linux-pam.org/whatispam.html "on linux-pam.org") (PAM) -PAM Operation -Utilities and Authentication

 

### PAM

Basically a way to authenticate users. You can put different types of authentication ways behind PAM. So that a software only needs to learn to authenticate to PAM and then PAM takes care of the behind-the-scenes-work.

For example you can have PAM connect to an ldap-server.

CLI: authconfig

Files: /etc/sysconfig/authconfig /etc/pam.d/ /etc/sssd/sssd.conf
