---
title: Installing Squid 3.2 on CentOS 5.3
date: 2011-04-20
category: it
tags: linux, proxy, shell, squid, squid, cache

Giving this one a shot :) I will be compiling it myself as well.

Squid for those who do not know is a [proxy server.](http://en.wikipedia.org/wiki/Proxy_server "on wiki") Proxys can be used for many things, but one great thing if you have a thinner connection to the Internet, you can use this to speed things up a bit. What it does is when you surf the web, the things you download are actually first downloaded to the proxy, and then your browser downloads it automagically from the proxy. If you afterwards browse to the same page the proxy should provide you with a cached copy and not re-download the whole page again.

### Downloading/compiling

It's a good idea to not run any service as root.

1. Download it from <http://www.squid-cache.org/> there are many options to chose from. Stable, unstable, 3.2, 3.1 etc. I just took a recent developer build from the 3.2 chain - squid-3.2.0.6.
2. Untar this somewhere, doesn't matter where. Move directory and:

To get the program to install itself in a location where you have access, you need to specify that while running the configure check.

You do this with:

./configure --prefix=/home/user/bin/squid-install

or wherever you want to put it. I just put it directly in /home/user/squid-inst.

If that completes without errors next step is to: make; make install. This will compile and then install it in the directory you specified above. After that completes sucessfully you can delete/hide the directory. I hide it just in case I want to change something in the configure or whatever.

### Then it's time to configure

Now proxy servers you need to put some kind of authentication on. Unless you want a hoard of unwanted visitors.

There are a gazillion of different settings in the squid.conf.documented.

Configuration is done via ~/squid-inst/etc/squid.conf

`cache_dir ufs /usr/local/squid/cache 100 16 256` The value 100 denotes 100MB cache size. This can be adjusted to the required size. `http_port 3128` This is the port you will be connecting to. Make sure you do not set one that other services on the machine uses. Might be a good idea to use a non-standard as well, to prevent some from "stumbling" onto it and trying to brute-force it.

### Starting squid

1. create cache directories with ~/squid-inst/sbin/squid -z
2. run it in debug ~/squid-inst/sbin/squid -NCd1

If everything is working fine, then your console displays: "Ready to serve requests".

You can now surf to your <http://host:port>

However, you cannot use it as a cache yet.

You need to set up the http\_access part. The ACL - access list.

This can be complicated.

See here for some examples of that: [http://wiki.squid-cache.org/SquidFaq/SquidAcl](http://wiki.squid-cache.org/SquidFaq/SquidAcl "squidacl")

However, all you "need" is as below. First, find out your IP-address. Let's say it's **12.24.48.96** for the fun of it. You can see what it is by surfing to [www.ripe.net](http://www.ripe.net "whatismyip")

add this somewhere on top near the other "acl" entries:

`acl me src 12.24.48.0/24`

Then a bit further down

`http_access allow me`

Now if you want to you can be more tight with the security, and you probably should. The setting above means that everybody on that subnet can use your proxy server. For example you might want to change it to only your IP - if you have a static one.

`acl me src 12.24.48.96/32`

If you change something in the configuration, you can do this to stop squid:

`~/squid-inst/sbin/squid -k kill`

`~/squid-inst/sbin/squid &`

is used to start it in a daemon mode (keeps running after you log off your shell).

There are other ways to set up password checks (used to be with .htpasswd) but I have no need for this today. I'll have a look into it some other day :) Also this proxy is transparent - meaning if you connect somewhere, people can see that you are indeed connecting through a proxy.

But first you need to set your browser to use the proxy, you do this under network settings.

Happy proxying!
