---
title: SAN Primer - Introduction to Data Storage
date: 2011-07-28
category: storage
tags: data, storage, introduction, iscsi, san, san, basics, storage, storage, network
<!-- prettier-ignore -->
---

You may have heard about this storage or SAN stuff, but what is it? Is it complicated and cool? Yes. Now it doesn't have
to be complicated, but it sure can be sometimes. This post is just a brief primer/introduction to storage and what it
entails. In case maybe you got a job interview or just would like to know a little bit more about it.

I'll update this post as I go, **last update 2012-07-13 -** added some books and free pdfs and links.

**What is a SAN?** ‘Storage Area Network’ - or storage network. Generally it doesn’t have to be a ‘network’ it could
just be direct connected equipment or peer 2 peer. But what it always entails is a shared storage, most often disk or
tape.

**What is in a SAN?** When it comes to disk storage on fibre channel there’s a few standard components: FC HBA in the
server, SFP and cables, SAN-switch, SFP and cables, FC port in the disk array controller and then there’s something
behind the controller that connects disks.

You can connect the FC HBA directly to the disk array.

**What is storage?** It's somewhere where you can store data. Most common today would be: hard drives, flash drives
(ssd), magnetic media (tape) and optical media (dvd/blueray/cd).  In a computer you cannot fit hundred of hard drives,
but sometimes there is an application that requires lots and lots of data (maybe for example CAD drawings, video
editing). This is when a SAN comes in, with only the help of for example a fibre channel card you can give a server
access to lots of storage.

**How do you do it?** If you want to give a server disk space from a fibre channel SAN this is what you do:

1. Fullfil the hardware requirements (so fibre channel HBA+drivers and multipath software, SAN-switch, disk array and
   sfps + cables)
2. On the SAN-switch create a zone with the disk array's and the FC HBA's domain id, port id or port wwn. It's possible
   to do it without zones, but they are good for fault isolation.
3. On the disk array you should now see the server/host, create a disk and map/present it to the host.
4. On the host you most likely need to do a rescan/reinitialize of the fc-bus.
5. After the server sees the LUN it will have a new hard disk available, you can use your normal
   partitioning/format/filesystem tools to create some usable space.

**Can I use the same disk on two servers?** This is a pretty common question, the answer is sometimes and the sometimes
depends on which file system you are using. It needs to support that more than one host can access it at the same time.
NTFS does not support this and if you try it anyway you'll corrupt the file system. For Windows you need to look into
CSV - clustered shared volumes or other networked file systems like NFS/CIFS.

**What is the difference between fibre channel and iscsi?**

FC is sending SCSI commands over fibre channel, it’s not always fibre or optical cables. While iSCSI is sending SCSI
commands over TCP/IP. FC is a whole network technology while iSCSI is running on top of a network technology -> TCP/IP.

**Some literature:**

Both the IBM and the HP one are quite lengthy. The HP one has a lot of HP specific guides, best practices and supported
configurations. The FC 101 by Brocade actually goes quite deep into the theory of the FC protocol.

- IBM's
  "[Introduction to Storage Area Networks and System Networking](http://www.redbooks.ibm.com/redpieces/abstracts/sg245470.html)"
  :
- Brocade’s
  [FC 101 – Introduction to Fibre Channel Concepts](http://www.brocade.com/downloads/documents/course_data_sheets/FC101-DataSheet.pdf).
  - This is really good because it takes you through the theory. There is also a page where  more books are mentioned.
- HPs
  [SAN Design Reference Guide](http://h20000.www2.hp.com/bizsupport/TechSupport/DocumentIndex.jsp?contentType=SupportManual&docIndexId=179911&locale=en_US&prodSeriesId=406734&prodTypeId=12169&taskId=101)
  - A pdf that goes through best practices for how to configure HP’s storage and san.
- [Evolution - Storage Brain -](http://www.amazon.com/Evolution-Storage-Brain-transformative-storage/dp/1451577648/)
  - Used to be used to train NetApp's new storage people:
