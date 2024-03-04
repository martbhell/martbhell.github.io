---
title: P6000 Firmware & Command View
date: 2011-06-17
category: storage
tags: abm, command, view, disk, array, disks, download, enterprise, virtual, array, eva, fcoe, firmware, hp, management, module, p6000, release, notes, storage, xcs, xcs, 10000000
<!-- prettier-ignore -->
---

The P6000 firmware XCS [10000000](https://h20392.www2.hp.com/portal/swdepot/displayProductInfo.do?productNumber=T4256-63141 "on hp.com") is out, or has been for a while now. You can find it on [http://software.hp.com](http://software.hp.com "http://software.hp.com") or the link above.

The Command View 9.4 release notes are [here](http://h20000.www2.hp.com/bizsupport/TechSupport/DocumentIndex.jsp?contentType=SupportManual&lang=en&cc=us&docIndexId=64179&taskId=101&prodTypeId=18964&prodSeriesId=471497 "cv 9.4 release notes").

Extra nice stuff (besides the obvious ones like new hw support):

- HDD upgrades via management module / ABM
- Disk Drive Remote Power cycling (apparently works after 09500000?)
- Thin Provisioning (requires extra license but with the P6300/6500 it comes with the normal CV license)
- Online migrations (change vraid lvl or disk group without impacting i/o - cool)
- Manage it over FCoE (so via an MPX200 for example)
- EVA3000/5000 events not propogated to Windows Event Log - I knew it!
- SSSU 9.4 - took away the 10s delay when executing commands.

And release notes for the XCS 10M is [here](http://h20000.www2.hp.com/bizsupport/TechSupport/DocumentIndex.jsp?contentType=SupportManual&lang=en&cc=us&docIndexId=64179&taskId=101&prodTypeId=12169&prodSeriesId=5062117 "hp.com").

More hw stuff ;)

- For HSV300 and above
- P6300 is HSV340 and P650 is HSV360
- M6612 is LFF (3.5" disks) and M6625 is SFF (2.5" disks)
- So are they smaller than the EVA8400?
- Both P6300 and P6500 have a management module (ABM)
- Events that indicate back-end cabling is incorrect -> NICE
- Some more SPOF fixes

It's confusing to read the release notes as it says P6000 everywhere but it refers to all EVAs. Also the older generations like EVA3000/5000 are called P6000!

I also wonder why the P6300/P6500 is named HSV340 and HSV360. So they're not better than the EVA6400?

This would put them on or slightly above the EVA6400/HSV400 series level:

"Up to 10 M6612 or M6625 are supported with the P6300 EVA up to 20 M6612 or up to 18 M6625 are supported with the P6500 EVA"

In terms of sizing it would make more sense to call them HSV420 and HSV440 or something like that :)

On this [page](http://h10010.www1.hp.com/wwpc/us/en/sm/WF04a/12169-304616-304648-304648-304648.html "comparison") it says active/active on the redundancy options, but it doesn't say this on the x400. Does this mean it's no longer asymmetrical A/A like it was on the previous EVAs?
