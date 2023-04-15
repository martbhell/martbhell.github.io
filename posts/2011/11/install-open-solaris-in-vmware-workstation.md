---
title: Install Open Solaris in VMWare Workstation
date: 2011-11-22
category: it
tags: openindiana, opensolaris, osol, solaris, vmware, vmware, workstation

Trying out osol-dev-134-x86.iso in vmware workstation. You can download it from here: (genunix.org doesn't work anymore - here is another place: http://okcosug.org/. Update 201308 this also broke. You can now use [http://virtualboxes.org/images/opensolaris/](http://virtualboxes.org/images/opensolaris/)) Host OS: Core i7 with Windows x64.

1 core and 1300MB RAM, bridged networking and 16GB disk.

Installation looks initially very similar to [openindiana](http://openindiana.org/ "http://openindiana.org/") (I guess it is the other way around..). Choose keyboard layout etc.

When you boot on the disc above you get directly into a desktop. If you only want text you can use the textinstall-134-x86.iso on the same page as above, the openindiana text-based installer had some more options than the ones in this graphical one in opensolaris. From there you can click an icon to install it. It only asks you for user/pw, timezone and partitioning stuff. 3.6GB needed. Nothing more, no packet selection or role customization.

I was not expecting the graphical desktop. Networking works straight from the box. Flash does not. However you can just download a .so file and get it working. _**Just**_ find out where firefox is installed and copy it to the plugins directory. But flash is apparently dying now anyway.

There is an update manager but it doesn't find any updates. Even though this version is from 2010. ? Why? Do I have to register to get updates? Register page takes me to Oracle. Perl version is 5.8.x and latest Perl now is 5.14.x. Supposedly 'pkg image-update' should update but it appears to not work anymore. There is now Solaris Express or whatever Oracle calls it which I presume they want you to update to and pay for. Of course openindiana is still there but it doesn't install on the bl460c.

Protip: To get root level permissions you type 'pfexec su -' or just 'pfexec bash'.

The main idea I wanted to do this was to see what 'touch /reconfigure' did. All it did was to add 'configuring devices' during the boot. Also tried this on a bl460c blade where we replaced the system board. Nothing special, it booted up just fine!
