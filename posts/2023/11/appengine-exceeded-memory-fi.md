---
title: Google AppEngine Exceeded hard memory limit of
date: 2023-11-27 11:57
category: it
lang: fi
tags: wtangy, nhl, gae, google, gcs, grafana, google app engine, python, gunicorn, wasthereannhlgamelastnight
<!-- prettier-ignore -->
---

Oletko näyhnyt tälläisiä viestiä Googlen AppEnginen logissa? Onko sinun palvelu hidas?

```bash
10:22:23.481686Z Exceeded hard memory limit of 384 MiB with 400 MiB after servicing 3 requests total. Consider setting a larger instance class in app.yaml.
10:18:23.473577Z Exceeded hard memory limit of 384 MiB with 393 MiB after servicing 7 requests total. Consider setting a larger instance class in app.yaml.
```

Näin nämä kun:

- Google's AppEngine ja Python Flask
- Yritän käyttää vaan Free Tier (ja dynamisia instansseja **F1**).

Ei vaan koska olen kitsas mutta vaan että [wtangy.se](https://wtangy.se/) on harrasteprojektti ja yritän pitää se ylös
ilman liikaa raha. Tällä hetkellä vaan domääni tarvitse raha.

Yritin ensin käytää [tracing](https://cloud.google.com/trace/docs/setup/python-ot) / opentelemetry, mutta se ei toimii
niin hyvin.

Tällä hetkellä saan mitä tarvitsen loggista, jos haluan tiettää kuinka kauan jotain tarvii voin vaan laskea se koodissa
ja lähettä se loggiin.

Tracing olisi kiva mutta se ei laitoi "span" kaikiessa paikassa kun yritin. Varmasti enemmän aika sinne saa se toimiva.
Ja ehkä myös oma jaeger olisi myös hyvä, että voi lähettää ihan kaikki sinne ja ei yritää käydä ilmainen Google
Monitoring jutut.

Nyt en muistaa miksi, mutta luin "appengine" python
[runtime dokumentaatio](https://cloud.google.com/appengine/docs/standard/python3/runtime#entrypoint_best_practices), ja
näin siellä yks taulu missä kerttoo kuinka monta guniorn workers sopii mille instanssi tyypille.

Ja en pitäinyt käyttää default - 4 workers koska **F1** on liian pieni. 2 olisi sopiva.

Näin massiivi nopeutus! Ennen oli aina > 300ms ja yleensä yli 5s per request. Nyt se on aika nopea. Aina < 250ms

## ennen (Y on sekunttia)

[![before](images/wtangy_before.png "before_latency")](images/wtangy_before.png)

## jälkeen

[![after](images/wtangy_after.png "after_latency")](images/wtangy_after.png)
