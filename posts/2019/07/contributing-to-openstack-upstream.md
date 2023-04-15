---
title: "Contributing To OpenStack Upstream"
date: 2019-07-22
category: it
tags: backporting, gerrit, git, keystone, openstack, puppet, rdo, vancouver

Recently I had the pleasure of **contributing** upstream to the [OpenStack](https://www.openstack.org/) project!

A link to my merged patches: [https://review.opendev.org/#/q/owner:+guldmyr+status:merged](https://review.opendev.org/#/q/owner:+guldmyr+status:merged)

In a previous [OpenStack](https://www.openstack.org/) summit (these days called OpenInfra Summits), (Vancouver 2018) I went there a few days early and attended the **Upstream Institute** [https://docs.openstack.org/upstream-training/](https://docs.openstack.org/upstream-training/) .  
It was 1.5 days long or so if I remember right. Looking up my notes from that these were the highlights:

- Best way to start getting involved is to attend weekly meetings of projects
- **Stickersssss**
- A very similar process to RDO with Gerrit and reviews
- Underlying tests are all done with ansible and they have ARA enabled so one gets a nice Web UI to view results afterward. Logs are saved as part of the [Zuul testing](http://zuul.openstack.org) too so one can really dig into and see what is tested and if something breaks when it's being tested.

Even though my patches were one baby and a bit over 1 year in time after the Upstream Institute I could still f[igure things out](https://docs.openstack.org/contributors/) quite quickly with the help of the guides and get bugs created and patches submitted. My general plan when first attending it wasn't to contribute code changes, but rather to start reading code, perhaps find open bugs and so on.

The thing I wanted to change in puppet-keystone was apparently also possible to change in many other puppet-\* modules, and less than a day after my puppet-keystone change got merged into master someone else **picked up the torch** and made PRs to like ~15 other repositories with similar changes :) Pretty cool!

**Testing** is hard! [https://review.opendev.org/#/c/669045/1](https://review.opendev.org/#/c/669045/1) is one backport I created for puppet-keystone/rocky, and the Ubuntu testing was not working initially (started with an APT mirror issue and later it was slow and timed out)... After 20 rechecks and two weeks, it still hadn't successfully passed a test. In the end we got there though with the help of a core reviewer that actually updated some mirror and later disabled some tests :)

Now **the change itself** was about "oslo\_middleware/max\_request\_body\_size" So that we can increase it from the default 114688. The Pouta Cloud had issues where our [Federation User Mappings](https://docs.openstack.org/keystone/pike/advanced-topics/federation/configure_federation.html#mapping) were larger than 114688 bytes and we coudln't update them anymore, turns out they were blocked by oslo\_middleware.

> (**does anybody know where 114688bytes comes** **from**? Some internal speculation has been that it is from 128kilobytes minus some headers)

Anyway, the mapping we have now is simplified just a long \[ list \] of "local\_username": "federation\_email", domain: "default". I think next step might be to try to figure out if maybe we can make the rules using something like below instead of hardcoding the values into the rules  

"name": "{0}" 

It's been quite hard to find examples that are exactly like our use-case (and playing about with is not a priority right now, just something in the backlog, but could be interesting to look at when we start accepting more federations).

All in all, I'm really happy to have gotten to contribute something to the OpenStack ecosystem!
