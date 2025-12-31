---
title: 2025 Recap at the office
date: 2025-12-31 22:57
category: it
lang: en
tags: fastapi, ceph, radosgw, s3, object storage, storage, r2
<!-- prettier-ignore -->
---

## At $Dayjob Instant Cluster

### A RadosGW temporary user API

Trip to Palo Alto and focus time to work on CEPH radosgw API, worked on a wrapper that replicated cloudflare R2's
[temporary access credentials](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/progress/)
that are given access to a certain prefix.

How would you implement something like that? This was for one single customer and a single bucket and I wanted to avoid
adding a database & state to this API that currently was just a wrapper in front of CEPH's radosgw API.

I went with radosgw user names with `_` separated keys & values to indicate:

- for which user this was for
- when it expires (epoch timestamp)

And then a cron task that calls an endpoint that goes through the users for this one customer and checks expiry time and
deletes those users.

This was quite fun to figure out as this also involves managing
[S3 policies](https://docs.ceph.com/en/quincy/radosgw/bucketpolicy/#limitations) and to create those for a bucket you
need to use the S3 API, not the radosgw API.
