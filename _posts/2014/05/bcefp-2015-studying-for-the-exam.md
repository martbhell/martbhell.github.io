---
title: "BCEFP 2015 - Studying for the exam"
date: "2014-05-07"
categories: 
  - "it"
tags: 
  - "brocade"
  - "brocade-certified"
  - "brocade-certified-ethernet-fabric-professional"
  - "certification"
coverImage: "original.gif"
---

In a [previous post](http://www.guldmyr.com/blog/brocade-certified-ethernet-fabric-professional-2015-beta-exam/ "Brocade Certified Ethernet Fabric Professional 2015 Beta Exam") I listed a some of the sources Brocade listed that one should use when studying for the BCEFP exam. Here I'm going through a those I found some comments on what what they are and what I think of them.

## Beta Course Material

The first of the **beta** material available is something called "[Brocade Ethernet Fabric Administration](http://www.brocade.com/forms/getFile?p=documents/course_data_sheets/CEF300-DataSheet.pdf "CEFP 300-WBT Course Data Sheet")". This is a few pdfs/slides with notes on them. Introduction of various features and components. Not much detail in the first 10 modules and basically all the modules are awfully short, some are one slide even. Hopefully this is just because it's a beta. Progressively they become more detailed, which is good to not overwhelm the reader I guess. Checking out the [data sheet](http://www.brocade.com/downloads/documents/course_data_sheets/CEF300-DataSheet.pdf) for the CEF 300 course should give you some idea what you should learn after going through the materials. There are free materials available for the **[Ethernet Fabric Specialist Accreditation](http://www.brocade.com/education/certification-accreditation/accredited-ethernet-fabric-specialist/curriculum.page "http://www.brocade.com/education/certification-accreditation/accredited-ethernet-fabric-specialist/curriculum.page")** \- it's even on [the tube](http://www.youtube.com/watch?v=V9tMZgCydYQ "http://www.youtube.com/watch?v=V9tMZgCydYQ"). The youtube video is quite long but it's an introduction to the thought behind the Ethernet Fabrics. It's a bit outdated already I hope as they the talk talks about immaturity a lot, less than a year old. The presenter - Chip Copper - also mentions a Fabric Essentials 201 that should be out "later on down the line" - which is not out yet. Boo Urns!

Questions I got while reading material:

- What is a hard-drop option in an extended ACL?
- What does "override the control packet trap entries" mean? Brocade communities to [the rescue](http://community.brocade.com/t5/Ethernet-Fabric-VDX-CNA/How-do-you-Enable-Configure-SSH-access-to-VDX-6710/td-p/54389). Is for normal transit traffic and traffic to the CPU == the management interface?

## [**BCEFP Nutshell**](http://www.brocade.com/downloads/documents/certification_study_tools/bcefp-nutshell.pdf "pdf on brocade.com")

I usually print these out, read through a few times and note down anything I don't get so that I can go through the course materials and user guides to completely understand it. This one is **vital**.

Some really useful sections:

- VCS Data Path
- VCS Fabric - Layer 3 Routing

Some questions I needed to clarify after reading the BCEFP nutshell guide (page numbers):

- Are there any new hardware represented in the BCEFP 2015 compared to the BCEFP 2013?
    - 6740 - 10GbE, 10GbE/FC and 40GbE ports
    - 6740T - 48 x 1/10GbE
- VDX6720:
    - Is the VDX 6720-60 oversubscribed?
    - Is the difference between switching and forwarding bandwidth that one is how much the backplane can handle and the other is how much the ports could do?
        - Looks like that, an older version of the [6720 Data Sheet](http://www.governmentbigdataforum.com/2012/files/Brocade_VDX_6720_DataSheet_01.pdf "GA-DS-1524-01") shows this, it's been removed in a future data sheet.
- [VCS / Logical chassis / Distributed](http://www.brocade.com/downloads/documents/html_product_manuals/NOS_410_AG/GUID-5255C5BC-9A1F-4B3B-83E9-3AE6EA37AC00.html "NOS Administrator's Guide"):
    - VCS Modes:
        - Logical Chassis: Requires NOS 4.0.0. Data and config paths are distributed. All is configured from the principal node.
            - **Distributed**
        - Fabric Cluster Mode: Data paths are distributed. Config is done independently on each node.
            - 8770 and 6740\* boot up into this mode by default.
            - **Local Only**
    - Standalone Mode: Only compact switches support this restricted mode - 6710-6730. Only support NOS 2.1 features. Only IP static routes and in-band management.
- VDX 8770 and what does N+1 mean? [Active passive.](http://en.wikipedia.org/wiki/N+1_redundancy "on wikipedia")
    - 8770-8 is N+1 with loss of one SFM
        - So it can loose one SFM and it still has a redundant SFM? Aye, this can have up to 6 SFM.
    - 8770-4 is not N+1 if one SFM is lost
        - This can have 3 SFM
- NOS 3 requires cold reboot of standby MM during failover & firmware upgrades. Does NOS 4 do too?
- What is an unsigned integer? - Hop Count Field in the trill frame.
    - It cannot be negative.
- VCS features:
    - VCS Edge Port config + LACP: With Brocade type are there more models than a CNA, VDX or Brocade 8000?
    - With NOS v2.0.0a max 8 ECMP paths per switch. Different with NOS 4?
- From show vcs detail (shows switches in the fabric):
    - What is the Internal IP used for? Unclear, the pattern is: 127.1.0.RBRIDGE ID
    - What does the state "Testing" indicate? Unclear, perhaps when running "diag \*" commands?
- show fabric
    - "show fabric islports" is similar to switchshow shows islports only, how to see device ports
        - show interface switchport # shows all ports in L2 mode (VLAN1)
    - "show fabric all" shows a short list of switches in fabric, similar to fabricshow
- What is  "Static MAC Pre-Provisioning on vLAG" ? (p55)
- The fibre length of a link should have deskew value of 7 microseconds. Is this configurable?
    - Looks like it's not. It's not in the NOS 411 cmd reference guide anyway.
- FCOE
    - FCF = FCoE Forwarder. A switch that does both Ethernet and FC
    - ENode = FCoE Node
    - FSB =  FIP Snooping Bridge (Can I get a Yay for nested acronyms?) A FCoE Switch that needs to be connected to an FCF (p67)
    - FCoE Profiles = (p84)
- priority-table command is just messed up. What do the numbers mean? (p66)
    - It's a mapping of Priority Groups to Classes of Services.
- Are Virtual Fabrics on FCoE supported these days?
    - No. FCoE needs to be on VLANs with ID < 4096.
    - Btw, Virtual Fabrics is also a feature on Ethernet. Not only FC. Used when one needs overlapping VLAN IDs - multitenancy.
- Is the max amount of RBridges in a fabric still 24? (p77)
    - Max 24 in Logical Chassis with VDX 6710-6730. Max 32 for 6740 and 8770.
    - It is the recommended amount. Theoretical max in NOS4 is 239. One below 1111000.
- Is there a pattern to the MAC addresses of the Switches/RBridges/FD/XD?
- What is a VMWare Port Group?
    - Found in [VMWare Virtual Networking Concepts](https://www.vmware.com/files/pdf/virtual_networking_concepts.pdf "pdf on vmware.com")
    - Important with VMotion, makes sure that when a VM moves to a different hypervisor it gets the same network configuration.
- In RBAC what does it mean that one can access a command but not execute it? (p86)
    - It means one can view the settings, like a 'show command' works but not 'command' to set the setting.
    - Btw: admin/user accounts are locked, only pw can be changed
- What are these FRUs: cid-card, compact-flash, mm, SFM? (p89)
    - MM - Management Module
    - SFM - Switch Fabric Modules
    - Compact-Flash - Supposedly where the firmware/configs are stored.
    - CID-Card - Chassis ID - each card has two EEPROM - one critical and a non-critical. The non-critical can be fixed with a "CID Recovery Tool"
- oscmd - more details about this, how to run a command? (p96)
    - oscmd arp -a
    - oscmd scp localfile remote.server:

The below I'll bring up in a later post:

## **VDX Troubleshooting Course**

VDX Troubleshooting Course

## **BCEFP practice questions / answers**

http://community.brocade.com/t5/Certification/BCEFP-2013-Exam-150-180-Practice-Questions/ta-p/4099

 

## Other

Intro to VCS Fabric Technology: http://www.brocade.com/downloads/documents/white\_papers/intro-vcs-fabric-technology-wp.pdf CFP- MSA CFP2 Hardweare Specs: About the 40/100Gbps CFP2 SFP. MSA - multi-source agreement. Code names of switches? Find the NOS firmware and look in the file "platform\_names". Quite a few bird names (nighthawk, dragon, superhawk, tomahawk ;), kestrel, falcon, blackbird).
