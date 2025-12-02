---
title: RHCSA – Rapid Track – Day 3
date: 2011-12-14
category: it
tags: book, certification, kickstart, linux, luks, red, hat, review, rhcsa, selinux, storage, studying
<!-- prettier-ignore -->
---

Wow, what a day!

### Some great stuff today

It ended with configuring a kickstart file, starting an unattended installation via PXE by referring to said kickstart
file on an http-server.

Before that we were playing with partitioning, making swap, encrypting with cryptsetup and LUKS. Also very interesting.

After we learned about partitioning we did changing booting kernel parameters, resetting root password, editing grub,
loading modules, setting module specific parameters etc.

And we started the day with SELinux. Very interesting, a lot of opinion about that in the room but honestly I can see
that SELinux is extremely useful and doesn't cause much harm on a desktop. Especially one where you don't run any
services. Also, there's so often 0-day exploits for various net-services that running SELinux can't be bad, right?
There's probably lots of other stuff you can do to do hardening in a Linux system.

Teacher did not mention chcon at all, only restorecon.

### More thoughts

This RHCSA course do assume that you know a bit. For example it assumes that you know scripting, we're not going through
that at all. Using vi, less, are also assumed. Parsing, grepping etc. There are people struggling keeping up in class.

[Going through all the objectives](https://www.guldmyr.com/rhcsa-preparation/ "Red Hat Certification – RHCSA – Preparation")
before attending is a great idea. It gives you some breathing room while doing the exercises in class and if you have
stumbled upon and questions while you were experimenting yourself - you have a great opportunity to ask these in class.
Another good thing with this is probably that it makes you faster at doing the task. If you can reset the root password
on a VM in 60 seconds, instead of 300s - because you're wondering about what commands to run, what parameters to send
and how to send them, etc, that'll save you a lot of time.

### Mini Book Review

But even that is not enough, you really need to be experienced with Linux before. How to use the CLI and things like
that. There are some good books around. Such as the book
[UNIX and Linux System Administration Handbook](http://www.amazon.com/UNIX-Linux-System-Administration-Handbook/dp/0131480057).
I haven't read all of it yet, actually just the part until Perl scripting, which is only the 2nd chapter! The stuff
before chapter 3 are just basic linux administration / using the system. After that it goes into booting, filesystem,
basically everything, and this is with some serious depth. Which is not for me.

### RHCSA Video

Found [http://www.youtube.com/watch?v=CjVYnK57YLA](http://www.youtube.com/watch?v=CjVYnK57YLA "on tube") on youtube.
Pretty cool, snapshotting in LVM!
