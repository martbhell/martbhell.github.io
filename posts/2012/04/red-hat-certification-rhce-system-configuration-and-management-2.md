---
title: Red Hat Certification – RHCE – System Configuration and Management
date: 2012-04-30
category: it
tags: certification, linux, red, hat, rhce, studying

# RHCE Preparation - System Configuration and Management

This is post 1 in a series of posts where I will be going through the objectives for the RHCE certifications. It builds on the initial post that has the objectives:

http://www.guldmyr.com/red-hat-certification-rhce-preparation/

_It appears that the objectives have been updated, at least if you compare between my post above and https://www.redhat.com/training/courses/ex300/examobjective_

_for example build a simple rpm is installs one package is not in the list._

I bet there are [many blogs](http://b.joaoubaldo.com/?page_id=623 "for example") about this topic. I'm doing this quite a lot for myself, but maybe somebody else finds these useful.

This post will be about the section 'System Configuration and Management'.

My setup: Core i7, 8GB RAM, Windows 7 x64, VMWare Workstation with CentOS installed.

Installing a fresh VM with 4 cores, 5GB RAM, virtualization and CentOS.

CentOS is a free clone of Red Hat, it's missing some stuff (satellite for example) but it does the job for learning. You can find it in many places, for example here: http://www.nic.funet.fi/pub/Linux/INSTALL/Centos/6/isos/x86\_64/

## IP Routing and NAT

The part "Routing / NAT" will be tricky, as I do not have a second computer that I could use for this. Maybe I can get something working inside the virtual machines though, but for now I think I will skip these two and get straight into the other ones.

 

## Use /proc/sys and sysctl to modify and set kernel runtime parameters.

 

Edit /etc/sysctl.conf

Or use sysctl -w to set it temporary

For example one is: vm.overcommit\_ratio

You can then do either of these to view the current setting:

cat /proc/sys/vm/overcommit\_ratio
sysctl vm.overcommit\_ratio

To set it temporarily:

echo "60" > /proc/sys/vm/overcommit\_ratio
sysctl -w vm.overcommit\_ratio="50"

To set each time on boot:

echo "vm.overcommit\_ratio = 50" >> /etc/sysctl.conf

##  Configure a system to authenticate using Kerberos.

Waiting with this. Need to set up a KDC - kerberos service first.

 

## Build a simple RPM that packages a single file.

This appears to be a bit complicated - the details below are about as simple as this can be made. There is a lot more nifty things that you can do with an rpm.

Would be nice to have a guide of this in for example /usr/share/doc

yum install rpm-build
cd $HOME/rpmbuild
mkdir {BUILD,RPMS,SOURCES,SPECS,SRPMS}
mkdir GetIP
cd GetIP

The "program":

cat getip.sh
#!/bin/bash

wget -q https://guldmyr.com/ip.php -O/tmp/ip
cat /tmp/ip

chmod +x getip.sh

Make an archive and put it in the SOURCES DIR:

cd $HOME/rpmbuild
tar -cf GetIP.tar.gz GetIP
mv GetIP.tar.gz SOURCES/

Edit a spec-file (**do this as a normal user instead of root, it will show the default entries**):

cd SPECS
vi sample.spec

Make it look like this:

Name:GetIP
Version:1.0
Release:        1%{?dist}
Summary: Get an IP wooop

Group:  Development/Tools
License:        GPL
URL:            https://guldmyr.com
Source0:        %{name}.tar.gz
BuildRoot:      %(mktemp -ud %{\_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:bash
Requires:bash

%description
Get an IP woop!

%prep
%setup -n GetIP

%build

%install
mkdir -p "$RPM\_BUILD\_ROOT/opt/GetIP"
cp -R \* "$RPM\_BUILD\_ROOT/opt/GetIP"

%clean
rm -rf "$RPM\_BUILD\_ROOT"

%files
/opt/GetIP
%defattr(-,root,root,-)
%doc

%changelog

Then make an rpm:

rpmbuild -v -bb $HOME/rpmbuild/SPECS/sample.spec

Then as root:

cd /home/user/rpmbuild/RPMS/x86\_64/
rpm -ivh GetIP-1.0-1.el6.x86\_64.rpm

Then as normal user you can now execute the installed file:

/opt/getip/getip.sh

If you wonder about things - check this fairly unreadable blog post out.

Basically you want to use the $RPM\_BUILD\_ROOT in front of where you want to install the software. By default there are 'make', 'configure' and nothing in the 'require' entries. I removed the make, configured and just put 'bash' in the require entries, it seemed to do the trick though.

More info is also available on [rpm.org](http://www.rpm.org/max-rpm/ch-rpm-build.html "rpm.org - directories") - which recommend to use /usr/src/redhat for building packages.

## Configure a system as an iSCSI initiator that persistently mounts an iSCSI target.

Waiting with this. Need to set up an iSCSI target first.

## Produce and deliver reports on system utilization (processor, memory, disk, and network).

sar -A

/etc/cron.d/sysstat

## Use shell scripting to automate system maintenance tasks.

Well, this can be a lot of things and is quite hard to prepare for.

But I think a 'for loop' is a good thing to know about and can help with a lot of system maintenance tasks.

an input file with usernames:

\[martbhell@rhce ~\]$ cat /tmp/userlist
bengt
goran

a scriptfile:

\[root@rhce ~\]# cat usersndirs.sh
#!/bin/sh

userlist=/tmp/userlist

for i in \`cat $userlist\`; do
echo useradd $i;
echo mkdir $i;
done

Remove the "echo" to create the users.

Of course, you could also use the 'newuser' command (interactive or send a file).

This happens a lot I think: You get an idea that "hey, I can do this with a script". But then a random amount of time later you find out that there is already a command that does this for you. That doesn't mean the time spent is a total waste, hopefully you learned something while doing it. Maybe your script even does a better job than the new one you found.

## Configure a system to log to a remote system.

syslog / rsyslog

man rsyslog.conf has an example for how to log to a remote machine

edit /etc/rsyslog.conf

add

       To  forward  messages  to another host via UDP, prepend the hostname with the at sign ("@").  To forward it via plain tcp, prepend two at
       signs ("@@"). To forward via RELP, prepend the string ":omrelp:" in front of the hostname.

       Example:
              \*.\* @@192.168.0.8

Set the IP to the machine that will be receiving the logs.

## Configure a system to accept logging from a remote system.

So this step you may want to do before the previous step (unless you already have a working syslogd server).

You edit /etc/rsyslog.conf

and uncomment the "reception" parts (don't forget firewall and restart service).

To test try to "su -" with the wrong password and then check in /var/log/secure on the loghost.

## Create a private repository

"To create a private repository you should proceed as follows: - Install the createrepo software package - Create a <directory> where files can be shared (via FTP or HTTP) - Create a subdirectory called Packages and copy all packages to be published in Packages - run createrepo -v <directory>"
