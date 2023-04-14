---
title: "The bash shell - Linux terminal keyboard shortcuts"
date: 2011-04-13
categories: 
  - "it"
tags: 
  - "bash"
  - "bash-shell"
  - "console"
  - "keyboard-shortcuts"
  - "linux"
  - "shell"
  - "terminal"
---

Hey!

Recently found out that there are some quite awesome shortcuts available that I've missed - extremely useful if you use the bash shell in \*Nix.

To see which one you are using you can type 'chsh' in a terminal - this will tell you if you are using /bin/bash.

Go try them out! This can speed up your work in the terminal incredibly.

\*\* Updated 2011-04-05 - there are many moooore! See this little link: [](http://www.faqs.org/docs/bashman/bashref_101.html#SEC108)[http://www.faqs.org/docs/bashman/bashref\_93.html#SEC100](http://www.faqs.org/docs/bashman/bashref_93.html#SEC100)

You can see the bindings by typing "bind -P"

### The easier shortcuts:

<table><tbody><tr><td>Ctrl + A</td><td>Go to the beginning of the line you are currently typing on. Extremely useful in those scenarios when left/right arrow keys do not work. Same as HOME button.</td></tr><tr><td>Ctrl + E</td><td>Go to the end of the line you are currently typing on. Same as END button.</td></tr><tr><td>Ctrl + L</td><td>Clears the Screen, same as the clear command.</td></tr><tr><td>Ctrl + U</td><td>Clears the line before the cursor position. If you are at the end of the line, clears the entire line.</td></tr><tr><td>Ctrl + H</td><td>Backspace.</td></tr><tr><td>Ctrl + R</td><td>Let’s you search through previously used commands. Hit again to roll through the hits in the history. Searches through .bash_history in the user's home directory.</td></tr><tr><td>Arrowkeys Up/Down</td><td>Same as CTRL + P and CTRL + N. This will browse through the history. Hit enter to execute the command.</td></tr><tr><td>Ctrl + C</td><td>Kill whatever you are running.</td></tr><tr><td>Ctrl + D</td><td>Exit the current shell - logout.</td></tr><tr><td>Ctrl + Z</td><td>Puts whatever you are running into a suspended background process. You can then use the terminal for something else. Type 'fg' in the terminal to restore the process.</td></tr><tr><td>Ctrl + W</td><td>Delete the word before the cursor.</td></tr><tr><td>Ctrl + K</td><td>Clear the line after the cursor.</td></tr><tr><td>Ctrl + T</td><td>Swap the last two characters before the cursor.</td></tr><tr><td>Esc + T</td><td>Swap the last two words before the cursor.</td></tr><tr><td>Alt + F</td><td>Move cursor forward one word on the current line.</td></tr><tr><td>Alt + B</td><td>Move cursor backward one word on the current line.</td></tr><tr><td>Tab</td><td>Auto-complete files and folder names.</td></tr><tr><td>Shift + Page Up / Down</td><td>Scrolls through terminal buffer.</td></tr></tbody></table>

 

### The shortcuts that are a little trickier:

<table><tbody><tr><td>Ctrl + X *</td><td>In a directory you have two files: awesomeapp1.deb and notawesomebutneededapp4.deb. You want to install both. In debian the program you call is "dpkg -i filename.deb". If you don't want to write out all the names, you can type this: dpkg -i *.deb <strong>CTRL+x *</strong> (first ctrl+x and then press the * on your numpad or * on your normal, like shift+') and then it will resolve the names so that your command will be "dkpg -i awesomeapp1.deb notawesomebutneededapp4.deb"</td></tr><tr><td>Ctrl + X Ctrl + V</td><td>Prints something like this: GNU bash, version 4.1.2(1)-release (x86_64-redhat-linux-gnu)</td></tr><tr><td>Macros</td><td><span style="color: #ff0000;"><strong>CTRL +X ( </strong></span>to start, <span style="color: #ff0000;"><strong>CTRL +X ) </strong></span>to save. For example: first hit <strong>CTRL+x SHIFT+8</strong> (this is on my keyboard layout) - then put in your commands. Everything you type after this is saved in a macro. Then <strong>CTRL+X SHIFT+9 to</strong> save. Then hit <span style="color: #ff0000;"><strong>CTRL+x e </strong></span>to run the macro.</td></tr></tbody></table>

Have fun!
