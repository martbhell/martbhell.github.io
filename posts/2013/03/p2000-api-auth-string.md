---
title: P2000 API Auth String
date: 2013-03-05
category: it
tags: api, dothill, md5, monitoring, p2000, perl
<!-- prettier-ignore -->
---

Ever wanted to do monitoring of a P2000 or MSA2000 from HP?

They are in secret Dot Hill hardware, for example DDN also resells these as for example EF3015.

There is a nice nagios script written by Tom <http://www.toms-blog.com/nagios-hp-msa-p2000-status-and-performance-monitor/>

To use that you need an API string which you can get from capturing traffic while logging in to the HTTP interface.

Another way to get the string is to run this perl code that gets the md5sum out of `manage_!manage` which is the default username and password:

```bash
# !/usr/bin/perl

use Digest::MD5 qw(md5_hex);
# generate MD5 hash using default username/password
my $md5_data = "manage_!manage";

# replace !manage with the new password in case you change the password
my $md5_hash = md5_hex( $md5_data );
print "$md5_hash\\n";
```

Code borrowed from "HP P2000 G3 MSA System CLI Reference Guide" <http://bizsupport1.austin.hp.com/bc/docs/support/SupportManual/c02520779/c02520779.pdf>
