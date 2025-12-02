---
title: check_irods - nagios plugin to check the functionality of an iRODS server
date: 2015-03-31
category: it, storage
tags: irods, monitoring, nagios
<!-- prettier-ignore -->
---

Part of my $dayjob as a sysadmin is to monitor all things.

Today I felt like checking if the users on our servers could use the local iRODS storage and thus `check_irods` was
born!

It checks if it can:

1. put
2. list
3. get
4. remove

a temporary file.

Dependencies:

- iRODS 3.2 with OS trusted authentication
- mktemp

Source: <https://github.com/martbhell/nagios-checks/tree/master/plugins/check_irods>
