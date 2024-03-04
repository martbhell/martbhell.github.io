---
title: SunOS 5.11 OpenSolaris Man Page Trick
date: 2011-08-01
category: finland
tags: bash, script, man, manpage, manual, opensolaris, solaris, sun
<!-- prettier-ignore -->
---

Ever had to read a man page on a Solaris system? You'll see these

SunOS 5.11 System Administration Commands

on each page in the manpage, making it quite hard to read.

To make it more readable you can run this: man $1|grep -v 'SunOS 5.11'|grep -v
'System Administration Commands'|less

With $1 being the command, for example mpathadm.

You could also put it in a bash script file, for example /usr/bin/man2, :

## !/bin/sh man $1|grep -v 'SunOS 5.11'|grep -v 'System Administration Commands'|less

Don't forget to set executable permissions with chmod 755 on the script file so
that normal users can run it. Then instead of running man, run 'man2 mpathadm'
and you'll have a much more readable manpage.
