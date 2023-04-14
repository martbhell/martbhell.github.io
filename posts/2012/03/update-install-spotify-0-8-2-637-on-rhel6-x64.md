---
title: "Update / Install Spotify 0.8.2.637 on RHEL6 x64"
date: 2012-03-26
category: it
tags: 0, 8, 2, 637, alien, qt, red, hat, rhel, spotify, ubuntu

Previous post:

[http://www.guldmyr.com/blog/how-to-update-spotify-on-rhel6-x64-native-client/](http://www.guldmyr.com/blog/how-to-update-spotify-on-rhel6-x64-native-client/ "http://www.guldmyr.com/blog/how-to-update-spotify-on-rhel6-x64-native-client/")

Installed spotify-client-0.8.2.637.g252b980.486-2.x86\_64.rpm - this is converted from the .deb package that is downloaded from: [http://repository.spotify.com/pool/non-free/s/spotify/](http://repository.spotify.com/pool/non-free/s/spotify/ "http://repository.spotify.com/pool/non-free/s/spotify/")

you convert with 'alien' and this command:

alien --to-rpm spotify-client\_0.8.2.637.g252b980.486-1\_amd64.deb

To install you need to uninstall first:

rpm -ev spotify-client
rpm -ivh Downloads/Spotify/spotify-client-0.8.2.637.g252b980.486-2.x86\_64.rpm
error: Failed dependencies:
libcef.so()(64bit) is needed by spotify-client-0.8.2.637.g252b980.486-2.x86\_64
libcrypto.so.0.9.8()(64bit) is needed by spotify-client-0.8.2.637.g252b980.486-2.x86\_64
libcrypto.so.0.9.8(OPENSSL\_0.9.8)(64bit) is needed by spotify-client-0.8.2.637.g252b980.486-2.x86\_
libssl.so.0.9.8()(64bit) is needed by spotify-client-0.8.2.637.g252b980.486-2.x86\_64
libssl.so.0.9.8(OPENSSL\_0.9.8)(64bit) is needed by spotify-client-0.8.2.637.g252b980.486-2.x86\_64

OK, that didn't work so well.

Install:

\# rpm -ivh --nodeps Downloads/Spotify/spotify-client-0.8.2.637.g252b980.486-2.x
Preparing...                ########################################### \[100%\]
   1:spotify-client         ########################################### \[100%\]

You'll get errors while trying to start spotify:

spotify 
spotify: error while loading shared libraries: libnss3.so.1d: cannot open shared object file: No such file

What you need to do is create symlinks:

ln -s /usr/lib64/libnss3.so /usr/lib64/libnss3.so.1d
ln -s /usr/lib64/libnssutil3.so /usr/lib64/libnssutil3.so.1d
ln -s /usr/lib64/libsmime3.so /usr/lib64/libsmime3.so.1d
yum -y install nspr nspr-devel
ln -s /usr/lib64/libplc4.so /usr/lib64/libplc4.so.0d
ln -s /usr/lib64/libnspr4.so /usr/lib64/libnspr4.so.0d

However, it still crashes when I try to right-click on an app - but now it has apps :)
