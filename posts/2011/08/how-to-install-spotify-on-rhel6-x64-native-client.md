---
title: How-To : Install Spotify on RHEL6 x64 native client
date: 2011-08-25
category: it
tags: red, hat, red, hat, enterprise, linux, rhel, spotify, spotify, for, linux

Hey!

You need premium for RHEL6 **native** client to work.

If you get it to work with WINE it would work for free (as a plus you get it with the very annoying ads).

My machine is a RHEL 6 64-bit.

The only requirement I had was that I did not have libQtWebKit.so.4 installed.

This was fixed with:

**sudo yum install qtwebkit-2.0-3.el6.x86\_64.rpm**

I found this package [online](http://rpm.pbone.net/index.php3/stat/4/idpl/15161517/dir/redhat_el_6/com/qtwebkit-2.0-3.el6.x86_64.rpm.html "link to get libQtWebKit.so.4"). It's needed because the spotify-install wants libQtWebKit.so.4 - this may be available in some other package available from within the red hat repositories but I couldn't find it. If you know how/where that would be great to know :)

I have qt 4.6.2-19 but adding the WebKit in this way hasn't caused any issues (yet).

You'll probably need other qt-stuff installed too (I did an ldd /usr/bin/spotify after install and what it wants you can find in this file: [spotify](http://www.guldmyr.com/wp-content/uploads/spotify.txt) ). There's a lot of them in there but libQtGui.so.4 , libQtCore.so.4 , libQtWebKit.so.4 , libQtDBus.so.4 , libQtNetwork.so.4 , libQtXml.so.4 are the libQt\* ones.

To find which qt packages you have installed in a Red Hat based system hit: **sudo yum list '\*qt\*'**

Download the spotify-client, I used spotify-client-qt\_0.5.2.84.g6d797eb-1\_amd64.deb. You can get the latest one via [http://repository.spotify.com/pool/non-free/s/spotify/](http://repository.spotify.com/pool/non-free/s/spotify/)

As spotify doesn't release an rpm anymore - you need to convert the debian .deb to rpm like this:

**sudo alien --to-rpm spotify-client-qt\_0.5.2.84.g6d797eb-1\_amd64.deb**

Then install spotify like this: **sudo yum install spotify-client-qt-0.5.rpm**

Run spotify (just hit spotify in the terminal) and log in!

Worked without changing any sound settings or anything like that! The volume control inside spotify controls the master volume, so be ware  and don't let it blow your ears out!

Happy musicing!

p.s.

I also tried to install spotify on a shell with WINE and load spotify with X11-forwarding enabled on the shell. Spotify loads and lets me log in but right after login it crashes for some reason.
