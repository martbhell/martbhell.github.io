---
title: Make your own L2 Firewall!
date: 2013-07-17
category: it
tags: coursera, firewall, learning, linux, pox, python, sdn, software, defined, networking, studying

Is what I did this week during the [SDN Course](https://www.coursera.org/course/sdn "https://www.coursera.org/course/sdn") on Coursera :)

Within [mininet](http://mininet.org/ "http://mininet.org/") or with a real OpenFlow capable switch, you can point the switch to use a controller. The controller would figure out all the smart stuff and the switch only does what the controller tells it to do.

[POX](http://www.noxrepo.org/pox/about-pox/ "noxrepo.org") is one of these APIs that you can use to create controllers, it's good for learning about controllers as it's not so low level as it's sibling NOX, which is in C++. There are switches in JAVA too ([Floodlight](http://www.projectfloodlight.org/floodlight/ "http://www.projectfloodlight.org/floodlight/")) and many more.

With POX there are some example switches, for example a basic L2 learning switch. It remembers (among quite a few other things) MAC addresses for hosts and remembers in which ports the MAC addresses can be found. With a simple ping: After L2 broadcast is done to find the MAC of the recipient, the controllers install the MAC\_source+port and MAC\_destination+port as flows on the switches.

What we did this week was to right after the switch is executed, run some extra code that parses a .csv file for MAC address pairs that are not allowed to talk and add these pairs into the flow table.

Pretty cool I think :)
