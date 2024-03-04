---
title: Storage FC HBA Transfer Size Tuning
date: 2012-03-06
category: storage
tags: bcu, brocade, emulex, fc, fibre, channel, hba, limtransfersize, performance, performance, tuning, qlfc, qlogic, san, storage, network, transfer, size, tuning
<!-- prettier-ignore -->
---

HP just published an advisory describing how to tune some parameters for Emulex, Qlogic and Brocade Fibre Channel HBAs: [c02518189](http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02518189). It sounds like these are new, but these changes have been around for at least 6 months in all three vendors' HBAs.

## **Emulex**

"Emulex driver version 2.42.002 or later, along with OneCommand Manager version 5.1.53.2 or later,"

Use HBAnywhere to change these.

Examples to tune the server or port level transfer size:

- 128 kbytes, set the LimTransferSize = 2 and ExtTransferSize = 0 (default)
- 512 kbytes, set the LimTransferSize = 0 (default) and ExtTransferSize = 0 (default)
- 1 Mbytes, set the LimTransferSize = 0 (default) and ExtTransferSize = 1

## Qlogic

This is part of the Qlogic SANSurfer utility.

- c:\\>qlfc -tsize /fc
- c:\\>qlfc -tsize /fc /set 128
- c:\\>qlfc -tsize /fc /set default

## Brocade

- bcu drvconf --key bfa\_max\_xfer\_len --val 64
- bcu drvconf --key bfa\_max\_xfer\_len --val 128
