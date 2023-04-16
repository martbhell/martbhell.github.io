---
title: Home Network Convergence
date: 2019-07-14
category: it
tags: chromecast, dnsmasq, hostapd, linux, media, server, openwrt, raspberry, pi, virtual, lan, wi, fi, wireless, access, point

Finally got around to sorting out an issue which basically was that the TV+Chromecast near the TV was on another network than the media server and thus I couldn't stream videos by using my phone.

I've been thinking lately and in previous posts that maybe I should just get an access point and plug it in a port in the correct VLAN near the TV, as mentioned in a previous posts in https://www.guldmyr.com/vlan-in-the-home-network/ or https://www.guldmyr.com/some-updates-to-the-home-network/

But then the other day I started looking at maybe the raspberry Pi I have as a media player could be turned into an access point? (some googling suggest it could be done, but several talk about basic linux install with hostapd and dnsmasq which maybe openwrt would be more fun).

Then I realized that I already have an access point over there which is what phones and the chromecast is connected to and I don't want a third wifi network at home!

Finally the solution is to get the media server onto the same network as the chromecast. This I could now after the VLAN changes do quite easily.

Steps: - take the desktop's cable and put it in a dumb 1GbE switch I had unused - new cable from my desktop's system board NIC to go same a switch - at this point ssh into media server from internet (because it has no monitor/keyboard) - add usb NIC to the media server and connect to the switch - setup static NIC without default gw etc - update firewalls

Things learnt: - the USB NIC got a funny and long interface name when I plugged it in. On next reboot it got eth0. So the network interface config I wrote initially didn't really work anymore :)

Feels good to not have to this this old and unmaintained media player on the raspberry pi anymore. The android app I use even supports EAC3!

Next I'm wondering what to do with that raspberry pi! retropie maybe?
