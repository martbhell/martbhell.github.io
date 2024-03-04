---
title: gnome-screensaver uses a lot of memory
date: 2011-04-14
category: finland
tags: dwm, gnome, screensaver, linux, memory, memory, hog, useage
<!-- prettier-ignore -->
---

Just checked out a memory useage script (because honestly I find top a but too
complicated). I found one that looks good on
[asim.pk](http://www.asim.pk/2011/03/28/find-memory-consumed-by-currently-running-processes-on-linux/ "memory useage perl script")
. The script is a nice little perl script. Just download it from the link and
set chmod +x ps_mem.pl and you can run it with "sudo ps_mem.pl", you need to be
root for some reason to run this script.

My machine is a Lenovo T400 with a radeon card.

This told me that gnome-screensaver was using some 400MB. A bit of googling did
not give me any real hints if there is a configuration change or so. So instead
I decided to change the way I lock my workstation in
[dwm](http://dwm.suckless.org "dwm").

Now, I call upon a program I called "screenlock", this I put in
/usr/local/bin/screenlock:

`killall gnome-screensaver; sleep 1; gnome-screensaver; gnome-screensaver-command -l`

That's it. (kills it, waits a bit, starts it, then locks)

Then in config.h for dwm this under /\* commands \*/:

`static const char *locksaver[] = { "screenlock", NULL } ;`

and under keys

`{ MODKEY, XK_l, spawn, {.v = locksaver } },`

with all the spaces/tabs that is in config.h, unsure if it's necessary but why
take a chance :p

Now it stays around 10MB :)
