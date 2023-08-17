#!/usr/bin/env python
""" Making all the links and copies files """

import os
import shutil
import glob

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--test", action="store_true", help="only test and fail if a link is missing"
)
args = parser.parse_args()

test_mode = args.test

posts_dir = "../posts"
content_dir = "."
image_dir = "./images"
output_image_dir = "../output/images"
extras_dir = "./extras"
extras_source_dir = "../extras"

debug = False

# Get a list of all .md files in the posts directory and its subdirectories

image_extensions = ["gif", "jpg", "png", "GIF", "JPG", "PNG", "webp", "WEBP"]
md_files = glob.glob(os.path.join(posts_dir, "**/*.md"), recursive=True)
extras_files = glob.glob(os.path.join(extras_source_dir, "*"))

image_files = []
for extension in image_extensions:
    image_files += glob.glob(
        os.path.join(posts_dir, f"**/*.{extension}"), recursive=True
    )

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

    if not os.path.islink(symlink_path) and test_mode:
        print(f"ERROR: {symlink_path} is not a link")
        os._exit(3)
    try:
        # Create the symlink
        os.symlink(md_file, symlink_path)
    except FileExistsError:
        if debug:
            print(f"Skipping {md_file}: symlink already exists.")

# Copy each image into output directory
for image_file in image_files:
    # Construct the target filename by getting the basename of the file
    image_basename = os.path.basename(image_file)
    if image_basename in posts:
        print(f"ERROR: {image_basename} is a duplicate. Stop it!")
        os._exit(4)
    posts.append(image_basename)

    # Construct the output dir image path by joining the output directory and the image's basename
    output_image_file_path = os.path.join(output_image_dir, image_basename)

    # Copy image into output/images preserving metadata
    if not os.path.exists(output_image_file_path):
        shutil.copy2(image_file, output_image_file_path)
        print(f"copied {image_file} to {output_image_file_path}")

# Create symlinks for each extras
for extra_file in extras_files:
    # Construct the symlink filename by getting the basename of the file
    symlink_filename = os.path.basename(extra_file)

    # Construct the symlink path by joining the content directory and the symlink filename
    symlink_path = os.path.join(extras_dir, symlink_filename)
    extra_file_path = os.path.join("..", extra_file)
    if not os.path.islink(symlink_path) and test_mode:
        print(f"ERROR: {symlink_path} is not a link")
        os._exit(6)

    try:
        # Create the symlink
        os.symlink(extra_file_path, symlink_path)
    except FileExistsError:
        if debug:
            print(f"Skipping {extra_file}: symlink already exists.")
