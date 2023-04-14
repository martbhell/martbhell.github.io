---
title: "Customized WebMail Notifier (x-notifier) Script for Squirrelmail"
date: 2011-01-26
categories: 
  - "it"
tags: 
  - "firefox"
  - "script"
  - "squirrelmail"
  - "webmail"
  - "webmail-notifier"
---

I use the [WebMail Notifier](http://webmailnotifier.mozdev.org/ "webmail notifier") / or as it's nowadays called - the X-notifier plugin in Firefox to see if I have gotten any new e-mails.

The standard ones - gmail or hotmail works great, but there are also [scripts](http://webmailnotifier.mozdev.org/scripts/ "webmail scripts") ([xnotifier scripts here](http://xnotifier.tobwithu.com/scripts.php "http://xnotifier.tobwithu.com/scripts.php")) to make this work with your own - or other e-mails based on other e-mail servers, for example Squirrelmail.

To customize this to work with your own setup you may need to change the script available on the link above (as of version 2011-01-04).

If your squirrelmail web server enforces https and is installed on for example https://guldmyr.com/squirrelmail and not https://guldmyr.com/src (which the script by default assumes), you will have to alter the script.

I had to change this function in the code to make it work:

``function init(){ if(this.server){ if(this.server.indexOf("**`https`**")!=0)this.server="**https**://"+this.server; if(this.server.charAt(this.server.length-1)=="/")this.server=this.server.substring(0,this.server.length-1); }else if(this.user.indexOf("@")!=-1)this.server="**https://mail.**"+this.user.split("@")[1]; this.loginData=[this.server+"**/squirrelmail/**src/redirect.php","login_username", "secretkey",]; this.dataURL=this.server+"**/squirrelmail/**src/left_main.php"; this.mailURL=this.server+"**/squirrelmail/**src/webmail.php"; }``

The WebMail notifier script [squirrelmail\_guldmyr](../wp-content/uploads/squirrelmail_guldmyr.js)

The X-Notifier script [squirrelmail\_guldmyr\_xnotifier](http://www.guldmyr.com/blog/wp-content/uploads/squirrelmail_guldmyr_xnotifier.js)
