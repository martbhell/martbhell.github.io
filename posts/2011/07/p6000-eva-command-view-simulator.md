---
title: P6000 - EVA - Command View Simulator
date: 2011-07-18
category: storage
tags: command, view, command, view, simulator, cv, cv, simulator, cvutil, disk, array, eva, firmware, hp, hsv300, p6000, simulator, sssu, storage, xcs

[https://h20392.www2.hp.com/portal/swdepot/displayProductInfo.do?productNumber=P6000EVASimulator](https://h20392.www2.hp.com/portal/swdepot/displayProductInfo.do?productNumber=P6000EVASimulator)

Command View EVA is HP's web based management tool for their EVA/P6000 products. It's been looking the same for quite some time except the quite old ones. It's simple to use compared to other management softwares but sure it has its limitations too. It's not based on JAVA anyway :)

# Install

Run the install file, this extracted the files but then it said something about it not being correctly installed. I then went to the folder and started the install manually. This completed after a while. After this:

To run it in Windows 7 x64:

Go to start menu -> accessories -> right-click on Command Prompt -> choose "run as Administrator".

In there type: cd C:\\Program Files (x86)\\Hewlett-Packard\\HP P6000 EVA Simulator\\evasim

Then hit: setup\_cv\_env.bat wait for it to complete

Then hit: start\_bundle.bat

Which will start the simulation services and open a web browser (IE for me even if Firefox is default). It looks like it works fine in Firefox 7 too - just surf to . There is no password required when logging in manually.

IE9 will complain about certificate, say that you agree and then you're in!

# Use

Well, this is where you learn how to do the things in Command View.

For example, create a vdisk, create a replication group, try out continuous access (data replication) and business copy (snapshots, clones). It's really like the real deal except that probably the error logs aren't there and you can't really present any disks to a host. But you can do everything simulated anyway :)

The firmware in the simulator is 10000090 (or CD1528lesl-10000090 ) on HSV300. A pre-release of the XCS firmware? Also the 6100/8100 EVAs in the simulator is on 6.220 - why not on 6.240?

Also do try the SSSU it is installed here C:\\Program Files (x86)\\Hewlett-Packard\\HP P6000 EVA Simulator\\evasim\\cveva and it works. So you can try scripting, try out scripts before you actually run them in your production system and stuff like that.

Even cvutil is installed. In the same directory as SSSU, just hit 'cvutil paths' for example to see the paths your machine has to the EVAs.

To shut down the simulator you can type 'exit' in the command windows that are opened by the software. Or just hit CTRL+C or the X in the window :)
