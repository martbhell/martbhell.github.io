#!/usr/bin/env python

import os
import glob

content_dir = 'content'

debug = False

EXCLUDE = [ 'images', 'MAKESYMLINKS.py', 'extras' ]

# Get a list of all .md files in the posts directory and its subdirectories

content_files = glob.glob(os.path.join(content_dir, f'**/*'), recursive=True)

if len(content_files) == 0:
    print(f"ERROR: Could not find any files where is {content_dir}")
    os._exit(1)

# Create symlinks for each file in the content directory
BAD = [ ]
for c_file in content_files:
    filename = os.path.basename(c_file)
    if filename not in EXCLUDE:
        if not os.path.islink(c_file):
            BAD.append(c_file)

if len(BAD) > 0:
    print(f"ERROR: Only symlinks in here yo or exclude these!")
    print(f"{BAD}")
    os._exit(2)
else:
    print(f"OK: directory {content_dir} is OK")
