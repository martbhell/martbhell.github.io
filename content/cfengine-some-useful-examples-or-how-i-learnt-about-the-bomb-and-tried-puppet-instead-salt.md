---
title: "cfengine - some useful examples / or how I learn't about the bomb and tried Puppet instead / salt?"
date: 2012-11-11
categories: 
  - "it"
tags: 
  - "automation"
  - "cfe"
  - "cfengine"
  - "cms"
  - "linux"
  - "puppet"
  - "resolv-conf"
  - "resolver"
  - "salt"
  - "salt-highstate"
  - "script"
  - "scripting"
---

Building on the [initial post](http://www.guldmyr.com/blog/cfengine-whats-that-all-about/ "cfengine – what’s that about?") about cfengine we're going to try out some things that may actually be useful.

My goal would be to make /etc/resolv.conf identical between all the machines.

The server setup is the lustre cluster we built in a previous post.

In this post you'll first see two attempts at getting cfengine and then puppet to do my bidding until success was finally accomplished with [salt](http://www.guldmyr.com/blog/cfengine-some-useful-examples-or-how-i-learnt-about-the-bomb-and-tried-puppet-instead-salt/#salt).

# Cfengine

Set up name resolution to be identical on all machines.

http://blog.normation.com/2011/03/21/why-we-use-cfengine-file-editing/

Thought about

Make oss1 and client1 not get the same promises.

Perhaps some kind of rule / IF-statement in the promise?

Cfengine feels archaic. Think editing named/bind configs are complicated? They are not even close to setting up basic promises in cfengine.

# Puppet ->

http://puppetlabs.com/

http://www.how2centos.com/centos-6-puppet-install/

vi /etc/yum.repos.d/puppet.repo
pdcp -w oss1,client1 /etc/yum.repos.d/puppet.repo /etc/yum.repos.d/puppet.repo

Sign certificates:

puppet cert list
puppet cert sign 
sudo puppet cert sign --all

For puppet there's a dashboard. This sounds interesting. Perhaps I won't have to write these .pp files which at a glancelooks scarily similar to the cfengine promises.

yum install puppet-dashboard mysqld

service start mysqld

set mysqld password

create databases (as in the database.yml file)

after this I didn't get much further... But I did get the web-server up. Although it was quite empty...

# salt

[Easy startup instructions](http://docs.saltstack.org/en/latest/topics/installation/fedora.html "http://docs.saltstack.org/en/latest/topics/installation/fedora.html") here for getting a parallel shell going:

After it's set up you can run a bunch of built-in special commands, see the [help section about modules](http://docs.saltstack.com/en/latest/#salt-in-depth "http://docs.saltstack.com/en/latest/#salt-in-depth").

salt '\*' sys.doc|less

will give you all the available modules you use :)

Want to use it for configuration management too? Check out the '[states](http://docs.saltstack.org/en/latest/topics/tutorials/starting_states.html "http://docs.saltstack.org/en/latest/topics/tutorials/starting_states.html")' section.

What looks bad with salt is that it's a quite new ([first release in 2011](http://en.wikipedia.org/wiki/Comparison_of_open_source_configuration_management_software#cite_note-43 "http://en.wikipedia.org/wiki/Comparison_of_open_source_configuration_management_software#cite_note-43"))

_Salt is a very common word so it makes googling hard. Most hits tend to be about cryptography or cooking._

To distribute (once) the resolv.conf do you run this on the admin-server: salt-cp '\*' /etc/resolv.conf /etc/resolv.conf

On to [states](http://docs.saltstack.org/en/latest/topics/tutorials/states_pt1.html "http://docs.saltstack.org/en/latest/topics/tutorials/states_pt1.html") to make sure that the resolv.conf stays the same:

1. uncomment the defaults in the master-file about file\_roots and restart the salt-master service
2. create /srv/salt and ln -s /etc/resolv.conf /srv/salt/resolv.conf
3. create a /srv/salt/top.sls and a /srv/salt/resolver.sls

 

In top.sls put:

base:
 '\*':
   - resolver

In resolver.sls put:

/etc/resolv.conf:
 file:
  - managed
  - source: salt://resolv.conf

Then run: salt '\*' salt.highstate

How to get this to run every now and then? Setting up a cronjob works.

Haven't been able to find a built-in function to accomplish this but then again, all I'm doing here is scratching at the surface so it's working and I'm happy :)
