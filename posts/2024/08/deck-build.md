---
title: Thinking of building a deck
date: 2024-08-5 22:57
category: finland
lang: en
tags: wood workshop, carpentry, woodwork, deck, step
<!-- prettier-ignore -->
---

We have a deck. The step up is quite steep (it is higher than 30cm).

## General idea

- on top use a ribbed plank as it will be in rain and will get slippery
- measurements:
  - about 100cm wide (fits between two posts)
  - 17cm high
  - 35cm long/deep so a foot can fit there easily :)

## More loose ideas

Put wood together by ?:

- A connector like an L-bracket or corner brace bracket?
- Just screw them together?

Attach to the deck itself.

Add some supports inside.

Should it be a box, have one or even two sides "open"?

## Can I make one myself?

- Did some measurements and drew a design on a napkin
- Sent picture to chatgpt and asked for a 3D design.
- Got a python script

### Challenges

I am not good at wood work so would like to make a drawing to see how all the
pieces would fit together and what exact sizes I need of wood.

### Jupyter?

Because I use WSL 2 to code at home. How do I print the drawing that ChatGPT
suggested?

It uses

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
```

One way is to:

```bash
jupyter notebook --no-browser \
   --ip `ip addr | grep eth0 | grep inet | \
   awk '{print $2}' | cut -d"/" -f1`
```

I haven't used jupyter from scratch but seems OK!

- Create a new notebook
- Paste in the code from ChatGPT 4
- Does not look like I want :D
- Drawing things with code is hard..

## Then I found

Sketchup?

Autodesk Fusion360 is free for personal use?

OK maybe I should take the time..
