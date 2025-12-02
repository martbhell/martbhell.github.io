---
title: EMC - Symmetrix and CLARiiON - 2
date: 2011-01-15
category: storage
tags: emc, finland, hp, storage
<!-- prettier-ignore -->
---

So we reserved two green old chairs. Just might need a nut and a metal plate for a bolt that's missing one then they'll
do nicely!

\*\*\*

Also been reading up on the CLARiiON now so far as to what I've found.

Hardware base is quite similar to the EVAs with the backend loops, CTS on the CX4 and loop io modules on the CX3. With a
max of 120 disks per loop. The number in the naming of the CX4 (maybe the others too) is that the number is max amount
of disks. CX4-960 is 960 disks and 8 loops (120 per loop then?). Loop pairs I hope.

Turns out Dell are selling these.

Hot sparing is used and a raid group is like an EVA disk group. Quite similar to the way HP's XP is creating the parity
groups. Navisphere for management on the CLARiiON and System Management Console on the Symmetrix.

Interesting stuff this is!

Symmetrix is high end and CLARiiON is mid range.

So Symmetrix has even more similarities to the XP. For example the blades with the directors(host ports, device ports,
disks, memory, cache) and assemblies.

Both appears to have more ways of configuring it than the EVA - the admin interface looks more complex anyway and you
can tune the cache which is neat ;)

<http://en.wikipedia.org/wiki/EMC\_Symmetrix> <http://en.wikipedia.org/wiki/EMC\_Clariion>

Both of these are quite extensive but especially the Symmetrix article looks **a lot** like an advertisement.
