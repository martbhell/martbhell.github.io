---
title: rtmpdump and ssh tunnel / socks proxy
date: 2011-12-29
category: it
tags: flash, video, linux, rtmpdump, rtmpe, ssh, tunnel
<!-- prettier-ignore -->
---

You can use rtmpdump on linux to download videos from a page that uses rtmpe /
flash to display the videos. If you want to, you can also run an ssh tunnel.
This could be used with benefit if you want to watch videos from a web site that
you can't because they're restricting access to it based on IP addresses.

1\. yum install rtmpdump (apt-get install rtmpdump i ubuntu) 2. ssh -D 2001
server-med-sshd 3. rtmpdump -S localhost:2001 -r rtmpe://address.to.mp4 -o
/tmp/fil1.mp4

rtmpe doesn't work with normal http proxy because it doesn't use the web
browser's proxy settings. It also operates on port 1935, 443 and lastly it tries
on port 80 if I googled right.

A VPN might be possible to use, but does that only work if you send all traffic
through the VPN?

This tool should work on Windows as well.
