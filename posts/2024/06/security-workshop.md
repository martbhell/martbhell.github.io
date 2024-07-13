---
title: Arranging a CTF - a Security Workshop
date: 2024-07-15 22:57
category: it
lang: en
tags: ctf, capture the flag, security workshop, security, it security, workshop, training
<!-- prettier-ignore -->
---

I organized a cybersecurity workshop during my last few days at IQM. The
attendees included:

- Myself, taking on more of a coaching role and solving some challenges in
  advance to provide hints.
- Some participants who had attended my previous events.
- a few that had previously tried and solved security challenges.
- 4-5 newbies.

It would have been beneficial to have a CTF expert and someone for
documentation/write-ups to create a well-rounded team.

Organizing the event involved a lot of non-security-related tasks, such as
securing a budget, booking venues and food, and transporting equipment.

## Challenges

We used [Hacky Easter](https://www.hackyeaster.com/) challenges, since it was
still ongoing and no answers had been leaked.

### Quantum Challenges

I also had two Quantum Challenges, one from a hackthebox event called
[Cyper Apocalypse 2024](https://github.com/hackthebox/cyber-apocalypse-2024/tree/main/misc/%5BMedium%5D%20Quantum%20Conundrum),
where participants had to submit a set of gates that passed specific tests. This
used Qiskit. The test checked that the final values after the gates were the
same as the initial values.

The second quantum challenge was about having the Control Software deployed in a
"vulnerable" mode with outdated versions of one open-source component that had
Arbitrary File Read vulnerability. (coupled with flag.txt docker mounted in a
reasonable place).

This was surprisingly difficult to get _right_. Not easy to give enough hints as
to what might be wrong, but some were needed as the Control Software in question
had many many ports available for listening.

### Lockpick Challenge

I also introduced a lockpick challenge using transparent locks from China, and a
cheap tiny padlock from Claes Ohlson. Very fun to see that all got opened
without the keys.

## Final Thoughts

In the Hacky Easter we together made it to level 5 or just before. Impressive to
see people make it so far, myself I struggled with many for what felt like a
long time. Nonetheless, it demonstrated how a dedicated and diverse team can
achieve good progress.

Finally we concluded with a sauna session, beverages, and some multiplayer
games, giving the event a nice LAN party feel! Thanks everyone that participated
for making it enjoyable.

Personally, the security related preparation and organization was quite fun,
some initial feedback I got was that this was something one could be offered to
companies.
