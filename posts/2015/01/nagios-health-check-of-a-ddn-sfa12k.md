---
title: Nagios Health Check of a DDN SFA12K
date: 2015-01-18
category: it, storage
tags: ddn, monitoring, nagios, sfa12k
<!-- prettier-ignore -->
---

Part of my $dayjob as a sysadmin is to monitor all things.

I'll be publishing my home-made nagios checks on github in the near future.

Here is the first one that uses the Web API of a DDN's
[SFA12K](http://www.ddn.com/products/storage-platform-sfa12kx/ "ddn.com product info")
(might work on the 10k too, haven't tried) which is a storage platform.

The URL to the check is located
here: [https://github.com/martbhell/nagios-checks/tree/master/plugins/check_ddn](https://github.com/martbhell/nagios-checks/tree/master/plugins/check_ddn)

Unfortunately it seems that the Python Egg (the library / API bindings) is still
not available online so one has to ask DDN Support to get that.

It's not perfect, there's much room for improvement, refactoring, moving the
password/username out of a variable and it makes many assumptions. But making it
work for you shouldn't be too hard. If you have any questions comment here or on
github :)
