---
title: Using Chat GPT or other LLM at for hobby projects
date: 2023-04-20 22:03
category: it
tags: it, llm, chatgpt, phind
lang: en
---

I find myself using chatGPT or similar like [phind](https://www.phind.com/) recently to help with some computer programming tasks.

I'll probably post more about what I'm using it for at work too.

It's a thing that's up-and-coming so seems like something useful I could learn!

## Some reasons why I used it during the migration of this blog post from jekyll to pelica:

I had some real needs where I maybe didn't want to write the whole script from scratch, or I thought I could get there quicker by making a few tweaks and instead ask for one of these bots? to make the first attempt for me.

First was a:

- python script that recursively loops through all .md files inside a folder called "posts" and creates symlinks to all those files inside a single directory called "content"

this worked quite well, but I needed to refine the script a few times by adding exception handling and creating directories:

- adding follow-ups like "The symlink should not have any directories in them, just the filename."
- 'the symlink need to have a ".." in the path' because the symlinks weren't working for me

Another was to help with some changes like:

- use python re.findall to replace all http://guldmyr.com with https://guldmyr.com

## As part of testing the site:

- a python script that crawls a single url front page only and exits with non-zero return code if there are any broken links

Turning the yaml lists in all the blog posts into a comma separated one I need to clarify a few times:

- I have hundreds of these files. I want to modify the files not make new files.
- The files have *.md file extension and are not 100% yaml so cannot be loaded.
- Can you make it look recursively for md files too?
- The elements in the list are quoted with double quotes, can we strip those too?
- re.error: unbalanced parenthesis at position 537 (line 12, column 117)
- This is tried to fix. But in the end the error was a bad blog post that looked too closely like yaml??


And in the end I needed to remove some double-quotes around the tags so rather than typing

"in bash Remove double quotes from any .md files recursively for lines that start with categories: or tags:"

It returned this pretty quickly, which I TBH could have figured out myself :)

```
find . -name '*.md' -type f -exec sed -i '/^categories:/ s/"//g' {} +
find . -name '*.md' -type f -exec sed -i '/^tags:/ s/"//g' {} +
```

## Formatting

I had a blog post which used poor syntax and stuff was all in a single line. So I pasted the thing to it and asked it to create a bash script out of it (basically figure out where the newlines should be). Worked very nicely :D


