---
title: Cyanogenmod on Xperia Active (ST17i or satsuma)
date: 2014-01-12
category: it
tags: android, cyanogenmod, sony, ericsson, xperia, active
<!-- prettier-ignore -->
---

Finally got fed up with the Xperia Active (ST17i or satsuma) - couldn't update anything because all the space was used up and it was rebooting when I wasn't touching it. Solution? Install Cyanogenmod!

Cyanogenmod's [wiki](http://wiki.cyanogenmod.org/w/Install_CM_for_satsuma) has a good overview of how to get it installed. Basically you reinstall the operating system - but the cyanogenmod one doesn't have all the extra crap you don't want.

All below done from Windows 7 x64.

## 1. Root it

Rooted with eroot as found on <http://forum.xda-developers.com/showthread.php?t=2219781>

## 2. Install ADB

I installed the whole SDK.. apparently not needed [http://forum.xda-developers.com/showthread.php?t=1474956](http://forum.xda-developers.com/showthread.php?t=1474956)

## 3. Unlock bootloader

Poweroff the phone and get into fastboot by holding volume up while connecting the USB cable to the computer.

There is a tool called Flashtool (.net) - but it's not necessary if you're comfortable with the command prompt.

Also, if you can find the fastboot drivers [from elsewhere](http://developer.sonymobile.com/downloads/drivers/ "there is one called fastboot here on sonymobile.com") that's probably safer than installing them from flashtool (unsigned).

Run cmd as administrator if it doesn't work or give the -waiting for device-.

Get the key from Sony via [http://unlockbootloader.sonymobile.com](http://unlockbootloader.sonymobile.com "http://unlockbootloader.sonymobile.com")/ - Thanks Sony!

## 4. Install CM 9.1.0

Or if you're ballsy there's CM10 the nightly build :)

Download  CM itself [http://download.cyanogenmod.org/?device=satsuma](http://download.cyanogenmod.org/?device=satsuma) and [Google Apps](http://wiki.cyanogenmod.org/w/Google_Apps) if you want that.

Pretty straight forward after this, just follow [the guide](http://wiki.cyanogenmod.org/w/Install_CM_for_satsuma "http://wiki.cyanogenmod.org/w/Install_CM_for_satsuma").

Use fastboot to send boot.img Use fastboot to reboot Your phones gets into clockwork recovery I ran wipeall (probably should have backed up the ROM..) Install cm9.1 from zip Install gapps from zip

## 5. Conclusion

One quite annoying thing I get is: “SIM network unlock PIN” even though I'm fairly sure my phone is not locked.

First time it booted it couldn't sign in to the phone network at all, but on second it could. I just press dismiss.. perhaps this is fixed in CM 10 Jelly Bean - but with that the phone might also be slower.

But besides that I'm quite happy with it so far.

At least I won't have to have large Office software installed anymore.

// Update a few days later: It's been working quite nicely, not rebooting at all :)

// Update a few weeks later: DHCP on WiFi apparently stops working after a while, major bummer. But setting a fixed IP solves it. It's [apparently](http://forum.cyanogenmod.com/topic/57475-wifi-problem/ "http://forum.cyanogenmod.com/topic/57475-wifi-problem/") also possible to fix it by either setting it then back to DHCP (didn't work for me) or by clearing out `/data/misc/dhcp/*` (did work for me) by opening a terminal and sending two commands:

```bash
su -
rm /data/misc/dhcp/*
```
