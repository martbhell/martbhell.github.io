---
title: "DWM editing the bar to show time"
date: "2011-03-14"
categories: 
  - "finland"
tags: 
  - "dwm"
  - "rhel"
  - "status-bar"
  - "statusbar"
---

`xrdb -merge ~/.Xresources while true; do # BAT=$(acpi | awk '{ print $4 }' | sed s/","//g) CLK=$( date +'%H:%M') # xsetroot -name "$BAT | $CLK" xsetroot -name "$CLK" sleep 1 done | while true; do ~/bin/dwm; done`

Will this work to on RHEL6 x64 on a T400 Lenovo/IBM? Let's see tomorrow :)

\*\*\* 14/3 0900- after a little modification the startup script now looks like this (just pointed to it in /usr/share/xsession/dwm.start) - script is also chmod a+x:

`# commands here and before the "while true; do" are run once #not applicable? I do not have this directory in my home dir. #xrdb -merge ~/.Xresources #open screensaver /usr/bin/gnome-screensaver #open power manager #gnome-power-manager

while true; do #battery remaining capacity in mh. About 10 every second. BAT=$( cat /proc/acpi/battery/BAT0/state | grep rem | awk '{ print $3 }' ) #time in this format Monday March 14 08:57:52 CLK=$( date +'%a %b %d %R:%S' ) #volume in % VOL=$( amixer get Master | tail -1 | awk '{ print $5}' | tr -d '[]' ) xsetroot -name "Vol: $VOL | Bat: $BAT | $CLK" sleep 1 done | while true; do /usr/local/bin/dwm; done`

**What I want to figure out is how to logout! .**:DD:dD MODKEY+SHIFT+Q only refreshes the screen. MODKEY+l (which I've set to run "gnome-screensaver-command -l" : lock - lets me run another user, but I cannot logout myself) so with this setup I have to reboot the computer for each time I want to re-load the configuration (after a change in config.h make;make install)

\*\* update 14/3 1600 `static const char *volup[] = { "amixer", "set", "Master", "15%+", NULL }; static const char *voldown[] = { "amixer", "set", "Master", "15%-", NULL };

{ MODKEY, XK_Up, spawn, {.v = volup } }, { MODKEY, XK_Down, spawn, {.v = voldown } },`

will lower/increase the volume with 15% with MODKEY+up or MODKEY+down :) if you are unsure what the key should be called you can run 'xev' which will tell you what they are

KeyRelease event, serial 27, synthetic NO, window 0x1a00001, root 0x111, subw 0x0, time 277994, (965,69), root:(966,87), state 0x0, keycode 111 (keysym 0xff52, **Up**), same\_screen YES, XLookupString gives 0 bytes: XFilterEvent returns: False

KeyPress event, serial 27, synthetic NO, window 0x1a00001, root 0x111, subw 0x0, time 278097, (965,69), root:(966,87), state 0x0, keycode 116 (keysym 0xff54, **Down**), same\_screen YES, XLookupString gives 0 bytes: XmbLookupString gives 0 bytes:
