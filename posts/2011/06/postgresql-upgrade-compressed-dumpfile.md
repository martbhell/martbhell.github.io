---
title: PostgreSQL upgrade - compressed dumpfile
date: 2011-06-19
category: it
tags: compression, database, linux, pgsql, postgres, postgresql, sql, upgrade
<!-- prettier-ignore -->
---

Why does a PostgreSQL upgrade require an export, uninstall, install and then import of the database? That big changes in
the database?

It would be nice to know how to import from a compressed archive, **anybody ever got this working?** If so, please leave
a comment! I've been googling my behind off but hasn't located one yet. And the
[pg_restore manual](http://www.postgresql.org/docs/8.4/static/app-pgrestore.html "on postgresql.org") says it should be
able to handle archives in the non-plain text format.

pg_dumpall |gzip > dumpall.gz

neither of these worked afterward the remove, install and initdb: pg_restore -Fc dumpall.gz pg_restore dumpall.gz

In the end I just decompressed the file and ran: psql -f dumpall

It would be nice to do because then you don't have to have as much free space available. The gzip compression took the
filesize down to 1G for an 8G dumpall.
