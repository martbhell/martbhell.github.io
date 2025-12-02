---
title: HP's Brocade firmwares compatible with other switches?
date: 2011-05-15
category: it, storage
tags: brocade, examdiff, firmware, gpl, hds, hp, ibm, san, san, switches, storage
<!-- prettier-ignore -->
---

After a [question](https://www.guldmyr.com/brocade-san-switch-firmware-upgrades/#comment-524 "link to question") in my
[SAN switch firmware upgrade article](https://www.guldmyr.com/brocade-san-switch-firmware-upgrades/) I made a comparison
of two downloads of 6.3.1b (one via IBM and one from HP) - the only differences were a file called ancillary and one
called EULA.pdf. I used [examdiff](http://www.prestosoft.com/edp_examdiff.asp "examdiff") to find the differences.

All the sub-directories were the same, only the above two files were added in the HP one. I believe quite strongly that
you can use the HP firmwares to upgrade Brocade switches that are branded by other vendors.

At least [IBM](<http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003220> "Link to "IBM" and Brocade Firmwares") and
normal Brocade ones.

As they are using the very same Brocade firmware that Brocade themself use, it might be hard for the vendors to change
the switch that much.

**It would be interesting to investigate if other vendors add something to make theirs not, but I have no way of
acquiring such a firmware.**

The EULA looks like a normal HP standard end user license agreement form. The HP ancillary.txt file contains this:

```text
"This ancillary.txt file provides information as to how to obtain the open source or other third party licenses in this distribution. To obtain such licenses, run the following CLI command at the prompt, "opensource"
```

vs

```text
This ancillary.txt file also provides the instructions for customers who require a copy of the machine-readable GPL Source Code by written request.  Upon your written request, HP will provide to You, for a fee covering the cost of distribution, a complete machine-readable copy of the GPL Source Code. Your written request for GPL Source Code can be sent via email to FC_Infrastructure_OpenSourceRequest@hp.com. In the request, include product name, version number, your name, and your shipping address. "
```
