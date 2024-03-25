---
title: BANAS - Brocade Accredited Network Advisor Specialist
date: 2014-02-27
category: it
tags: bna, brocade, certification, network, advisor, studying
<!-- prettier-ignore -->
---

Finally got around to start preparing the last certificate/accreditation -
[BANAS](http://www.brocade.com/education/certification-accreditation/accredited-network-advisor-specialist/curriculum.page)
to complete the Brocade Data Center Track (ok, not last. There are plenty more!).

It looks like it's an accreditation showing that the taker can do some basic
tasks in Brocade Network Advisor (BNA). This used to be a certification, so it's
probably a bit harder than it might seem!

Please note, this post is not meant to be a replacement for the official Brocade
studying recommendation, just my notes on how I'm practicing for it.

## **Methods:**

- Learn about the different features of BNA.
- Install BNA 12.1.4 in a VM - the "SAN Professional" version is free and there
  is a
  [try-out version available too](http://www.brocade.com/services-support/drivers-downloads/software-evaluations/index.page).
- Use it with some switches attached.
- Check out the "BNA 101 - Introduction to BNA" course on Brocade's training
  page. There is
  also [BNA 200-WBT Brocade Network Advisor Training](http://www.brocade.com/downloads/documents/course_data_sheets/BNA200-WBT-DataSheet.pdf)
  but I'm gonna try to do it without that.
- Until May 15 2014 there is also
  this: [http://community.brocade.com/t5/Certification/Free-Training-Through-May-15th-on-Brocade-Network-Advisor/ta-p/56511](http://community.brocade.com/t5/Certification/Free-Training-Through-May-15th-on-Brocade-Network-Advisor/ta-p/56511)
  free training!
- Learn about the different licensing options and versions of the software.
  [FAQ](http://www.brocade.com/downloads/documents/faqs/brocade-network-advisor-faq.pdf)
  is useful.
- Watch youtube videos of BNA
- Good documents
  - BNA
    FAQ <http://www.brocade.com/downloads/documents/faqs/brocade-network-advisor-faq.pdf>
  - Brocade Network Advisor SAN + IP User Manual
  - Brocade Network Advisor Installation and Migration Guide

### Install in a VM

Not much can be tested without any switches, but installing it a few times is
probably helpful. Also getting acquainted with the UI and some things can still
be done in the UI like:

- Set UI options
- Set up a firmware repository (at least import firmwares, release notes and md5
  checksums)
- Retrieve a SupportSave

Either register on Brocade's site and get the download that way. Or get it via
HP's public page - for example
[here](http://www8.hp.com/us/en/products/storage-software/product-detail.html?oid=3832744#!tab=features).
Click on Download. Because I'm lazy I'm installing it in a Windows 7 x64 VM 2
cores and 4GB RAM is much faster than 2GB. For just installing it you'll need
3-4GB disk space. Find install.exe within na1214_hp_windows.zip

The default user/password is: Administrator/password The user/password you set
during installation is for the database.

FTP/SCP/SFTP, syslog, snmp, https. Uses a postgreSQL database.

On the http/https page there are MIBs and the BNA client.
