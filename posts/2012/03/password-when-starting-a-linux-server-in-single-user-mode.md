---
title: "password when starting a linux server in single-user mode"
date: "2012-03-08"
categories: 
  - "it"
tags: 
  - "hardening"
  - "init"
  - "inittab"
  - "linux"
  - "red-hat"
  - "rhel"
  - "scientific-linux"
  - "security"
  - "single-user"
  - "singleuser"
  - "slc"
  - "su"
  - "sulogin"
  - "sushell"
---

http://www.cromwell-intl.com/unix/linux-break-in-howto.html

On RHEL 6.2-based systems (like Scientific Linux 6.2): edit /etc/sysconfig/init

\# Set to '/sbin/sulogin' to prompt for password on single-user mode # Set to '/sbin/sushell' otherwise

Like this:

SINGLE=/sbin/sulogin

Then if you add an 's' to the grub entry when the server boots it will ask you for a password , or hit ctrl-d. Ctrl-d makes the server enter normal boot (telinit \*).

Should all linux machines be installed this way? To me this sounds like a definite deal, especially if you have the console physically or remotely accessible.
