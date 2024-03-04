---
title: DWM - start up script that works with GDM login manager
date: 2011-03-18
category: it
tags: dwm, gdm, gnome, linux, rhel, window, manager
<!-- prettier-ignore -->
---

Goal: Be able to exit [DWM and](http://dwm.suckless.org "dwm at suckless.org") get back to the GDM - gnome login manager. To be able to hit MODKEY+SHIFT+Q, exit dwm and get me back to the login manager. Where I can chose another user or window manager. Or if I make a change in dwm and need to re-load it, this would work as well. Before I had to reboot :)

Finally got this working like I want it to - with some help from #suckless on
irc.oftc.net. This works for me with RHEL6, GDM --version 2.30.4 and DWM 5.8.2.
My problem was that before (you can see how that looked in
[this post](https://www.guldmyr.com/dwm-editing-the-bar-to-show-time/ "dwm not so good"))
I ran the dwm also in a loop. But this is not necessary. If you want to keep the
statusbar updated with some goodies by running a while loop, you only need to
run the xsetroot in a while loop.

/usr/share/xsessions/dwm.desktop

Looks like this:

```text
[Desktop Entry]
Encoding=UTF-8
Name=dwm
Comment=This session starts dwm
Exec=/usr/local/bin/dwm-start
Type=Application
```

/usr/local/bin/dwm-start

Looks like this (updated on 2011-04-18):

```bash
#!/bin/sh
#not applicable? I do not have this directory in my home dir.
#commands here and before the "while true; do" are run once #xrdb -merge ~/.Xresources #open screensaver (so that gnome-screensaver-command -l works)
/usr/bin/gnome-screensaver & #open pwer manager #exec gnome-power-manager

#black bg #want this #path to background #/usr/share/backgrounds/abstract/Flow.png

xsetroot -solid black

while true; do
    #battery
    battotal=$(awk '/last full capacity/{print $4}' < /proc/acpi/battery/BAT0/info)
    batfree=$(awk '/remaining capacity/{print $3}' < /proc/acpi/battery/BAT0/state)
    battper=$(( 100*$batfree/$battotal ))
    battery=$(awk '/charging state/{print $3}' < /proc/acpi/battery/BAT0/state)

    #memfreak to get it in MB
    memfreak2=$(grep MemFree /proc/meminfo | awk '{ print $2 }')
    memfreak=$(( $memfreak2/1024 ))

    #time
    CLK=$(date +'%a %b %d %R:%S %Z')

    #volume
    VOL=$(amixer get Master | tail -1 | awk '{ print $5 }' | tr -d '[]')

    #loadavg
    AVG=$(cat /proc/loadavg | cut -d ' ' -f -3)

    #network stats in Bytes
    #NW=$(dstat -n --nocolor 1 1 | tail -1 | awk '{ print $1, $2 }')
    #this one is not so good, increases a delay of 1-2s of the updating.
    #put it in the xsetrootname plz (tip of the day, do not put | as first char after "

    xsetroot -name "$AVG | $memfreak MB | $battper% $battery | Vol: $VOL | $CLK | "
    sleep 1

#loop is done? :p

```

`#traying sleep 1 /usr/bin/ck-launch-session & /usr/local/bin/stalonetray & /usr/bin/nm-applet & /usr/bin/gnome-volume-control-applet & feh -z -Z --bg-scale /home/jguldmyr/Pictures/dwm_pattern.png #feh -z -Z -B black -b trans --bg-scale /home/jguldmyr/Pictures/Flow.png #start dwm after loop exec /usr/local/bin/dwm > /dev/null`
