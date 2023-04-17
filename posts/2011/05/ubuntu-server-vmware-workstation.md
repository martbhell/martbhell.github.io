---
title: Ubuntu Server + VMWare Workstation
date: 2011-05-30
category: it
tags: chat, eyeos, irssi, linux, sharepoint, ubuntu, virtual, machine, vm, vmware, workstation, windows

### **0/ Have your own virtual machine in your desktop is not hard!**

#### 0.1/ Some Terminology

- OS - Operating System
- Host OS - Underlying OS - in this you install [VMWare Workstation](http://www.vmware.com/products/workstation/ "vmware workstation").

> - Host needs to be stared for the guest to be able to start.

- Guest OS - The extra OS you install inside the host or in VMWare Workstation.
- VM - Virtual machine.

### **1/ Pre-install**

#### 1.1/ Storage space, memory, CPU

What do you want to do? Do you have enough of it? My desktop has an Intel i7-920, 8GB RAM and two 500GB hard drives. Generally when testing I would give it 1GB or maybe 2GB for Windows. This can be decreased later if you feel the need. You can also increase storage, memory and CPU after you create your virtual machine. It is easy to create a new virtual machine so do not worry if you make it too small or too big.

#### 1.2/ Network setup, LAN, Bridged, Hidden.

Do you want to be able to access your VM from your LAN, Internet or do you want a completely private network between your virtual machines?

Especially if you do set up a Windows guest OS (perhaps to use as a client in your test environment) please do remember that before you connect it to the Internet (to install patches etc) you should definitely **think about installing an anti-virus solution** on it. I recommend [Microsoft Security Essentials](http://www.microsoft.com/security/pc-security/mse.aspx "on microsoft.com") (MSE) - it is free and takes up little resources. I read recently that the time you have until your unprotected computer is infected is about 10 seconds. But if your computer is behind a NAT - broadband router (so it has an IP like 192.168.x.x or 10.x.x.x or 172.16.x.x.x) then it is safer, but not safe from other computers on your network.

### **2/ Install the OS**

#### 2.2/ Download Ubuntu, easy setup wizard

There are two versions of Ubuntu - desktop and [server version.](http://www.ubuntu.com/server "ubuntu server") If this is your first time with Linux you may be better of starting with the desktop variant. I used the server version (uses less resources - no graphical user interface).

[Here is a guide](https://www.guldmyr.com/ubuntu-10-10-minimal-virtual-kernel-vmware-workstation/ "ubuntu-10-10-minimal-virtual-kernel-vmware-workstation") for using the Ubuntu Virtual Kernel with VMWare Workstation.

#### 2.3/ Windows 2008 R2?

[sharepoint-2010-foundation-windows-2008-r2-vmware-workstation](https://www.guldmyr.com/sharepoint-2010-foundation-windows-2008-r2-vmware-workstation/ "sharepoint-2010-foundation-windows-2008-r2-vmware-workstation")

### **3/ Set up management**

#### 3.1/ sshd - autostart if you reboot host OS / Windows.

I haven't managed to set up autostart of the VM when rebooting the OS. But then again, I do not run "life-critical" services in the virtual machine, just some cheap bash-script and an EyeOS. Not sure if I want to have it autostart, I like to have a fast reboot.

#### 3.2/ Timezone, time.

Quite frustrating, but here is how it worked out in Linux: [time-sync-for-linux-vms-in-vmware-workstation](https://www.guldmyr.com/time-sync-for-linux-vms-in-vmware-workstation/ "time-sync-for-linux-vms-in-vmware-workstation/")

### 4/ Post-Installation Joy

#### 4.1/ Something simple like screen + irssi

This is really easy to set up. Basically all you need to do is install these in a Debian style Linux (like Ubuntu):

**sudo-apt get screen irssi openssh-server**

then start a screen session called chat and the command 'irssi'

**screen -S chat irssi**

It then starts irssi in a screen. You can hit CTRL+A+D (or, CTRL+A D also works) to detach it and get back to the terminal. You can then close the terminal / log off from the server. Next time you log on you can just type:

**screen -rdx chat**

[Irssi](http://irssi.org/ ".org") is my IRC tool of choice, it's slim and well, I've gotten used to it. It has scripts and you can do encryption and lots of nice little things with it if you want to.

Of course the screen does not resume when you restart the whole server / virtual machine.

#### 4.2 Other ideas:

[Red Hat Enterprise Linux in VMWare Workstation.](https://www.guldmyr.com/red-hat-enterprise-linuxrhel-in-vmware-workstation/ "red-hat-enterprise-linuxrhel-in-vmware-workstation/") [How small VM can you have for just IRSSI?](https://www.guldmyr.com/ubuntu-10-10-vmware-irssi/ "ubuntu-10-10-vmware-irssi/") [File share from Windows to Ubuntu in a VM.](https://www.guldmyr.com/file-share-from-ubuntu-10-10-with-windows-7-client/ "file-share-from-ubuntu-10-10-with-windows-7-client/") [EyeOS](https://www.guldmyr.com/eyeos-cloud-desktop-in-your-browser-part-2/ "eyeos-cloud-desktop-in-your-browser-part-2/") - OS in your web browser.
