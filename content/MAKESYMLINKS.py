#!/usr/bin/env python

import os
import glob

posts_dir = '../posts'
content_dir = '.'
image_dir = './images'

# Get a list of all .md files in the posts directory and its subdirectories

image_extensions = ['gif', 'jpg', 'png', 'GIF', 'JPG', 'PNG']
md_files = glob.glob(os.path.join(posts_dir, '**/*.md'), recursive=True)
image_files = []
for extension in image_extensions:
  image_files += glob.glob(os.path.join(posts_dir, f'**/*.{extension}'), recursive=True)

print(image_files)
posts = []

if len(md_files) == 0:
    print("ERROR: Could not find any files")
    os._exit(1)

# Create symlinks for each file in the content directory
for md_file in md_files:
    # Construct the symlink filename by getting the basename of the file
    symlink_filename = os.path.basename(md_file)
    if symlink_filename in posts:
        print(f"ERROR: {symlink_filename} is a duplicate. Stop it!")
        os._exit(2)
    posts.append(symlink_filename)

    # Construct the symlink path by joining the content directory and the symlink filename
    symlink_path = os.path.join(content_dir, symlink_filename)
    try:
        # Create the symlink
        os.symlink(md_file, symlink_path)
    except FileExistsError:
        print(f"Skipping {md_file}: symlink already exists.")

# Create symlinks for each image in the content directory
for image_file in image_files:
    # Construct the symlink filename by getting the basename of the file
    symlink_filename = os.path.basename(image_file)
    if symlink_filename in posts:
        print(f"ERROR: {symlink_filename} is a duplicate. Stop it!")
        os._exit(2)
    posts.append(symlink_filename)

    # Construct the symlink path by joining the content directory and the symlink filename
    symlink_path = os.path.join(image_dir, symlink_filename)
    image_file_path = os.path.join('..', image_file)
    try:
        # Create the symlink
        os.symlink(image_file_path, symlink_path)
    except FileExistsError:
        print(f"Skipping {md_file}: symlink already exists.")
