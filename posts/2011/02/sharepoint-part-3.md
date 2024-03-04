---
title: Sharepoint - Part 3
date: 2011-02-04
category: it
tags: it, sharepoint, vmware, workstation, windows
<!-- prettier-ignore -->
---

The previous posts: [Part 1](https://www.guldmyr.com/sharepoint-2010-foundation-windows-2008-r2-vmware-workstation/ "sharepoint part 1") \- installing Sharepoint 2010 Foundation. [Part 2](https://www.guldmyr.com/sharepoint-2010-foundation-part-2/ "sharepoint par t2") - basic features in the web interface.

I said I was going to look into the RSS updates, how to manually edit the database and look into the underlying structure of the Sharepoint. But, only went through the last of the obvious administration tools :p

## Other management tools

Under the start menu there are three new programs:

### Central Administration -

This opens a page to `http://win2k8:48820/default.aspx` - I could log on with my extra account (the one with admin/owner privileges).

The sections are:

### Application Management

Manage web apps, create site collections, service apps, content databases.

Under Manage Web apps there are some nice stuff you can change on each site. Select the site you want to work on and click on "General Settings".

The central admin is it's own site so by default there are two and the changes you make on one does not replicate over to the other one. For example you can set timezone, resource throttling, outgoing e-mail, workflow, enable/disable some features.

In the bar on the top there is the possibility to change policy settings.

Back one step to App Management there is the possibility to add more databases and database servers.

### System Settings

Manage farms and alternate access mappings. Like adding features and solutions, change outgoing e-mail settings (notifications)

### Backup and Restore

What ^^ says. "To recover the data, use the PowerShell restore command Restore-SPSite."

### Monitoring

Review problems and solutions, check job status.

### Security

manage farm admin group and configure service accounts

also you can specify anti-virus settings, block file types, and self-service site creation

### Upgrade and Migration

check product, patch and upgrade status for example you can see what versions you have installed: I have:

> Microsoft SharePoint Foundation 2010  - 14.0.4763.1000 Microsoft SharePoint Foundation 2010 1033 Lang Pack - 14.0.4763.1000 Microsoft SharePoint Foundation 2010 Core - 14.0.4763.1000

### General Application Settings

configure send to connections, convert document settings, report services,

### Configuration Wizards

none by default

## Management Shell

This did not work, gave me this error: "The local farm is not accessible. Cmdlets with FeatureDependencyId are not registered."
