---
title: "Running Ubuntu on a Desktop"
date: 2012-12-15
category: it
tags: desktop, install, linux, operating, system, tips, ubuntu

# Introduction

Recently I've had the pleasure of installing Ubuntu on my desktop. Here are some thoughts and what I initially do:

Machine is a:

Motherboard: Gigayte GA-EX58-UD3R CPU: Intel Core i7 Memory: 8GB Disks: Intel i300 SSD, 2x500GB and 1x3TB Western Digital Drives. Graphics Card: AMD HD6800

Here are some of the things figured out along the way:

- grub2 does not like keyboard, but if I boot on the Ultimate Boot CD (grub) - the keyboard does work. This is with flipping all the USB keyboard, mouse, storage, legacy .. settings on and off in BIOS.
    - After removing Ubuntu 12.10 and installing 12.04 (this is with USB things enabled in BIOS) - the keyboard works in grub2 menu.
- to install better drivers, easiest is to open Ubuntu Software, edit sources and allow post-release things.
    - then go to settings and "additional drivers"
- after upgrading to fglrx,
    - to change speed of the GPU fan to 20% hit: aticonfig --pplib-cmd "set fanspeed 0 20"
    - to view the speed of the GPU fan hit: aticonfig --pplib-cmd "get fanspeed 0"
    - to view the GPU temperature hit: aticonfig --adapter=0 --od-gettemperature

If you do decide to try with newer drivers for the ATI - card, make sure you have the installation CD/DVD handy. Or even better, get it on a USB-drive, way faster.

To find the devices for / and /boot - at least when I boot up there are these disk icons in the side-bar on the left side. If you hover over the icon you'll see the size, if you click, it mounts and then a folder is opened. Then in the output of 'mount' you can see which device it is. Unmount and then proceed with these to get a working chroot:

sudo mount /mnt /dev/devicethathasroot
sudo mount /mnt/boot /dev/devicethathasslashboot

sudo mount ‐‐bind /dev /mnt/dev
sudo mount ‐‐bind /proc /mnt/proc
sudo mount ‐‐bind /sys /mnt/sys
xhost +local:
# above xhost is to get x things working from within a chroot (possibly unsafe?).
chroot /mnt
# you can get network working, it needs a good /etc/resolv.conf first. Either overwrite the existing one or somehow get the local nameserver up and running

# Install some good software

apt-get install screen openssh-server tmux openjdk-6-jre unrar p7zip pidgin vim

Spotify Repository - http://www.ubuntuupdates.org/ppa/spotify

Google Chrome Repository - http://www.ubuntuupdates.org/ppa/google\_chrome

[Universal Media Server](http://www.universalmediaserver.com/ "fork of ps3 media server")

For UMS you'll also need:

apt-get install ffmpeg mplayer mencoder libzen-dev mediainfo

You also need to make sure zen and mediainfo works - check trace log in UMS to see if there are any errors in the beginning that they are not found. If so the hack is to create symlinks. For me the libzen.so and libmediainfo.so are in the /usr/lib/x86\_64-linux-gnu/ directory.

## Getting graphite running (for graphing / system monitoring )

One reason was that I wanted to learn more about this tool - but another reason is that it's quite light weight, especially if you're going to be running an httpd anyway.

To install it, follow this guide: [http://coreygoldberg.blogspot.fi/2012/04/installing-graphite-099-on-ubuntu-1204.html](http://coreygoldberg.blogspot.fi/2012/04/installing-graphite-099-on-ubuntu-1204.html)

Carbon-cache initd-script: [https://gist.github.com/1492384](https://gist.github.com/1492384)

### To monitor temperature and fan speed of your AMD/ATI card put this script in /usr/local/bin/atitemp.sh:

#!/bin/bash
# Script to monitor temp and fanspeed of an AMD/ATI card.
# amdccle required? Also X?

HOST1="$(hostname -s)"
DEBUG="0"

CMD="$(which aticonfig)"

if \[ "$?" != "0" \]; then
        echo "Cannot find aticonfig, check paths and if it's even installed."
        exit $?
fi

while \[ 1 \];
do

TEMP=$(/usr/bin/aticonfig --adapter=0 --od-gettemperature|grep Sensor|awk '{print $5}'|sed -e 's/\\.00//')
SPEED=$(/usr/bin/aticonfig --adapter=0 --pplib-cmd "get fanspeed 0"|grep Result|awk '{print $4}'|tr -d "%")
DATU="$(date +%s)"
LOGF="/tmp/atitemp.log"

echo "##########" >> $LOGF

if \[ "$TEMP" != "" \]; then
echo "servers.$HOST1.atitemp $TEMP $DATU"|nc localhost 2003

if \[ "$DEBUG" == "1" \]; then
echo $TEMP >> $LOGF
fi

fi

sleep 1
if \[ "$SPEED" != "" \]; then
echo "servers.$HOST1.atifanspeed $SPEED $DATU"|nc localhost 2003

if \[ "$DEBUG" == "1" \]; then
echo $SPEED >> $LOGF
fi

fi

sleep 60;
done

### To graph useful system resources (network bandwidth, cpu/mem-usage, disk space)

Would be good to install collectl and just export to graphite. But this does not work well currently because the version of collectl with Ubuntu 12.04 LTS is 3.6.0 (3.6.3 with 12.10). 3.6.1 is needed to make it work with graphite and 3.6.5 to make it work good if you want to group servers.

There are plenty of other options though. You can write some scripts yourself, use diamond or a few other tools that has graphite-support.

Diamond is another option, to install follow these two links [https://github.com/BrightcoveOS/Diamond/wiki/Installation](https://github.com/BrightcoveOS/Diamond/wiki/Installation) (only addition is first you have to clone the git repository, from in there you run make builddeb).

How to manually configure a custom collector: [https://github.com/BrightcoveOS/Diamond/wiki/Configuration](https://github.com/BrightcoveOS/Diamond/wiki/Configuration)
