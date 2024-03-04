---
title: wtangy.se – site rename and automatic deployments!
date: 2017-10-25
category: finland
tags: appengine, google, nhl, travis, wasthereannhlgamelastnight, wtangy, wtangy, se
<!-- prettier-ignore -->
---

This is a good one!

Previous entries in this series: [https://www.guldmyr.com/wasthereannhlgamelastnight-com-now-using-object-storage/](https://www.guldmyr.com/wasthereannhlgamelastnight-com-now-using-object-storage/) and  [https://www.guldmyr.com/wasthereannhlgamelastnight-appspot-com-fixed-working-again/](https://www.guldmyr.com/wasthereannhlgamelastnight-appspot-com-fixed-working-again/)

# Renamed to wtangy.se

First things first! The website has been renamed to [wtangy.se](https://wtangy.se)! Nobody in their right mind would type out wasthereannhlgamelastnight.com.. so now it's an acronym of wasthereannhlgame**yesterday**. [wtangy.se](http://wtangy.se) . Using Sweden .se top level domain because there was an offer making it really cheap :)

# Automatic testing and deployment

Second important update is that now we do some [automatic testing and deployment.](https://github.com/martbhell/wasthereannhlgamelastnight/blob/master/.travis.yml)

This is done with [travis-ci.org](https://travis-ci.org/martbhell/wasthereannhlgamelastnight/builds) where one can view builds, the configuration is done in [this file.](https://github.com/martbhell/wasthereannhlgamelastnight/blob/master/.travis.yml)

In google cloud there's different _versions_ of the apps deployed. If we don't promote a version it will not be accessible from wtangy.se (or wasthereannhlgamelastnight.appspot.com) but via some other URL.

Right now the testing happens like this on every commit:

1. deploy the code to a _testing_ version (which we don't promote)
2. then we run some scripts:
    1. pylint on the python scripts
    2. an [end to end test](https://github.com/martbhell/wasthereannhlgamelastnight/blob/master/e2e_test.py) which tries to visit the website.
3. if the above succeeds we do deploy to master (which we do promote)
