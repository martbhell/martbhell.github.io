---
title: Raspberry Pi 4 network disconnects
date: 2024-01-29 22:03
category: it
tags: it, network, rpi, raspberry pi, raspberry pi 4, eee, bcmgenet, eth0
lang: en
---

## What was going on?

The wired network connection lost connection every now and then. Most of the time this didn't bother because buffering but sometimes it did annoy.

This was visible in `dmesg -T` output:

```bash
[Mon Jan 22 20:48:23 2024] bcmgenet fd580000.ethernet eth0: Link is Down
[Mon Jan 22 20:48:34 2024] bcmgenet fd580000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
```

## What was tried

 - disabling wifi and bluetooth (done by setting this in /boot/config.txt):

```bash
[all]
dtoverlay=disable-wifi
dtoverlay=disable-bt
```
 - disable eee (Energy-Efficient Ethernet), done by adding this to /etc/rc.local:

```bash
/usr/sbin/ethtool --set-eee eth0 eee off
exit 0
```

## What really really helped

 - making sure the cable is properly connected into the switch, the plastic flap that keeps it in is apparently broken
