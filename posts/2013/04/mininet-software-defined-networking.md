---
title: Mininet - Software Defined Networking
date: 2013-04-29
category: it
tags: coursera, mininet, networking, sdn, software, defined, networking, vm
<!-- prettier-ignore -->
---

## Mininet

Mininet is a network emulator written in Python. With it you can create a test
network consisting of many devices, for example inside your laptop. It's **a
lot** more light-weight compared to emulating switches/routers in GSN3.
Initially Mininet appears to be more about easily getting working network rather
than tinkering with all the features of devices, but OpenFlow has a lot of nifty
capabilities that Mininet makes it a lot easier to explore. Anyway I think it's
great that there are free software tools to learn how to setup the network.
Check out the link below, there are some
[assignments](https://github.com/mininet/mininet/wiki/Assignments "or if lazy click this link")
that are used at Stanford about how to create your own link state routing
protocol. Cool!

It's easy to set up a network with many switches, routers and hosts. You can
specify packet loss, queue size and delays on links.

[They](http://reproducingnetworkresearch.wordpress.com/ "reproducingnetworkresearch")
did some tests between ssh and
[mosh](http://mosh.mit.edu/ "http://mosh.mit.edu/"), to see how much better mush
was when there were packet loss or delays.

You could deploy a setup similar to what you've tested inmininet, with real
products. [OpenFlow](http://en.wikipedia.org/wiki/OpenFlow "on wikipedia") is
used in both mininet and in the real products :)

## Install the mininet VM and test it

There are
[many ways](https://github.com/mininet/mininet/blob/master/INSTALL "INSTALL on the github")
to install mininet. They provide a VM that you can boot or you can install it in
your OS, but it requires root access.

They got a [walkthrough](http://mininet.org/walkthrough/) that is quite a nice
intro to how to set things up mininet.

A note when using the VM image: If you're already running Linux, for example I
run Ubuntu on my machine all I had to do was to "ssh -X mininet@ip-to-vm" to be
able to run wireshark in the vm. That's a capital X.

## SDN -  software defined networking

Some sources of information:

[http://mininet.org/](http://mininet.org/) - The network emulator

[https://github.com/mininet/mininet/wiki/Documentation](https://github.com/mininet/mininet/wiki/Documentation) -
On the github there are assignments that you can use to learn more about
mininet.

[https://www.coursera.org/course/sdn](https://www.coursera.org/course/sdn) - On
Coursera there is a free introduction course to SDN starting May 27! I'm joining
it, are you?

[http://www.opennetsummit.org/archives-april2013/](http://www.opennetsummit.org/archives-april2013/) Free presentations about
SDN inside.

[http://tech.slashdot.org/story/13/04/29/2324200/inventor-of-openflow-sdn-admits-most-sdn-today-is-hype](http://tech.slashdot.org/story/13/04/29/2324200/inventor-of-openflow-sdn-admits-most-sdn-today-is-hype)
SDN is just a hype?
