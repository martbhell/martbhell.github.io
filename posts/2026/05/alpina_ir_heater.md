---
title: Alpina IR Heater
date: 2026-05-11 23:57
category: it
lang: fi
tags: ir, infrared, heater, flipper zero
<!-- prettier-ignore -->
---

## Alpina Infrared Heater 2000 W

Ostin tämä terassille vuosi sitten, toiminut ihan OK. No, paitse että sulake trippaa ekä kerttaa joka kerttaa kun painan
"yksi" (laittaa se päällää), mutta toinen kerttaa se toimii..

1. paina "1" kaukosäädin
2. Sulake trippaa
3. Flippaan sulake takaisin
4. paina "1" : laite alkaa lämmittää

Anyway, aihe tästä postista on että pelkäsin että hukasin kaukosäätimen.

Käytin [flipper zero](https://flipper.net/) IR lukija.

Output infrared kerttoo että protocol on `NEC`, osoite on `00 00 00 00` ja command on kuin:

- Power On: `0D 00 00 00`
- Taso 1: `40 00 00 00`
- Taso 2 (lämpömämpi): `43 00 00 00`

[extras/Heater.ir](extras/Heater.ir) [Heater.ir](Heater.ir)
