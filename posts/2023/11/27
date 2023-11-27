---
title: Google AppEngine exceeded memory limits 
date: 2023-11-27 11:57
category: it
lang: en
tags: wtangy, nhl, gae, google, google app engine, python, gunicorn 
---

If you are using Google's AppEngine to run a Python Flask webserver for example. And you want to do so while sticking to Free Tier (and dynamic instance F1). Then you shouldn't use the default gunicorn settings of 4 workers, but rather follow their guidance and use 2!

Massive speedup seen, from always >300ms and frequently over 5 seconds to respond, it's now down to just a few milliseconds. Probably because the instance was I guess using all the memory. But when memory really was exceeded the app was killed and restarted resulting in even higher latency.
