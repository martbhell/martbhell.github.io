---
title: File share from Ubuntu 10.10 with Windows 7 Client
date: 2011-02-08
category: it
tags: 10.10, apt, get, file, share, guide, kernel, linux, samba, ubuntu, virtual, kernel, vm, vmware, vmware, workstation, windows

Figured I would give this a shot and see how this is done in Linux.

## Overview

1x Ubuntu 10.10 VM in VMWare Workstation. Installed with virtual kernel. 1x Windows 7 VM. All updates.

Not going to go through the installations in this post, just the domain/LDAP part. See [previous post](http://www.guldmyr.com/tag/ubuntu/ "tag ubuntu")s for installation stuffs.

Found this article on ubuntu.com -> -> 10.10/serverguide/C/network-authentication.html .. But this does not exist anymore.

Whoa, quite a lot to do. Think I will read the manuals this time :)

Basically I think I just need to install and then configure [Samba](http://www.samba.org/samba/docs/SambaIntro.html "samba intro"). Because it has file-sharing and authentication/authorization.

So, first step will be to install Samba and try file-sharing.

## File Sharing

sudo apt-get install samba

installs these:

The following NEW packages will be installed: libavahi-client3 libavahi-common-data libavahi-common3 libcups2 libfile-copy-recursive-perl libgnutls26 libldap-2.4-2 libsasl2-2 libsasl2-modules libtalloc2 libtasn1-3 libwbclient0 samba samba-common samba-common-bin update-inetd

After that I can run \\\\192.168.0.ip which is the IP of the VM running samba - it gives me a login prompt.

Uncommenting this in /etc/samba/smb.conf

\[homes\] comment = Home Directories browseable = yes

Still asks for a password. Tried with user@ip - this seems to work. It shows a directory called "homes" but it doesn't work to browse into it.

\[2011/02/06 16:30:45.949726,  1\] smbd/service.c:678(make\_connection\_snum) create\_connection\_server\_info failed: NT\_STATUS\_ACCESS\_DENIED

Set 'share' and set the guest account = nobody  then I got this:

\[2011/02/07 13:22:06.770082,  0\] smbd/service.c:988(make\_connection\_snum) canonicalize\_connect\_path failed for service foo, path /mnt/foo

Then what I did was this:

1. created a directory called /samba
2. sudo chmod +x /samba
3. sudo chmod 777 /samba
4. sudo chown nobody /samba
5. add this to /etc/samba/smb.conf
6. \[foo\] comment = foo path = /samba read only = no guest ok = yes guest only = yes browseable = yes
7. security = share
8. guest account = nobody

And then \\\\ip\\foo and woopsie! I can both write and read :)

\[2011/02/07 13:23:14.022980,  1\] smbd/service.c:1070(make\_connection\_snum) 192.168.0.ip (192.168.0.ip) connect to service foo initially as user nobod

yay!
