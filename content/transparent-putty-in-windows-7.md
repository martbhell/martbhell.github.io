---
title: "Transparent PuTTY in Windows 7"
date: 2011-02-18
categories: 
  - "it"
tags: 
  - "appearance"
  - "auto-login"
  - "it-2"
  - "linux"
  - "putty"
  - "set-opacity"
  - "ssh"
  - "terminal-client"
  - "transparency"
  - "tray-icon"
  - "windows"
---

PuTTY is a terminal client, it does telnet, raw, serial, ssh, [rlogin](http://en.wikipedia.org/wiki/Rlogin "rlogin wikipedia"). I've only ever used telnet, raw, serial and ssh.

The normal client can be downloaded from [http://www.putty.nl](http://www.putty.nl "putty.nl")

But, maybe you want to make PuTTY prettier?

Like this?:

\[caption id="attachment\_414" align="alignnone" width="659"\][![putty pretty](images/putty2.png "putty2")](http://www.guldmyr.com/blog/wp-content/uploads/putty2.png) putty pretty\[/caption\]

Well, there are a couple of ways to get the transparency.

- Get a transparency tool for Windows or your OS that you can use to make anything transparent.
- If you are in Linux eterm does it - you just need to make some changes to the config.
- For Windows you can also download **[PuTTY Tray](https://puttytray.goeswhere.com "puttytray")**.

PuTTY Tray is still developed.

Go ahead and download PuTTY Tray, it will re-use the profiles you have already configured with normal PuTTY so don't worry about losing them.

If you have a profile already set up for PuTTY you can load it and then go and make the changes, don't forget to save it afterwards :)

Settings:

Window

- Deselect "show scrollbar" - (you can use shift+pageup/pagedown for that anyway)
- Set Opacity to 225 as a start - (you will probably alter this later)

Windows -> Appearance

- Set "gap between text and window edge" to 0

Window -> Behavior

What confused me was that by default PuTTY Tray sends the application to the tray, and not to the activity field. So I thought the program was terminating itself :)

- To have the program in the activity field you need to set the "show tray icon" to "Always"
- Also set "accept single-click to restore from tray".
- Full screen on alt-enter is also handy to enable here.

That's it!

Another thing I find handy to write in is to add an "auto-login username" under Connection -> Data. Saves a lot of time if you use the same username a lot.

I only have Windows 7 but I don't see why this would be different on Windows XP - excepting from the systray behavior then.

P.s. if you're on Windows 10 you can use Bash on Windows! Do iiit - much nicer than putty!
