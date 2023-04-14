---
title: "New Home Network Plan!"
date: 2020-07-05
categories: 
  - "it"
---

Changing apartment again so a pretty decent time to change the network at home.

Doing it a bit on the cheap this time around.

We'll get a docsis cable connection. Fortunately I have a modem used to connect to the same ISP from a previous apartment. Unfortunately the modem was a **_bit shit._** Or it used to reboot or need a reboot every now and then.

The plan is now to put the modem into **bridge mode** and move the brains into two other devices.

First device: A **Raspberry** Pi 3B with openwrt installed. It'll have an extra Realtek 8153 1Gbps USB port.

Internal NIC 100Mbps goes to LAN and will have DHCP Server. The external will have the WAN connection. The RPI 3b also has a WiFi, but it's only 2.4GHz so we'll only use that for local admin access.

Second device is a **[Cisco AP](https://www.guldmyr.com/blog/air-lap1142n-e-k9-to-autonomous-mode-adventure/)** that I blogged about not too long ago. That can do 5GHz :) This hasn't been used but I set it up so I can just plug it into an L2 with a DHCP and it should just work.

Will also use an unmanaged switch to connect stuff on the LAN.

One nice thing with the current apartment is the Ethernet in all rooms. New one might only have one cable TV/antenna port. Hoping for more. I'd rather not have to use some Ethernet over Power as there's also a media server to connect onto the LAN or wifi near the Chromecast.. sometimes it's nice to not throw everything away. Thought I had thrown away the cable modem too, but turns out I hadn't. New one is 180€ and used ones seems to go quite quickly on second hand marketplaces.

**Update0**: after move! All worked on the first power on - yay!

**Update1**: Not so yay - no WiFi reception one floor up as far as possible (15m?) from the AP. Hmmm. Maybe need to just put the AP in a more central spot.

**Update2**: Tried to move AP but no luck. Instead now took an unused Internet Gateway ( Huawei HG635) and turned it into bridge mode and set the same SSID and passwords. Had to delete the existing Ethernet connection first and set it to internet. Then found some unused Zyxel Powerline adapters and got the AP connected upstairs. Had to put the 'Internet' in one of the LAN ports. But handy, can use it as a switch for my desktop upstairs too. So far so good! Had issues with this Ethernet over Power; before in a previous apartment, where the connection would break every now and then.
