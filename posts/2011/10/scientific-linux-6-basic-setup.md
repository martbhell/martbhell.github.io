---
title: Scientific Linux 6 - Basic Setup
date: 2011-10-26
category: it
tags: certification, kvm, learning, linux, red, hat, rhcsa, rhel, scientifix, linux, sl, studying, vmware, workstation
<!-- prettier-ignore -->
---

## Not allowing root to log in

By default sshd is running on SL6 and you can ssh in with 'root'.

Probably a good idea to change this in /etc/ssh/sshd_config

permitrootlogin no

But first, create a user that can log in.

useradd mart passwd mart

Then you can change sshd_config and 'service sshd reload'.

Then you can ssh in and either hit' su -' to get root access. Or, if you hit 'visudo' and add your user. You can later
just type 'sudo bash' to get a root bash shell.

## Firewall

iptables -L to view the firewall setup, note that there is a 'virbr0' interface that has forwarding rules. This is
probably for NAT or bridging for potential virtual machines, and was probably created when we chose 'Virtual Host' as
the role for the system. iptables-save : another view that may be easier to understand. This you can put in 'file' and
then hit iptables-restore < file.

## Slow before you get the login prompt while ssh-ing?

To see what is happening, ssh in with 'ssh -v ip'. In my case I saw

> debug1: An invalid name was supplied Cannot determine real for numeric host address

A little googling showed me that this is because your machine doesn't have a name lookup for that IP. So go ahead and
add one in /etc/hosts and then it will be fast.

## Notice that your ssh stops working after a while? Doesn't accept input?

If so, add this to your ~/.ssh/config file:

Host \*    ServerAliveInterval 60

Make sure there is at least a space on the second line. I have three :p You can change the \* to a specific domain if
you do not want to do this on all your boxes. If the file doesn't exist, create it.

## Run sshd on a second port

1. Edit /etc/ssh/sshd_config
2. Add a line saying: Port 6666
3. look in /etc/hosts.allow (any entries? good)
4. iptables-save > ~/fwrules
5. vi fwrules
6. copy the --dport 22 line and paste a new one above the -j REJECT lines (vi commands: yy and P)
7. change the 22 to 6666 (vi commands: x for delete, R for replace mode. :wq! to save and quit)
8. iptables-restore < ~/fwrules
9. /etc/init.d/sshd restart

If you want you can hit: iptables -L or iptables-save. These will also show the current iptables rules. See ip6tables
for IPv6 rules.

Now the port is running on another non-standard port (you could set it to whatever you want, as long as it's lower then
65536 and preferably higher than 1024). This might be good for security reasons. You could still have port 22 open for
access from your internal network (see adding a -s ip.add.r.ess on the row in the iptables rules) and the other one
accessible from the internet or maybe even a specific network / address on the internet for even more security.
