---
title: RHEL and web-server
date: 2011-02-28
category: it
tags: firewall, guide, http, httpd, iptables, port, port, 80, rhel, ssh, sshd

Another thing you will notice if you are used to debian is that RHEL has iptables enabled by default.

To alter it you use the 'iptables' command. It is quite complex and there are good guides out there.

If you just want to let http and ssh through you can run this:

**iptables -I RH-Firewall-1-INPUT 3 -p tcp -m tcp --dport 80 --tcp-flags SYN,RST,ACK SYN -j ACCEPT** **iptables -I RH-Firewall-1-INPUT 3 -p tcp -m tcp --dport 22 --tcp-flags SYN,RST,ACK SYN -j ACCEPT**

You do not have to change anything in httpd (made by apache by the way) to enable it. Just point your browser. The document root is by default: /var/www/html
