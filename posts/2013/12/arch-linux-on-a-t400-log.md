---
title: "Arch Linux on a T400 - Log"
date: 2013-12-14
category: it
tags: arch, arch, linux, install, laptop, lenovo, linux, t400

Trying out Arch Linux on a Lenovo T400!

First step after getting the T400 Dual Core Centrino 2.26GHz 4GB RAM: replace the 160GB spinning rust to a 120GB Samsung 840. Very easy to take out the old disk and put the new SSD in the carrier.

[https://wiki.archlinux.org/index.php/Lenovo\_ThinkPad\_T400](https://wiki.archlinux.org/index.php/Lenovo_ThinkPad_T400) has some details.

[https://wiki.archlinux.org/index.php/Installation\_Guide](https://wiki.archlinux.org/index.php/Installation_Guide) and the [Beginner's Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide) are quite helpful.

To make it easy, the partition layout I created with parted was:

mklabel: MSDOS mkpart: pri, 0%, 300M /boot ext4 - flag bootable mkpart: pri, 300M, 100%, /, ext4 No swap!

Install base and some important packages to disk after mkfs and mounting and setting up mirrors:

pacstrap /mnt base dialog iw wpa\_supplicant grub parted sudo alsa-utils vim ttf-dejavu openssh screen

[Beginners'\_Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide) had sufficient instructions to set up the boot loader, except this was needed or the grub-mkconfig would fail with syntax error.

echo "GRUB\_DISABLE\_SUBMENU=y" >> /etc/default/grub

After successful boot time to get a graphical display up and running :)

Beginner's guide to the rescue: [Beginners'\_Guide#Graphical\_User\_Interface](https://wiki.archlinux.org/index.php/Beginners'_Guide#Graphical_User_Interface)

[Lightdm](https://wiki.archlinux.org/index.php/LightDM) was easy to set up and worked right out of the box, which GDM did not. [DWM](https://wiki.archlinux.org/index.php/Dwm) was easy too, I think I can get used to using the ABS/makepkg stuff. Nicer than compiling it and copying the binary around.

Windows key is Mod4Key in config.h for DWM.

Packages and getting chromium-pepper-flash working:

1. [Install all the dependencies for Aura](https://wiki.archlinux.org/index.php/Aura)
2. Download aura and makepkg -i install it
3. aura -A chromium-pepper-flash

alsamixer and pressing "m" mutes/unmutes a channel :)
