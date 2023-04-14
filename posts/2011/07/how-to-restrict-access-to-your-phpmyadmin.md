---
title: "How to restrict access to your phpmyadmin"
date: 2011-07-27
category: it
tags: apache, hardening, linux, phpmyadmin, security, ubuntu, vm

Went through the apache logs on my web-server and saw some access requests to my phpmyadmin page.

It's probably a good idea to restrict access to this web based sql admin interface (in case there is an exploit I don't want somebody to use it on this).

## How to make phpmyadmin a bit more secure

sudo vi /etc/phpmyadmin/apache.conf or sudo nano /etc/phpmyadmin/apache.conf

Under **"Alias /phpmyadmin /usr/share/phpmyadmin" <Directory /usr/share/phpmyadmin> add this:**

Order Deny,Allow Deny from all Allow from 127.0.0.1 Allow from 192.168.0.0/24

\---

This will let your vm access the /phpmyadmin part and also anything with an IP on the 192.168.0.0/24 network.

Also, up there in the alias where it first says /phpmyadmin - change this to something else like **"Alias /youcannotguessthis /usr/share/phpmyadmin"** and it will be a lot harder for automatic scanners to find it.

[Here is some more information.](http://httpd.apache.org/docs/2.2/howto/access.html "on apache.org")
