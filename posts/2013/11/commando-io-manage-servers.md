---
title: commando.io - manage servers
date: 2013-11-13
category: it
tags: cms, commando, commando, io, configuration, management, software, servers

[https://command.io](https://command.io "https://command.io") is up for public beta now. It is a page from where you can manage your servers online in a pretty web interface.

It uses ssh - you need to allow commando.io's server to ssh into your server. You can specify with which user, which port and then it uses an ssh key to log in.

When you sign up, first you get to choose your own subdomain, like awesome.commando.io and then add your user into there. The subdomain you get, let's say awesome.commando.io is pointing to an IP. It is with this IP that commando is connecting to your server. So this should be firewalled.

First thing I noticed was that on a CentOS 6 the command you get to copy-paste does not account for that CentOS6 sets permissions to 775 by default when running mkdir ~/.ssh. I sent a message to commando.io with the built-in messaging tool at 13th of November at 1223. 12 minutes later I had a reply, so quite quick at responding.

Also sent in a suggestion that they look into ssh-copy-id instead of making ~/.ssh and setting permissions manually :)

Real easy to add a recipe and then run it on a server.

I could not find any existing recipes, nor where there any links to a repository or community page where one could share recipes or even example recipes.

All in all:

- It looks nice and mostly works.
- Is it safe? Do I want to give access to a third party provider that doesn't have any obvious information declaring their high intent of security.
- Some things that would be nice:
    - scheduled executions
    - using states - puppet-like, to insure that something that was done in a recipe once is still the current state of the machine.
    - group import of servers
