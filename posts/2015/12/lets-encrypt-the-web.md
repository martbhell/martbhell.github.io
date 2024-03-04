---
title: let's encrypt the web!
date: 2015-12-05
category: it
tags: https, letsencrypt, nginx
<!-- prettier-ignore -->
---

Letsencrypt is finally in public beta!

Got
[from ssllabs.com](https://www.ssllabs.com/ssltest/analyze.html?d=mat.rix.fi)
https enabled on my own play [webhost](https://mat.rix.fi) today with let's
encrypt!

There are many good guides for getting this setup. This is how I got it working
with nginx (without using the experimental nginx plugin of letsencrypt).

on the webhost (not as root):

`git clone <https://github.com/letsencrypt/letsencrypt> letsencrypt-auto`

**eventually** this generates some certificates into /etc/letsencrypt _of course_

you should read scripts before running anything, there are for
example [acme-tiny](https://github.com/diafygi/acme-tiny),
[gethttpsforfree.com](https://gethttpsforfree.com/) and [letsencrypt-nosudo](https://github.com/diafygi/letsencrypt-nosudo) that
might be better. #mozilla has some server side SSL recommendations
on <https://wiki.mozilla.org/Security/Server_Side_TLS>

Modify your nginx site file to have something like this:

```bash
server {
 listen [::]:443 ssl ipv6only=off;

ssl on;
 ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
 ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

ssl_session_cache shared:SSL:50m;
 ssl_session_timeout 5m;
 ssl_session_tickets off;

ssl_protocols TLSv1.1 TLSv1.2;
 ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK';
 ssl_prefer_server_ciphers on;

ssl_dhparam /etc/nginx/dhparams.pem;

# ssl_stapling on;

# ssl_stapling_verify on

# resolver 193.166.4.24

 root /var/www;
 index index.html index.htm index.php;

# Make site accessible from http://localhost/
 server_name localhost;

add_header Strict-Transport-Security "max-age=15724800";

}
```
