---
title: "HEPIX Spring 2011 – Day 2"
date: "2011-05-04"
categories: 
  - "it"
  - "storage"
tags: 
  - "cooling"
  - "cpu"
  - "cpu-naming"
  - "dell"
  - "disk-failures"
  - "drupal"
  - "green-it-cube"
  - "heat-exchanger"
  - "hepix"
  - "hepix-spring-2011"
  - "hs06"
  - "puppet"
  - "scientific-computing"
  - "synchrotron"
---

Guten aben!

Darmstadt is a very beautiful city. It's quite old and there are lots of parks and eh, cool, houses.

A person from the UK said yesterday (in the pub Ratkeller) something like this: _"A particle physicist's raison d'être is to find complexities, they wouldn't turn away from one if their life depended on it. These are the people we provide IT for."_

So no wonder that their IT systems/infrastructure is a little bit complex too!

Today's topics are: Site Reports, IT Infrastructure (Drupal, Indico, Invenio, Fair 3D cube) and Computing(OpenMP, CMS and Batch nodes).

### Site reports

Some of these institutions have a [synchrotron](http://en.wikipedia.org/wiki/Synchrotron "on wikipedia") which is a cyclic particle accelerator - looks quite cool on the pictures. Some use [cfengine](http://en.wikipedia.org/wiki/Cfengine "on wikipedia") for managing the clusters - as in they want to avoid logging on to each node and doing configuration but instead do it from a tool. One such tool that is quite common ([Puppet](http://en.wikipedia.org/wiki/Puppet_(software) "on wikipedia")) can also be used for Desktops.

Not many use HP storage stuff, [DDN](http://www.datadirectnet.com/ "datadirect.com") is quite common. [Nexsan](http://www.nexsan.com/ "nexsan.com"), [bluearc](http://bluearc.com/ ".com")

One site had big problems with their Dell servers - caused by misapplied cooling paste on the CPUs - Dell replaced 90% of the heatsinks and fixed this.

One also had disk failures during high load.They ran the [HS06](https://twiki.cern.ch/twiki/bin/view/FIOgroup/TsiBenchHEPSPECWlcg "on cern wiki") – Hep Spec 06 – test and while running that disks dropped off.Disk failures traced to anomalously high cooling fan vibration. After replacing all components, and then moving fans to another machine, they saw the error.

### IT Infrastructure

CERN is working on moving to Drupal for their web sites. Investigating Varnish (good for ddos, caching and load balancing). Drupal is hard to learn.

Then there were some sessions about programming - CMS 64-bit and OpenMP. One thought here: is it possible to discern the properties of an Intel/AMD CPU based on the name? Like E5530? Maybe [this link](http://www.intel.com/products/processor_number/ "on intel.com") on intel.com can be of some assistance.

#### Fair 3D Tier-0 Green-IT Cube

Quite cool concept(patented) that they are very soon starting to build here in Germany. Using water vaporization with outside air (and fans in summer) to cool the air, and also water based heat exchangers in each rack to push warm air (by pressure built up by fans, so the racks needs to be quite air tight) from the back of the servers through the heat exchanger that cools the air, and then pushes it over the aisle to the next row of racks. They managed to get down to a PUE of 1.062 at best.

Next Days: [Day 5](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-5/ "day5") [Day 4](http://www.guldmyr.com/blog/hepix-spring-2011-day-4/ "day4") [Day 3](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-3/ "day3")

[](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-2/ "day2")

Previous Day: [](http://www.guldmyr.com/blog/hepix-spring-2011-%e2%80%93-day-2/ "day2") [Day 1](http://www.guldmyr.com/blog/hepix-spring-2011-day-1/ "day1")
