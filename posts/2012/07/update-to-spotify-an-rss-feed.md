---
title: Update to Spotify - An RSS Feed
date: 2012-07-08
category: it
tags: bash, feed, ftp, linux, repository, rss, rss, feed, script, spotify, web

After some time the solution I devised on [http://www.guldmyr.com/blog/script-to-check-for-an-update-on-a-web-page/](http://www.guldmyr.com/blog/script-to-check-for-an-update-on-a-web-page/) just did not elegant enough (also it stopped working).

Instead of getting some kind of output in a terminal sometimes somewhere I decided to make an RSS feed that updates [http://guldmyr.com/spotify/spot.xml](http://guldmyr.com/spotify/spot.xml) instead :)

I suspect that the repository itself could be used to see if there's an update to it. It has all these nice looking files in here: http://repository.spotify.com/dists/stable/ - but I also suspect this is a repository for debian/ubuntu which I cannot use on my RHEL-based workstation.

Thus:

A bash script was written. It uploads the spot.xml whenever there is an update. The script does not run on the web-server so it ftps the file to the web-server, it would be nice if it did because then the actual updating of the feed would be so much more simple (just move/copy a file).

But, I hope it works :) Guess we'll see next time there's an update to spotify!

The script itself is a bit long and I hope not too badly documented, so it's available in the link below: [http://guldmyr.com/spotify/update.spotify.rss.feed.sh](http://guldmyr.com/spotify/update.spotify.rss.feed.sh "the script")

Or, more easily, you can just add [http://guldmyr.com/spotify/spot.xml](http://guldmyr.com/spotify/spot.xml "put this in an RSS reader") to your RSS reader (google's reader, mozilla's thunderbird, there are many of them).

Some things I learned:

- Latest post in an RSS feed is just below the header, making it a bit awkward to update via a script as you cannot just remove the </channel> and </rss>, add a new <item></item> and then add the </channel> and </rss> at the end again.
- lastBuildDate in the header also needs to be updated each time the feed is updated. In the end I decided to re-create the file/feed completely every time there was an update.
- Some rss-readers appear to have a built-in interval that they use to check if there's an update. So for example you could update the rss-feed and press 'refresh' but the client still won't show the new feeds. Google Reader does this for example. With Mozilla's Thunderbird you can ask it to update (Get Messages) and it will. You don't need an e-mail account in Thunderbird to use it as an RSS reader by the way.
- [http://feedvalidator.org](http://feedvalidator.org "http://feedvalidator.org") is a great tool, use it.

_I claim no responsibility if you actually use the script, the feed however should be fairly safe to subscribe to._

 

[![[Valid RSS]](images/valid-rss-rogers.png "Validate my RSS feed")](http://feedvalidator.org/check.cgi?url=http%3A//guldmyr.com/spotify/spot.xml)
