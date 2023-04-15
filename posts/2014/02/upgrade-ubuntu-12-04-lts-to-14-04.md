---
title: "Upgrade Ubuntu 12.04 LTS to 14.04"
date: 2014-02-03
category: it
tags: 12, 04, 14, 04, dist, upgrade, lts, ubuntu, upgrade

Yesterday I upgraded Ubuntu 12.04 LTS to 14.04 devel release. This is not recommended :)

I wonder what will happen when 14.04 real is out.. \*update: it is out now, so the "-d" in "update-manager -d" is no longer necessary?

How to? Just run "update-manager -d" and click on some buttons!

Update process was nice, I like apt-get over yum when it sees a conflicting file it doesn't just overwrite or write the file as .rpmsave  but instead it displays see the difference(s) between the two files and you get to decide what to do!

One issue I have heard about is VMWare Workstation 10.0.1 on 14.04 and recompiling kernel modules. Patching instructions in here: http://dandar3.blogspot.cz/ and patch file is the one at the bottom of this post https://communities.vmware.com/message/2326986
