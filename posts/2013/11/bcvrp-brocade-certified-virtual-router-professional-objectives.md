---
title: BCvRP – Brocade Certified virtual Router Professional – Objectives
date: 2013-11-10
category: it
tags: bcvrp, brocade, certified, exam, objectives, open, source, virtualization

For training these I set up networks. Many. Drawing the networks first in LibreOffice Draw and then setting them up with virtual machine templates and LAN segments.

The exam I took in October and because it was a beta exam the results aren't out until December :)

The BCvRP has the below [objectives](http://community.brocade.com/docs/DOC-3349 "http://community.brocade.com/docs/DOC-3349") (included for free are some of my comments on each topic). None of this should be taken as a replacement for taking the actual course and actually doing these things on a vrouter. And honestly, the various concepts and technologies described in the objectives below can become very complex. So before taking this course/exam you at a minimum want to know the basics of BGP and setting up an OSPF network should be a breeze.

 

# OSPF Multi-Area Concepts

- **_Describe OSPF routing concepts_**

- Stub area - replace external routes with a default route
- NSSA - not so stubby - can have a local external route inside a stub area
- no-summary : exclude inter-area routes
- LSA - link state advertisements
    - 1 All OSPFs: Lists subnets/links directly connected, does not cross area boundaries
    - 2 from DR: Lists routers connected to a network, does not cross
    - 3 from ABR: Lists networks from outside the local area
    - 4 from ASBR: Summary, lists location of ASBR
    - 5 from ASBR: AS external, list networks outside OSPF AS. 7 for NSSA.
- Summarization: Good to have continuous addresses in an area, easier to summarize.
    - Do not summarize routes originating in Area 0.

# BGP, EBGP and IBGP Concepts

- **_Describe gateway protocol concepts_**

- BGP Basics
    - Purpose is to determine best path (not necessarily the shortest)
    - TCP Connection, no periodic updates.
    - iBGP - within an AS / eBGP - between AS
    - Attributes - BGP policies - costs
    - eBGP - best to be on the same network
    - TCP port 179
    - A unique AS number is needed, there are [private AS numbers](http://en.wikipedia.org/wiki/Autonomous_System_(Internet) "64512 to 65534").

**eBGP**

set protocols bgp AS# router-id IP set protocols bgp AS# neighbor ip-address remote-as as-number set protocols bgp AS# network address/mask

exact match must be in the router's table: create a static route to blackhole on the router

**iBGP** = same AS on the BGP peer (the neighbor)

iBGP - a full mesh is necessary. iBGP does not forward routes learned from other iBGP peers. One can use "next-hop-self" so that iBGP router's change the next-hop address to a network whenever it propagates the route. update-source - this needs to be the same as the router-id.

iBGP required settings: local AS number, neighbor address and "update source".

bgp does not reset advertised routes after an administrator's changes. Changes to eBGP does not come into affect until you run the reset: '**reset ip bgp external out**'. The BGP table can be large - gigabytes. Use the word soft to only request updates and not reset the peer connection.

reset ip bgp external \[ipv4 address\]

 

#### Tuning attributes and priority

1. Local preference - only included within an AS. Default is 100. Higher is better.
2. AS Path - always forwarded - shorter is better
3. Origin - lowest
4. Multi-exit discriminator # modified by an ISP to indicate preference
5. eBGP preferred over iBGP
6. Lowest Peer ID
7. Community # group of prefixes with a common property. Can be used in filters.

 

Prepending: insert your AS number in the AS in the beginning of the AS path. Communities are created with: set policy community list

### BGP troubleshooting

An active peer - not good. Trying to actively set up a session.

 

### iBGP design

- Does not have to be physically connected (as in BGP).
    - Connectivity over BGP
- Peer to loopback address
- Full mesh is required
    - Doesn't scale. You can use a Route reflector ("concentrator") and have other iBGP routers as clients.
    - route reflectors must be meshed
    - You can also create multiple private AS within your AS. Reduces members in the mesh. Called a confederation.
        - Public AS number is only visible in the config
        - The Private numbers are visible in the show ip bgp commands.

 

Create a peer group, set BGP settings on the peer group. Then assign peers to the group.

## **Route Redistribution**

- Describe route redistribution design and configuration

- Best practices:
    - Set metrics
    - Do not redistribute into or out of BGP
    - Use network statements
    - Statements to direct towards BGP exit points
    - Only redistribute a network from one host (VRRP)
- OSPF: metric type (increase cost)
- Only active routes are redistributed

## **IPsec VPNs**

- Identify IKE Phase 1 and Phase 2 operations
- Describe how to configure and troubleshoot an IPsec VPN

## **OpenVPN Concepts**

- Identify the features of OpenVPN
- Describe OpenVPN configuration

## **VRRP Concepts**

- Describe VRRP concepts and operations

## **Optimization**

- Describe the attributes of WAN load balancing
- Describe QoS features and configuration

# Policy-Based Routing

- Explain where policy-based routing falls in Brocade Vyatta packet flow
- Configure and verify policy-based routing

- Default: drop route entry . By default it only takes the first action that matches.
- Rule -> Filter -> Route Map (excluding deny filters) > Take action as defined
- Filter list: prefix 172.16.0.0/16, le 24. Any netmasks between /16 and 24, including /16.
- Regexp for matching AS lists - use underscore to match whitespaces

- Filter has the rules.
    - permit/deny in the filters affects if the rule is applied to the filter.
- Route-maps has the rules.

# Multicast Routing

- Describe multicast protocols/elements
- Configure and troubleshoot multicast routing
