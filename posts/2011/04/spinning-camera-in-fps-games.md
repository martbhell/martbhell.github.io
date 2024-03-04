---
title: Spinning Camera in FPS games
date: 2011-04-21
category: it
tags: ati, call, of, duty, camera, camera, spin, cod, fps, games, logitech, mouse, mouse, spin, pc, portal2, spinning, spinning, camera, spinning, mouse, steam, windows, windows7
<!-- prettier-ignore -->
---

Ever experienced this relatively frustrating phenomena?

My setup:

Windows 7 x64 with an ATI Card HD5700 series. A logitech wireless
keyboard+mouse.

Camera just keeps on spinning and if you move the mouse it changes pitch, speed
or whatever.

Things to try:

- Got a joypad/joystick in the vicinity? Plug it out.
- Got a bluetooth thing and a controller nearby? Disable bluetooth.
- When it's spinning you can try plugging out your mouse/kebyoard/joypad to see
  if it stops then.
- Update graphics drivers
- Try with a wire (cheap as you can find) keyboard and mouse.

I had been runnnig synergy for a week or so, this is an application for
controlling the mouse on another computer - over your network - by just dragging
the cursor to the edge of your screen. Was working fine, I had it running while
playing Portal 2, Call of Duty, Crysis. Working fine except that it minimized
the game when I was at the edge..

Then I decided to update Windows with Windows Update (bunch of security fixes
only..) and new AMD/ATI Drivers for my HD5770 card.

Then suddenly it started (the updates required reboots).

I rolled back driver, unplugged mouse/keyboard, rebooted a couple of times. Went
through the windows update. Killed synergy - by default even if you run a
program in full screen it will switch over to the other monitor, which is not so
awesome because it minimizes games like Portal 2. I scoured the
[Steam Forums](http://forums.steampowered.com/ "steam forums") but nothing that
helped.

In the end I found a 'synergys' process running even though the service was
disabled and stopped. To stop it I had to select the "view processes for all
users" and then end it.

Then whoop! No more spinning! I suspect it may have been the same even with the
updates if I had just done a reboot.
