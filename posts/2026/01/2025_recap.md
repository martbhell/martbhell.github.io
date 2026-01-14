---
title: 2025 Recap at the office
date: 2026-01-14 22:57
category: it
lang: en
tags: fastapi, ceph, radosgw, s3, object storage, storage, r2, infiniband, clustering, clustermax, roce, nccl, all_reduce_perf
<!-- prettier-ignore -->
---

## At $Dayjob Instant Cluster

Major things at verda / what did I do | learn?

I got better at making coffee in the Sage machine, still not perfect but it's getting there :)

### Instant Cluster product went live

We got Bronze in two ClusterMaxx [v1](https://www.clustermax.ai/v1) and [v2](https://www.clustermax.ai/v2).

I've spent quite much time into finding race conditions.

What I'm looking forward to next year is to get around to making the backend backend API for this even more resilient.
For example, wouldn't it be nice to be able to do a rolling upgrade of the API without affecting existing flows?

### multi-node all_reduce_perf with RoCE backend network

Sure took a while to learn:

- `show_gids` command to find out which IB_GID_INDEX

These kind of extra flags to `mpirun` to get [all_reduce_perf](https://github.com/NVIDIA/nccl-tests) running:

```bash
mpirun -H 10.1.1.5:8,10.1.1.6:8 \
      -x NCCL_IB_GID_INDEX=5 \
      -mca coll ^hcoll \
      -mca pml ob1 \
      -mca btl tcp,self \
      ./build/all_reduce_perf -e 8G -n 200 -b 512M -f 2 -g 1
```

Do you know of a better way to run it?

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
