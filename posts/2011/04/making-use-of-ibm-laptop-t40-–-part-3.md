---
title: Making use of IBM Laptop T40 – Part 3
date: 2011-04-18
category: it
tags: hdd, ibm, laptop, linux, pata, replace, hard, drive, t40, thinkpad, ultimatebootcd

### Preface

Two previous posts:

[Part1](http://www.guldmyr.com/making-use-of-ibm-laptop-t40-part-1/ "PART1") - thoughts before installing [Part2](http://www.guldmyr.com/making-use-of-ibm-laptop-t40-%E2%80%93-part-2/ "par2") - ultimate boot CD - for diagnostics

I ran the laptop with google-chrome 10 and two flash-pages loading all night, no blue-screens, no errors in event viewer. No actually it looks and feels pretty ok. It's not very fast, but I suspect this is the hard drive being slow.

Turns out I do have some CDs lying around!

Starting off easy with ubuntu-10.10-desktop-i386. The reason why I'm not trying the 11.04 is because I tried that in a VM the other day and it gave lots of errors. I also read some post about that 5/11 users managed to crash the Unity VM. So not stable :p

If that works (maybe even just try live-cd? nah, that's chicken) then maybe later I will can try something else like:

archlinux (which apparently requires setting up x-servers (required for graphical interface):

### How to boot:

Put in CD, press F12 during boot, chose the ACPI CD0 entry.

### The install:

Ubuntu loading logo looks like crap during boot (green pixelation around it). However during the actual install it looks fine. It would be good to have an UTP cable so that you can have internet access during install (download updates to packages etc). I did not have a UTP cable so I will hope that the wireless works and that I can update after install. I like that while the CD is copying files, you get to set some settings:

partition layout/hard disk layout, timezone, keyboard layout, username, passwords, computer name, home directory encryption,

While setting up the computer name, the installer automagically found out that it is a Thinkpad T40 that I have!

When it's done, the CD pops out, take it, press enter, wait, log in!

[Next post](http://www.guldmyr.com/making-use-of-ibm-laptop-t40-%E2%80%93-part-4/ "setting up") is about logging in and doing the initial setup.
