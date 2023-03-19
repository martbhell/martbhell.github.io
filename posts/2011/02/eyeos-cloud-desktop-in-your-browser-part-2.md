---
title: "EyeOS - Cloud Desktop in your browser - Part 2"
date: "2011-02-05"
categories: 
  - "it"
tags: 
  - "10-10"
  - "activemq"
  - "apt-get"
  - "cloud"
  - "dns"
  - "eyeos"
  - "http"
  - "icloud"
  - "kaazing"
  - "pico"
  - "ubuntu"
  - "virtual-desktop"
  - "vmware"
  - "vmware-workstation"
  - "web-2-0"
---

After [my first comment ever](http://www.guldmyr.com/blog/eyeos-cloud-desktop-in-your-browser/#comment-42 "eyeOS part 1") by Adrian from the eyeOS forum I will now try this again and try not to install eyeOS wrongly by following a guide!

1/ Because I also tried to install cactii on the same VM the other day - and after that I saw some nasty out of memory messages. I will create a new VM - fresh, and with only 256MB RAM!

However, the guide is only for 2.x - So I will freestyle this time too. But follow the installation instructions on eyes.org :)

## Overview

1/ Install Ubuntu 10.10 2/ Follow guide Not possible because uh, there is none for Ubuntu. There is one that begins with graphic interface for Debian. 3/ Win!

Requirements - PHP5

## Installing Ubuntu

I use VMWare Workstation. File -> New VM. Typical, installer disc image. I used ubuntu-10.10-server-amd64 - I have an intel core i7.. (this is the one I used before, tried to find on ubuntu.com which one I should use but it says if you have a 64-bit, you'll get the amd64..). Anyway. and also apparently it's possible to press [F4](https://help.ubuntu.com/community/ServerFaq#What%20are%20the%20differences%20between%20server%20and%20virtual%20kernels?) during install and it will install a 'virtual kernel' which is good for when running in a virtualized environment! I had to change memory down to 256MB and then I also set the network type to "bridged" - so that it gets IP/DNS settings from my router instead of from my computer.

Also found a [forum post](http://ubuntuforums.org/showthread.php?t=1423743 "x86 or amd64?") that confirms, if you have an Intel 64-bit CPU - it is the "amd64" version you want to install.

So first time when I entered the VM through the VMWare shell everything worked fine. Except that they keyboard was a bit messed up. When I pressed down it sent an enter. In SSH via PuTty it's working so I'll do it that way instead. If you have this problem, check out [this post](http://ubuntuforums.org/showthread.php?t=1116511 "down arrow not working ubuntu vmware") \- might be a VMWare bug or you may fix it with some CLI magic.

sshd is not installed by default -> **sudo apt-get install openssh-server**

_Also probably good to change IP in the beginning, in case you want it on a static IP. See my [previous post](http://www.guldmyr.com/blog/eyeos-cloud-desktop-in-your-browser/ "unbuntu static ip") how to set that. It's a at the bottom of the post._

### Time

Another good thing would be to set the time zone on the VM. You can find out how to do that in [this pos](http://www.guldmyr.com/blog/lifehack-currency/ "lifehack / set timezone")t about lifehack/currency exchange rate.

To sync the time - so that it is up to date (mine was 30mins off) -

Edit /etc/default/ntpdate Add a pool or use the default one - http://www.pool.ntp.org/zone/fi for Finnish ones. Then run **sudo ntpdate-debian**

Do I really need to run this anymore? I'll just let it be and try to keep track of it :p

\*\*\* Update: Just checked in on the time some 2 hours later and:

4 Feb 14:43:45 ntpdate\[2494\]: step time server 194.100.2.198 offset 910.266238 sec

So we need to have this executed every now and then, especially if it's off 15minutes in just a couple of hours!!

Also found post on [debian.org](http://lists.debian.org/debian-user/2002/12/msg04091.html "don't use ntpdate in crontab") which clearly says that ntpd is awesome for fixing this. Especially in my case where the clock appears to be going slowly.

sudo apt-get install ntp sudo pico /etc/ntp.conf

add your NTP-servers in there, I added those from the link above on ntp.org

then if you run this: sudo /etc/init.d/ntp status it will tell you if it is running or not

I'll check back tomorrow to see if this improved things ;)

\*\*\* 0847 unfortunately time is by now almost an hour off (0757).

martbhell@ubuntu:/var/www$ sudo /etc/init.d/ntp status \* NTP server is running

martbhell@ubuntu:/var/log$ ntpq --peers remote           refid      st t when poll reach   delay   offset  jitter ============================================================================== europium.canoni 193.79.237.14    2 u   12   64  377   44.012  2995645 13778.9

but supposedly this only runs once a day?

there is a program called ntp under /etc/cron.daily/

i'll wait until today afternoon

\*\* 2045  - it is now over an hour late.. \*\* rebooted, now time is 2215.. 23 minutes too much! \*\* rebooted again, now time is good, 2054. :s

\*\* a day later (maybe more)- and now it's 3 hours behind.

[supposedly](http://serverfault.com/questions/220836/why-is-ntpd-not-updating-the-time-on-my-server "why ntpd doesn't update") ntpd will catch the drift after a while.

stopped VM and made a copy of hostname.vmx

then edited this with pspad and and changed

tools.syncTime = "FALSE"

to

tools.syncTime = "TRUE"

now time is good (Tue Feb  8 15:12:34 EET 2011), is that because of the reboot? Probably. That's how it looks in syslog anyway.

Checking back in a day or two.

\*\*\* Wed Feb  9 06:45:09 EET 2011 - now 45minutes late.

\*\*\* Set up a script that monitors the offset. Looks like this:

offset = 3287.419925,;Tue Feb 15 04:30:01 EET 2011; offset = 3634.005591,;Tue Feb 15 06:30:01 EET 2011; offset = 3980.517817,;Tue Feb 15 08:30:01 EET 2011;

347,346,374

From /etc/ntp.conf I found that the drift file is this:

/var/lib/ntp/ntp.drift

it contains this value: 0.000

Manually changing this to -346.500

Also changed the default values to this in /etc/ntp.conf

restrict -4 default kod notrap nomodify restrict -6 default kod notrap nomodify

#restrict 127.0.0.1 #restrict ::1

and rebooting the server, again.

bbl.

ok, this is bs.

sudo apt-get remove ntp

then running this:

sudo ntpdate 0.fi.pool.ntp.org

confirmed it updates time

44 \* \* \* \* /usr/sbin/ntpdate 0.fi.pool.ntp.org >> /home/user/tid/tid.log

bbl

ok, looked one hour later at 1445 and the time was right. can now keep an eye on that tid.log file instead :)

don't forget to add that to the root user crontab, with 'sudo crontab -e'

\*\*\* a week later

ok that was an ugly fix and I do not condone doing that, that was me being a little frustrated :)

See [http://www.guldmyr.com/blog/time-sync-for-linux-vms-in-vmware-workstation/](http://www.guldmyr.com/blog/time-sync-for-linux-vms-in-vmware-workstation/ "ntpd sync") for how it worked out..

## lamp

[Download 1.x](http://ubuntuforums.org/showthread.php?t=1116511 "eyeos1 download")

install LAMP -> **sudo apt-get install lamp-server^** The ^ needs to be there! All you need to do is to insert a mysql root password.

After this you can surf into http://localhost or http://ip of the VM.

### phpymadmin

I also want to put in phpmyadmin (sudo apt-get install phpmyadmin) as well, this is nice tool to manage the mysql db. In that installation, choose apache2 by pressing space, then tab to get to the OK button. Then it asks about dbconfig-common, I chose no here because the db(mysql) is already installed. Then surf to http://ip/phpmyadmin/ and log on. If you see any databases there already -> you are now connected to the mysql you created before! Woop!

## EyeOS Install

cd - this gets you to your homedir mkdir eyeos cd eyeos wget $URL of eyeOS install unzip -> sudo apt-get install unzip unzip $FILENAME put this in your web dir. by default this is /var/www by default you do not have permission to put files there, so use sudo to put the eyeOS folder in there.

sudo mv eyeOS /var/www after this the user you have logged on with have ownership inside /var/www/eyeOS - means you don't have to write sudo all the time :)

point your web browser to http://ip/eyeOS (note that it is case sensitive) it will tell you that you need to chmod 777 some files, do that.

Then it will tell you to install these packages: SQLite and IMAP if you want mail client.

sudo apt-get install php5-sqlite (restart apache with 'sudo apachectl restart' and hit F5 on the installation page to see that the installation script now finds it) sudo apt-get install php5-imap (free-styled that, worked out well ;)

put in a password and then hit install

then it's installed!

## eyeOS - nice!

It's a lot slimmer than eyeOS 2.x and stuff appears to be working just off the bat. Everything runs so fast too, in comparison to 2.x.

**1.9.x for the win!**

Do I really want to use this? Would I find it useful? Honestly I am a little scared by running this on my own pc.
