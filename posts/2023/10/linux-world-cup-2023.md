---
title: Linux World Cup - 2023
date: 2023-10-30 22:57
category: it
lang: en
tags: linux, ctf, world cup
---

spoiler alert!

## Top 3

| | | |
|-|-|-|
| Position | Competitor  Alias | Total Time to Solve |
| 1 | aretea | 42 mins 13 secs|
|2 & 3| martbhell |47 mins 12 secs|
|2 & 3 | mgubenko| 47 mins 21 secs|

## The challenges

[Recording from this event](https://sadservers.com/ranking_lwc)

### Chennai

I was best! Took 21mins 28seconds

Still 21 minutes was quite a beast!

I spent some time in advance here learning about rabbitmq. But sure, during these 21mins I was reading [rabbitmqctl guide](https://www.rabbitmq.com/management-cli.html)

I had some experience with rabbitmq from before so the concepts weren't that far away.

### Monaco

Also best. [3mins 46seconds](https://sadservers.com/replay/i-0ee2f3007d5494cc2) - link to the asciinema recording

- I kept looking inside .bash_history but that did not help at all.
- Finally looked in `git status`` even though from initial`ls -la` I could have seen it.

### Ivujivik

Quite a lot slower. 11m 26secs vs 2m32 for winner.

Winner: Used some awk (typed it in without copying, so could have prepared a bit better :) to parse. Very elegantly and small compared to .. my python.

I wrote some python to read it. Had it prepared. But still managed to introduce typos and indentation issues. Could have prepared the csv reader much more in advance. But OK, I wanted a challenge under pressure. Keep forgetting that it's all strings.. vim recover file.

While typing figured out how I wanted to solve it instead of thinking it through beforehand.

### Unimak

Also slower. 3mins 14s vs 1min 31s.

Winner: jq . the_json and printed top 10 lines and took the first one??

I:

- prepared some python to read json
- very very slowly updated the python to read the json and get to what I needed
  - introduced and fixed bugs in the python as I went along :D

### Taipei

Ridonc. I took 7mins 18 vs 31s of winner.

Hahha. So this challenge was a port knocker. The fastest just **nmapped** all ports and then curled to localhost!

Whereas I:

- downloaded some knocker.py
- messed around inside the source code..
- guessed that range would be in 56400 because that's where..
- then tried to _hack_ the system to get the config of the program that was handling the knocking (knockd)
- tried to read the ansible tmp files to get it
- tried reading log files to find it
- went back to knocker.py and ran it with -b
- ...

## All in all

 Great fun, warmly recommend fixing some sad servers :)
