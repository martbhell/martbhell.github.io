---
title: "Tiny Core Linux"
date: "2012-03-03"
categories: 
  - "it"
tags: 
  - "linux"
  - "operating-system"
  - "testing"
  - "tiny-core-linux"
---

[http://distro.ibiblio.org/tinycorelinux/welcome.html](http://distro.ibiblio.org/tinycorelinux/welcome.html "http://distro.ibiblio.org/tinycorelinux/welcome.html")

Micro Core Linux!

Like super small!

WOop woop...

[http://distro.ibiblio.org/tinycorelinux/downloads.html](http://distro.ibiblio.org/tinycorelinux/downloads.html "http://distro.ibiblio.org/tinycorelinux/downloads.html")

Three versions:

## Core

Core (8MB) - CLI only

This literally boots in 3 seconds after pressing enter at the boot loader, nice!

To get root access hit: 'sudo sh'.

Basically nothing is installed, but you can download whatever you need with 'wget'. You'll need to compile things from source as there's no packet manager. Or, after trying out the other versions, there may be a packet manager hidden in there somewhere somehow.

## Tiny Core

Tiny Core (12MB) - Good for new users and wired connections.

This one boots into a graphical interface with the mac-style bar at the bottom of the screen with icons that pop out. It also has an appbrowser.

Search for something (perhaps 'seamonkey') and press 'go'. This starts to download things. Lots of things. But in the end it completes and it works.

The appbrowser is missing quite a lot, there's no progress bar so you have no idea how much needs to be downloaded or how long an install might take. You can see in the 'depends' tab which the dependencies are and that might give you a clue.

openssl is not installed by default! This is quite a surprise, to me this is almost the basis of a linux-based distribution. But if you don't need to connect to it remotely or connect from it to another host then I guess you don't need it :)

[irssi doesn't work by default](http://forum.tinycorelinux.net/index.php?topic=12252.0).

If the packet manager cannot handle installing irssi I call it a crappy distro.

Nuff is e'nuff.

## Core Plus

Core Plus (64MB) - Extra nicestuff, good for beginners, wireless and non-US keyboards.

Wonder if irssi works here? - Not in the default terminal or Eterm no! Xchat works though it is full of shieeet.

core plus has a lot nicer boot manager, and it shows a lot more options, such as fluxbox.

## Think about:

It takes a fair amount of time to install something (or, it feels longer because there's no progress bar) if you run it off the livecd. So, if you decide to try another OS without installing apps on disk, be prepared to reinstall apps.
