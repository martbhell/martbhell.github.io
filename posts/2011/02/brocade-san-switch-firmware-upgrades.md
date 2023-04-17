---
title: Brocade SAN Switch Firmware Upgrades
date: 2011-02-01
category: it, storage
tags: brocade, brocade, san, fabric, fabric, os, firmware, guide, hp, hp, support, ibm, san, san, switches, storage, switch, tutorial, update, upgrade

# Overview

[TOC]

This is my guide/template to upgrading Fabric OS (FOS) - Firmware - on the Brocade SAN Switches. If **you** have any additions, comments or questions please go ahead and comment or if you have any questions you can find my e-mail on [https://guldmyr.com](http://guldmyr.com "go to the cv"). The post has been updated over 188 times according to my WordPress revisions, first update in January 2011.

This article was originally built from my experience with HP branded Brocade SAN Switches - not with any other OEM or pure Brocade switches. I have however since beginning this document gotten experience with other vendors. I do not think others are different except for licenses and some default fabric.ops. I made a [comparison](../hps-brocade-firmwares-compatible-with-other-switches/ "comparison") of two downloads of the 6.3.1b Fabric OS Firmware (one via IBM and one from HP). You can find a link to the "IBM" firmware and release notes after 6.x in that article too. I found that they are very similar and the HP firmware works on the IBM switch and vice versa. Another example is that firmware gotten from HDS works on an HP branded Brocade switch.

When you see 7.2.x this means any version in the Fabric OS 7.2.x series. For upgrades, this would generally mean the latest available in that series (like 7.2.1g for 7.2.x or 8.0.2d for 8.0.x) unless of course there is a problem with the latest. Sign up for your vendor's security and update alerts to get notified about new releases.

Carefully plan the upgrade, it takes time but it is rewarding and worth it.

## Updates in this article:

<details><summary>Old Updates < 2013</summary>

- **2011-02-22:** Updated links because the release notes I had before to 6.1.x and above did not work anymore. Also changed the sub-versions in 6.1.x and above to the latest released one by HP.

- **2011-02-24:** Found link to [5.2.x and 6.0.x FOS](http://h20000.www2.hp.com/bizsupport/TechSupport/SoftwareDescription.jsp?lang=en&cc=us&prodTypeId=12169&prodSeriesId=3414314&prodNameId=3414317&swEnvOID=54&swLang=8&mode=2&taskId=135&swItem=co-86625-1 "FOS 6.0.x and 5.1.x") on HP.com with the help of an ITRC thread.
- **2011-04-21:** Added links for correlating Brocade Product name, model number and HP name. Latest in 6.4.x series is now 6.4.1b
- **2011-05-05:** Added link to Web Tools for 6.2.x with reference to how to upgrade Firmware via the web tools.
- **2011-05-15:** A note added about compatibility regarding the 'HP' firmware files and other vendors - as far as I can tell the ones downloaded from HP will work on other non-HP switches. Also posted a [new blog post](http://www.guldmyr.com/hps-brocade-firmwares-compatible-with-other-switches/ "works?") about that. Added [link](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003220 "IBM SAN b-type Firmware Version 6.x Release Notes") to IBM.com - for correlating product names and for getting (all Fabric OS) firmwares. EMC [also has Brocade products](http://www.brocade.com/partnerships/oems/index.page "on brocade.com").
- **2011-05-18:** Added a link to a post on [HP's support forum](http://h30499.www3.hp.com/t5/Storage-Area-Networks-SAN/Upgrade-of-EVA-4400-Switches/m-p/4788345 "on new HP's ITRC Forum") where the post helped a bit. Also made post a little easier, wrote a little about the release.plist confusion.
- **2011-05-24:** Added example to show that driver updates are important. Some more restructuring of the article.
- **2011-07-12:** Added FOS 7.0.0a
- **2011-07-14:** Added [link](http://h20566.www2.hp.com/portal/site/hpsc/public/psi/mostViewedResults/?d-8034386-p=&d-8034386-o=&sort=updatedDate&tableId=tableA&dir=desc&page=&d-8034386-s=&showSecondTableA=&action=tableAction&sp4ts.oid=3742051 "searching for HP SAN Switch b-series 8/80 advisories") to HP knowledge base and updated a link to an ITRC forum thread to point to the new forum.
- **2011-09-29:** Added FOS 7.0.0b and section about CF cards.
- **2011-10-19:** Wrote a bit about firmware upgrade order.
- **2011-10-24:** The HP links to 6.0.0c and 5.3.x seems to not work anymore. I could not find either of these for download on HP's website. The IBM one still has 6.0.0c (release notes anyway).
- **2011-12-05:** Went through all links to make sure they worked. Re-wrote some of the steps and re-ordered so that 'decide' is before 'prepare'. Added output from switch when doing the firmware upgrade via CLI.
- **2011-12-10:** Added table of contents via a plugin.
- **2012-01-02:** Added FOS 7.0.0c
- **2012-01-09:** Added EMC branded switches default pw
- **2012-02-14:** Added HP's [link](http://h20000.www2.hp.com/bizsupport/TechSupport/SoftwareIndex.jsp?lang=en&cc=us&prodNameId=315080&prodTypeId=12169&prodSeriesId=315078&swLang=8&taskId=135&swEnvOID=54 "on hp.com") to FOS 5.x. firmware.
- **2012-02-15:** Added [IBM's link](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003855 "on ibm.com") to FOS 7 info and downloads.
- **2012-02-21:** Some notes about which switches can do which firmware. Re-wrote a part of the upgrade order section.
- **2012-02-27:** Note about licenses.
- **2012-02-29:** Added note about 5.1.x to 5.3.x, made upgrade path clearer. Also made how to find 5.3.x and 6.x firmwares a little clearer for HP's page.
- **2012-03-01:** Added 6.2.2f and 7.0.1 and note about plist/ftp for 5.1.x
- **2012-04-03:** Addeed 6.3.2e
- **2012-04-24:** Added 7.0.1a
- **2012-04-27:** Rewrote some part of the upgrade section.
- **2012-06-07:** Added 6.4.3 and 7.0.1b
- **2012-06-14:** Added link to [Brocade FOS Target Path](http://www2.brocade.com/en/backend-content/pdf-page.html?/content/dam/common/documents/content-types/target-path-selection-guide/brocade-fos-target-path.pdf "on brocade.com") in decide section.
- **2012-10-27:** Some grammar updates and 16G FOS 7.x requirement. 6.4.3b and 7.0.2.
- **2012-11-05:** Updated links to release notes. Perhaps it's time to condense the updates list. Notes about passive/active ftp, ifmodeshow|ipaddrshow and java version required (listed in release notes).

</details>
<details><summary>Old Updates < 2020</summary>

- **2013-03-10:** 7.0.2b and 6.4.3c added some notes about compatibility. Improved list of which FOS works with which FC speeds.
- **2013-03-29:** Added 7.1.0a and 7.0.2c. Only HP is out with 7.1.0a as of now. Brocade may have it non-publicly, at least I cannot see it in [my brocade](http://my.brocade.com/ "http://my.brocade.com/"). Other minor updates.
- **2013-04-04:** Added link to 6.4.3d
- **2013-05-02:** Updated link to FOS Target Path.
- **2013-06-23:** Changed some ftp:// links to http://
- **2013-07-16:** Added link to IBM's [pdf](http://www.ibm.com/developerworks/aix/library/au-aix-san-switch-firmware/au-aix-san-switch-firmware-pdf.pdf "pdf") with pictures for firmware upgrade.
- **2013-08-03:** 6.4.3e by IBM - not available by HP yet. Disruptive upgrades are OK from 6.2 to 6.4.
- **2013-08-05:** Added 7.1.1, updated some links to release notes.
- **2013-10-03:** Made it a bit clearer regarding which is the earliest firmware you can upgrade from. Newer revisions of some Brocade release notes. 7.0.2d out and 6.4.3e link to hp.com
- **2013-11-14:** Removed comment that B300 does not support 6.4.x - it does! It should have been the 200E! Thanks Eugene :)
- **2014-02-01:** As of 2014-02-01 HP does not allow anybody without a valid support agreement to download firmwares. Release notes and at least some firmware links appears to still be working. Expect difficulty and broken links while hunting for firmwares. Fabric OS firmwares downloaded from IBM's site works on HP switches too, but there might be some differences (although I couldn't find any important ones when I compared 6.3.1b). So far it seems this restriction of access to firmwares only applies to HP servers.
- **2014-02-07:** Added new link to [HP's page for FOS 5.2 to 6.3](http://ftp.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer_Statement.htm "http://ftp.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer_Statement.htm")  Thanks Leo R!
- **2014-02-11:** Added 7.2.0b and 7.1.1c (HP have 7.1.1c release notes up but IBM does not - to find Brocade version go to IBM's download the firmware page that's on Brocade.com and get the release notes from there). Also 3 years anniversary on this post on 2014-02-01!
- **2014-02-17:** But be careful with 7.2.0b - IBM has a note on their [7.x page](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003855 "http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003855") about 7.2.0b saying: "_IBM recommends that customers not deploy FOS 7.2.0b if virtual switch capability is needed. Virtual switch users should migrate to an earlier version as soon as possible._"
- **2014-03-17:** The problem with 7.2.0b was likely DEFECT000491192 fixed in 7.2.0c and later also DEFECT000494570 was fixed in 7.2.0d. 7.2.0x seems a bit unstable at the moment. 7.2.1 is currently available for download via HP's pages but not via IBM/Brocade's. Also no release notes available. Archived 2013 updates.
- **2014-04-18:** Added 6.4.3f and 7.1.1c and 7.1.2 is out. Updated migration paths a bit. The Brocade release notes of 7.1.x actually have a decent list of the migration path needed now. See the section "Recommended Migration Paths to FOS v7.1.2".
- **2014-08-06:** 7.2.1a, 7.1.2a, 7.0.2e. Updated some links that had gone bad ([FOS Target Path](http://www2.brocade.com/en/backend-content/pdf-page.html?/content/dam/common/documents/content-types/target-path-selection-guide/brocade-fos-target-path.pdf)) and made the "Show/Hide" Updates work again.
- **2014-09-28:** 7.1.2b and 7.2.1b is out.
- **2014-10-01:**  7.3.0a is out but can't find any release notes for it.
- **2014-10-25:** 7.2.1c
- **2015-01-18:** 7.2.1d, 7.3.0c. "HP's" release notes are too hard to find.. Added a note about FileZilla being a good ftp server. Thanks Harry Redl!
- **2015-02-20:** 6.2.2g, 6.4.3g
- **2015-04-06:** 7.3.1a from HP
- **2015-04-21:** 7.3.1a from IBM
- **2015-06-19:** Note about FileZilla being hosted off sourceforge - installer might contain malware.
- **2015-07-07:** 7.4.0a, 7.3.1b, 7.2.1e. Removed link to HP's webkey license page. Doesn't work anymore. Note about BNA version required to manage Fabric OS v7.4 switches.
- **2015-08-31:** 6.4.3g and 7.3.1b new revision of release notes. 7.2.1f, 7.4.0b
- **2015-09-01:** 7.3.1c
- **2015-09-16:** New versions of release notes.
- **2015-10-25:** [7.4.1](ftp://public.dhe.ibm.com/storage/san/fos7/v7.4.1_ReleaseNotes_v1.0.pdf) is out for the brave and 6.4.3h (Fixes to OpenSSL CVE-2015-0286, CVE-2015-0288, CVE-2015-0289, CVE-2015-0292)
- **2015-12-05:** 7.2.1g and 7.3.1d. Updated some links. Need to go through a lot of the HP ones here to point to HPE..
- **2016-02-24:** 7.4.1b
- **2016-03-15:** 7.3.2
- **2016-05-17:** 7.4.1c
- **2016-08-13:** 7.3.2a, 7.4.1d
- **2016-12-19:** 7.3.2b, 7.4.1e
- **2017-03-10:** 8.x has been out for a while
- **2017-04-29:** new links to Brocade FOS target path and better links for where to fetch firmwares
- **2017-05-03:** 8.0.2b and added links to Upgrade Guides for [8.0](http://www.brocade.com/content/dam/common/documents/content-types/software-upgrade-guide/fos-800-upgradeguide.pdf).0 and [7.4](http://www.brocade.com/content/html/en/software-upgrade-guide/FOS_740_UPGRADE/).0)
- **2017-05-13:** [7.4.2](ftp://public.dhe.ibm.com/storage/san/fos7/v7.4.2_ReleaseNotes_v2.0.pdf)
- **2017-08-07:** [8.1.0c](http://public.dhe.ibm.com/storage/san/fos8/v8.1.0c_ReleaseNotes_v1.0.pdf)
- **2017-11-09:** [8.1.1a](ftp://public.dhe.ibm.com/storage/san/fos8/v8.1.1a_ReleaseNotes_v1.0.pdf)
- **2017-12-05:** [8.0.2c](ftp://public.dhe.ibm.com/storage/san/fos8/v8.0.2c_ReleaseNotes_v1.0.pdf)
- **2018-01-01:** [8.1.2a](ftp://public.dhe.ibm.com/storage/san/fos8/v8.1.2a_ReleaseNotes_v1.0.pdf) and [7.4.2b](http://:http://service.boulder.ibm.com/storage/san/fos7/v7.4.2b_ReleaseNotes_v1.0.pdf)
- **2018-02-08:** [7.4.2c](http://service.boulder.ibm.com/storage/san/fos7/v7.4.2c_ReleaseNotes_v1.0.pdf) and [8.0.2d](http://service.boulder.ibm.com/storage/san/fos8/v8.0.2d_ReleaseNotes_v1.0.pdf)
- **2018-06-15:** [8.2.0a](ftp://public.dhe.ibm.com/storage/san/fos8/v8.2.0a_ReleaseNotes_v1.0.pdf) and [8.1.2d](ftp://public.dhe.ibm.com/storage/san/fos8/v8.1.2d_ReleaseNotes_v1.0.pdf) and [8.0.2e](ftp://public.dhe.ibm.com/storage/san/fos8/v8.0.2e_ReleaseNotes_v1.0.pdf)
- **2018-10-11:** fixing some links, Brocade is now Broadcom so some links are not working anymore surprise. Some HP links no longer work so removed those too.
- **2018-12-07:** [7.4.2d](http://service.boulder.ibm.com/storage/san/fos8/v8.0.2f_ReleaseNotes_v2.0.pdf) and [8.0.2f](http://service.boulder.ibm.com/storage/san/fos8/v8.0.2f_ReleaseNotes_v2.0.pdf) and [8.1.2f](http://service.boulder.ibm.com/storage/san/fos8/v8.1.2f_ReleaseNotes_v2.0.pdf)
- **2019-04-18:** [FOS Target Path](https://docs.broadcom.com/docs/53-1003916) on Broadcom.  From a reader got a link to NetApp's [Brocadeassist portal](http://www.brocadeassist.com/public/NetAppRelease) where **newer firmware** can be found than on IBM's. Some more link updates and link to [8.2.1b](https://portal.broadcom.com/web/support/netapp?p_p_id=AssistPortal&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=directDownloadURL&p_p_cacheability=cacheLevelPage&_AssistPortal_mvcRenderCommandName=landingPageURL&downloadURL=/u002/extwebportal/ORACLE/INBOUND/DOCSAFE/TEMPDOWNLOADS/18140880443172713.pdf&filename=v8.2.1b_releasenotes_v1.0.pdf)
- **2019-04-19:** More link fixes.  FOS 6.x - 8.x firmwares can all be downloaded from the brocadeassist portal.
- **2019-04-20:** 8.1.2g and 8.2.1b on IBM release notes so updated links
- **2019-08-23:** 8.2.1c is on NetApp's link but there are no release notes - I'd pass
- **2019-11-21:** **all** links to firmware downloads don't work right now. Only one I have found is to HPE, but there you need support contract.
- **2020-05-10:** Also some new releases, 8.2.2 is out.
- **2020-09-27:** 9.0.0a got released in August
- **2020-12-12:** 9.0.0b is out

</details>

## Recent Updates
- **2023-04-02:** moved to martbhell.github.io. Keeping this for posterity. Firmware Downloads are via Broadcom these days! Also [HPE has them](https://support.hpe.com/connect/s/softwaredetails?language=en_US&softwareId=MTX_241cfaab2fed4696a003f38ee0).
- **2023-04-04:** 9.1.1a with link to broadcom

## Steps

1. [decide](http://www.guldmyr.com/brocade-san-switch-firmware-upgrades#decide)
2. [prepare](http://www.guldmyr.com/brocade-san-switch-firmware-upgrades#prepare)
3. [upgrade](http://www.guldmyr.com/brocade-san-switch-firmware-upgrades#upgrade)

# Decide

One major release at a time is required for the upgrades after 5.2.x, see details below at the release notes section.

If you have to upgrade many steps, you should upgrade to the latest in the series (or if it's very new, probably safest to go with the second newest, just check the release notes of the newest to make sure nothing related is fixed).

If the switch is on 5.1.x you can go directly to 5.3.x.

What I usually recommend is this path: **5.0.1d -> 5.2.3 -> 5.3.2c -> 6.0.1a -> 6.1.2c -> 6.2.2g -> 6.3.2e -> 6.4.3h > 7.0.2e > 7.1.2b > 7.2.1g > 7.3.2a > 7.4.2f > 8.0.2f > 8.1.2g > 8.2.2b > 9.0.0b > 9.1.1b**

_It's also possible to upgrade from a version earlier than 6.4.1b to 7.0.x or from 7.0.x to 7.2.x  - but this is a **disruptive** upgrade (meaning ports will go offline/online during upgrade)._

Brocade now has a document that describes a process of determining the 'ideal' version of Fabric OS you should be running. It is called [Brocade FOS Target Path](https://docs.broadcom.com/docs/53-1003916 "Brocade FOS Target Path").

Yet one more official document to help is the [Brocade Fabric OS Features and Standards Support Matrix, 8.2.x](https://portal.broadcom.com/web/support/netapp?p_p_id=AssistPortal&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=directDownloadURL&p_p_cacheability=cacheLevelPage&_AssistPortal_mvcRenderCommandName=landingPageURL&downloadURL=/u002/extwebportal/ORACLE/INBOUND/DOCSAFE/TEMPDOWNLOADS/15892599006389262.pdf&filename=fos-821-fsm.pdf)

There is also a section (Recommended Migration Paths to FOS ) in the release notes describing how to get to the release you're reading notes for. In addition to these, there are Upgrade Guides from Brocade, at least for newer Fabric OS ( [7.4.0](http://www.brocade.com/content/html/en/software-upgrade-guide/FOS_740_UPGRADE/) and [8.0.0](http://www.brocade.com/content/dam/common/documents/content-types/software-upgrade-guide/fos-800-upgradeguide.pdf)).

There are newer releases being released every now and then, in several series at the same time. You can think of it as releasing updates for Windows XP and 7 at the same time. For example, in February 2011 6.4.1a **and** 6.2.2e were released by HP. You can see this on HP's site if you look at the date next to the download. Quite often Fabric OS versions are not released by the OEMs at the same time, for example "Customer Notice of 7.1.0a release 25th of March 2013" HP released 7.1.0a before IBM.

Which is the recommended one? Usually it's the latest one in the highest series that the switch supports. If you have storage from more than one vendor you may want to check with all and see if they all support the version you want to upgrade to. Vendors certify their equipment with different firmware versions. If you have a tape library, ask the vendor if they have a recommended / list of certified versions.

HP: HP B-series Connectivity stream (available in [HP SPOCK](https://www.hpe.com/storage/spock)). Brocade: "[Brocade FOS Target Path](http://www2.brocade.com/en/backend-content/pdf-page.html?/content/dam/common/documents/content-types/target-path-selection-guide/brocade-fos-target-path.pdf)" Other: Contact them for their compatibility matrices, for example IBM, HDS, EMC, Fujitsu. Brocade also has their own "[Brocade Fabric OS 7.x Compatibility Matrix](https://docs.broadcom.com/docs/12379670?eula=true "pdf on brocade.com - original link found on Brocade's Compatibility Page")" which lists compatibility with other vendors.

You could in principle also say that (some blades in directors are excepted from these generalizations):

2G cannot upgrade to Fabric OS 6.x 4G and 8G can be on Fabric OS 6.x All 4G except some 4/8 & 4/16 (that's 200E) and HP's P- and C-class 4G blade switches (4012 & 4024) can run 6.4.x 8G can run Fabric OS 6.4.x 8G and above can run Fabric OS 7.x 16G (Gen5) needs to be on Fabric OS 7.x or Fabric OS 8.x 32G (Gen6) and 64G (Gen7) needs to be on Fabric OS 8.x or Fabric OS 9.x

Do you want to use the latest one in each series? Probably. Do check for published advisories and the release notes in the firmwares. Some models or blades may work on 7.0.x and not on 7.1.x or vice versa. Fabric OS 7.3.x supports all hardware that supports 7.2.x. Basically you **need** to read the release notes for at least the version you are upgrading to, to confirm that it supports your switch.

## Download firmware links:

- 5.x and 6.x at HPE's [http://whp-aus2.cold.extweb.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer\_Statement.htm](http://whp-aus2.cold.extweb.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer_Statement.htm)
    - New Link for some older 5.3-8.0.x from HPE: [https://support.hpe.com/hpsc/swd/public/detail?swItemId=MTX-fd389e31ce584b35911249126f](https://support.hpe.com/hpsc/swd/public/detail?swItemId=MTX-fd389e31ce584b35911249126f)
    - 6.0.x can also be found here: [ftp://ftp.hp.com/pub/softlib/software10/COL22074/](ftp://ftp.hp.com/pub/softlib/software10/COL22074/)
- For [FOS 7.x](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003855 "on ibm.com")
- For [FOS 8.x](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1009577)
- NetApp's Broadcom/Brocade link: http://www.brocadeassist.com/public/NetAppRelease
    - This has more documents and **newer** firmware than the IBM one.

If you go to downloads for HP's 4/16 there is a link that also takes you to the older FOS firmware. If you don't click through it also only have the firmware that this switch supports. So the latest on there at the moment is 6.2.2f.

On the link above you can also download HP's branded NA (Network Advisor, previously known as DCFM - Data Center Fabric Manager), see notes about that below.

If you click on manuals on the left side you will also be able to download release notes and other guides and references.

5.0.x firmware can also be found at [http://ftp.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer\_Statement.htm](http://ftp.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer_Statement.htm)

6.x, 7.x and 8.x. can be found in the IBM and NetApp links.

## Firmware Upgrade Order

You also probably want to decide on an order to upgrade the firmware on the switches. It's possible to do it via DCFM (now called Network Advisor, used to be something else) one switch at a time or even in parallel. I'd advice against doing it in parallel. One at a time and one step at a time seems the most cautious one. It's not too bad to run a SAN with switches in different firmwares. One idea is to have all switches of one model on the same firmware. If you need to upgrade in several steps, do one step at a time.

Also, switches that are of higher importance like Principal Switch, Core Switches or Seed Switches for DCFM/NA. Should you start with these or perhaps start with another switch of less importance to make sure the upgrade goes smoothly?

With more recent firmwares (6.4 and 7.x) it's possible to jump more than one hop - if you are ok with disruptions in the network. Nice if you need to upgrade switches that aren't in production.

# Release notes:

Please note. Most of these no longer works. But maybe just having the filenames help?

**FOS  [7.x](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003855)[IBM\_Link](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003855 "IBM/Brocade FOS release notes")& [8.x IBM Link](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1009577)**

Brocade release notes in .pdf:

 - [5.2.3](http://public.dhe.ibm.com/storage/san/fos5/v5.2.3_ReleaseNotes_v1.0.pdf)
 - [5.3.1c](http://public.dhe.ibm.com/storage/san/fos5/v5.3.2c_ReleaseNotes_v1.0.pdf)
 - [6.0.0c](http://service.boulder.ibm.com/storage/san/fos6/v6.0.0c_ReleaseNotes_v2.0.pdf "on ibm's ftp")
 - [6.1.2c](http://service.boulder.ibm.com/storage/san/fos6/v6.1.2c_ReleaseNotes_v1.0.pdf "on ibm.com")
 - [6.2.2g](http://service.boulder.ibm.com/storage/san/fos6/v6.2.2g_ReleaseNotes_v1.0.pdf)
 - [6.3.2e](http://service.boulder.ibm.com/storage/san/fos6/v6.3.2e_ReleaseNotes_v1.0.pdf "on ibm.com")
 - [6.4.3h](http://public.dhe.ibm.com/storage/san/fos6/v6.4.3h_ReleaseNotes_v1.0.pdf)
 - [7.0.2e](http://public.dhe.ibm.com/storage/san/fos7/v7.0.2e_ReleaseNotes_v1.0.pdf "release notes")
 - [7.1.2b](http://service.boulder.ibm.com/storage/san/fos7/v7.1.2b_ReleaseNotes_v1.0.pdf "http://service.boulder.ibm.com/storage/san/fos7/v7.1.2b_ReleaseNotes_v1.0.pdf")
 - [7.2.1g](http://service.boulder.ibm.com/storage/san/fos7/v7.2.1g_ReleaseNotes_v1.0.pdf) 
 - [7.3.2b](http://service.boulder.ibm.com/storage/san/fos7/v7.3.2b_ReleaseNotes_v1.0.pdf "http://service.boulder.ibm.com/storage/san/fos7/v7.3.1a_ReleaseNotes_v1.0.pdf")
 - [7.4.2](http://service.boulder.ibm.com/storage/san/fos7/v7.4.2d_ReleaseNotes_v3.0.pdf)
 - [8.0.2f](http://service.boulder.ibm.com/storage/san/fos8/v8.0.2f_ReleaseNotes_v2.0.pdf)
 - [8.1.2g](http://public.dhe.ibm.com/storage/san/fos8/v8.1.2g_ReleaseNotes_v3.0.pdf)
 - [8.2.1a](http://public.dhe.ibm.com/storage/san/fos8/v8.2.1a_ReleaseNotes_v1.0.pdf)
 - [8.2.2b](http://service.boulder.ibm.com/storage/san/fos8/v8.2.2b_ReleaseNotes_v2.0.pdf)
 - [9.0.0a (hp release notes, thin on information)](https://downloads.hpe.com/pub/softlib2/software1/pubsw-windows/p2007118470/v186294/HPE_FOS_9.0.0a_RN_v1.0.pdf)
 - [9.1.1a](https://docs.broadcom.com/doc/FOS-911a-RN) [9.1.1b HPE](https://downloads.hpe.com/pub/softlib2/software1/pubsw-windows/p2007118470/v225909/HPE_FOS_9.1.1b_RN_v1.pdf)

## Notes from the release notes:

 - Upgrading from Fabric OS 5.0.x to 5.2.3 is supported
 - Upgrading from Fabric OS 5.1.x to 5.3.1a is supported, but upgrading from Fabric OS 5.0.x or a previous release directly to 5.3.1a is not.
 - Upgrading to Fabric OS 6.0.0b is only allowed from Fabric OS 5.3.x. (6.0.0c is a special upgrade version, only meant to be used in between firmware upgrades)
 - Upgrading to Fabric OS 6.1.2c is allowed only from Fabric OS 6.0.0b
 - Upgrading to Fabric OS 6.2.2f is allowed only from Fabric OS 6.1.0a or later.
 - Upgrading to Fabric OS 6.3.2e is allowed only from Fabric OS 6.2.0a or later.
 - Upgrading to Fabric OS 6.4.3f is allowed only from Fabric OS 6.3.x. You can upgrade non-disruptively from 6.2
 - Upgrading to Fabric OS 7.0.2 can be done non-disruptively from Fabric OS 6.4.1a or later.
 - Upgrading to Fabric OS 7.1.2 can be non-disruptively upgraded from 7.0.x and 7.1.x. With caveats: For example, any previously existing error log entries with FOS v7.1.0 will be permanently lost once upgraded to FOS v7.1.2.
 - Upgrading to Fabric OS 7.2.x can be done non-disruptively from 7.1.x. Disruptively from 7.0.x is supported.
 - Upgrading to Fabric OS 7.3.x can be done non-disruptively from 7.2.x. Disruptively from 7.1.x is supported (see the FOS\_UpgradeGuide\_v730.pdf and the Brocade Release notes).
 - Upgrading to Fabric OS 7.4.x can be done non-disruptively from 7.3.x. From 6.4.x with firmwarecleaninstall
 - Upgrading to Fabric OS 8.0.x can be done non-disruptively from any Brocade 16G (Gen 5) platform and all blades in the Supported blades table running any FOS v7.4 firmware. From 7.3.0 with "firmwaredownload -s"
 - Upgrading to Fabric OS 8.1.x can be done non-disruptively from Brocade platform running 8.0.2 or later. From 7.4.x disruptively with "firmwaredownload -s".
 - Upgrading to Fabric OS 8.2.x can be done non-disruptively from Brocade platform running 8.1.0a or later. From 8.0.x disruptively with "firmwaredownload -s".
 - Any Brocade platform listed in the Supported Device section running any FOS 8.2 version can be non-disruptively upgraded to FOS 9.0.0
 - Upgrading to Fabric OS 9.1.x "For Brocade X6, G630, X7, and G730 a valid Trusted FOS (TruFOS) Certificate is _required_"

About non-disruptively: This means you **can** go to 7.0.xfrom earlier  than 6.4.1a but ports will go offline during the upgrade. See the release notes or Upgrade Guides for more details.

### DCFM: Data Centre Fabric Manager / BNA: Brocade Network Advisor .

From 6.2.2a release notes:

With the introduction of Fabric OS 6.1.1, certain features and functions were removed from Web Tools (resident in the firmware) and migrated to the DCFM management application. HP recommends that, before you upgrade to Fabric OS 6.1.1x or later, if DCFM is not running on your fabric, you review the Web Tools functionality moved to DCFM, page 29 in these release notes and take note of what has changed so you can assess the impact on your fabric.

Fabric OS 7.x cannot be managed by DCFM 10.4 or BNA 11.0. You need BNA 11.1.0, see the release notes for 7.x.

Brocade Network Advisor 12.4.0 or later is required to manage switches running FOS 7.4.0 or later. Brocade Network Advisor 14.0.1 or later is required to manage switches running Fabric OS 8.0.1 or later

### Updates to documents

Sometimes Brocade releases updates to the manuals without actually updating the manuals. On HP's page you can find them as "Documentation Updates", "Fabric OS Administrator's Guide Update".

### Fabric Watch and MAPS with FOS v7.3

Users running Fabric Watch for switch monitoring in FOS v7.3 are advised to convert to MAPS monitoring before upgrading to FOS v7.4. If you don't, Fabric Watch will stop working.

Also the APM have been replaced with Fabric/Flow Vision.

### Interoperability

See the release notes of the firmware for the specifics. For example Fabric OS 8.0.2 cannot be in the same fabric as for example HP C-Class 4/12 FC switches (4024) and one must use Fibre Channel Routing.

# Prepare

## Download old Brocade Fabric OS Firmware.

Basically, you need to update in steps.

To get FOS 5.2.1b and 6.0.0c firmware: Contact OEM Vendor or Brocade. I've found that two vendors have the firmware available online for free: HP and IBM, see below: Eventually after looking around on HP's old pages we found to [http://ftp.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer\_Statement.htm](http://ftp.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer_Statement.htm) - [this link sometimes changes](http://whp-aus2.cold.extweb.hp.com/pub/softlib/software12/COL22074/co-86832-6/FOS-Drawer_Statement.htm).

[Link to IBM's page for downloading FOS 6 firmwares](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003220 "get brocade firmwares here"). This has firmwares going back all the way to FOS 2.6, it even has Fabric OS 6.0.0c and 5.2.3. On the page they have listed release notes and a little further down there is a link called "Release 6 Firmware". Actually, if you click on 'Release 6 Firmware' you are taken to a page on brocade.com where you can find many different firmwares, including 5.x and 7.x IBM also have a [link about FOS 7.x](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003855 "on ibm.com") and [FOS 8.x](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1009577)

Also note that some features does not exist/work on older Fabric OS. For example on Fabric OS 5.1.x DHCP and SCP may not work (which forces you to use static IP and ftp).

## Equivalent Product Names

[Page with the equivalent Brocade and HP product names.](http://www.brocade.com/partnerships/oems/hp/products_solutions.page "on brocade.com") [Page with the model number as seen in switchshow and HP's model and Brocade's model.](https://support.hpe.com/hpsc/doc/public/display?docId=mmr_kc-0100588 "on hp.com emr_na-c01777657") This is a good one. [Page for correlating IBM and Brocade product names.](http://www-01.ibm.com/support/docview.wss?uid=ssg1S1003855 "on ibm.com")

## Recommendations

HP recommend that you upgrade one fabric and one switch at a time. **Waiting a week or at least a couple of days after you upgrade the first fabric is a good idea - gives you time to see if anything went wrong, if you can fix it and if you can do anything different next time.** See [HP SPOCK](https://www.hpe.com/storage/spock "hp spock") for more details in regards to compatibility and interop modes. The HP B-series Connectivity Stream lists the recommended firmware and all the supported ones for each switch model. It also has a list of the supported SFPs. Find it by clicking on "[Switches](http://h20272.www2.hp.com/Pages/spock2Html.aspx?htmlFile=hw_switches.html "HP SPOCK - SAN Switches")" in the left-hand navigation pane under the "Other Hardware" section. The Connectivity Stream is great and it is updated often so I will not link directly to it. You need an HP Passport to log on to HP SPOCK - it is free to create and you do not need a contract or product in warranty.

Other vendors have similar matrices. HP for example does not have a list stating which Fabric OS firmware is supported with which HP P6000 firmware. The idea is that you go with the general recommendation of Fabric OS firmware.

Do read the release notes for the firmware(s) you decide on: for example not all 4GB SAN-switches can run the 6.4.x FOS. The 8- and 16-port 4Gbps switches (Brocade 200E) do not run 6.4.x or 6.3.x. Only 8Gb and 16Gb switches can run the 7.x.x FOS. The release notes also have the fixes, enhancements, upgrade paths and supported switches. Generally the Brocade versions of the release notes are more verbose when it comes to fixes, but if you have an HP branded it might be easier to use the HP one as that has the HP names of the products. Also it might be hard to find the Brocade release notes if you do not have a contract with Brocade. Other vendors (like IBM/Fujitsu/HDS) provide you with the Brocade version of the release notes. You can find the release notes from their support pages.

Do  consider updating OS patches, HBA drivers/firmware, management softwares and storage drivers/firmware. [For example](http://community.brocade.com/thread/5751?start=15&tstart=0 "on the brocade forum") Qlogic had driver updates to their drivers that prevent HP blades from getting stuck in G\_port after a reboot. Another for Qlogic FC cards was to not write a partition table on Dell servers at 2TB on the LUN (not so nice for > 2TB disks)..

## Upgrading Tools

SANLoader is an unofficial HP tool to upgrade firmwares. With this you do not have to create an ftpserver etc. Contact HP Support, they may give this to you. This is meant to be used when the other ways does not work, but it helps out a lot as you do not have to set up an FTP/SCP server.

Sanloader used to (winter 2010) not work well on Windows 7 and may not work flawlessly on the pre 6.x firmwares.

Other ways:

- Set up a ftp/scp server and upgrade via the CLI (command line interface).
- Use DCFM ( Data Center Fabric Manager - now called Network Advisory ) to upgrade firmware.
- Firmware can also be upgraded through the web interface (click on switch admin and then on firmware download). You will still need an FTP/SCP server for this though. See the [web tools admin guide](http://bizsupport1.austin.hp.com/bc/docs/support/SupportManual/c01731559/c01731559.pdf "web tools admin guide for fos 6.2.x") page 73-74 (FOS 6.2.x but it hasn't moved).

FileZilla is a free FTP-server that works well. There are many alternatives around. But unfortunately some don't work sometimes (not 100% sure but probably combination of older FOS with older ftp client with FTP server that couldn't handle that client) as listed in the comments thread in this post. FileZilla is however still on sourceforge so you may want to be careful about installing that - it might contain malware. Storing them on a Synology NAS works - thanks Henny!

For FTP clients:

- /usr/bin/ftp in Ubuntu (also in Ubuntu on Windows)
- [WinSCP](http://winscp.net/ ".net") for a free opensource Windows alternative that does both ftp and SCP (and more).

For SCP any machine with Linux and sshd on should work. You can also get an scp-server running on Windows, OpenSSH would work. Both protocols are old, [SCP is safer](http://en.wikipedia.org/wiki/Secure_copy "on wikipedia") while FTP is sending data in clear text.

Personally I like doing this via the CLI. The Network Advisor way gives you the possibility to upgrade in parallel, but that's also risky. If you use a Linux server to provide the firmwares via SCP don't forget to let the switches in via firewall or tcp.wrapper ( /etc/hosts.allow ). If you do the upgrade via ftp - make sure that passive and active ftp both works.

## How to access the SAN-switch

The most common way is to access the CLI of a Brocade switch by connect to the IP of it with an ssh- or telnet-client, [PuTTy](http://www.putty.org/ "putty.nl") is the name of a free Windows client. If you are comfortable with CLI, Windows 10 has WSL and a good ssh and scp client built in. Telnet is unsafe so do try to use the ssh at all costs. Windows 10 has Bash which is in my opinion much nicer to use than putty. It's also possible to access the switch CLI via a serial cable, however as the firmware files are several 100MB (approaching 1GB for 6.4.x) that's not really viable when upgrading firmware. Hyperterminal is a free windows tool that comes by default in some Windows versions. You can also use PuTTy for serial access. To access the web interface just point the web browser to . It requires Java. The Java version that's supported is listed in the release notes of the Fabric OS.

# Upgrade

[Here on HP's Support Forum](http://h30499.www3.hp.com/t5/Storage-Area-Networks-SAN/Upgrade-of-EVA-4400-Switches/m-p/4788345 "on new ITRC") are some more notes about v6.x. Basic steps:

Note: version 6 does not require to specify the exact folder location SWBDxx: it just needs the root containing "the install" file

1) Unpack the downloaded firmware in the FTP or SCP download directory 2) Start the FTP/SCP Server and allow access 3) Connect to the CLI of the switch via telnet or ssh 4) Type this in the CLI: firmwaredownload 5) Answer all questions: when it asks for File Name be sure to write /v6.4.1b, that is the folder under which you find all the SWBDxx folders. Failing to do so makes it impossible to download the firmware 6) Wait for reboot of the switch and reconnect, check the firmware version with the "version" command

## More notes about the upgrade

CLI Command to start the update process is **firmwaredownload** - this starts the interactive version, it is possible to specify user, directory, host directly via the CLI. See the [Command Reference Guide](http://www.brocade.com/content/html/en/command-reference-guide/fos-741-commandref/wwhelp/wwhimpl/js/html/wwhelp.htm "Link to manuals for HP B-series switches on hp.com") for details. There are reference guides for each major Fabric OS release.

### Specifying Directory

Please use forward slashes when specifying directories.

For example when you unzip the firmware file and it creates a sub-folder in the FTP-root that is called v5.3.1a then you need to specify /v5.3.1a as the directory.

For firmwares prior to 5.3.x you have to specify the release.plist - /v5.2.2a/release.plist. _However it says in the release notes for 5.2.3 that release.plist is no longer needed._

In some cases you may have to specify the sub directory. For example the 4/16 HP Switch is a Brocade 200E with switchtype 34. So you would then use directory SWBD34 - /v5.3.1a/SWDB34. You can also try with /v5.3.1a/release.plist, /v5.3.1a/SWDB34/release.plist or /v5.3.1a/install. However with 5.3.1a you _should_ not have to so /v5.3.1a should be enough.

### firmwaredownload example:

```bash
switch:admin> firmwaredownload
Server Name or IP Address: IP.TO.SCP.SERVER
User Name: username
File Name: /path/to/v6.2.2e
Network Protocol(1-auto-select, 2-FTP, 3-SCP) \[1\]: 3
Password:
Server IP: IP.TO.SCP.SERVER, Protocol IPv4
Checking system settings for firmwaredownload...
System settings check passed.
You can run firmwaredownloadstatus to get the status
 of this command.
This command will cause a warm/non-disruptive boot on the switch,
 but will require that existing telnet, secure telnet or SSH sessions
 be restarted.
Do you want to continue \[Y\]: y
 Firmware is being downloaded to the switch. This step may take up to 30 minutes.
 Preparing for firmwaredownload...
 Start to install packages...
 dir ##################################################
 \[\[lots of these for all packets\]\] ##################################################
 \[\[also stuff like these are seen many times:\]\]
 warning: /etc/fabos/pki/switch.0.rootcrt created as /etc/fabos/pki/switch.0.rootcrt.rpmnew
 kernel-module-ipsec ##################################################
 Removing unneeded files, please wait ...
 Finished removing unneeded files.
All packages have been downloaded successfully.
 Firmware has been downloaded to the secondary partition of the switch.
 HA Rebooting ...

```

### Transfer Protocol and Connectivity

If you are using SCP and that does not work, please try with FTP. If neither works, see if something else can log on to the FTP/SCP server. And of course, make sure the right permissions/root directory are set on the FTP-server. If your FTP/SCP server has log files, check them. If it works from one client but not from the switch, check the logs and see if there's a difference. Sometimes if the SCP doesn't work via CLI it might work by doing SCP (but starting it from the Web Tools, thanks Eric in the comments for this!).

If you are logged on as root on the SAN-switch you can use the scp- or ssh-client on the switch to confirm connectivity, like this:

**ssh username@server ls /tmp/v6.0.1a** to list the /tmp/v6.0.1a on the SCP server.

_You need to be root to run the above command._

If that also does not work, you have some kind of networking problem - you can try direct connecting a laptop to the LAN interface of the switch. To see the network settings on the switch: ifmodeshow and ipaddrshow

### Passwords

Sometimes when upgrading from 6.1.1d to 6.2.2 we have seen that the passwords have gotten reset.

Default password is then "password" or "fibranne".

You can reset the password with the CLI command "passwd admin" to reset password on the admin account.

If you forget all passwords it might be possible to be able to reset it via the serial cable interface while booting the switch.

On EMC branded switches the default password might be: [Serv4EMC](http://community.brocade.com/thread/6127 "link to forum post on brocade.com")

### CF Cards

If your switch is out of warranty/contract and it's still working. I'd suggest making a copy([dd  in linux for example](http://community.brocade.com/thread/6406 "post about it on brocade's forum")) of the CF-card. Then if the CF card decides to fail you can just get a new one from random\_electronic store and dd the contents of the flash back.

### Licenses

When replacing a switch make sure that the licenses are correct. If for example you have a switch with 'power pack' - then for HP there is a special spare part number for a switch with power pack and one without. Power pack is a grouping of licenses,  which licenses are in the pack differs between models.
