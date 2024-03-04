---
title: Studying for Openstack Certified Administrator
date: 2018-11-04
category: it
tags: certification, cloud, openstack
<!-- prettier-ignore -->
---

The plan : study a bit and then attempt the
[coa](https://www.openstack.org/coa#coa-details) exam. If I don't pass then
attend the course during openstack
summit: [SUSE](https://www.openstack.org/summit/berlin-2018/summit-schedule/events/22735/rsvp-required-suse-two-day-training-openstack-administration-prepare-for-the-certified-exams-day-2)

And what to study? I've been doing openstack admin work for the last year or
two. So I have already done and used most services, except **Swift**. But there
are some things that were only done once when each environment was setup. Also
at $dayjob our code does a lot for us.

One such thing I noticed while looking
through [https://github.com/AJNOURI/COA/wiki/02.-Compute:-Nova](https://github.com/AJNOURI/COA/wiki/02.-Compute:-Nova)

Was setting the default project quota. I wonder if that's a cli/webui/API call
or service config. But a config file would be weird, unless it's in
Keystone. *Turns out default quotas are in each of the services' config files.
It's also possible to set a default quota with for example the nova command.*

Another perhaps useful thing I did was to go through the release notes for the
services. $dayjob run
[Newton](https://releases.openstack.org/newton/index.html) so I started with the
release after that and tried to grok and look for biggest changes. Introduction
of placement was one of them and I got an introduction to that while playing
with devstack and "failed to create resource provider devstack" error. After
looking through logs I saw a "409 conflict" HTTP error or placement was
complaining that the resource already existed. So somehow during setup it was
created but in the wrong way? I deleted it and restarted nova and it got created
automatically and after that nova started acting a lot better :)
