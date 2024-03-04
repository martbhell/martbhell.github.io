---
title: Let's encrypt the web - renewal
date: 2016-02-15
category: it
tags: encryption, letsencrypt

So easy!

just:

As I ran the letsencrypt-auto [last time](https://www.guldmyr.com/lets-encrypt-the-web/), I did again.

- sudo systemctl stop nginx
- cd letsencrypt
- git pull
- ./letsencrypt-auto
- enter enter etc
- sudo apache2ctl stop # .. why did it start apache2 automatically?
- sudo systemctl start nginx

Since letsencrypt-auto version 0.5.0 it's:

- sudo systemctl stop nginx
- cd letsencrypt
- git pull
- ./letsencrypt-auto --standalone --domains "my.example.com,2.example.com"
- sudo systemctl restart nginx

Since [certbot](https://github.com/certbot/certbot)\-auto (renamed from letsencrypt):

- sudo systemctl stop nginx
- ./certbot-auto renew
- sudo systemctl start nginx
