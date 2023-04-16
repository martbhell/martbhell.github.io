---
title: Command View P6000 EVA Simulator 10.0
date: 2013-04-24
category: it, storage
tags: command, view, command, view, simulator, cv, cv, simulator, cvutil, disk, array, eva, firmware, hp, hsv300, p6000, simulator, sssu, storage, xcs

Due to somewhat popular demand here's another post detailing the steps for somewhat successfully installing HP P6000 Command View Simulator on Windows 7 x64. It can be a bitch.

The [older post](http://www.guldmyr.com/p6000-eva-command-view-simulator/) is from 2011 with CV 9.4, this one also has PA - performance advisory bundled.

- Download: [http://software.hp.com](http://software.hp.com/ "http://software.hp.com/")
- Two files: EVA Simulator 10.0 (Z7550-00252\_EvasimInstaller\_100fr\_v1.exe) and a readme
- There is an e-mail listed in the readme!
    - But if you want to, you can put in a comment below saying how sexy I am :p
- The readme is quite long but most of it is about how to use the PA (performance analyzer), Appendix B is a required read. It describes how to add the Groups so you can log on to CV.
    - A [previous blog](http://www.guldmyr.com/to-create-a-new-user-group-in-windows-7/) post by myself truly also goes through how to add a user group :)

## For lazy hounds:

1. _(optional)_ Disable UAC in Windows and make yourself admin.
2. Put an account in the Windows Group called "HP Storage Admins".
3. Launch the downloaded file (it extracts a setup.exe and .msi file)
4. Launch setup.exe - it's located in the same directory where you launched the Z7550-00252\_EvasimInstaller\_100fr\_v1.exe
5. Next, next, next, next, yes, yes, Wait, yes, Installed!
6. Try out the "Start HP P6000 EVA Simulator" new icon on your desktop, does it work? Profit!

"XF application has stopped working" - some friendly error I got and CV simulator did not start.. Most likely permission issue. Peaking through one of the command-prompts it repeats access denied.

It's amazing that the CV simulator still relies on .bat scripts. Guess it's for backwards compatibility with XP and Vista? Only one file necessary for all those Windows OS variants.

With default Windows security, the Simulator runs into a problem when it tries to write to files under c:\\program files (x86)\\ . There are probably many ways to remedy that, one might be step 1 above. This worked:

1. Go to C:\\Program Files (x86)\\Hewlett-Packard\\HP P6000 EVA Simulator\\evasim
2. Right-click on 'start\_bundle.bat' and run it as an administrator. This should start the simulator.
3. Open up a command prompt with Admin Privileges, cd your way into evasim directory and type: "start startcv.bat"
4. That should launch the Command View process and also IE pointing to CV.
5. If not, point your web-browser to: https://localhost:2374/SPoG/ or https://localhost:2374/
6. Log in with the user/password you added into the "HP Storage Admins" group earlier.

## Some tips:

In one of the "DOS" windows, there might be more clues as to what's going on.

Open a command prompt with admin privilieges by typing "cmd" in the search bar then right-clicking and starting as administrator.

Inside the Simulator DOS prompt you can hit enter and if you see some commands (save, stop, exit, start) then that's the simulator window.

If you want your changes to be kept, type "save" in the simulator window before quitting.

## Some thoughts:

It feels a bit ruggish. I bet this whole mess could be improved quite easily with some decent scripts. Here's one I'd like to see:

if $os == Win7:
    if $write\_read\_permissions\_in\_program\_files != "allowed":
        print\_in\_big\_letter("You need more axx! Do $THIS")
        exit\_everything\_and\_die
