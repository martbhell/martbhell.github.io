---
title: RHCSA – Rapid Track – Day 4
date: 2011-12-15
category: it
tags: net, acl, automounter, certification, kickstart, linux, red, hat, rhcsa, selinux, sssd, storage, studying
<!-- prettier-ignore -->
---

Last day!

A little more kickstarting, LVM - logical volume management and File ACL. Then a
rehearse of the previous chapters.

Feeling a bit excited about tomorrow!

These ACL were a bit more complex than I thought, but they could be made very
complicated if you want to. But there's the default ACL and then there's the
normal ones. Chmod +s for sticky bits.

Also got a 4GB USB pen that does about 4.4MB/s :p

Some important ones:

mount -o remount,rw / /usr/share/doc/initscripts\*/sysconfig.txt kernel-doc
package and /usr/share/doc/kernel-\* rpm -qd; rpm -qc

Some important but not importantest:

getsebool -a setsebool -P usermod -a sssd - service that caches authentication
stuff

Automounter /etc/auto.master ->

/home/guests /etc/auto.guests

/etc/auto.guests ->

\* -rw nfsserver:/path/to/mount/on/home/guests/&

If on nfsserver there is an nfsshare that is: /path/to/mount/on/home/guests/ and
in there you have home directories for users. Then this will automount these
directories when anybody tries to access them. Same concept as doing:

ls /net/nameofnfsserver/
