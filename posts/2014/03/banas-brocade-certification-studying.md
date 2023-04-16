---
title: BANAS - Brocade Certification - Studying
date: 2014-03-30
category: it, storage
tags: bna, brocade, certification, network, advisor, studying

I'm going to focus on the below things when studying for BANAS: They are based on the current objectives listed on Brocade's [page](http://www.brocade.com/education/certification-accreditation/accredited-network-advisor-specialist/index.page "http://www.brocade.com/education/certification-accreditation/accredited-network-advisor-specialist/index.page").

 

## Brocade Accredited Network Advisor Specialist Exam Topics

- The Brocade Accredited Network Advisor Specialist exam has these objectives:

### Product Features

- Demonstrate knowledge of Brocade Network Advisor product features

### Installation and Configuration

- #### Describe the installation and configuration of Brocade Network Advisor
    
    - Taken care of in my [previous blog post](http://www.guldmyr.com/banas-brocade-accredited-network-advisor-specialist/ "BANAS – Brocade Accredited Network Advisor Specialist"). Can be installed in a VM for practice.
- #### Perform SAN Discovery
    
    - What are seed switches?
- #### Perform IP Discovery
    
    - BNA 170-WBT is a course that's currently free by Brocade - it's about IP Discovery in BNA!
    - Once discovered devices are stored in the Management application database. First IP of the device discovered becomes the primary address of the device.
    - Simple/Profile based discovery: single: hostname/IP. Profile: range.
    - Requirements
        - Users must have Discover Setup-IP and "All IP Products AOR" privileges
            - For rediscovery only "All IP Products AOR" is needed?
        - ICMP or telnet must be enabled on devices
        - Snmpv1+v2 or v3 read-write
        - IP range of devices must be known
        - All devices must have SNMP MIB support
    - Access by: "Discover -> IP Products".
    - One can add default username/password. One can add several and it tries the default and then the rest..
    - It uses OIDs to select products to include/exclude.
        - Cisco/Juniper are available by default.
    - Seed address: the IP the BNA server will use to contact the switches?

### Migration

- Describe considerations when migrating to Brocade Network Advisor from other tools
    - Check out the Installation Guide for BNA.

### Troubleshooting

- Demonstrate knowledge of troubleshooting Brocade Network Advisor
