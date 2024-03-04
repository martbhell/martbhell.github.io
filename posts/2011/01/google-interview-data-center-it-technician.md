---
title: Google Interview - Data Center IT Technician
date: 2011-01-21
category: finland, it, storage
tags: data, center, data, center, technician, data, centre, datacenter, datacentre, google, hamina, interview, it, job, questions
<!-- prettier-ignore -->
---

- Updated 2011-01-29
- Updated 2011-03-08 Dtek contributed some more questions from the first
  interview.
- Updated 2011-03-23 - Added question about PCI/PCIe and DOS partitions. **Also
  I have been asking the few who have commented to add their input but not so
  much feedback yet. Feel free to drop me an e-mail or put in a comment :)**
- Updated 2011-03-24 - Wrote a little more about the '100 broken computers'
  question.
- Updated 2011-05-21 - Added some more detail/discussion about the questions in
  the first section.

A little while ago I had an interview for a position with Google as a Data
Center IT Technician, I never signed an NDA so should be safe to put them up
here :)

However, if you want to play it safe I'd refrain from posting here until after
the interviews are over.

I didn't get the job, they never answered why I didn't pass when I replied back
for some feedback (besides the template e-mail).

If you read this go ahead and comment, maybe we can figure out a better way to
approach the questions :)

## First Interview

First there was one interview which had 20 questions (I don't remember all)
around basic (older - like no SATA) PC stuff: **What are all the components in a
PC or Server?** PC: chassi, system board, psu, cpu, ram, hdd, fans, cables,
graphics card, dvd, monitor, keyboard/mouse Server: same with deduction of a
extra graphics card (is one on the system board), and addition of hdd
controller, possibly backplane, no cd/dvd, extra nic, double cpu, ram, psu,
fans, remote monitoring/console.

- **What protocol is used by ping?** \-
  [ICMP](http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol "ICMP")
  (this is a sneaky question - an obvious fault is to go for TCP or UDP)
- **How many IDE devices can you have in a PC?** \- two per channel (usually 4)
- **How many can you have on each channel? What are they called?** \- 2 / master
  and slave
- **What is the resolution in Windows 2000 safe mode?** - 800x600 or 640x480?-
  see
  [this link](http://www.mydigitallife.info/2008/06/22/how-to-change-screen-resolution-and-display-colors-quality-in-safe-mode-of-windows/ "windows safe mode resolution")
  on mydigitallife or
  [this post](http://www.tomshardware.co.uk/forum/34809-35-screen-resolution-safe-mode "screen resolutino safe mode")
  on tom's hardware.
- **What is a MAC address?** -
  [Media Access Control](http://en.wikipedia.org/wiki/MAC_address "wikipedia link") -
  a unique identifier for network devices. Used by many protocols.
- **What is the name of the Ethernet plug?** -
  [RJ45](http://en.wikipedia.org/wiki/RJ45 "RJ45 on wikipedia")
- **How do you recognize a broken hard drive without software or removing it
  from the machine?** - 1) Noise (tick tack sound of the arm getting
  stuck/hitting something) 2) Any leds on the disk, system board, controller 3)
  Any vibration or anything from the disk?
- **How do you find the first disk in a linux OS?** - Look under /dev/ for a
  disk like /dev/sda(SATA) /dev/hda (PATA). Then /dev/sda1 is the first
  partition.
- **Name two devices needed to make a network:** switch and router (well,
  network card (NIC) and router should do it, or a switch and network card..
  depends how big you want to make it, really i guess you can have a network
  with a crossover cable and two nics).
- **What is BIOS?** Basic input/output system. Responsible for initializing
  hardware, POST/startup diagnostics, boot the OS and varies hardware settings.
- **What is the bit rate of a serial interface of a network device?** \- the
  default apparently in hyperterminal - 9600 (this might be tricky, in my
  experience this varies between the devices - max is probably 115200bps). Maybe
  what they are asking for is what is the
  [default speed](http://www.cisco.com/en/US/products/hw/switches/ps700/products_tech_note09186a008010ff7a.shtml#connecttermtocat "cisco catalyst console port")
  of a Cisco switch's aux or console port? If so, the answer is 9600.
- **What is the port used for HTTP?** - 80
- **What is the difference between PCIe and PCI?** \- PCI-e is newer than PCI
  and PCI-x. The slots look different and they are not compatible.
- **How many primary partitions can you have in DOS?** - Four primary and
  maximum one active per disk. See
  [this link](http://www.pcguide.com/ref/hdd/file/structPartitions-c.html "dos partitions")
  for some explanations. Unsure at this stage what the exact question was.
- **What did you do in your previous jobs?**
- **Would you be able to re-locate?**

- **What does HTTP stand for?** Hypertext Transfer Protocol
- **What controls GPU CPU Mem at boot up? What is ROM?** Read Only Memory - Used
  for storing data that you do not want somebody to write to.

- **Length of cat5 transmission?** 100m
- **What does NIC stand for?** Network Interface Card

- **What is the standard type of filesystems now?**
  [disk filesystem](http://en.wikipedia.org/wiki/Filesystem#Types_of_file_systems) and network
  filesystems
- **How would you create an EXT4 filesystem on the first partition of the first
  SCSI drive?** mkfs.ext4 /dev/sda1
- **How would you install lilo?**
- **How do you get IP info from Linux or Windows?** "ip addr" or "ifconfig" in
  Linux and "ipconfig" in Windows.
- **What is the subnet mask for a Class B Network?** 255.255.0.0

## Second Interview

Then there was a second one that was done by a person who worked in a data
center and had questions like these:

**You have 100 broken computers, how do you proceed.** Personally I didn't do
very well on this question I think. There are lots of ways to approach this one,
how far can you take it? One way to make this a little easier/visible would be
to make a tree or
[mindmap](http://en.wikipedia.org/wiki/Mind_map "mindmap on wikipedia") and keep
on expanding it.

But thinking about this afterwards I would probably approach it something like
this, (not necessarily in this order):

1. Get an overview - where are they, what kind of hardware, importance, severity
   of problem, the wider you can make this the better. To have this done
   automagically is important and speeds up troubleshooting immensely. Consider
   monitoring softwares like nagios, ganglia, cactii. They not only monitor
   hardware but can also services.
2. What's the status of the central components? Network, power, etc.
3. Hopefully not all have the same problem, try to find certain groups of them
   that have the same obvious error.
4. Maybe there are more than one underlying issues, but they appear to be the
   same - or gives the same problem.
5. Maybe there is one problem on one computer that is causing problem for all
   the rest. For example bad ethernet/fibre channel card or cable can cause
   network interruptions on the whole network or SAN.
6. Maybe a service and there is something in that software on one node that is
   causing this issue. Like a job that runs on many machines but it broke on one
   machine and that caused the rest to break.
7. Look in logs of the systems/services.
8. Run a diagnostic CD on computers like ultimateboot CD to look for hardware
   errors. Server vendors may have their own diagnostic tools. memtest86 is a
   good boot CD for memory testing (probably best to test memory that way, the
   least amount of memory locked by the OS)
9. For severe hardware problems you can look in the POST of the machine, check
   leds on them, but for 100 machines this might be more of a last resort.
10. If you suspect the problem is SW - again try to find something they have in
    common - same manufacturer, same softwares/patches installed. Maybe this
    software has a monitoring part that can tell you more. Check the logs.
11. When did the problem start? At the same time as a power outage, after a
    patch deployment, etc.
12. Are they all physically close? Anything else gone down?

- **How do you see what happens during boot of the OS in Linux?** Answer: output
  of command dmesg and also in /var/log/syslog
- **Where do you find the logs in Linux?** Answer: /var/log
- **How do you mount a disk?** Answer: mount
- **Every boot?** Answer: fstab
- **How do you see what version of the kernel is running?** Answer:  uname -v
  (-r gives 2.6.x etc)
- **How do you put an image on a pc?** Answer: pxeboot as an example
- **How do you turn a room into a data center?**

Maybe something like this? If you have any additions please go ahead and let me
know :)

floor strong enough to hold the weight of all the equipment? physical security -
bar windows, access control(keys), cameras, guards ventilation - perforated
tiles? cooling anti-fire racks UPS - electrical work

- **What is the difference between a switch and a router** said that the diff is
  that switches are closer to the hosts and the routers are further away -> in
  the core
- **Did you have experience writing documents - kb?**
- **Worst job you ever had?**
- **What do you expect from your colleagues and your boss?**
- **What do you do outside work? Do you have any questions?**
