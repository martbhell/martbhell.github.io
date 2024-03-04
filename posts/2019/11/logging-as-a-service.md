---
title: Logging as a Service
date: 2019-11-12
category: it
tags: logging, laas, system
<!-- prettier-ignore -->
---

Is there an open source thing out there I could use??

So if I only want to use mostly free and open source it there's a bunch of tools
one need to glue together:

These days I'd like to for primary ingestion have a BGP ECMP/anycast for rsyslog
receivers. These also run logstash (or beat?). Or maybe one can have a load
balancer up front which redirects traffic based on incoming port (and maybe a
syslog tag for some 'authentication' ? ) to a set of logparsing/rsyslog servers.

These would write to a Kafka cluster.

Then we would need more readers to stream events on to elastic, siems or Hadoop
or for example longer term storage engines.

For the as a Service bit I'd like to play with Rundeck and have users configure
most of the bits themselves. Logstash grokking/parsing though needs outsourcing
too. Fewer rules means more throughput so would be good with different logstash
processes for different logs. Could like loggly direct users to ship logs with a
tag to get them into the correct lane.

For reading just grafana and kibana should be a good start.
