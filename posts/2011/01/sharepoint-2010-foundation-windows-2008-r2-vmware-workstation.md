---
title: Sharepoint 2010 Foundation + Windows 2008 R2 + VMWare Workstation
date: 2011-01-30
category: it
tags: it, sharepoint, vmware, workstation, windows
<!-- prettier-ignore -->
---

## Overview

I just write down notes from the installation. But intended as a guide for how
to set up your own sharepoint lab.

### Guides and Documentation

Sharepoint server on technet:
[http://technet.microsoft.com/en-us/library/cc303422.aspx](http://technet.microsoft.com/en-us/library/cc303422.aspx "sharepoint server technet")

SQL Server 2008 R2 and Sharepoint 2010 server I downloaded the trial from
Microsoft.

### Terminology

VM - Virtual Machine Host OS - I installed VMWare Workstation on my home
desktop, so the Host OS will in my case be Windows 7 as that's what's installed
on it. Guest OS - On this host OS I have installed Windows 2008 R2 - this will
be running inside VMWare Workstation. NAT - Network Address Translation

## Installation

1. Install VMWare Workstation
2. Install Windows 2008 R2
3. Install a client - Windows 7 x64 - or connect from the host os.
4. Install SQL Server 2008 R2
5. Install Sharepoint

### Windows 2008 R2

Easy Setup may not be the best choice -> when I did it took the timezone I was
in and decided that Ukrainian would be a good language.

In the beginning it's probably best to have the VMs connected to the Internet
(so you can apply patches) - setting is called NAT when setting up the VM. I
chose 2GB RAM and 40GB disk space (guide says 4GB RAM and 80GB disk).

The password/account you specify needs to meet the Windows 2008 password
requirements.

Install patches Set up remote desktop - so you can connect from your host and
connect your host OS local disk drive to the guest OS - good way to share files
between them.

I did not read the documentation or find a good step-by-step, figured I would
try it out without any of that - this way I would learn better.

#### Initial Roles

Figured that a domain would be good to start with.

Select AD Domain Services and install. This installed .net 3.5.1 and then asked
me to run dcpromo.

DCpromo - new forest - fqdn: guldmyr.lan - forest functional level: 2008 R2.
Then it examines DNS configuration, takes forever, probably because I don't have
a DNS server installed. A while later it asks if you want to install the DNS
server. Which recommends having a static IP. Changed ip to 192.168.232.10. Then
it asks something about delegation, went to next and there you see a summary -
with install DNS selected. That went without a hitch. Restarting. You get to set
a special AD password as well. **Reboot**.

To test that the AD was probably installed - you now can either install a new VM
with a client to try to log on. Or you can use the remote desktop and
authenticate with a domain account. Also a "ping win2k8" or "ping guldmyr.com"
showed that dns might be working as well. After the reboot the DNS server in the
ipv4 configuration was changed to localhost - 127.0.0.1.

This worked for me with only the above steps - pretty easy!

When I open server manager there are some errors but none seems to awful. There
are best practices you can run to improve things / harden the setup - but this
is not so important at the moment - I just want to get a sharepoint server up
and running.

### SQL Server 2008 R2

Installing this package: SQLFULL_ia64_ENU of 1.4GB. This extracts everything
inside and takes roughly 2GB of space. Turns out the IA64 does not work on an
x64 system. So then I tried to download SQL Express 2008 R2 instead, and it's
free and only 250MB! <http://www.microsoft.com/express/Database/>

Let's see how this goes :) Installing this package: SQLEXPRWT_x64_ENU of 250MB

New installation, accept, chose default settings in regards to directories and
what to install, named instance - default settings,  Create an account - I named
it SQL - click on browse to select it - format is GULDMYR\\SQL. Then you get to
specify SQL Server Admins. After that it's installing. Completed without any
hitches. Pathces. **Reboot**.

SQL Server Management Studio - could not connect.

**Uninstalling SQL Server 2008 R2.** Selected the R2 x64. That took care of
most. ALso ENU and native client I uninstalled. Because in the hardware/software
requirements this is mentioned Preparation Tool installs "SQL Server 2008
Express with SP1"

### Sharepoint Server 2010

Couldn't install -  error: "installation of this package failed" Couldn't
extract the file either - broken download. Re-downloaded.

OK, this extracted. Now it says that the language is not supported. Stupid
Ukrainian. Reinstalling Win2k8

Reinstalled win2k8 - chose "install OS later" to get rid of the auto-install.
Also changed RAM to 3GB and disk to 40GB (it doesn't use space until it's used).

Now all is in English!

Did not install AD services this time. Did not configure a second account, doing
the install with the Administrator account.

Downloading Sharepoint 2010 Foundation instead of the server version.

Selected "install software pre-requisities". This installed
[lots of stuff](http://technet.microsoft.com/en-us/library/cc262485.aspx "pre-requisities")
successfully. **Reboot**. Install continues afterwards. Ran installation file
again, chose standalone setup. Completed OK. Then a wizard runs. Completed.

Opens `http://win2k8/` - log on with administrator

And now we got a sharepoint!

## Summary

With the Foundation version there are a minimal amount of settings to configure
when following the wizards. No choice in terms of storage, sql server, accounts.
Just click-click-click!

Total size of the VM after all this is 13.6GB (14 661 324 079 bytes).

1. Install Windows 2008 R2
2. Patch it.
3. Run Sharepoint 2010 Foundation pre-requisities install
4. Run Sharepoint 2010 Foundation install
5. Point your web browser to `http://localhost` or `http://servername`. OR
   `http://ip` (this will work from the host os).

Next post will be about what to do inside sharepoint!
