---
title: Lifehack currency
date: 2011-01-18
category: finland, it
tags: currency, it, lifehack, money, script
<!-- prettier-ignore -->
---

Haven't gotten around to the e-mail script yet, what would qualify? I check it
so regularly often anyway that that is not something I want, I also don't get
that many e-mails.

On to another script that would assist me when I need to send money between a
non-euro country and a country with euro. How to keep track of when the non-euro
currency gives as much euro as possible?

Also, good thing I checked with the girlfriend: When sending money **to** a
**non-euro country** **from** a **euro country**, you want to get as **many
non-euro** as possible.

When sending money **to** a **euro country** **from** a **non-euro country**,
you want to use as **few non-euro** as possible to make **a euro**.

```bash

#/bin/sh

webpage=http://url.com/page.html
inputfile=/home/user/valuta/valuta.html
play=/home/martbhell/valuta/playfile
outputfile=/var/www/valuta.log

wget $webpage -O $inputfile cat $inputfile | grep EUR/SEK -m 1 > $play
awk '{print $4}' $play >> $outputfile
date >> $outputfile
```

This is how the bash script looks like at the moment.

I would prefer to have the date after the value of EUR/SEK because then it's a
lot easier to read. But I was thinking maybe I can sort this out via a
php-script when presenting the file. Basically every 2nd line should have a new
line, not every one which is how the file looks like after the above bash
script, see below:

> 8.9134 Tue Jan 18 10:15:05 PST 2011

_In Ubuntu Server (what I'm running as a virtual machine to test the scripts) to
set timezone it is: **dpkg-reconfigure tzdata**_

\*\* just about to go to bed, but why don't I remove the date from the lines,
and then instead add them via php? .. hmm. but then i won't have the date of
when the value was taken.. is it important? seems kind of relevant, it's not
really the date the exchange rate was updated, just when script was run so
perhaps during the night we'd see updates on the numbers but not on the rate. to
be contemplated I guess - also maybe put this in a mysql db?\*\*

\*\* After sleeping on it I ended up doing it like this:

```bash
wget $webpage -O $inputfile
cat $inputfile | grep EUR/SEK -m 1 > $play
# - this greps for EUR/SEK and only line 1 (there are three on that .html)
P=$(awk '{print $4}' $play)
# - column 4 from output file of the above cat/grep
S=$(date) # - just to put the date in a variable
T='TAG BR TAG' # - to put an HTML BR tag at the end of each line
U=, # - to add a [comma between the values](http://en.wikipedia.org/wiki/Comma-separated_values), might come in handy if I want to import/export this.

echo $P$U $S$U $T >> $outputfile
```

This does the trick and the output now looks like this in the file, and comes
out like that on the webpage too.

> 8.9082 Wed Jan 19 07:40:54 EET 2011 8.9082 Wed Jan 19 07:50:54 EET 2011

Now I just have to find a way to run this and put it on my webhost :) \*\* OK
believe I have a way but it's not so good as it's via unsecure ftp :/

Thinking about the mysql thing but as my webhost don't have a shell that would
mean some sneaky "shortcuts" to get the things in the db :/ \*\* 01/20/2011 -
Added CSV in the outputfile too.
