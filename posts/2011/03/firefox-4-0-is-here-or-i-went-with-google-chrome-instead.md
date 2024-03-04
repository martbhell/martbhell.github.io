---
title: Firefox 4.0 is here! - Or - I went with Google-Chrome instead
date: 2011-03-22
category: it
tags: chrome, firefox, firefox4.0, google, google, chrome, linux, red, hat, rhel6
<!-- prettier-ignore -->
---

Firefox download links:

**Windows** [http://releases.mozilla.org/pub/mozilla.org/firefox/releases/4.0/win32/en-US/Firefox%20Setup%204.0.exe](http://releases.mozilla.org/pub/mozilla.org/firefox/releases/)

**Linux** [http://releases.mozilla.org/pub/mozilla.org/firefox/releases/4.0/linux-i686/en-US/firefox-4.0.tar.bz2](http://releases.mozilla.org/pub/mozilla.org/firefox/releases/)

**Mac** [http://releases.mozilla.org/pub/mozilla.org/firefox/releases/4.0/mac/en-US/Firefox%204.0.dmg](http://releases.mozilla.org/pub/mozilla.org/firefox/releases/)

Going to test this as soon as I get home on My Windows machine.

On my RHEL6 laptop however I couldn't just unpack the linux version and run the ./firefox. I also couldn't find the installation guide. Nonetheless, it complains about this;

`./firefox-bin: error while loading shared libraries: libgtk-x11-2.0.so.0: cannot open shared object file: No such file or directory`

But `sudo yum install gtk2` gives:

> Package gtk2-2.18.9-4.el6.x86\_64 already installed and latest version.

And after a 'find /' I found the file here:

> cat ~/find.all | grep libgtk-x11-2.0.so.0 /usr/lib64/libgtk-x11-2.0.so.0.1800.9 /usr/lib64/libgtk-x11-2.0.so.0

How do I proceed? - Did not find anything online quick enough that would help me. The [other requirements](http://www.mozilla.com/en-US/firefox/system-requirements.html "firefox requirements") I could also find in my system.. I tried to run ./firefox-bin which complained about libxul.so which I also have in my system. I tried to run it in a sudo, no difference.

If anybody reads this and has some ideas or so - please let me know :)

...

So I tried **Google Chrome** instead (haven't tried this before) and wow, compared to Firefox 3.6.x which is the default one on RHEL6 it is really fast!

This is the link I used to install it and it worked perfectly:

[http://www.if-not-true-then-false.com/2010/install-google-chrome-with-yum-on-fedora-red-hat-rhel/](http://www.if-not-true-then-false.com/2010/install-google-chrome-with-yum-on-fedora-red-hat-rhel/)

1. Add this to _/etc/yum.repos.d/google.repo_

```bash
[google64]
name=Google - x86_64
baseurl=http://dl.google.com/linux/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
```

1. `yum install google-chrome-unstable`
2. start google-chrome with: google-chrome
