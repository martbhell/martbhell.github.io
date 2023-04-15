---
title: Ubuntu + Automatic Software Updates
date: 2011-07-12
category: finland
tags: apt, get, cronjob, crontab, linux, script, ubuntu

How often do you actually log on to your machine - hit sudo apt-get update; sudo apt-get upgrade without reading what the changes are? I do it every time, unless it's a dist-upgrade we're talking about.

So how do we get this going?

The tool you're looking for is called cron-apt.

$sudo apt-get install cron-apt

This installs postfix for you as well (I chose local server, bah to e-mails, no pain, no gain). After this, edit /etc/cron.d/cron-apt to your preferences. If you want to see what it does - just hit what it says in that file:

test -x /usr/sbin/cron-apt && /usr/sbin/cron-apt

and see what it does!

Test -x (file exists and execute permission is granted) Second one runs it (but this did not produce any output) Check out /var/log/cron-apt/log for details of what it does.

Please note that the cron-apt also runs "apt-get dist-upgrade" which would upgrade your distribution. So be careful. It also runs autoclean :)

If you want more details - it's possible to do this other ways (for example with anacron and /or bash scripts). See this link: https://help.ubuntu.com/community/AutoWeeklyUpdateHowTo
