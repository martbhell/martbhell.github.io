#!/usr/bin/env python

import os
import glob


def test_content_dir():
    content_dir = "content"

    debug = False

    EXCLUDE = ["images", "MAKESYMLINKS.py", "extras", "ADD_PRETTIER_TAG.sh"]

    # Get a list of all .md files in the posts directory and its subdirectories

    content_files = glob.glob(os.path.join(content_dir, f"**/*"), recursive=True)

    if len(content_files) == 0:
        print(f"ERROR: Could not find any files where is {content_dir}")
        os._exit(1)

    # Create symlinks for each file in the content directory
    BAD = []
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


def test_output_dir():
    content_dir = "output"

    debug = False

    EXCLUDE = []

    # Get a list of all files under output

    content_files = glob.glob(os.path.join(content_dir, f"**/*"), recursive=True)

    if len(content_files) == 0:
        print(f"ERROR: Could not find any files where is {content_dir}")
        os._exit(1)

    # Create symlinks for each file in the content directory
    BAD = []
    for c_file in content_files:
        filename = os.path.basename(c_file)
        if filename not in EXCLUDE:
            if os.path.islink(c_file):
                BAD.append(c_file)

    if len(BAD) > 0:
        print(f"ERROR: Only symlinks in here yo or exclude these!")
        print(f"{BAD}")
        os._exit(3)
    else:
        print(f"OK: directory {content_dir} is OK")


test_content_dir()
test_output_dir()
