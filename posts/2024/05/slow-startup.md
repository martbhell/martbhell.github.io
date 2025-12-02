---
title: Slow Startup?
date: 2024-05-05 22:57
category: it
lang: en
tags: windows, windows 10, proxy, slow, startup
<!-- prettier-ignore -->
---

## Slow Startup

Does this happen on your computer?

- After starting start menu / task bar might become unresponsive
- After opening browser it takes a while (lots of seconds) before pages starts to load

## Try these things

- It is often/always DNS. Is one of the DNS server your computer is set to use perhaps no longer working? That'd sure
  make things slower.
- Except when it's not. Is your computer setup to use a proxy server? For me unticking the "automatically detect proxy
  settings" did the trick. I'm using a
  [setup script](https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_PAC_file).
