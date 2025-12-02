---
title: Disobey 2025 Loihde Challenges
date: 2025-03-10
category: it
lang: en
tags: ctf, disobey, disobey2025, hacking, hacker, reverse, rev, reverse engineering, radare2, r2
<!-- prettier-ignore -->
---

[Loihde](https://www.loihde.com/en/media/blog/disobey-2025-ctf-walkthrough-for-loihde-challenge?hs_amp=true) had a great
CTF :)

- It got me doing something physical and talking to people.
- I also got to learn about $MFT / some kind of NTFS metadata (also contained whole files if the files are small
  enough?)
- That it's very nice with a team. Case in point: I was trying to discover the password to login to a place, I even had
  the laptop in my hands. But I didn't actually try anything.. just looking for things and _maybe_ (not necessarily..)
  writing them down. Other team member sent picture of the possible password to another teammate that tested it and got
  in!

The final challenge of the CTF about needing to reverse engineer a binary.

The walkthrough in the link up top goes through it. I did not figure it out. **Just that 1234 was a bad password.**

I even tried to bruteforce it for a little while but yeah I didn't have that exact shrug emoji in there :D

This is quite a perfect simpler type of reverse engineer excercise / walk through.

I should try more these types of challenges to get more used to the tools and even find write-ups walkthroughs and try
to follow them just to get the basics down.

Basically walkthrough has two paths:

- use the `iz` command in radare2. It can show strings that `strings` can't.
- use gdb and breakpoint right when it's about to compare the password to the secret. Then print the registers.

## Radare2 Commands

Some radare2 stuff that I forget between the events:

`r2 -A`

Useful commands:

- `aaaa`
- `vv`: Show a linear disassembly
- `VV`: Graphs - show which functions are connected. [binary ninja](https://cloud.binary.ninja/) was also pretty useful
  to visualize it. But `VV` is a great starting point.
- `/ /root/flag.txt`: Find if /root/flag.txt about where it's used
- If ^^ returns an address hit for example `axt 0x0040308c` to see where it's called from
- `iz` prints strings in data section
