---
title: Prometheus and SNMP from a printer
date: 2021-04-07
category: it
tags: monitoring, printer, prometheus, snmp
<!-- prettier-ignore -->
---

The other week I finally for this thing working I've been trying weakly to do every now and then when I had a few
minutes free: send an alert before a toner runs out in a printer!

Way back I set up [SNMP_exporter](https://github.com/prometheus/snmp_exporter) to fetch metrics from switches. This
worked very nicely. ( In retrospect this works nicely because it's the default type of device )

But for printers we didn't get much useful data out. Even though we use the vanilla upstream
[snmp.yml](https://github.com/prometheus/snmp_exporter/blob/main/snmp.yml) which has printer stuff in it. And when I did
an snmpwalk I did manage with some research to find the correct OIDs to query to get the level of ink in the toners. So
I knew the printer did publish the information I was looking for.

The answer? Select a **module** when sending the request to the exporter! I didn't select **printer_mib** so it used
if_mib that only has interface statistics.

What would have helped? Not suing the vanilla (large) snmp.yml and only use a custom one that has the data we wanted..

Printers are no fun :/

Prometheus is!
