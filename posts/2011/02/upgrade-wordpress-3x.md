---
title: Upgrade WordPress 3.x
date: 2011-02-24
category: it
tags: guide, phpmyadmin, safemode, update, upgrade, upgrade, wordpress, webhost, wordpress

Hi!

If your webhost is running in php safemode then you may run into some issues, for example you cannot do the upgrade of WP automagically via the admin interface and neither can you upgrade plugins manually, which is a hazzle.

To do the upgrade follow this guide:

[http://codex.wordpress.org/Upgrading\_WordPress\_Extended](http://codex.wordpress.org/Upgrading_WordPress_Extended "Upgrade WordPress")

I went from 3.0.4 to 3.1 and from 3.1 to 3.1.3 and from 3.1.3 to 3.2

The way I do it is like this:

1. Download your blog ( in my case /blog) to your local machine.
2. Make a backup of your mysql database ( via phpmyadmin in my case ). Good idea is to delete spam comments before you do this, saves a few bytes.
3. Download and extract the latest wordpress on your local machine.
4. In the directory where you extracted the new wordpress files, remove the directories that you are supposed to keep (mentioned in red text in the guide/link above and in #6 below).
5. Copy over the files from your blog that you are supposed to keep, get them from where you downloaded the new files to your local machine.
6. In my case the things I needed to copy were: wp-config.php, the folders under wp-content - and their content,  .htaccess
7. The rest did not apply to me, as I did not have the cache, wp-images, plugins/widget and not using special language or special robots.txt
8. On your web-host, rename the folder of your blog (I have mine under /blog)
9. Upload the new directory from your local machine (the new one where you have copied in the things you needed to keep).
10. Surf to /wp-admin
11. Click upgrade db
12. Take this opportunity to update some plugins if you have that are out of date.
13. I did not have to alter my permalinks, the setting was the same (%postname%) and the links are still working.
14. Done!

If you do run into problems this way, check out the [forums](http://wordpress.org/tags/upgrade "wordpress forum upgrade") for some assistance.

There are things you can use to make this a lot faster. For example maybe a lot of files aren't different between the versions. If you don't do backup or maybe if you don't upload the whole new directory that will save you lots of time.

Some ftp-clients (flashfxp for example) have what's called a skip-list where you can specify that files with the exact same size should not be over-written but skipped.

>What I did last time was to just download 3.2. Extract the archive. Remove the wp-content. Upload and overwrite the files on the web host. Tada. Not so complicated at all :)
