---
title: linux.conf.au.2016 and a FreeIPA workshop
date: 2016-03-31
category: it
tags: redhat, rh414, rhce, vagrant, virtualbox

[https://github.com/freeipa/freeipa-workshop](https://github.com/freeipa/freeipa-workshop)

In preparation for the RH414 course I'm taking next week I think I should have a look at kerberos, freeipa and bind a bit :)

During linux.conf.au.2016 there was a [workshop](https://linux.conf.au/schedule/30130/view_talk) on FreeIPA. (There were many other interesting talks there, for example the [Network Performance Tuning](http://jbainbri.github.io/) by Jamie Bainbridge).

There is a video to accompany it: [https://www.youtube.com/watch?v=VLhNcirKFDs](https://www.youtube.com/watch?v=VLhNcirKFDs)

## Notes

- Bonus feature: get acquainted with vagrant too!

Vagrant 1.7.4 and Virtualbox 5.0 works just fine together (except I had some issues with network interfaces on Ubuntu 15.10 and Virtualbox 5 and Vagrant - the MAC addresses were the same on the VM's interfaces to the "NAT" network- they also got some weird IP addresses there). I could only find that IP used in resolv.conf (from the dhcp) - so that could be changed.
