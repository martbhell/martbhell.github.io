---
title: EyeOS - Cloud Desktop in your browser
date: 2011-02-03
category: it
tags: activemq, apt, get, cloud, eyeos, icloud, kaazing, pico, ubuntu, virtual, desktop, vmware, workstation

Useful? Hopefully! Interesting? Very!

Download on eyeos.org //update 2011-12-20 : turns out there's been some changes here. 2.5 is the one now and it's found under open-source. There's also professional or other editions.

## Installation

The installation manual can be found in the above link as well - will I try to use it first? No :)  What is the fun in that ;)

### 1st attempt

sudo apt-get -d install eyeos - this did not work, no such package.

### 2nd attempt

\- downloading the .tar.gz - surfed to the sourceforge. There is a 2.x and a 1.x of eyeOS - link above goes to 2.x

Commands: wget/mv (super long file) then

`tar -zxvf` (no errors). This extracts the whole archive into the directory you are, so probably best to put the archive in a new and empty directory before doing this.

Files are index.php, settings.php (maybe the installation is done by just surfing into it?). There are some sub directories too: resource, eyeos, install. The install dir also has index.php

cp -R files/ /var/www cd /var/www mv files/ eyeos cd eyes chmod 777 \*

surfing to 192.168.232.128/eyeos ->

> EyeErrorException: fopen(./system/conf/libs/log4php/logs/eyeos\_20110131.log): failed to open stream: Permission denied

\-> a lot nicer, gives a welcome to eyeOS 2 installation!

You then get to click on "install" and it will check the requirements.

I did not have these (working php, mysql and apache already installed, quite clean ubuntu 10.10 installation in a VMWare Workstation):

### Sorting out the pre-requirements

if you don't know what to run you can either google or check out [packages.ubuntu.com](http://packages.ubuntu.com "packages ubuntu")

#### curl

`sudo apt-get install php5-curl`

> The following NEW packages will be installed: libcurl3 php5-curl

```bash
Failed to fetch <http://us.archive.ubuntu.com/ubuntu/pool/main/p/php5/php5-curl\_5.3.3-1ubuntu9.1\_amd64.deb>  404  Not Found \[IP: 91.189.92.171 80\] E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
sudo apt-get update
```

then trying again, working a lot better ;)

install looked a bit weird, or it went very fast.

anyway, did a `sudo apachectrl restart` and then curl was OK in the installation (it didn't install any of the others by chance though :/)

#### sqlite extensions and  PDO sqlite driver

php5-sqlite - this package should do the trick new packages: libsqlite0 php5-sqlite searched for sqlite pdo on packages and it didn't find anything so starting with the above one and it installed both, restarted apache and now it's a lot greener :)

#### python

Python simplejson:    Not installed (Needed in collaborative features) - **python-simplejson**

new packages: libjs-jquery python-simplejson

installed without a hitch - comes up as installed

Python uno:    Not installed (Needed to convert office documents) - **python-uno** - takes up 255 MB - skipping it for now.

Python stomp.py:    Not installed (Needed in collaborative features) - package name: **python-stompy** (I am unsure about this one, it looks old and on packages it doesn't say hardy).

> The following NEW packages will be installed: python-dingus python-nose python-pkg-resources python-stompy

after a restart of apache and refresh -> doesn't come up as installed. But I really want this so googling.

<http://stomppy.googlecode.com/files/stomp.py\_3.0.2\_all.deb> found on <http://code.google.com/p/stomppy/>

wget that. then `sudo dpkg -i stomp.py_3.0.2_all.deb`

now it's green in eyeOS pre-req check! Check!

#### php.ini display errors is enabled (eyeos recommends disabled)

keeping this as it is for now

#### recoll:    Not Instaled (Needed for document indexation)

package name: recoll

`sudo apt-get install recoll`

> The following NEW packages will be installed: aspell aspell-en fontconfig libaspell15 libaudio2 libice6 liblcms1 libmng1 libqt4-dbus libqt4-designer libqt4-network libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-mysql libqt4-xml libqtcore4 libqtgui4 libsm6 libtiff4 libxt6 recoll x11-common

worked fine, no need to restart apache and it showed up as installed

#### exiftool:    Not Instaled (Needed to extract MP3 metadata)

found this package: libimage-exiftool-perl

same story: `sudo apt-get install libimage-exiftool-perl`

worked like a charm :)

#### OpenOffice Daemon:    Not running (Needed to convert office documents)

skipping this for now

#### Kaazing gateway:    Not running (Needed for real time notifications)

no hits in ubuntu packages

googled and found this:

```bash
sudo wget into /usr/share/kaazing
sudo tar -zxvf
cd /usr/share/kaazing/kaazing-websocket-gateway-demos-2010.05.1.21/bin
./gateway.start
```

then script shows it as good!

#### ActiveMQ Daemon:    Not running (Needed for real time notifications)

no hits in ubuntu packages

google found this: <http://www.nic.funet.fi/pub/mirrors/apache.org//activemq/apache-activemq/5.4.2/apache-activemq-5.4.2-bin.tar.gz>

found in README - installation guide: [http://activemq.apache.org/version-5-getting-started.html](http://activemq.apache.org/version-5-getting-started.html "activemq getting started")

```bash
sudo wget into /usr/share/php5/apachemq
sudo tar -zxvf
cd /usr/share/php5/apachemq/apache-activemq-5.4.2/bin/activemq
./activemq # This did not work, complaining about JAVA.
```

> ERROR: Configuration varaiable JAVA\_HOME or JAVACMD is not defined correctly. (JAVA\_HOME='', JAVACMD='java')
> INFO: Invoke the following command to create a configuration file ./activemq setup \[ /etc/default/activemq | /home/user/.activemqrc \]

```bash
sudo ./activemq setup /etc/default/activemq
sudo chown root:nogroup '/etc/default/activemq'; sudo chmod 600 '/etc/default/activemq'
./activemq # then only complains about this:
```

> ERROR: Configuration varaiable JAVA\_HOME or JAVACMD is not defined correctly. (JAVA\_HOME='', JAVACMD='java')

`sudo pico /etc/default/activemq`

has this:

`JAVACMD="auto"`

and

> martbhell@ubuntu:/etc/default$ whereis java java: /usr/share/java

this directory is however quite empty, just a libintl.jar

searching for java - going for this package: sun-java6-jre did not work, not in the repository.. Found this [link](http://www.ubuntugeek.com/how-to-install-java-runtime-environment-jre-in-ubuntu-10-10-maverick-using-ppa.html "install JRE in Ubuntu server 10.10") which advises to run "sudo add-apt-repository ppa:sun-java-community-team/sun-java6" . This command lets me know that add-apt-respository does not exist

and cat /etc/issue gives me 10.10

`sudo apt-cache search java`

meh, ok, opening the installation guide..

didn't help much, more talk about repositories

Found this on [ubuntuforums](http://ubuntuforums.org/showthread.php?t=1662947 "install JRE in Ubuntu server 10.10")

went to /etc/apt/sources.list - searched for 'partner' and uncommented that line.

then `sudo apt-get update; sudo apt-get install sun-java6-jre`

> The following NEW packages will be installed: avahi-daemon consolekit dbus gsfonts gsfonts-x11 java-common libasound2 libavahi-common-data libavahi-common3 libavahi-core7 libck-connector0 libdaemon0 libeggdbus-1-0 libfontenc1 libltdl7 libnss-mdns libpam-ck-connector libpolkit-gobject-1-0 libpython2.6 libxfont1 libxi6 libxtst6 odbcinst odbcinst1debian2 sun-java6-bin sun-java6-jre unixodbc xfonts-encodings xfonts-utils

that's a lot. 115MB too.

but went pretty fast, trying to run activemq again changed the JAVACMD setting back to "auto" after it gave some kind of permission error

then `sudo ./activemq restart`

> martbhell@ubuntu:/usr/share/php5/apachemq/apache-activemq-5.4.2/bin$ sudo ./activemq status INFO: Loading '/etc/default/activemq' INFO: Using java '/usr/bin/java' ActiveMQ is running (pid '5995')

after that it comes up as green ;) adding this to boot as well now

#### autostart activemq and kaazing

add this to /etc/rc.local

`sudo /usr/share/php5/apachemq/apache-activemq-5.4.2/bin/activemq start & sudo /usr/share/kaazing/kaazing-websocket-gateway-demos-2010.05.1.21/bin/gateway.start &`

__note from future Johan haha that's a way to start things on boot too sure__ 

### Configuration during install

Clicked on the next, where it asks for mysql login information and eyeOS root password

this was already filled in so went with that :)

however, still gives this:

**EyeErrorException: fopen(./system/conf/libs/log4php/logs/eyeos\_20110131.log): failed to open stream: Permission denied**

/var/www/eyeos$ chmod 777 \* -R

## Logging in

Login prompt does not show up in FF4 B10 or Chrome. It does show up in IE8. But when I click on new user nothing happens. apachectrl restart trying with both root/martbhell account

After looking around in the mysql server I didn't see any new stuff. So: To fix it I had to create a db called whatever I filled out in the form ;)

Creating new user works too!

## Static IP in Ubuntu Server 10.10

Changed to static IP on the server by editing /etc/network/interfaces

to make it look like this :

```bash
auto eth0
iface eth0 inet static
    address 192.168.1.100
    netmask 255.255.255.0
    network 192.168.1.0
    broadcast 192.168.1.255
    gateway 192.168.1.1
```

Restart the neworking service using the following command

`sudo /etc/init.d/networking restart`

and changing to a bridged ethernet - then it's on my local LAN network :)

a restart also shows stuff is running (by going back to the installer)

## Summary

It's not really excellent. Documents didn't work (as in I cannot open them), but I suppose that is because I didn't install the OpenOffice stuff. But I just don't like the feel of it. It's not smooth enough. Maybe it's because the VM only has one CPU and 2GB RAM?

Well just looking at 'top' while clicking around and CPU idle goes down to 18-19% and then goes back to 100% after whatever I started in eyeOS is done.

Maybe I'll try to install the OO parts and see if that does the trick. I just got the feeling that this is probably something that iCloud can do better (at least the screenshots look nicer on their web page). There's quite a few other hits on 'webos' on the Intarweb and quite a lot of them aren't updated.. Like lucid, some kind of windows4all on sourceforge..

Looks nice, but maybe the web browser isn't ready to be the OS just yet?
