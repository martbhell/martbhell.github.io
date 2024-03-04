---
title: DWM - not your average mainstream window manager
date: 2011-03-16
category: finland
tags: dwm, gnome, linux, rhel, window, manager
<!-- prettier-ignore -->
---

Have been playing around with a new window manager (new as in for me, I've only
used fluxbox, kde and gnome before) called DWM - see more information on
[www.suckless.org.](http://www.suckless.org "suckless.org")

I'm running it on a T400 with RHEL6 (which uses gnome login manager - gde).

## Basically

1. if you want to make a change like modify keyboard shortcuts, rules, tagging,
   top bar stuff, you need to **edit config.h and then compile** (make and then
   make install). Then you need to re-load dwm.
2. after that is done, create a properly formatted file under
   /usr/share/xsession/
3. then in the login manager you can chose dwm :)

## Notes

1. install dmenu as well, it is neat. ALT+P, then type what you want to run,
   then hit enter. Also if you type in 'lock' it will find xlock etc.
2. ALT+SHIFT+ENTER gives you the terminal, ALT+SHIFT+Q quits dwm and gets you
   back to the login manager.
3. ALT is the default, can be modified to apple- or windows-key

## My problems

1. re-load dwm can be done in several ways but I have not found one that works
   well for me. If you do like me and run dwm in a while loop the only way I've
   found out so far is to reboot the whole machine. Because I don't know how to
   log off the session and get back to the gdm login manager. I hope I do find a
   way around because rebooting kind of sucks ;)
2. gnome-session-save --logout does not work -gave some kind of error
3. MODKEY+SHIFT+Q only seems to re-fresh the screen, doesn't actually re-load
   the whole she-bang.

DWM top bar can be edited to show other things than DWM version. See
[my post here](https://www.guldmyr.com/dwm-editing-the-bar-to-show-time/ "editing top bar in dwm")
about that.
