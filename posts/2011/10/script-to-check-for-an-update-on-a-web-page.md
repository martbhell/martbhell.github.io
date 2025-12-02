---
title: Script To Check For an Update on a Web Page
date: 2011-10-19
category: it
tags: bash, bash, scripting, linux, script, scripting, spotify, wget
<!-- prettier-ignore -->
---

Hey!

This is used for me on my Linux workstation to get a notification if there is a new spotify release whenever I open a
new terminal.. It would be applicable for other (probably also simple) pages that aren't updated frequently.

Reason: [http://repository.spotify.com/pool/non-free/s/spotify/](http://repository.spotify.com/pool/non-free/s/spotify/)

I wanted to see if there was a new spotify release for Linux/QT.

Method: The URL is above - but what if I do not want to go there every day and get disappointed?

Way nicer to have a script do it for me.

This script saves the index.html from the URL above of each day.

Then each day when it downloads the .html it checks if it's different from yesterday.

This has its limitations, if there is an update in the weekend I will never know.

The script should check the last x amount of days and if any of them are different from today it should tell me. The
script checks if any of the files are different from today, if so, it will write something into another file. The script
then checks if this file is non-empty, if it has data in it, it will write to this other file that. Tada. :p

If it is, then it will write to a file that is referenced in $HOME/.bashrc.

The layout of the blog doesn't like really long lines in `<pre>`, but you can select below and only get the post (and
not the stuff on the right side).

spot_check.sh:

```bash
# !/bin/sh

dat1=$(date +%Y.%m.%d)
daty=$(perl -MPOSIX=strftime -le 'print strftime "%Y.%m.%d",localtime (time - 86400)')
dat2=$(perl -MPOSIX=strftime -le 'print strftime "%Y.%m.%d",localtime (time - 172800)')
dat3=$(perl -MPOSIX=strftime -le 'print strftime "%Y.%m.%d",localtime (time - 259200)')
dat4=$(perl -MPOSIX=strftime -le 'print strftime "%Y.%m.%d",localtime (time - 345600)')
dat5=$(perl -MPOSIX=strftime -le 'print strftime "%Y.%m.%d",localtime (time - 432000)')

path="$HOME/Downloads/Spotify/saved"
out="$HOME/Downloads/Spotify/diff.log"
bout="$HOME/.spotcheck"
wget -q http://repository.spotify.com/pool/non-free/s/spotify/ -O $path/$dat1.html

diff -q $path/$dat1.html $path/$daty.html > $out
diff -q $path/$dat1.html $path/$dat2.html >> $out
diff -q $path/$dat1.html $path/$dat3.html >> $out
diff -q $path/$dat1.html $path/$dat4.html >> $out
diff -q $path/$dat1.html $path/$dat5.html >> $out

if [[ -s $out ]] ; then
echo $out "is not empty";
echo "#!/bin/sh" > $bout;
echo "echo new spotify release" >> $bout;
chmod +x $bout;
else
echo $out "is empty";
echo "No new spotify release.";
rm $bout;
fi;
```

Crontab (daily at 0915):

`15 09 * * * /bin/bash /home/username/Downloads/Spotify/spot_check.sh 2>&1`

.bashrc:

```bash
if [ -f ~/.spotcheck ]; then
cd $HOME
./.spotcheck
fi
```
