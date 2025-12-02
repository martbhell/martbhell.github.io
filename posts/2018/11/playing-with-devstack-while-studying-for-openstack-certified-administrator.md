---
title: Playing with devstack while studying for OpenStack Certified Administrator
date: 2018-11-08
category: it
tags: cloud
<!-- prettier-ignore -->
---

Below I'll go through some topics I thought about while reading through the
[requirements](https://www.openstack.org/coa/requirements/) for COA:

- Users and passwords because we use a LDAP at $dayjob. How to set passwords and stuff?
  - openstack user password set
  - openstack role add --user foo member --project demo
- Users and quota. Can one set openstack to have user quota?
  - _guess not :)_
- How to default quota with CLI?
  - nova quota-class commands. Found in operator's guide in the docs.
- Create openrc without horizon
  - TIL that OS_AUTH in devstack is <http://IP/identity> . No separate port :) And couldn't really find a nice way.
    After it's working there's an $ openstack configuration show though which tells stuff..
- Cinder backup
  - cool, but this service is not there by default in devstack.
- Cinder encryption
  - another volume type with encryption.  Shouldn't need barbican with a fixed_key but I don't know, cinder in my
    devstack wasn't really working so couldn't attach and try it out. Have some volumes with a encryption_key_id of
    "000000..." so maybe? Attaching my LVMs isn't working for some reason. Complaining about initiator ?
- Cinder groups.
  - Details found under cinder admin guide under rocky.. not Pike. Using cinder command one can create volume group
    types and then volume groups and then volumes in the volume group. All with cinder command. After you have added
    volumes into a group you can take snapshots of a volume group. And also create a volume group (and volumes) from the
    list of snapshots.
- Cinder storage pool
  - backends. In devstack it's devstack@lvmdriver-1apparently one can set volume_backend_name both as a cinder.conf and
    as a property

- Object Expiration. Supported in CEPH rados gateway? Yes, but in
  [luminous](http://docs.ceph.com/docs/luminous/radosgw/s3/)
  - available in default devstack, done with a
    [magical header](https://docs.openstack.org/ocata/user-guide/cli-swift-set-object-expiration.html) X-Delete-After:epoch
- Make a Heat template from scratch using the docs.
  - can be made quite minimal
- Update a stack
- Checking status of all the services
- Forget about ctrl+w.

## Study Environment

A [devstack](https://docs.openstack.org/devstack/latest/) setup in an Ubuntu 18.04 in a VM in $dayjob cloud. This means
no nested virtualization and I wonder how unhappy neutron will be because port security. But it's all within one VM - it
started OK, not everything worked but that's fine with me :) Probably just need a local.conf which is not the default!

> One thing I got to figure out was the LVM setup for cinder. Always fun to read logs :)
