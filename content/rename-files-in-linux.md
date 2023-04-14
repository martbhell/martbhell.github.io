---
title: "Rename files in Linux - mv"
date: 2011-05-02
categories: 
  - "it"
tags: 
  - "cli"
  - "command-line"
  - "linux"
  - "mv"
  - "rename"
  - "rename-files"
  - "shell"
---

Hey!

This is an awesome little trick I just learnt about:

instead of doing

`mv file1.txt file1.txt.old`

you can do this

`mv file1.txt{,.old}`

and it will automagically add a .old at the end of the filename.

This is called a brace expansion: [http://tldp.org/LDP/Bash-Beginners-Guide/html/sect\_03\_04.html](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_04.html)
