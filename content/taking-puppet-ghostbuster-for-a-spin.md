---
title: "Taking puppet-ghostbuster for a spin"
date: 2019-07-18
categories: 
  - "it"
tags: 
  - "hiera"
  - "puppet-software"
  - "ssh"
---

We use puppet at $dayjob to configure OpenStack.

I wanted to know if there's a lot of unused code in our manifests!

\*\*From left of stage enters: https://github.com/camptocamp/puppet-ghostbuster \*\*

Step one is to install the puppet modules and gems and whatnot, this blog post was good about that: [https://codingbee.net/puppet/puppet-identifying-dead-puppet-code-using-puppet-ghostbuster](https://codingbee.net/puppet/puppet-identifying-dead-puppet-code-using-puppet-ghostbuster)

Next I needed to get the HTTP forwarding of the puppetdb working, this can apparently (I learnt about ssh -J) be done with:

> ssh -J jumphost.example.org INTERNALIPOFPUPPETMASTER -L 8081:localhost:8080

Then for setting some variables pointing to hiera.yaml and setting

> PUPPETDB\_URL=http://localhost:8081 HIERA\_YAML=/tmp/hiera.yaml

Unsure if hiera.yaml works, just copied it in from the puppetmaster

Then running it

> find . -type f -name '\*.pp' -exec puppet-lint --only-checks ghostbuster\_classes,ghostbuster\_defines,ghostbuster\_facts,ghostbuster\_files,ghostbuster\_functions,ghostbuster\_hiera\_files,ghostbuster\_templates,ghostbuster\_types {} \\+|grep OURMODULE

Got some output! Are they correct?

> ./modules/OURMODULE/manifests/profile/apache.pp - WARNING: Class OURMODULE::Profile::Apache seems unused on line 6

But actually we have a role that contains:

> class { 'OURMODULE::profile::apache': }

So I'm not sure what is up... But if I don't run all the ghostbuster and instead skip the ghostbuster\_classes test I get a lot fewer warnings for our module.

> /modules/OURMODULE/manifests/profile/keystone/user.pp - WARNING: Define OURMODULE::Profile::Keystone::User seems unused on line 2

Looking in that one we have a "OURMODULE::profile::keystone::user" which calls keystone\_user and keystone\_user\_role. However we do call it but like this:

> OURMODULE::Profile::Keystone::User<| title == 'barbican' |>

Or in this other place:

> create\_resources(OURMODULE::profile::keystone::user, $users)

Let's look at the next. which was also a "create\_resources" . Meh. Same same. And if I skip the ghostbuster\_defines? No errors :) Well it was worth a shot. Some googling on the topic hints that it might not be possible with the way puppet works.
