---
title: Upgrade Ubuntu 10.10 to Natty
date: 2011-05-23
category: it
tags: 10.10, 11.04, kernel, linux, natty, ubuntu, upgrade, vmware, workstation

Saw this note today in the MOTD - that I can upgrade with **do-release-upgrade.**

Official [instructions/details](http://www.ubuntu.com/download/ubuntu/upgrade ".com") from Ubuntu and [here](http://www.unixtutorial.org/2011/03/upgrading-ubuntu-with-do-release-upgrade/ "unixtutorial") is another quality post  on unixtutorial.

My Ubuntu 10.10 is running inside a VMWare Workstation Virtual Machine on my Windows 7 x64.

I did it over ssh with 'sudo screen -S upgrade **do-release-upgrade**' . Probably not wise to do this over ssh, but the setup started an extra sshd service on another port, just in case something breaks.

It would need to download about 210MB of packages, if you press on 'd' at the right time you'll get into a 'less' of all the removes, upgrades and new installs. Press q to exit that.

## During upgrade

- I got to chose keyboard (I have an IBM Thinkpad T40, but it wasn't in the list, took an R60 instead, looked pretty similar).
- It then asks for which services that are using NSS (I had no idea, so just used the default of rsync, mysql, apache and one more).
- memtest86?? Does it come with this automagically? This is pretty cool, I've only heard about this being used in an iso to quite thoroughly test memory. The OS uses quite a lot of the RAM so if you test RAM from inside the OS you will not be able to test all, thus the boot CD. However, later on it turns out that memtest86 is actually put in the grub/boot menu! Very handy!
- [apparmor](http://en.wikipedia.org/wiki/AppArmor "on wikipedia") - this is a security module - apparently you can give applications profiles
- [2.6.38](http://kernelnewbies.org/Linux_2_6_38 "on kernelnewbies.org")! woop! See the link for more updates in the kernels. On that page - kernelnewbies.org - you can also find details about the other updates. Kernel.org only has detailed change log as far as I could see (lots of text).
- Later on it asks you, do you want to delete these packages (d for details): libisc60, libdns66, [linux-image-2.6.35-22-generic](https://www.guldmyr.com/upgrade-ubuntu-10-10-to-natty "This is the kernel, you are installing a newer one :)"), python-newt, [libxapian15](http://packages.ubuntu.com/hardy/libxapian15 "supposedly a new indexer has been introduced"), [byobu](http://packages.ubuntu.com/natty/byobu "a profile switcher, supposedly a new one has been introduced here as well")
- ﻿﻿Last question: do you want to reboot? - **No pain, no gain.** Is 'adventurous' to do kernel upgrades remotely ;)
- VM came back online after what felt like just 15 seconds.
- ﻿Welcome to Ubuntu 11.04 (GNU/Linux 2.6.38-8-generic x86\_x64)!
