---
title: haproxy lab setup!
date: 2017-08-07
category: it
tags: ansible, haproxy, openstack
<!-- prettier-ignore -->
---

Been seeing haproxy more and more lately as it seems even the stuff I work with
are moving towards web :)

So a good time as any to play around with it!

First setup is the tag "single-node"
in [https://github.com/martbhell/haproxy-lab](https://github.com/martbhell/haproxy-lab) -
this means it just configures one apache httpd and one haproxy. In the haproxy
it creates multiple vhosts with content being served from different directories,
and then it points to each of these as a haproxy backend.

To illustrate the load balancing the playbook also installs php and shows the
path of the file that's being served.

I used ansible for this and only tested it with CentOS7 in an OpenStack. The
playbook also sets up some "dns" in /etc/hosts.

There are also "ops_playbooks" for disabling/enabling backends and setting
weights.

I wonder what's a good next step. Maybe multiple hosts / Docker containers?
Maybe SSL termination + letsencrypt? Maybe some
[performance benchmarking/tuning](https://medium.freecodecamp.org/how-we-fine-tuned-haproxy-to-achieve-2-000-000-concurrent-ssl-connections-d017e61a4d27)?
I like the help for
the [configuration file](http://www.haproxy.org/download/1.5/doc/configuration.txt)
\- it begins with some detail about what an HTTP request looks like :)
