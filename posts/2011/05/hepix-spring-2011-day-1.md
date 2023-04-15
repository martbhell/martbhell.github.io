---
title: "HEPIX Spring 2011 - Day 1"
date: 2011-05-02
category: it, storage
tags: activemq, batch, system, cern, cisco, routers, conference, fermilab, frankfurt, gsi, hard, drive, failures, hepix, hepix, spring, 2011, hp, it, 2, kit, lustre, nikhef, pue, super, computing, supermicro, tty, hack

Morning. Got in last night at around 2140 local time. I should've done a little more exact research for how to find my hotel. Had to walk some 30 minutes (parts of it the wrong way) to get to it. But at least I made it to see some ice hockey.. . to bad Detroit lost.

Today's another day though!

First stop: breakfast.

Wow. What a day, and it's not over yet! So much cool stuff talked about.

### Site Reports

The first half of the day was site reports from various places.

GSI here in Darmstadt (which is where some of the heaviest elements have been discovered). They have started an initiative to keep [Lustre](http://lustre.org "lustre.org") alive - as apparently Oracle is only going to develop this for their own services and hardware. They are running some SM - [SuperMicro](http://supermicro.com "supermicro.com") servers that have infiniband on board - and not like the HP ones I've seen that has the [mellanox](http://mellanox.com ".com") card as an additional mezzanine card. Nice. They were also running some really cool water cooling racks that uses the pressure in some way to push the hot air out of the racks. They found that their SM file servers had much stronger fans at the back, and not optimized airflow inside the servers so they had to tape over some (holes?) over the PCI slots on the back of the server to make it work properly for them. They were also running the servers in around 30C - altogether they got a [PUE](http://en.wikipedia.org/wiki/Power_usage_effectiveness "PUE on Wikipedia") of around 1.1 which is quite impressive.

Other reports: [Fermilab](http://fnal.gov "fermilab") (loots of storage, their Enstore has for example 26PB of data on tape), KIT, Nikhef (moved to ManageEngine for patch and OS deployment, and Brocade for IP routers), CERN (lots of hard drives had to be replaced.. around 7000.. what vendor? HP, Dell, SM?), DESY (replaced Cisco routers with Juniper for better performance, RAL (problem with LSI controllers, replaced with adaptec), SLAC (FUDForum for communication).

 

Rest of the day was about:

### Messaging

Some talk about messaging - for signing and encrypting messages. Could be used for sending commands to servers but also for other stuff. I've seen [ActiveMQ](http://activemq.apache.org/ "ActiveMQ") in EyeOS and it's also elsewhere as well. Sounds quite nice but apparently not many use it, instead they use ssh scripts to run things like that.

### Security

About various threats that are public in the news lately and also presentation of some rootkits and a nice demo of a TTY hack. Basically the last one consists of one client/linux computer that has been taken hacked, then from this computer a person with access to a server sshs there. And then the TTY hack kicks in and gives the hacker access to the remote host. Not easy to defend against.

There was also a lengthier (longest of the day) 1h-1.5h presentation of a French site that went through how they went ahead when replacing their home-grown Batch management system with [SGE](http://en.wikipedia.org/wiki/Oracle_Grid_Engine "OGE on wikipedia")(now Oracle Grid Engine).

\*\*\* Updated the post with links to some of the things. Maybe the TTY hack has another name that's more public.

Next Days:

[Day 5](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-5/ "day5") [Day 4](http://www.guldmyr.com/blog/hepix-spring-2011-day-4/ "day4") [Day 3](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-3/ "day3") [Day 2](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-2/ "day2")
