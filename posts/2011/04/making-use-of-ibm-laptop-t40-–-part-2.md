---
title: "Making use of IBM Laptop T40 – Part 2"
date: 2011-04-17
categories: 
  - "it"
tags: 
  - "hdd"
  - "ibm"
  - "laptop"
  - "linux"
  - "pata"
  - "replace-hard-drive"
  - "t40"
  - "thinkpad"
  - "ultimatebootcd"
---

Previous post in this series: [http://www.guldmyr.com/blog/making-use-of-ibm-laptop-t40-part-1/](http://www.guldmyr.com/blog/making-use-of-ibm-laptop-t40-part-1/ "previous post")

I'm going to try to put ubcd on an old USB pen I have, lots easier than burning a CD/DVD. Which I may not even have. It's an old Jens of Sweden 1GB mp3-player, that doesn't start unless plugged in a USB-port..

On the UBCD (you can mount this on  your pc) there is a tool under x:\\ubcd\\tools\\win32\\ubcd2usb

Open a command prompt on your PC type:

- x:
- cd ubcd/tools/win32/ubcd2usb
- ubcd2usb.cmd CDROM: USBDRIVE: (like ubcd2usb.cmd D: E:)

Then you need to put in the USB-pen, boot your computer. Check BIOS and put USB drive at the top.

Turns out I have forgotten my thinkpad supervisor password.. So that is a no-no because apparently to reset that I need to do some soldering. Also there is only a CDRW-drive, and I do not have an empty CD to burn, only DVDs :/

PXE boots is also an option, but this looks incredibly difficult. It probably isn't (should be just DHCP and tftp server, but gotta make floppy boot disks, etc).

But, got a hold of my lovely laptop, boots up WinXP just fine. Going to patch it now and keep it going for a while running something, we'll see if it crashes or not. Maybe it is OK?

[Next post](http://www.guldmyr.com/blog/making-use-of-ibm-laptop-t40-%E2%80%93-part-3/ "part3") in this series will be published on the 18th of April. That one is about installing Ubuntu on the Thinkpad T40!
