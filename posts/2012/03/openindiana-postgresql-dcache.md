---
title: "OpenIndiana + PostgreSQL + dCache"
date: "2012-03-01"
categories: 
  - "it"
  - "storage"
tags: 
  - "dcache"
  - "esx"
  - "esxi"
  - "grid"
  - "openindiana"
  - "postgres"
  - "postgresql"
  - "vmware"
  - "vmware-workstation"
---

## This is a test for installing openindiana and set up a working dCache test-vm.

dCache is a storage element of the Grid (scientific computing).

OI == OpenIndiana. Kind of like opensolaris with an Illumos kernel, not the sun/oracle kernel.

With [http://www.guldmyr.com/blog/esxi-vmware-workstation/](http://www.guldmyr.com/blog/esxi-vmware-workstation/ "http://www.guldmyr.com/blog/esxi-vmware-workstation/") as a base for how to set up ip settings etc in OI.

[oi-dev-151a-text-x86.iso](http://openindiana.org/ "get it from openindiana.org") installed

pkg install package/pkg

pkg update

java -version

mkdir /var/postgres

useradd postgres

groupadd postgres

chown postgres:postgres /var/postgres

chmod 755 /var/postgres

The pkg update makes it into 151a2

If you do not create the ones above the install of service/postgres will fail and create a new BE.

pkg install pkg:/database/postgres-84
pkg install pkg:/service/database/postgres-84

vi /etc/passwd

change postgres to 90:90 and homedir to /export/home/postgres

mkdir /export/home/postgres

chown postgres.postgres /export/home/postgres
root@oi:~# vi /export/home/postgres/.profile
PATH=/usr/postgres/8.4/bin:${PATH}
PGDATA=/var/postgres/8.4/data
export PATH PGDATA

you probably also want to add these to the root user's path

svcadm enable postgresql-84:32\_bit

root@oi:/var/log# svcs -a|grep postg
disabled       17:29:37 svc:/application/database/postgresql\_84:default\_64bit
online         17:31:35 svc:/application/database/postgresql\_84:default\_32bit

su - postgres

psql

\\l

I initially did this in an ESXi VM in VMWare Workstation, but that keept freezing so I went over to a 'real vm' instead. The VM is more responsive.

### dCache stuff

wget it from [www.dcache.org](http://www.dcache.org "http://www.dcache.org")

pkgadd -d dcache-server-1.9.12-16.pkg

follow [http://www.dcache.org/manuals/Book-1.9.12/start/in-install.shtml](http://www.dcache.org/manuals/Book-1.9.12/start/in-install.shtml "http://www.dcache.org/manuals/Book-1.9.12/start/in-install.shtml") for the instructions of which postgresql-scripts and users and stuff to create

It's however not enough :

root@oi:~# /opt/d-cache/bin/dcache start
/opt/d-cache/bin/dcache\[127\]: local: not found \[No such file or directory\]
/opt/d-cache/bin/dcache\[128\]: local: not found \[No such file or directory\]
/opt/d-cache/bin/dcache\[129\]: local: not found \[No such file or directory\]
/opt/d-cache/bin/dcache\[130\]: local: not found \[No such file or directory\]
/opt/d-cache/bin/dcache\[131\]: local: not found \[No such file or directory\]
/opt/d-cache/bin/dcache\[132\]: local: not found \[No such file or directory\]
/opt/d-cache/bin/dcache\[317\]: .\[162\]: local: not found \[No such file or directory\]

so, edit /opt/d-cache/bin/dcache and remove the if in the beginning that will make it use /usr/xpg4/bin/sh - so that it uses /bin/bash instead.

Like this:

if \[ "$1" = "%" \]; then
    shift
elif \[ "\`uname\`" = "SunOS" \]; then
    if \[ -x /bin/bash \]; then
        exec /bin/bash $0 % "$@"
    else
        echo "Cannot find POSIX compliant shell. This script will"
        echo "probably break, but we attempt to execute it anyway."
    fi
fi

after I changed this, I noticed in the console that it said:

rpcbind: non-local attempt to set

bad?

anyway, then start dCache

root@oi:/opt/d-cache/bin# /opt/d-cache/bin/dcache start
Starting dCacheDomain done

in /var/log/dCacheDomain.log you'll find why it's not working:

touch /etc/exports

and it appears to be stable, except for some errors about (NFSv3-oi), however, we disregard those for now, we just want to get it running!

vi /opt/d-cache/etc/dcache.conf
dcache.layout=single
mkdir /pool1

and

vi /opt/d-cache/etc/layouts/single.conf

uncomment the pool1 section, set a maxDiskSize=2G to specify max disk space allowed. Specifics are in the installation part on dcache.org in the book.

Then point your webbrowser to - see any blue buttons?! **yay, it's up!**

Next step is to try it out, this might prove a little bit more difficult (to find dcap/root/srm client for opensolaris/oi).

### PostgreSQL problem

so maybe next time you restart the vm it gives some errors and puts the postgresql-server in maintenance mode. Look in /var/adm/messages for some tips, it should point you to

svcs -xv svc:/application/database/postgresql\_84:default\_32bit

/var/svc/log/application-database-postgresql\_84\\:default\_32bit.log

which will tell you more about what's going on and how to fix it

svcadm restart svcadm clear

## Use dCache with webdav

We'll start with trying to use Webdav (doesn't require anything fancy on the client side, except maybe a browser plugin for uploading).

go to the layout file and uncomment the webdav part, add

webdavAnonymousAccess=FULL
webdavRootPath=/data/world-writable

The script /opt/d-cache/bin/chimera-cli.sh sadly assumes that you need bash or a special version of bash somehow. So running

bash /opt/d-cache/bin/chimera-cli.sh mkdir /data

works, but

/opt/d-cache/bin/chimera-cli.sh mkdir /data

does not.

See http://www.dcache.org/manuals/Book-1.9.12/start/intouch-client.shtml for the rest.

If you keep the webdav in the same domain you'll need to restart the whole dcache.

In Windows 7 you can then mount a new network folder and click "Connect to a web site that you can use to store your documents and pictures" and in there type:

Now you get another folder in your computer where you can create folders. These will also show up if you surf to , sadly however, you cannot write files. [gridpp.ac.uk](https://www.gridpp.ac.uk/wiki/DCache_Log_Message_Archive#Pool_too_high) says it's because pool is full. But it's 2048MiB and all free?

https://twiki.grid.iu.edu/bin/view/Storage/MeetingMinutes2009Sep02

suggests minimum pool size might be 4G, changed pool maxdiskspace to 8G.

tada, now the copy starts, or the file creation starts, but I cannot actually write anything to it. So if I create a .txt file, I can give it a name and save it, unless I try to write anything inside it!

some errors to accompany this:

 (WebDAV-oi) \[door:WebDAV-oi@dCacheDomain:13295xxx\] Your resource factory returned a resource with a different name to that requested!!! Requested: null returned: world-writable - resource factory: class org.dcache.webdav.DcacheResourceFactory
 (WebDAV-oi) \[door:WebDAV-oi@dCacheDomain:13295xxx\] resource is being locked with a null user. This won't really be locked at all...
 (WebDAV-oi) \[door:WebDAV-oi@dCacheDomain:13295xxx\] resource is being locked with a null user. This won't really be locked at all...
 (WebDAV-oi) \[door:WebDAV-oi@dCacheDomain:13295xxx\] Your resource factory returned a resource with a different name to that requested!!! Requested: null returned: world-writable - resource factory: class org.dcache.webdav.DcacheResourceFactory
 (pool1) \[00002CBCC971ABC14BDC9E496A0AEAA31FC3\] A task was added to queue 'store', however the queue is not configured to execute any tasks.

### trying dccp

```
[root] #
```

### NFSv41

uncomment the nfsv3 and add nfsv41 then on a system you should be able to 'apt-get install nfs-common'; modprobe nfs; mkdir /nfsv4 mount -t nfs4 ip.to.server:/ /nfsv4'. But for me this stops working with an "cp: closing \`./bash': Input/output error". Possibly because I could not specify -o minorversion=1 on this ubuntu install (3.0.0-16).

 

#### NFSv41 with dCacheToGo

Download dCache2Go from here:

To convert it into VMware format:

VBoxManage clonehd source.vdi target.vmdk --format VMDK

Then create new vm and set the new vmdk file as the disk.

When this VM is up (and the dCache server of course), hit:

mount -t nfs4 -o minorversion ip.to.dcache.host:/ /mnt

then

cd /mnt/data/world-writable
mkdir another
cd another
cp /bin/bash .
cp bash /tmp/bash
diff /tmp/bash /bin/bash

## SCORE! We have a working dCache setup in a VM running openindiana!
