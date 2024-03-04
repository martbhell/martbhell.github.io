---
title: Asus Eee Pad Transformer TF 101 + root + arch in chroot
date: 2012-09-05
category: it
tags: android, arch, asus, asus, eee, pad, asus, transformer, chroot, linux, tf101
<!-- prettier-ignore -->
---

Just got one of these - thought it would be a great tool when going to
[conferences](https://www.guldmyr.com/brocade-analyst-and-technology-day-2012/ "Like Brocade Analyst and Technology Day 2012 for example")
for example or somewhere where I would need a small computer but don't want to
bring a long my normal heavy laptop.

Normally I prefer pen and paper when going to meetings or conferences, but if
there's a lot of information needed to be written down or if I want to check
something online it sounds quite nice.

Got a keyboard with it too. The stuff I've wanted do to so far works perfectly
and it is very nice to play around with - though I haven't done any serious work
or task for any longer period of time yet. If I can do that without any/much
issues I will be very happy about it.

[Rooted](http://forum.xda-developers.com/showthread.php?t=1689193 "link to xda-developers.com")
it without any problems (from a Windows 7 x64 PC). Needed to install the USB
drivers from
[Asus's page](http://www.asus.com/Eee/Eee_Pad/Eee_Pad_Transformer_TF101/#download "asus.com")
-  (choose OS android).

It would also be nice to have a
[Linux chroot terminal running inside Android](http://lrvick.net/arch_linux_terminals_in_android/ "on lrvick.net").
This tutorial works pretty great - at least to get a basic setup :) Still need
to play some more with it to get things working (vpn perhaps?). After you got
the sshd running on the android you can connect to localhost with an ssh client,
for example irssi connectbot. In there you run the commands outlined in the last
link.

After you create a user you need to add the user to
[the appropriate group](http://android-dls.com/wiki/index.php?title=Android_UIDs_and_GIDs "on android-dls.com").
At least if you want network access. What was strange was that if my user was in
only aid_inet I could ssh and irssi to an IP-address, but I could not ping said
address. Neither could I ping or ssh to a dns-name. After adding group
aid_net_raw and your user to that group that was possible.

After that you can use 'pacman -S irssi' to install for example irssi!

Happy transformer arching!
