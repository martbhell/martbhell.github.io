---
title: Raspberry Pi 4 with external SSDs
date: 2023-06-13 22:03
category: it
lang: en
tags: it, ssd, rpi, raspberry pi, raspberry pi 4, sata, usb
<!-- prettier-ignore -->
---

## Why This Exercise?

Before this post I had an old mini-itx server with ssds at home.

- a 120GB, 4TB and a 2TB SSD all from Samsung, and one fourth 1TB now broken/missing one device that doesn't power on anymore :/.

This really shouldn't have been an issue but I didn't want to do RAID1 because the data wasn't that important to me and I had added them into an LVM RAID0 instead.

Fortunately I don't remember exactly what I did with the 1TB storage device, maybe I wasn't using it anymore but it was still part of the LVM VG? Anyway, files couldn't be read and there were some corrupted sqlites.

## What

I first looked around for some cheap NAS boxes to put the SSDs in. No avail and definately not cheap.

Then I looked behind my monitor on my desk and saw an unused raspberry pi 4 with 8GB RAM.

Huh. Can I?

Insert research to find some good posts [like this](https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-set-up-an-ssd-with-the-raspberry-pi)  from thepihut.

It also had some link to a cable but unfortunately I couldn't order it. Maybe my card doesn't work outside EU?

## Next

- before powering off the old server I vgexported the LVM
- usb active plus right SATA to USB cables with controller? That RPI 4 likes.
  - [startech](https://www.startech.com/en-us/hdd/usb312sat3cb) had some overpowered 10Gb cables
  - firmware for the cable was not needed to update
- Why was i Lazy with the lvm raid0 stripe lol of course first disk dies
- always running out of more power extension at home, but now I think we're OK again
- Got an Active USB hub from TPlink(TP-LINK UH720 active 7-port USB3.0) (needed because the RPi4 cannot power these disks)
  - Doesn't exactly match the 3.1 USB of the USB to SATA cables.

### I tried to recover some of the data just for the practice

After plugging in both disks via the active hub:

- `vgs` finds it!
- `vgchange -ay vg_data --activationmode partial`
  - 1 LV activated!
- `mount -t /dev/vg_data/lv_data /mnt/recovery -o ro`
  - works! And just tried to copy one image out and that worked woop! 2.8TB used with 3.4T free.
  - now what, get another 4TB disk and copy stuff there then juggle stuff around?
    - mount as rw and delete data until it's < 2TB
      - possibly risky?
      - did it anyway and it had "mounting fs with errors" in `dmesg` output
      - du has input/output errors to parts of this, but not the whole thing
      - started to delete stuff
    - Make sure all data is on the 2TB PV sounds like a good idea
    - Remove 4TB PV from VG `vgsplit`  or `vgreduce`
      - tried vgreduce - wasn't happy
      - wanted a vgreduce with --removemissing but that complained about partial LVs in the VG
      - Maybe just easier to copy stuff out I want to save and then start from scratch?
    - Create a new LVM with the 4TB then move stuff there
    - Then create another VG with the 2TB and put some other stuff there?

## In the end

- Copied stuff out from the rpi4 into my desktop which had a few 100GB free on a disk.
- Then wiped out the LVM on the two SSDs and created some new setup.
