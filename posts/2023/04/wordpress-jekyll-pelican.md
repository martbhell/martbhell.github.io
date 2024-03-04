---
title: Moving from WordPress to This
date: 2023-04-15 21:57
category: it
lang: en
tags: blog, wordpress, jekyll, pelican, cloudflare, dns, linux, web hosting
<!-- prettier-ignore -->
---

## Background Story

I had this great webhost.

They had the first `$SHELL` I ever used. I learnt a lot about bash scripting
there. I ran eggdrops and IRC clients and used screen :D

I experienced the hacks when they got pwned, because those things happened back
then (2001-2002 probably).

Anyway, eventually I also had some websites with them and this blog used to live
there in a wordpress.

Until the other day when I think wordpress had gotten auto-updated beyond the
now quite old PHP version.

## Let's try Jekyll They Say

First I thought: hey how can I keep on paying very little money for this? Is
exporting and importing the wordpress somewhere that? No. At least not on this
one web hotell I checked :)

Then I thought: hmm how hard is it to export the wordpress into static MD files
and server those somewhere? (Turns out not so hard)

Third: Let's try to use GitHub Pages because that's where I'd like to keep the
code anyway?

- Changed nameserver to a service and then pointed guldmyr.com to github pages.
- What pages to use? Uhhh.. jekyll??
- Lots of fighting and it looked quite bad.

Fourth: Let's not use Ruby because I can't.

- Cloudflare also looks cool and I'd like some experience with that
- Cloudflare has pages too?
- It has support for some Python framework called Pelican!
- To use Cloudflare pages and get guldmyr.com and not just <www.guldmyr.com>
  here I need to move my DNS to them :/
- Cloudflare has free DNS? Why did I pay a yearly thing in advance???

Anyway, here we are and I'm quite happy with this pelican and cloudflare thing.
A few things I found annoying with GitHub Pages:

- It took I kid you not 16min for jekyll to render the html from the markdown of
  this blog.
- No preview built-in so I broke the website several times.
- And because (Rust?) I couldn't easily figure out how to jekyll on my local
  machine.

Are now much better with Pelican. And because it's python if I need to modify
something it is often relatively easy for me. OK we are missing some things.
There's no search options. For which I'm glad I've been adding lots of tags on
posts over the years. So yeah. Poor man's search is now the [tags](tags/) page!

Anyway. Welcome to the blog. Let's see how long until the next post :D
