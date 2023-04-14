---
title: "LSC  - LDAP Synchronization Connector"
date: 2021-09-28
categories: 
  - "it"
tags: 
  - "java"
  - "ldap"
  - "sync"
  - "synchronization"
---

At $dayjob I recently found this tool.

[https://lsc-project.org/doku.php](https://lsc-project.org/doku.php)

Use case was a workaround to get our good old posixGroups into groupOfNames; because some tools like bitwarden on premise requires that members of the groups are DNs for them to be able to figure out who's member of what group.

Got it working pretty nicely after [learning](https://lsc-project.org/documentation/tutorial/synchronizeposixgroupstogroupofnames) some fun things like:

- settings in the lsc.xml have to be in the correct order
- Connection settings in [documentation](https://lsc-project.org/documentation/2.0/configuration/connections/ldap) listed as mandatory, are not mandatory (as in don't have to be explicitly defined in the lsc.xml).
- LSC 2.1 requires java8 :(

För monitoring it, I opted to parse the output of the tool rather than reading the log file. There's a nice logback.xml one probably could use to improve this bit. Maybe somehow log to JSON or some such to get machine readable output?
