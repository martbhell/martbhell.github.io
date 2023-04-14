---
title: "RHCSA - Rapid Track - Day 1"
date: 2011-12-12
categories: 
  - "it"
tags: 
  - "certification"
  - "linux"
  - "red-hat"
  - "rhcsa"
  - "studying"
---

First day done!

What hit me was that there are many commands in linux, some you maybe only use for one purpose. But there are some things that you haven't done with it before, so an old command can still cause some trouble. For example crontab and the last \* (or, day of week) in conjunction with day/month or by itself.

Already seen one double negative (/usr/share/doc/initscripts/sysconfig.txt and PEERDNS= directive) - so beware and read carefully.

**Cool things:**

ls -l /net/dns.to.nfs.server/

Will automagically mount the nfs server in there. Pretty nice!

automount, autofs, with /etc/auto.master so that you can for example set up dynamic mounting of nfs directories for users that haven't logged on to the system.

configuring ldap authentication best done via system-config-authentication GUI tool. Doing it via the CLI takes about a gazillion (26) variables/commands.

anacron for crontab that runs the script again if the machine was off when it was supposed to run.
