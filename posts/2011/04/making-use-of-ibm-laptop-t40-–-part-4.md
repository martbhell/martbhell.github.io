---
title: Making use of IBM Laptop T40 – Part 4
date: 2011-04-19
category: finland
tags: 10, 10, hdd, hdparm, ibm, laptop, linux, pata, replace, hard, drive, synergy, t40, thinkpad

Logging in!

Wireless worked straight from the start. It says that my battery probably is broken (only 28% capacity). Some 2.6~GB is used by the default installation out of my 40GB disk. 1.6GB for swap.

### Step 1 - set up Synergy.

This is so I don't have to use the laptop keyboard/mouse but instead can just move the mouse from my desktop and I can then control the laptop. It is pretty awesome. To do this, go to the Applications/ubuntu software center and search for synergy. Then install QuickSynergy. I had to click on "use this source" first.

Then go to accessories and quicksynergy and put in IP of the machine where you have synergy and a screen name. Tada. I wonder if this works after a reboot. But doesn't matter much, you can just drag the entry in the applications menu to the ubuntu desktop and then you'll see it when you log in.

You can find more details on the [Ubuntu community pages](https://help.ubuntu.com/community/SynergyHowto "synergyhowto").

Trying this out, it's a little tricky. Managed to bork the login with this. Cannot even get into recovery console. Probably a wrong character somewhere :/ If this happens, hit CTRL+ALT+F1 to get to the console prompt.

Anyway, follow that guide. But you do not have to have the while thing when putting the stuff in the gdm session files. Instead you can just put the "sleep 1". This means you'll have a lag of 1 second. But it's working.

/usr/bin/killall synergyc
sleep 1
/usr/bin/synergyc --name identifywithname IP.IP.IP.IP

### Step 2 - Install Updates.

This popped up automagically. 302MB of extra updates does it want to install. I just went with the default, always good to have updates :) The root password is the same as your normal password, unless you've done something special. During the updates the cursor when I was using synergy was lagging behind. But that's because I'm using a poor wirless connection (maxes out at 580kB/s) and the update probably uses all it can get. The normal mouse works fine :)

You may have heard that 'you don't need to reboot in Linux' this is true unless you make a change to the [kernel](http://en.wikipedia.org/wiki/Linux_kernel "linux kernel on wikipedia"). Which is what this update updated.

### The rest - whatever you feel is important :)

### hdparm - testing hard drive

I have some suspicion that the internal hdd is singing on its last verse. The built-in tool to test IDE/ATA drives is: [hdparm](http://en.wikipedia.org/wiki/Hdparm "hdparm on wikipedia"). First though you want to find what device name your disk has. If you type 'mount' you will see on top something like this:

`/dev/sda1 on / type ext4 (rw,errors=remount-ro,commit=0)`

This will tell you that /dev/sda1 is where / is installed. / is root. The file system.

The syntax to test the hard drive cache:

`martbhell@bottle:~$ sudo hdparm -T /dev/sda`

`/dev/sda: Timing cached reads:   688 MB in  2.00 seconds = 343.59 MB/sec martbhell@bottle:~$ sudo hdparm -tT /dev/sda`

 

`/dev/sda: Timing cached reads:   774 MB in  2.00 seconds = 386.65 MB/sec Timing buffered disk reads:  102 MB in  3.00 seconds =  33.95 MB/sec`

So that looks good. I feel better now :)

### webbrowser - ubuntu 10.10 comes with Firefox 3 and when I search it doesn't find Firefox 4

So we install google chrome!

All you have to do is go use firefox and find google chrome page. Download the .deb package (ubuntu is based on debian). And open, this will open Ubuntu Software Center. Install.

### DWM in Ubuntu

find dwm in ubuntu software center, also installing dzen2 with the add-on "i3status". When you install dwm you also get suckless-tools - which include dmenu and more.

#### To start it:

- get to the login screen
- select user
- change from ubuntu desktop to dwm
- login!
- then in there, hit ALT+p - type quick, (you'll see quicksynergy) - hit enter
- set that up, and then you can use synergy in there as well
- to log out: ALT+SHIFT+Q

#### To change stuff:

To change stuff in DWM you need to re-compile the package. Because I found dwm in ubuntu software center I was inclined to use that. But maybe the best option would be to do it manually..

Then, downloading it from suckless.org Making sure that the config.mk points to where dwm is not currently installed. (Maybe I should have uninstalled it first).

See /usr/share/xsessions/dwm.desktop That is the file that starts dwm. It's also a good idea to point the xsession startup script to a script that runs xsetroot in a loop, if you want to update 'xsetroot -name' with time, for example.

You can see more details and my scripts in [this blog post](http://www.guldmyr.com/blog/dwm-start-up-script-that-works-with-gdm-login-manager/ "dwm script"):

When I try to compile dwm, it complains that X11/cursorfont.h is missing. Probably because libx11-dev is not installed. After installing, it complains that X11/extensions/Xinerama.h is missing. Installing libxinerama-dev. After that it compiles just fine and runs just fine.

Previous posts:

[Part1](../making-use-of-ibm-laptop-t40-part-1/ "PART1") – thoughts before installing [Part2](../making-use-of-ibm-laptop-t40-%E2%80%93-part-2/ "par2") – ultimate boot CD – for diagnostics [Part3](http://www.guldmyr.com/blog/making-use-of-ibm-laptop-t40-%E2%80%93-part-3/ "part3") – Installing Ubuntu
