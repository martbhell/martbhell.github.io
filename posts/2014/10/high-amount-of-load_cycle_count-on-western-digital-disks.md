---
title: High amount of Load_Cycle_Count on Green Western Digital disks
date: 2014-10-26
category: it, storage
tags: idl3ctl, llc, load_cycle_count, ubuntu, wd, wdidle3, wdidle3, exe, western, digital
<!-- prettier-ignore -->
---

You are monitoring the SMART values of your disks right? They're usually a real good indicator of the health of the
drive.

Thought I'd check out the SMART value of the disks in my desktop today (while checking if I had notifications from
smartd on).

Low and behold, the Load_Cycle_Count (LLC) was really high, much higher than power_cycle_count on the 3TB WD disk I
have. It turns out this is quite an old problem so there are a few posts about this on the Internets. The
Interwebs [says](http://www.storagereview.com/how_to_stop_excessive_load_cycles_on_the_western_digital_2tb_caviar_green_wd20ears_with_wdidle3%20)
max in the specs are 300k load cycles. Smartctl -a says I'm already at 218602 after 9302 power on hours (387 days but I
power off the computer at night).

Disk:

Model Family: Western Digital Caviar Green (AF, SATA 6Gb/s) Device Model: WDC WD30EZRX-00DC0B0

For Windows there's a wdidle3.exe that is a DOS program that one can put on a bootable floppy (...) and boot a computer
on to change some stuff on a disk.

Fortunately I run Linux (Ubuntu 14.10 since yesterday) and there's a tool called **idl3ctl** - one can grab it from
here: [http://idle3-tools.sourceforge.net/](http://idle3-tools.sourceforge.net/ "http://idle3-tools.sourceforge.net/")

I got the latest source code and compiled it myself because there had been some updates to it since the last release
(2012 vs 2011 ..). "idl3ctl -g" shows that the disk was set to park itself after 8s. I disabled that with idl3ctl and
powered off and on the computer and now the tool says it's disabled.

Hopefully this should increase the lifetime of my disk.
