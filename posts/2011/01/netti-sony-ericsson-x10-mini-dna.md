---
title: Netti + Sony Ericsson X10 Mini + DNA
date: 2011-01-28
category: finland, it
tags: access, point, android, apn, dna, internet, netti, sony, ericsson, suomi, x10, mini
<!-- prettier-ignore -->
---

So you just got your SE X10 Mini in another country and wants to use it in Finland with the telephone service provider
DNA? Not as easy as it seems! Well, first it's hard to get the actual number, but after you get your social security
number it should not be that hard.

For me it worked, but only with the native browser. Not with any other apps like facebook, gmail, opera mini, market.

When your phone registers on the DNA network it gets some access point profiles that supposedly will let you get online.

To view your profiles go to Settings -> Wireless & Network Settings -> Mobile Networks -> Access Point Names. In here I
had a profile called "dna wap" and one more - which I got after first registering on the dna network.

Spoke with DNA in Kamppi who said it was the phone's problem - that that the access point profiles were good (they did
mention the Internet one, but said that not all phones has it). Even had a chat session with the Sony Ericsson support
who said that the access point profile is not correctly configured.

After quite some translated search I managed to find this profile:

> Name: dna internet APN: Internet Proxy: not set Port: not set Username: not set Password: not set Server: not set
> MMSC: not set MMS Proxy: not set MMS Port: not set MCC 244 MNC 12 APN type: not set

Which makes it all work! DNA does not sell Sony Ericsson cell phones - I suppose they do not like it because they are
"made" in Sweden.
