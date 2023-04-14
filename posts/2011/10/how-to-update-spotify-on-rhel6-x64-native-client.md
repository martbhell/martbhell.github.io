---
title: "How-To : Update Spotify on RHEL6 x64 native client"
date: 2011-10-14
category: it
tags: red, hat, red, hat, enterprise, linux, rhel, spotify, spotify, for, linux

See [the post](http://www.guldmyr.com/blog/how-to-install-spotify-on-rhel6-x64-native-client/ "how-to-install-spotify-on-rhel6-x64-native-client/") for how to install spotify on a Linux Client (RHEL 6 x64 in my case).

This post is for how to upgrade.

2012-02-01: Updated, added --nodeps to the rpm upgrade. 2013-01-08: This has been confirmed to work with spotify-0.8.8, updated typo in symlink part.

Why? http://repository.spotify.com/pool/non-free/s/spotify/spotify-client-qt\_0.6.1.309.gb871a7d-1\_amd64.deb is out!

Is available. Maybe right-click works?? =)

1. Get the .deb into a place where you can run the program 'alien'. I have ubuntu in a virtual machine so fired that up, downloaded the .deb
2. sudo alien --to-rpm spotify-client-qt\_0.6.1.309.gb871a7d-1\_amd64.deb
3. e-mailed spotify-client-qt-0.6.1.309.gb871a7d-2.x86\_64.rpm to myself
4. save the .rpm, close spotify,  and hit:
5. sudo rpm -Uvh spotify-client-qt-0.6.1.309.gb871a7d-2.x86\_64.rpm
6. this failed, it needed

error: Failed dependencies: _libcrypto.so.0.9.8()(64bit) is needed by spotify-client-qt-0.6.1.309.gb871a7d-2.x86\_64 libcrypto.so.0.9.8(OPENSSL\_0.9.8)(64bit) is needed by spotify-client-qt-0.6.1.309.gb871a7d-2.x86\_64 libssl.so.0.9.8()(64bit) is needed by spotify-client-qt-0.6.1.309.gb871a7d-2.x86\_64 libssl.so.0.9.8(OPENSSL\_0.9.8)(64bit) is needed by spotify-client-qt-0.6.1.309.gb871a7d-2.x86\_64_

[A forum post with some more details about this](http://forums.fedoraforum.org/showthread.php?t=270230 "on fedoraforum.org").

_whereis spotify ldd /usr/bin/spotify gives me: libssl.so.10 0> /usr/lib64/libssl.so.10 libcrypto.so.10 0> /usr/lib64/libcrypto.so.10_

hit:

cd /usr/lib64 

sudo ln -s libcrypto.so.10 libcrypto.so.0.9.8 sudo ln -s libssl.so.10 libssl.so.0.9.8

If still no go, some advise to rename/delete ~/.config/spotify and ~/.cache/spotify

If neither of the above still works, run

 

rpm -Uvh --nodeps spotify-client-qt-0.6.6.10.gbd39032.58-2.x86\_64.rpm

It's now possible to right-click on playlists! Also to click on 'File' works! Woop!

Right-click on artist worked a few times. Then after a while it stopped working. AGREGHA!!#45

_(still crashes with Spotify 0.6.6.10)_

I would guess that the problem lies with qt or webkit.

Sharing works though. It sucks a bit to not be able to add files to playlists. But clicking the star works so you can find the songs you don't want to forget in there. Scrobble/last.fm also works. Cannot select top list for another country.
