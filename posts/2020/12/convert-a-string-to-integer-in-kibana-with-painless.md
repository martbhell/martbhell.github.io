---
title: Convert a string to integer in Kibana with painless
date: 2020-12-16
category: it
tags: kibana, painless, grok, apache
<!-- prettier-ignore -->
lang: en
---

if (doc\['bytes.keyword'\].size()!=0) {
    return Integer.parseInt(doc\['bytes.keyword'\].value)
}

This took me a while to figure out!

The above only works for Integer (so no 1.1 or 2.22).

It works on ELK 7.10

I needed it because I'm using %{COMBINEDAPACHELOG} GROK pattern.

That GROK pattern is built-in with logstash and just says NUMBER:bytes and number is (?:%{BASE10NUM})

[https://github.com/logstash-plugins/logstash-patterns-core/blob/master/patterns/httpd#L5](https://github.com/logstash-plugins/logstash-patterns-core/blob/master/patterns/httpd#L5)

There's actually a way to specify in the grok pattern that it's an integer:

%{NUMBER:field:integer}

[https://github.com/logstash-plugins/logstash-patterns-core/issues/173](https://github.com/logstash-plugins/logstash-patterns-core/issues/173) is an open issue from 2016 about this issue.

I guess what I should do is just make my own pattern with this fixed where I want it... I would really like to not fiddle with templates or add logstash mutate rules..
