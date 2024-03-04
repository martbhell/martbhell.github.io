---
title: Some updates to the home network 1/2
date: 2019-05-15
category: it
tags: cable, modem, home, network, isp, nat, network, ps3, raspberry, pi, server, computing, vlan, wi, fi, wifi
<!-- prettier-ignore -->
---

Current layout:

![Before](images/home-net-current-20190504-1.jpg)

- The corner:
  - Cable MODEM NAT&WiFi ISP A
  - One server
  - One desktop who should be on both networks, default gw on one
  - Phones and tablets wifi
- TV Area:
  - DSL Modem NAT&WiFi ISP B
  - One raspberry pi connected to the server
  - Phones and tablets wifi
  - One chromecast, would be nice to have connected to the server too
  - One ps3
- 20m, a microwave, and walls in between the two areas (and most importantly the
  server and the raspberry pi) so wifi is spotty.

Most import factor: **One long ass 30m UTP cable connecting the raspberry pi to
the same network as the server**

It would be cool to: **A)** be able to connect the desktop to the modem out by
the TV and **B)** Get the chromecast (WIFI only) onto the same network as the
server, perhaps with an AP for ISP A network near the TV area

Stay tuned for another post in the hopefully near future when I've got something
working to help with A/B :)

Update : another graphical representation of the networks:

![Before-with-colors](https://lh5.googleusercontent.com/aUuKseUdXT87v4A5lfBYPcyAykhygf2_5MJGveTSKEvzgmOh509-6_NA2gALnRQ5YEXAQqNp4Sh2_PLcrYEyh3LVVemDXLXwFFDBAz3-ii-n7drfh5TezQd9Y7GF131WFnKFYN-M)
