---
title: Attempting to get better at pwning
date: 2025-03-21
category: it
lang: en
tags: ctf, hacking, hacker, reverse, rev, reverse engineering, radare2, r2
<!-- prettier-ignore -->
---

Usually in Capture the Flag (CTF) challenges I get stuck when it comes to reverse engineering.

Or is it pwning? Probably both.

The difference:

- Pwning: Binary exploitation. Making software do things it wasn't supposed to do.
- Reversing: Figuring out how a program ticks.

Taking some time as part of the monthly Training Day at datacrunch to get a bit better at this.

I was thinking, maybe if I just try a few challenges and just follow write-ups? Maybe some stuff will just eventually fall into place?

- hackthebox [Execute](https://github.com/jon-brandy/hackthebox/blob/main/Categories/Pwn/Execute/README.md)
  - Uh. So somehow realize that the program will shellcode.
  - That it doesn't allow any characters. xor "/bin/sh" and store that in a variable? that doesn't contain any of the bad characters.
  - Not so easy :D

Maybe picoCTF is easier?

- picoCTF PIE Time
  - Uh hmm.. so when the program runs it prints the address to main() and one can enter an address.
  - Exit codes are different. Sometimes it's SIGKILL / exit code -4, 58, 59, 0..
  - Maybe I can start the process. Then use gdb to find out the address of the win()? Maybe. How does one use `r2 -d $(pidof vuln)` to
    to find the address of the function?
    - command `is~win` in radare2 returns `0x59d28578e2a7` vaddr for `0x59d28578e33d` or `0x5bec819872a7` vaddr for `0x5bec8198733d`
    - this is 0x96 always difference - so then I could connect to the address on the container in picoCTF and get the flag!
  - Before this I tried another approach: Modify the code and adding `printf("Address of win: %p\n", &win);` printed the thing to enter.
    - There was a difference of `162` / `0xa2` between the functions always.
    - But that didn't work with the vanilla `./vuln`. Because I added code, it would something shorter..


Third approach / not complete idea:

Python code for running ./vuln with different inputs to see what happens. 

Basically bruting it :)

It could work, just need to go deeper.

```python

from pwn import *

exe = './vuln'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'DEBUG'

for extra in range(1,8):
    p = process(exe)
    # p = remote('localhost', 52605)
    
    # Receive the output
    received_data = p.recvuntil(b"Enter the address to jump to, ex => 0x12345: ")


    try:
        address_line = received_data.split(b"\n")[0] #split by newlines, take first line
        address_hex = address_line.split(b": ")[1].strip() #split by ": ", take second part and remove whitespace.
        main_address = int(address_hex, 16)
        print(f"Main address: {hex(main_address)}")
    
        # Calculate the address to jump to (main_address + 1)
        jump_address = main_address - extra
    
        # Send the jump address as input
        p.sendline(hex(jump_address).encode())
    
        # Receive and print the response
        response = p.recvall()
        print(f"Response:\n{response.decode()}")

    
    except (IndexError, ValueError) as e:
        print(f"Error parsing address: {e}")
        p.close()
        exit(1)

p.close()


```
  

