---
title: BCFP - VF - Virtual Fabrics
date: 2011-07-30
category: finland
tags: bcfp, brocade, brocade, certified, fabric, professional, fabrics, san, storage, network, vf, virtual, fabrics

The free material does not go through the virtual fabrics and the [exam objectives](http://community.brocade.com/docs/DOC-2041 "bcfp 16g exam objectives") does not mention them specifically. Even so - it's probably a good idea to get some grip about it anyway as it is mentioned in the BCFP 8G material and there are questions concerning it in the Nutshell Guide and the BCFP 8 knowledge assessment. Also it is mentioned in the pre-requisites for the BCFP (the AFS 141).

[Brocade's overview page of Virtual Fabrics](http://www.brocade.com/solutions-technology/technology/platforms/fabric-os/virtual_fabrics.page "overview")[.](http://www.brocade.com/solutions-technology/technology/platforms/fabric-os/virtual_fabrics.page "overview")

 [FAQ on Virtual Fabrics](http://www.brocade.com/downloads/documents/faqs/FOS6%202_Virtual%20Fabrics%20FAQ%201-9-2009%20Final.pdf "faq")

There is also quite a lot of information about VF in the FOS Administration Guide. You can find this guide in lots of places but it is in the exam objectives in the link above.

## The theory

It is what it says it is - a way to create independent and logical fabrics and switches that you can use to segment your SAN. It does not require a license.

There's logical fabrics and logical switches.

From the FAQ: _A Logical Fabric is an implementation of a Fibre Channel fabric with one or more Logical_ _Switches participating in the fabric. A Logical Fabric has its own independent instance of_ _fabric services, name server, zoning database, and so on._

A logical switch needs a fabric id. Default is 128 but can be changed. Same FID cannot be used for same logical switch in the same chassi. You move ports from the default to the new switches. `VE_` and `EX_` ports needs to be configured after the move. LD, QoS, `F_port` buffers/trunking may not be enabled on the port.

Max 8 VFs in the DCX, enabling it is disruptive (requires a reboot).

DCX uses 10-bit addressing. Uses part of the last part of the ALPA part of the PID. Means that that part of the PID does not always indicate a port area. Increases limit of NPIV, support loop devices.

## Hardware

For 8G products it's available on the DCX, B5100 and the B5300. For 16G it's available on 6510, VA-40FC FC10-6, FS8-18, FCOE10-24 ports can only be part of the default switch.

## (X)ISL -- interconnecting switches

The default switch - is the first logical switch you create.

To connect a logical switch (henceforth known as LS) to another one you can just have one of the ports in the LS as an `E_port`, or you can use XISL - extended ISL.

To use XISL you designate one LS as a **base switch**. This is used for interconnects and you can have ISLs for several fabrics on this one port/cable. It can have E, VE and **EX, VEX** ports. `x_ports` can only be in the base switch. One base switch per chassi, on DCX platforms the default cannot be the base switch. You connect the base switch to other base switches and then the other logical switches with the same FID merge. By default the logical switches are enabled to use XISL. You can combine normal ISL and XISL. Normal ISL have a lower cost.

ISL (between physical switches) DISL (between Logical Switches) IFL (routing, not merging) XISL (several LISLs inside) LISL (part of an XISL)

With XISL a logical port is created, their WWN start with 5x.

## CLI

```bash
fosconfig --enable vf lscfg --create FID [-base] [-force];
setcontext FID;
swichdisable (set Domain ID etc);
configure;
switchenable lscfg --config 128 -slot <slot> -port <port>
lscfg --delete non-default-logical-switches
lscfg --show
lscfg --change 5 --newfid 7 (disables switch and sets it);
fosexec --fid FID -cmd "switchenable"`
```

```bash
fosexec --fid FID  -cmd "cmd" (how to run a command on another LS)
fosexec --fid all -cmd "cmd" (on all logical switches)
ipaddrset -ls 123 --add 10.10.10.10/24 (set an IP for a logical switch, to segment management)
```
