---
title: "BCvRE - Brocade Certified virtual Router Engineer - Objectives"
date: "2013-09-08"
categories: 
  - "it"
tags: 
  - "bcvre"
  - "brocade"
  - "certified"
  - "exam"
  - "objectives"
  - "open-source"
  - "virtualization"
---

This post will be continuously updated with my short notes under each concept. It's not meant to be a replacement of the official training materials. I'm just starting out playing with the vRouter Core / open source version and installing it in a VM and set up some networks and firewalls is probably one of the best way to learn this. Learn by doing!

The **Brocade Certified vRouter Engineer 2013** exam has these [objectives](http://community.brocade.com/docs/DOC-3336 "http://community.brocade.com/docs/DOC-3336"):

 

## Brocade Vyatta vRouter System Operations

- Describe show command system usage
    - show - in operational mode shows status of components
    - show - in configurational mode shows the configurations
    - run show -  in configurational mode shows status of components
- Identify key CLI operations
    - set/delete
    - copy (configs)
    - renew (new dhcp IP)
    - install (to disk)
- Describe the commit and save processes

## Ethernet Concepts

- Identify Ethernet operations
- Identify VLAN operations and settings
    - set interface ethernet eth0 vif <vlanid> # this creates eth0.<vlanid> a subinterface. This looks like a normal ethernet interface.
    - set interface pseudo-ethernet # these can be used if you want to set the MAC-address. Some features are not allowed for these peth devices though (VLAN, bonding).
- Identify bonded interface operations
    - Two NICs on the same network
    - set interface bonding (IP address, mode)
    - set interface ethernet (bond-group)
- Demonstrate knowledge of configuration and operation using show commands

### **TCP/IP**

- Demonstrate knowledge of the relationship between Layer 2, IP and TCP/IP
- Identify TCD and UDP differences
- Identify address subnets

### **DHCP and DNS Troubleshooting**

[http://www.guldmyr.com/blog/?p=2022](http://www.guldmyr.com/blog/?p=2022) I'm going through how to set it up.

- Describe troubleshooting of DHCP operations
    - show dhcp server leases
    - show log dhcp
- Describe troubleshooting of DNS forwarding
    - monitor dns forwarding # I could not get anything into the log)
    - show dns forwarding # shows cache size for example)

### **Routing**

[http://www.guldmyr.com/blog/?p=2022](http://www.guldmyr.com/blog/?p=2022) went through how to set up static routes

- Identify uses for routing
- Identify show commands for use with routing
- Identify configuration of different types of static routes

### **Firewalls**

- Describe firewall operations and troubleshooting using show commands
- Describe firewall rulebase operations
    - set firewall name <name> default-action
    - set firewall name <name> rule 1 destination/source
    - set firewall name <name> rule 1 action <action>
    - set interface bonding bond0 firewall in/local/out name <name>
        - in - into the router (matching on destination IP)
        - out - out from the router  (matching on source IP)
        - local - to the router itself

### **NAT**

- Describe NAT concepts

## Upgrades

- Describe the Brocade Vyatta [upgrade process](http://vyatta.org/getting-started/how-to-update "http://vyatta.org/getting-started/how-to-update")
    - 1\. Install 6.5R1 to disk.
    - 2\. add system image URL
    - 3\. reboot
    - It is also possible to copy the config elsewhere and reinstall

## Logging and Packet Captures

- Identify logging options for firewall and NAT operations
    - set firewall name <name> rule <num> log enable
    - commit; exit
    - monitor firewall .. # and see matches to the rule.
- Identify methods to verify operations and troubleshooting

## OSPF Single-Area

[http://www.guldmyr.com/blog/?p=2022](http://www.guldmyr.com/blog/?p=2022) set up an area 0 OSPF

- Describe OSPF show command output
- Describe how to configure OSPF
