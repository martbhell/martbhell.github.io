<!-- markdownlint-disable  MD027 -->
---
title: Non Brocade Branded USB stick activation
date: 2020-09-17
category: storage
tags: brocade, usb
<!-- prettier-ignore -->

Another submission courtesy of **Eberhard**.

Run anything here at your own risk. From what I can tell they should be fairly safe. Do make sure you run them on the switch itself. Pretty nice in case you don't want to shell out for a Brocade branded USB stick to transfer firmwares!

Hi,

_I found a description how to format a USB-Stick that could be accessed  
by the brocade OS._

In fact after some investigation I noticed an error of this description  
that prevents to  
access this special configured stick.

To make life easier I modified the /sbin/hotplug script by adding one line.  
Now any USB-Stick may be used for installation or backup purposes.

The modified hotplug script adds the VENDOR string to  
/etc/fabos/usbstorage.conf if the vendor is unknown.  
If you redo the "usbstorage -e" command the previously unknown Vendor  
stick is been recognized by hotplug  
and the activation of the access succeeds!

It might be annoying to do the activation of a stick twice but this has  
to be done only if the vendor of the  
usb-stick is new for your brocade switch.

Fabos is capable to handle VFAT32-formatted sticks.

The stick needs 5 directories (1 and 4 children):  
/brocade/  
/brocade/config  
/brocade/firmware  
/brocade/firmwarekey  
/brocade/support

Here is the diff

> \# diff hotplug.orig hotplug  
> 62c62  
> <  
> \---
>  > echo   "VENDOR $vendor" >> $USBCONFIG  
> 63a64  
>  >
>
> The above output means - "Add the 'echo ... ' bit on line 62"

All stuff is been tested with FOS v7.4.2f.

Insert stick in a switch and run this script as root:

```bash
#!/bin/bash -x
insmod /lib/modules/default/kernel/drivers/usb/core/usbcore.ko
insmod /lib/modules/default/kernel/drivers/usb/host/hcd-driver.ko
insmod /lib/modules/default/kernel/drivers/usb/storage/usb-storage.ko
sleep 10
lsmod | grep usb
/bin/mknod -m 660 /dev/sda b 8 0
/bin/mknod -m 660 /dev/sda1 b 8 1
/bin/mknod -m 660 /dev/sda2 b 8 2
```

Sometimes the above script fails and you need to run it until it has usb\_storage and usbcore modules listed as loaded kernel modules.

Now I can mount an ext3 formatted USB-stick:

```bash
# mkdir /usb_ext3

# mount -t ext3 /dev/sda1 /usb_ext3

# ls /usb_ext3/

bin/         dev/     fabos/   libexec@  sbin/           tftpboot/ var/
boot/        diag@    import/  mnt/      share@          tmp/
config/      etc/     initrd/  proc/     standby_sbin/   users/
core_files/  export/  lib/     root/     support_files/  usr/

# mkdir /usb_vfat

# mount -t vfat /dev/sda1 /usb_vfat

# ls /usb_vfat/
.Trash-1000/  brocade/  config/  firmware/  firmwarekey/  hda1.dmp* support/
```

I'll stop here at the moment because now I need to know how u-boot  
starts an OS from an USB-stick...
