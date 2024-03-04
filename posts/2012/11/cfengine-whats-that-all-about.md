---
title: cfengine - what's that about?
date: 2012-11-03
category: it
tags: cfengine, cluster, clustering, cms, configuration, management, software
<!-- prettier-ignore -->
---

[http://cfengine.com/what-is-cfengine](http://cfengine.com/what-is-cfengine "http://cfengine.com/what-is-cfengine")

It's a (old) software that is used to make sure that (for example) the same
config files are used on all machines. There are several other CMSs, for example
[puppet.](http://puppetlabs.com/ "puppetlabs.com") Wikipedia has a nice
[overview](http://en.wikipedia.org/wiki/Comparison_of_open_source_configuration_management_software#Basic_properties)
of them.

Let's use the
[lustre](https://www.guldmyr.com/setup-a-3-node-lustre-filesystem/ "Setup a 3 Node Lustre Filesystem")
  machines we set up in a previous post.

On cfengine.com there are many examples too.

Inside a policy you have a promise.

### Install

Installing on an RPM-based distribution is easy, cfengine has their own
repository where the community edition is available.

[http://cfengine.com/cfengine-linux-distros](http://cfengine.com/cfengine-linux-distros "http://cfengine.com/cfengine-linux-distros")

Get the gpg-key, import it, set up the repository-file and install
"cfengine-community".

Check if "cfengine3" is set to start on boot.

### Test

A small example how to write a promise.

- "cf-promise -f " can be used to test that a promise is valid (syntax and more
  is OK)
- "cf-agent -f" run the promise, so if we use the example in the link above it
  echoes a Hello World.

### Client/Server

Client pulls policies from the server.

policy-server: mds - 192.168.0.2 client1: client1 - 192.168.0.4 client2: oss1 -
192.168.0.3

on the policy-server hit: "/var/cfengine/bin/cf-agent --bootstrap
--policy-server 192.168.0.2"

open port 5308 on the policy-server.

After you see "-> Bootstrap to 192.168.0.2 completed successfully" you can run
the same cf-agent command on the client. This points it to use 192.168.0.2 as
the policy-server.

No need to open port on the clients.

On the policy-server add this to /var/cfengine/masterfiles/cftest1.cf:

bundle agent test { files: "/tmp/cf_test_file" comment => "Promise that a plain
file exists with stated permissions", perms => mog("644", "root", "sys"), create
=> "true"; }

Then in /var/cfengine/masterfiles/promises.cf you can't follow the guide
verbatim, the promises.cf needs to look like this (really important to have ", "
as a separator between the bundles, notice the space after the ",".

body common control { bundlesequence => { "main", "test" }; inputs => {
"cfengine_stdlib.cf", "cftest1.cf", }; version => "Community Promises.cf 1.0.0";
}

After that you can run "cf-agent -Kv" on the client, and it will do what is
promised in the cftest1.cf file!

Try to change ownership/permissions on the file, in a while it will have been
changed back :)

In /var/cfengine/promise_summary.log you'll see if it couldn't keep a promise
and if it corrected the mistake.

### Distribute it

And to get oss1 the same file. Just run the good old "/var/cfengine/bin/cf-agent
--bootstrap --policy-server 192.168.0.2" on it and eventually that file /tmp
will pop up in there too. Nice!

### Some useful stuff

I'll probably try out some more useful things in the near future.

Streamline resolv.conf settings, ip routes, config files for software like to
make sure /etc/dcache/dcache.conf is the same on all pool servers or why not a
kind of user database? Like for /etc/passwd? Check out the solutions on
cfengine.com!
