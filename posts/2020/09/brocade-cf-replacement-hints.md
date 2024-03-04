---
title: Brocade CF Replacement Hints
date: 2020-09-13
category: storage
tags: brocade, fc, fibre, channel, san, san, network
<!-- prettier-ignore -->
---

This post is based on a submission from a reader of this blog **Eberhard**,
maybe primarily of the popular
[Brocade SAN upgrades](https://www.guldmyr.com/brocade-san-switch-firmware-upgrades/)
post. Many thanks for this, hoping it will help someone out there!

The topic here is how to replace the embedded Compact Flash card if that breaks.

You can read about how to do that in the PDF below:

[brocade_cf_replacement](https://github.com/sanswitcher/CF-Installer)

If your CF drives are **exactly** the same size (not in GB, in blocks) as the
one in Brocade then you could get away with dding the whole /dev/sda - which
would simplify the process a little.

Again, many thanks for the contribution!
