---
title: Raspberry Pi 4 verkkoyhteyden katkeaminen
date: 2024-01-29 22:03
category: it
tags: it, network, rpi, raspberry pi, raspberry pi 4, eee, bcmgenet, eth0
lang: fi
---

## Mitä tapahtui

Langalla verkkoyhteys kotona katkkeili usein. Yleensä ei ollut ongelmä mutta pikkuhiljaa puskurointi ei auttanut enää.

Tämä oli näkyvissä `dmesg -T`:

```bash
[Mon Jan 22 20:48:23 2024] bcmgenet fd580000.ethernet eth0: Link is Down
[Mon Jan 22 20:48:34 2024] bcmgenet fd580000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
```

## Yritetään

- Poista wifi ja bluetooth käytöstä (lisää seuraava /boot/config.txt-tiedostoon):

```bash
[all]
dtoverlay=disable-wifi
dtoverlay=disable-bt
```

- Poista eee käytöstä, muokkaa /etc/rc.local-tiedostoa:

```bash
/usr/sbin/ethtool --set-eee eth0 eee off
exit 0
```

## Mitä oikeasti auttoi lopulta

_Muut keinot auttoivat myös, mutta lopulta ongelma ratkesi seuraavasti:_

- Varimsta, että kaapeli on hyvin kiinnitetty kytkimeen; omassa kaapelissani muovien lukitusklipsi oli ilmeisesti rikki, ja kaapeli pääsi liukumaan ulos portista!
