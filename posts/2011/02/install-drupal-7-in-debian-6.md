---
title: Install Drupal 7 in Debian 6
date: 2011-02-11
category: it
tags: admin, accounts, apt, get, database, settings, debian, debian6, drupal, guide, http, it, phpmyadmin, script, upgrade, web, server, apache

Time for another go!

### Drupal is ..

.. a pretty famous and widely used CMS out there - so here we go ->

1\. Get sudo [configured](http://wiki.debian.org/sudo "configure sudo") on debian. Sucks to have to log on as root all the time when installing apps etc.

2\. [Download](http://drupal.org/project/drupal "drupal") and untar drupal 7

3\. Read INSTALL.TXT

Requirements:

\- A web server. Apache (version 2.0 or greater) is recommended. - PHP 5.2.4 (or greater) (http://www.php.net/). - One of the following databases: - MySQL 5.0.15 (or greater) (http://www.mysql.com/).

**"sudo apt-get install lamp-server^"** does not work in Debian 6 :/

Following [this guide](http://wiki.debian.org/LaMp "lamp debian") instead.

1. aptitude update  and then upgrade (maybe not necessary because I used apt-get.. why have two??)
2. sudo apt-get install mysql-server mysql-client (in Debian 6 you put in sql root user password during install)
3. sudo apt-get install apache2 php5 php5-mysql libapache2-mod-php5 phpmyadmin
4. Surf to http://ip/phpmyadmin and log on to the mysql db - does it work? yay!
5. Create drupal db - see INSTALL.mysql.txt - basically this just tells you to create a database and a user. It asks you to do this via manual SQL queries, but we have phpmyadmin so we just have to; 1. click on databases and create a new one. 2. after that, click on privileges and create a new user. 3 just type in username and password, leave the rest for default.
6. Copy extracted files to your www directory. Beware of rights, use chmod and possibly chown. /var/www/ is the default directory.
7. Surf to http://ip/drupal (where install.php is)
8. Standard setting
9. Then it complains that it doesn't have access. Because I had to set chmod 777 on the 'sites' directory under /drupal.
10. Then I need to copy a file and make it writeable, just doing what the script tells me to.
11. Configure the database settings.
12. Now you can remove write access permissions on the sites/default directory and sites/default/settings.php
13. Put in contact and admin accounts stuff.
14. Done! Wow, that was easy :)

So much to do in there! I will have to get back about this in another post :)
