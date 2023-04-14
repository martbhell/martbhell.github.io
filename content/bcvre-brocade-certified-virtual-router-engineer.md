---
title: "BCvRE - Brocade Certified virtual Router Engineer"
date: 2013-09-08
categories: 
  - "it"
tags: 
  - "bcvre"
  - "brocade"
  - "certified"
  - "exam"
  - "open-source"
  - "virtualization"
---

Been checking out the Vyatta vRouter a bit closer. Mostly because of the BCvRE exam but I'm slowly starting to think there might be some benefits to using it elsewhere too.

1. See [vyatta-a-routervpnfirewall-in-a-vm-brocade-certified-vrouter-engineer/](http://www.guldmyr.com/blog/vyatta-a-routervpnfirewall-in-a-vm-brocade-certified-vrouter-engineer/) for where to find manuals or training materials.
2. See [the objectives](http://www.guldmyr.com/blog/?p=2041).

I tried installing [Vyatta](http://vyatta.com/ "http://vyatta.com/") vRouter 6.6 amd64 Live ISO to disk first in a Virtualbox VDI file and then uploading said file to openstack. This works, but:

Ethernet interfaces might get renamed but a startup, log in and save, poweroff and another boot should get the first interface back to eth0.

In the openstack available to me I could set up my own networking topology like this:

- Create one network (VLAN) and define several subnets inside (these are still kind of firewalled based on IP and MACs).
- Then create machines and add the network.
- Power off and start the machines again (or the links stay DOWN).

VMs should see an individual eth interface per subnet. The machines still get an IP assigned to each interface/subnet even if DHCP is disabled. If DHCP is disabled you still have to statically assign only this assigned address on the interface. The interfaces are in order: the IP listed at the top is the IP you need to put on the first interface (eth0).

Because a lot of the things you can do with a router involves creating networks and assigning IP addresses, which openstack would block for security reasons - it was much easier to do all of these in VMWare Workstation:

## **DHCP/DNS**

1. Install a Vyatta VM - bridged and a private network (without a DHCP).
2. Install another OS in a VM - this will be a client - only on the private network.
3. Put both VMs in the same network.
4. Configure dhcp on the Vyatta VM:

configure
delete interfaces ethernet eth1 address dhcp 
set interfaces ethernet eth1 address 10.1.1.1/24
commit

Configure dhcpd on the Vyatta VM:

configure
set service dhcp-server
set service dhcp-server shared-network-name ETH1\_POOL subnet ??? # pool, dns, router

Then, set up so that the Vyatta VM routes traffic from the private network to the Internets. A NAT. This is called a source NAT in the vyatta CLI.

set nat source rule 10 ??? # Put in the settings you need. Source, outbound interface and the IP they should be seen as from the outside.

Real easy to set up a DNS forwarding server too:

set service dns forwarding listen-on eth1 
set service dns forwarding name-server 8.8.8.8
commit

Now we have a client behind the Vyatta gateway that can access the Internet!

It's possible to set up different kinds of VPNs. For example site-to-site or remote access.

It is possible to ssh from the vyatta VM - you can even run ssh-keygen. How to add an authorized key you wonder?:

set system login user vyatta authentication ...

## Routing

Another thing to test: launch a bunch of Vyatta VM and use them to route IP traffic, woop woop! The BCvRE objectives actually mention OSPF so this would be wise to test.

### Starting with static routing

_Key: Network Name (IP subnet, interface on the host)_

- _VM hostname - Interface inside the VM: IP address_

Topology:

Public (192.168.1.0/24, bridged):

- Vyatta - eth0: 192.168.0.23

Network A (10.1.1.0/24, vmnet2):

- Vyatta - eth1: 10.1.1.1
- V1 - eth0: 10.1.1.10
- V2 - eth1: 10.1.1.20

Nework B (10.2.2.0/24 , vmnet3):

- V2 - eth2: 10.2.2.20
- V3 - eth0: 10.2.2.30

Static routing:

Vyatta: set protocol static 10.2.2.0/24 next-hop 10.1.1.20
V1: set protocol static 10.2.2.0/24 next-hop 10.1.1.20
V3: set protocol static 10.1.1.0/24 next-hop 10.2.2.20
V3: ping 10.1.1.10

### OSPF!

Adding host V4 that is in Network B and Network C. Basically Vyatta, V2 and V4 are routers. V1 and V3 do not run OSPF, they have their default gateway to one of their local routers. So V3 has 10.2.2.20 and V1 has 10.1.1.1.

Public (192.168.1.0/24, bridged):

- Vyatta - eth0: 192.168.0.23

Network A (10.1.1.0/24, vmnet2):

- Vyatta - eth1: 10.1.1.1
- V1 - eth0: 10.1.1.10
- V2 - eth1: 10.1.1.20

Network B: (10.2.2.0/24, vmnet3)

- V2 - eth2: 10.2.2.20
- V3 - eth0: 10.2.2.30
- V4 - eth0: 10.2.2.40

Network C: (10.3.3.0/24, vmnet4)

- V4 - eth1: 10.3.3.40

Remove all static routes we did previously on Vyatta and V\[1-2,4\]:

delete protocols static route
commit
save
show proto

Set up OSPF - define the networks on each router that that router share with another router:

ALL: set loopback interface IP to something unique and with a /32
ALL: set protocols ospf redistribute connected
V4: set protocols ospf area 0 10.2.2.0/24
V2: set protocols ospf area 0 10.2.2.0/24
V2: set protocols ospf area 0 10.1.1.0/24
Vyatta: set protocols ospf area 0 10.1.1.0/24
V3: set system gateway 10.2.2.20
V1: set system gateway 10.1.1.1

Test:

V4: ping 192.168.0.23
V4: show ip ospf route

Debug:

V2: monitor protocol ospf enable lsa
V4: reboot # and wait
V2: show log|less
