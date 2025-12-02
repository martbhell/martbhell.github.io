---
title: wasthereannhlgamelastnight.com - now using object storage!
date: 2017-10-07
category: it, storage
tags: cloud, gcloud, google, nhl, programming, wasthereannhlgamelastnight
<!-- prettier-ignore -->
coverImage: "screenshot.png"
---

To continue this series of blog posts about the
awesome [https://wasthereannhlgamelastnight.appspot.com/WINGS](https://wasthereannhlgamelastnight.appspot.com/WINGS) web
site where you can see if there was in fact, an [NHL](http://nhl.com/schedule) game last night :)

Some background: First I had a python script that scraped the website of nhl.com and later changed that to just grab the
data from the JSON REST API of nhl.com - much nicer. But it was still outputing the result to stdout as a set and a
dictionary. And then I would in the application import this file to get the schedule. This was quite hacky and ugly :)
But hey it worked.

As of
[this commit](https://github.com/martbhell/wasthereannhlgamelastnight/commit/391c154670c4577c5d185937e56a340ff912810c)
it now uses Google's [Cloud Object Storage](https://cloud.google.com/storage/):

- a special URL (one has to be an admin to be able to access it)
- there's a cronjob which calls this URL once a day (22:00 in some time zone)
- when this URL is called a
  [python script](https://github.com/martbhell/wasthereannhlgamelastnight/blob/master/src/update_schedule.py) runs
  which:
  - checks what year it is and composes the URL to the API so that we only grab this season's games (to be a bit nicer
    to the API)
  - does some sanity checking - that the fetched data is not empty
  - extracts the dates and teams as before and writes two variables,
    - one list which has the dates when there's a game
    - one dictionary which has the dates and all the games on each date
      - probably the last would be enough ;)
  - finally always overwrites the schedule

To only update it when there are changes would be cool as then I could notify myself (and possibly others) when there
have been changes, but it would mean that the JSON dict has to be ordered, which they aren't by default so I'd have to
change some stuff. The
[GCSFileStat](https://cloud.google.com/appengine/docs/standard/python/googlecloudstorageclient/gcsfilestat_class) has a
checksum-like metadata of the files called [ETAG](https://en.wikipedia.org/wiki/HTTP_ETag). But probably it would be
best to first compute a checksum of the generated JSON and then add that as an extra metadata to the object as this ETAG
is probably implemented differently between providers.

<https://www.guldmyr.com/wasthereannhlgamelastnight-appspot-com-fixed-working-again/>
