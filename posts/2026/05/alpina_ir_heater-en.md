---
title: Alpina IR Heater
date: 2026-05-17 23:57
category: it
lang: en
tags: ir, infrared, heater, flipper zero
<!-- prettier-ignore -->
---

## Alpina Infrared Heater 2000 W

I got an Alpina Infrare Heater 2000W off of amazon, it's been working fine except the fuse trips every time we use it.

So it's using too much initially but then works nicely.

It comes with a remote and if I:

1. press "1"
2. fuse trips
3. I flip the fuse
4. press "1" : the heater heats!

Anyway, the topic of this post is that I'm worried about losing the remote.

[flipper zero](https://flipper.net/) IR reader enters the chat!

The flipper tells me it's `NEC`, sending to `00 00 00 00` and the commands are:

- Power On: `0D 00 00 00`
- Level 1: `40 00 00 00`
- Level 2 (warmer): `43 00 00 00`

[AlpinaHeater.ir](extras/Heater.ir)
