---
title: wasthereannhlgamelastnight.appspot.com - fixed - working again!
date: 2017-10-04
category: finland, it
tags: api, gcloud, google, json, nhl, python, rest, wasthereannhlgamelastnight
<!-- prettier-ignore -->
---

With NHL 2017-2018 season coming up and I had some extra spare time I thought why not finally fix this great website
again :)

As NHL changed the layout of their schedule page about two seasons ago - there's these days "infinite scrolling" or
whatever it's called when the page only loads what you see on the screen. This means it's a bit difficult to scrape the
page (but not impossible).

Lately I've been using REST API and JSON data for quite many things - after a short search I managed to find this hidden
gem: <https://statsapi.web.nhl.com/api/v1/schedule?startDate=2016-01-31&endDate=2016-02-05&expand=schedule.teams,schedule.linescore,schedule.broadcasts,schedule.ticket,schedule.game.content.media.epg&leaderCategories=&site=en\_nhl&teamId=>

Now that's a link to an API provided by NHL where you get the schedule and you can filter it. I'm not sure what all the
parameters do, they're not all needed. You just need the startDate and endDate. The API also has standings and results.
I have not managed to find any documentation for it. Best so far seems to be
[this blog post](https://www.kevinsidwar.com/iot/2017/7/1/the-undocumented-nhl-stats-api). So I'm not sure about if it's
OK to use it or if there are any restrictions.

p.s. - there is a shorter URL to the main page: [https://rix.fi/nhl](https://rix.fi/nhl) - but the commands -
like  [https://wasthereannhlgamelastnight.appspot.com/MTL](https://wasthereannhlgamelastnight.appspot.com/MTL) \- does
not work.

<https://www.guldmyr.com/was-there-an-nhl-game-last-night/>
