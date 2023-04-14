---
title: "Red Hat Certification – RHCE – Network Services - httpd"
date: 2012-05-02
categories: 
  - "it"
tags: 
  - "apache"
  - "centos"
  - "certification"
  - "httpd"
  - "linux"
  - "red-hat"
  - "rhce"
  - "studying"
---

[1st post](http://www.guldmyr.com/blog/red-hat-certification-rhce-system-configuration-and-management-2/ "1st post") \- System Management and Configuration

This post is about Network Services.

During all these exercises I try my hardest not to use google, as that's not available during the exam anyway.

[Objectives](https://www.redhat.com/training/courses/ex300/examobjective "on redhat.com")

# Network services

Network services are an important subset of the exam objectives. RHCE candidates should be capable of meeting the following objectives for each of the network services listed below:

- Install the packages needed to provide the service.
- Configure SELinux to support the service.
- Configure the service to start when the system is booted.
- Configure the service for basic operation.
- Configure host-based and user-based security for the service.

User should be able to do the following for all these services:

- http/https
- dns
- ftp
- nfs
- smb
- smtp
- ssh
- ntp

## httpd:

- Install the packages needed to provide the service.
    - yum install httpd
- Configure SELinux to support the service.
    - supports by default, if changing documentroot/defaultroot use:
    - chkcon -R --reference /var/www/html /var/newhtmldir
- Configure the service to start when the system is booted.
    - chkconfig httpd on
- Configure the service for basic operation.
    - rpm -qc httpd (find config file)
- Configure host-based and user-based security for the service
    - host-based -> iptables
    - user-based -> htpasswd for httpd

### htpasswd

An htpasswd file contains users/passwords.

A .htaccess file points to the htpasswd

The .htaccess file is not the recommended way to set up authentication, instead you should do it in the Directory section of httpd.conf.

To get more information about httpd in general do:

yum install httpd-manual

Then surf to http://hostname/manual.

To generate a htpasswd:

\[root@rhce webpages\]# htpasswd -c /etc/httpd/conf/.htpasswd user
New password:
Re-type new password:
Adding password for user user

Then add this .htaccess file:

AuthUserFile /etc/httpd/conf/.htpasswd
AuthGroupFile /dev/null
AuthName "Private Area"
AuthType Basic
AuthBasicProvider file
Require user user

## https

The s - means the httpd uses another port - 443 and that it uses certificates.

yum install mod\_ssl

This adds /etc/httpd/conf.d/ssl.conf

That config file actually has a 'listen' directive for port 443.

So add that port in the firewall and restart httpd.

After that you can surf to https://ip and it will complain about the certificate (which is a default generated one).

## But wait, there's more!

### Configure a virtual host.

This is can be used when you want to have several hostnames or domains on the same machine.

There's some info in httpd.conf but there's quite a lot in the manual via httpd-manual package.

To test this you could either put several IP addresses on the server or point several domains towards it (might be easiest, /etc/hosts). But in VMWare it's very easy to just add another network interface.

1. Add another ethernet interface on the same network as the existing one (mine is bridged behind a NAT).
2. Edit /etc/hosts on a client and on the server so that ww1.example.com and ww2.example.com points to the IP addresses on the server
3. Make sure /etc/nsswitch.conf has 'files' in the hosts row.
4. If you have very narrow firewall add the new IP address.
5. mkdir /var/www/ww1.example.com; mkdir /var/www/ww2.example.com; chcon -R --reference =/var/www/html /var/www/ww\*
6. Edit /etc/httpd/conf/httpd.conf

and add this at the end:

NameVirtualHost \*:80

    ServerAdmin webmaster@dummy-host.example.com
    DocumentRoot /var/www/ww1.example.com
    ServerName ww1.example.com

    ServerAdmin webmaster@dummy-host.example.com
    DocumentRoot /var/www/ww2.example.com
    ServerName ww2.example.com

7\. service httpd restart

Then on the client point your browser to and (add different index.html in each to make it easy to see).

### Configure private directories.

I'd say this fall under the htpasswd section.

### Deploy a basic CGI application.

FOSwiki for example uses CGI. Perhaps it should be a custom CGI application, like a small [hello-world script.](http://www.lies.com/begperl/hello_cgi.html "simple cgi hello world script")

/var/www/cgi-bin is where CGI scripts are stored by default.

A simple .cgi script is just a perl script with another extension that outputs .HTML text.

### Configure group-managed content.

Group-managed. So this would be somehow using the AuthGroupFile in .htaccess?

Or could be done by creating a new directory under www-root and give specific access to this directory. That means it can be managed by a unix group, (access is a different story however).
