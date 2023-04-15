---
title: Ubuntu 11 in VMWare Workstation
date: 2011-04-03
category: it
tags: 11, 04, it, 2, natty, ubuntu, virtual, machine, vmware, vmware, workstation

Time for another test! This time it's Ubuntu 11.04 Natty.

My setup is a Intel Core i7 920 on Windows 7 x64 with 8GB RAM.

\*\*\* Update 2011-04-29 - I just heard that if you run this in a Virtual Machine you do not get all the shebang on the default graphical user interface. But for me it looks fine. Also when I looked on this video it didn't look much different except for the left side bar. If you want to check out the supposedly nicer graphical user interface I would recommend that you put Ubuntu on a CD/DVD and then boot your desktop with it. That way you can see if it's for you and if it works without doing anything to your hard drives :)

\*\*\* Update 2011-04-29 Also added link where to get Ubuntu 11.04 as now it's not in beta anymore.

### Installing

1. Install VMWare Workstation
2. [Download the Ubuntu ISO. (I got the x64 / AMD64 one) from http://www.ubuntu.com/testing/natty/beta](http://www.ubuntu.com/testing/natty/beta "on ubuntu.com")
3. As it's public now, you can get it from [http://www.ubuntu.com/download/ubuntu/download](http://www.ubuntu.com/download/ubuntu/download " get ubuntu")
4. Add new Virtual Machine (VM) in VMWare Workstation, browse to the .iso and it will with easy install find Ubuntu 64-bit.
5. Gogogo! Chose language and set up your user account. That's all. After that you can log on to the desktop. It took quite some time for me to install it - though I wasn't in a rush so did not measure time and just left the PC. Maybe it went sleeping or something.

Uses 5.2GB effective disk space (checked properties on the directory from Windows) after install and that upgrade below.

## **After install.**

Looks pretty smooth. Quite different from what I remember. I set it to 2GB  RAM and it's only using 300MB from scratch. This is nice. And it turns off in a couple of seconds.

- Unity thing in VMWare Workstation works from scratch (7.1.3 and 7.1.4). In 7.1.4 even with the VMWare Tools not installed updated.
- First thing I ran was a software update - 160MB already after it being out only a couple of days. Guess some big package got an update.. however, no reboot required for it!
- One thing you should be aware of, is that the program options/menu bar, is at the top of the screen, "File", "View", stuff like that. So quite a bit like Mac OS (if I'm not mistaken).
- Audio is also working from start.
- Resolution/screen proportions are automagically updated so that Ubuntu fits the whole screen. Nice. Ubuntu 10.10 does not do this in Virtualbox on RHEL6.

### Comes default with these programs:

- Mozilla Firefox 4.0
- Libreoffice (not openoffice??) - looks like openoffice anyway.
- Evolution Mail/calendar
- Empathy chat cilent
- Gwibber - twitter I guess
- Transmission - torrent client
- Shotwell photo manager
- "ubuntu software manager" - where you download apps. There is still however apt-get and synaptic.

This "ubuntu software manager" is a bit of a fail. It seems very mainstream.

### For example:

- irssi cannot be found there

That's about all I can think of for now.

### Adobe Flash:

- No flash from the start. But! Search for it in the software manager and you can install it. This however failed. I tried to report but it required a login so I skipped.
- After fail the app still has a green check-mark on it.
- Flash still works though. And it's not lagging for me at all. But hey, I just tried it right after starting the browser. Maybe it gets choppier after some heavy browsing :p

### Unity

The unity thing is pretty darn neat. What it does is it gives you an "extra" start-button. It's not visible all the time, only when you go near your normal one - it pops out. With that you can then start a program from the Ubuntu virtual machine and it will look like any other program on your PC.

Supposedly Unity may work better after upgrading VMWare Tools. I got a little bar at the bottom of the screen, extracted and ran the thing. Then it was gone.

### Conclusion

All in all, feels pretty good! I have some plans to get a laptop of mine up running this. Just need some other work done on it first I believe. There were some bugs, but that's not surprising, considering it is in beta. Always liked ubuntu because installing it is so smooth. Might not be the most awesome for preserving system resources but honestly, only using 300MB from start is pretty ok isn't it? If I get it on my laptop, I'll definitely be trying another window manager, like awesome or dwm -  should bring the memory usage down :)
