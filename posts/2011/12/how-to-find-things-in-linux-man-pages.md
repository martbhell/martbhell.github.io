---
title: "How to find things in Linux man pages"
date: "2011-12-20"
categories: 
  - "it"
tags: 
  - "apropos"
  - "grep"
  - "help"
  - "linux"
  - "man"
  - "man-pages"
  - "manual"
  - "red-hat"
  - "rhel"
  - "search"
  - "xargs"
  - "yum"
  - "zgrep"
---

There's a couple of places (naturally).

It's easy to be fooled and think: "anybody can type man man". But in all fairness, you need to figure out which man page to look into, or what command to run and sometimes it's just a blank.

In RHEL there is /usr/share/doc where there are some special places, for example /usr/share/doc/initscripts\*/sysconfig.txt for all config files that relate to the boot-up process. There is also /usr/share/man. In /usr/share/man/man5 which has all the level 5 man pages in gzip format. For example "man 5 yum.conf" you can find in /usr/share/man/man5/yum.conf.5.gz.

To open a man page you just type 'man yum'. To get the man page for yum, or 'man man' for the manual for man.

To search through man-pages you can use either of these (they are the same):

man -k yum
apropos yum

While inside a man-page you can search by typing: / and then what you want to search for and then ENTER. Like this: /priority This will hilight all the matched entries, you move to the next match with 'n'. This might differ between operating systems, it depends on which viewer is used to present the man page.

Sometimes these don't find what you are looking for. In that case you could manually move into /usr/share/man/man5 and hit:

zgrep priority \*

to grep through the gzip files looking for any entries that says 'priority'.

or, if you want to you could use this to search through all directories:

find . -name "\*"|xargs zgrep -i priority

or even better (if you're not looking for a language specific man page):

find /usr/share/man\* -name "\*"|xargs zgrep -i gpgcheck

These are all relatively slow though, if you read this and have any suggestions please let me know :)
