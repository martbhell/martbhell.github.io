---
title: Sharepoint 2010 Foundation - Part 2
date: 2011-02-02
category: it
tags: it, sharepoint, vmware, workstation, windows
<!-- prettier-ignore -->
---

## Overview

See the
[installation guide](https://guldmyr.com/sharepoint-2010-foundation-windows-2008-r2-vmware-workstation "installation guide")
which I published recently.

This article is a brief look what to do in Sharepoint after it has been installed!

## Accounts

I don't want to log on with the built-in Administrator account anymore. Still no AD services installed. Created a new
standard account with no password - could not log on. Logged on with account and set a password - could log on but

**Error:** Access Denied

In computer management there are three new groups: WSS_ADMIN_WPG - write access to "system resources" for Sharepoint
Foundation WSS_WPG - read access to "system resources" for Sharepoint Foundation Added my new user to both - did not
work. Neither did if it's in "administrators" group. Then in side the web page, up in the left corner there is something
called "site actions". Added my new user as a member/contributor" and whoopsie now it can log in! This account can
however not see all the actions under "site actions". So put it in the "owner" group - and now the account can see most
of the settings.

- Now over to the fun stuff! All the things we can do inside the Sharepoint.

## Site Administration

Set locale, RSS (niice! don't think google reader will work for me), search/indexing (presuming robot.txt stuff),
workflow(maybe authoring - reviews etc of documents?)

## Site Features

You can create pages (wiki - so Sharepoint is like a wiki as well, never saw that part when I've used it before, I've
only used it to upload documents :) - anyway - nice). Calendar, lists, discussions, share documents (libraries), tasks,
announcements, links, surveys, subsites and workspaces.

### Change home page

Apparently some stuff requires me to install another Software - Sharepoint Designer. Free.

Anyway, you cannot go into pages and then click on Home to edit the front page. To edit the home page: go to the Home
Page click on -> site actions and then Edit Page.

In there it feels free, you can add pictures, write things, change font, size, color, etc and you can drag things
around.

## Galleries

Here you can make fancy changes to what appears to be relatively complicated things such as defining content types,
columns, templates, themes, master pages (default?) and dom-dom-dom Solutions.

## Looksie Feelsie

Here you can change name of sharepoint, customize the menu on the left or on the top (top appears to only be able to
give URL:s)

Stay tuned, there will be more things coming about Sharepoint! I will look into the RSS updates, how to manually edit
the database and look into the underlying structure of the Sharepoint.
