---
title: Frustration?
date: 2011-06-20
category: it
tags: firmware, it, itrc, learning, upgrade
<!-- prettier-ignore -->
---

This is from a post on the ITRC forum, I will copy it into here because the
forum are moving soon and you never know if the links will work or not :) Also I
do want to immortalize it.

Title: **Is it just me? Or does everything required a fw update?**

Begins with some posts with some people never having any problems and some
people who have had. Then gregersenj posted what I have pasted below, which is
just a very honest and in my opinion accurate view of daily IT life. It may not
be what others want to hear, maybe especially the people paying for the
IT-services. But I believe nobody understands the **whole** picture in an
IT-system. You may believe a lot but for everybody there are some areas that you
don't understand _completely_. Like drivers, kernel, just as an example.

<table border="0" cellspacing="1" cellpadding="4" width="560" bgcolor="#CCCCCC"><tbody><tr bgcolor="#E7E7E7"><td align="LEFT" valign="TOP">gregersenj</td><td align="LEFT" valign="TOP"><table border="0" cellspacing="0" cellpadding="0" width="100%"><tbody><tr><td valign="bottom">Jun 18, 2011 13:24:53 GMT&nbsp; &nbsp;&nbsp;Unassigned</td><td align="RIGHT"></td></tr></tbody></table><div></div><hr size="1" noshade="noshade"><div></div><table><tbody><tr><td id="tdIdName5">Frustration allways come from 2 reasons. 1. Lack of knowledge. 2. "Religion" 1 often lead to 2. And that lead to Frustration.&nbsp;<div></div>Things to realize: There's no 100% uptime. There's nothing bug free. There's allways a risk.<div></div>Ralize the aboave, and learn how stuff works.<div></div>I don't got a lot of knowledge on the Itanium/PA risc systems. But, on some RX26xx model(s) you mst enable the embedded smart array controller from the EFI.<div></div>OA and ILo is a on-line, non-disruptive upgrades. A backup of the OA configuration is recommended, just in case.<div></div>Interconnect modules can be upgraded on-line. On-line FW upgrades neee a reboot to activate new FW. VCSU upgrade modules, then reboot them 1 by 1. Do you trust your enviroment? Do you want to take the risk?<div></div>Yes, the blade must be powered off to activate a profile. I don't know why, but I believe that the engineers have a good reason.<div></div>I will recommend you to create a FW anf Driver base line, and ensure, that you are allways within supportet release sets.<div></div>Most release notes do say upgrade at earliest convinience.<div></div>I learn new stuff every day, and the more I learn, the less knowledge I blieve that I have.<div></div>Theory is: It don't work, but we know why. Real life is: It work, but we don't know why.<div></div>Wish you a lot of fun learning, and hope you get less frustratet.<div></div>BR /jag</td></tr></tbody></table></td></tr></tbody></table> <!-- markdownlint-disable MD013 MD033 -->
