import os
import re

# Define a function to recursively search for Markdown files
def find_md_files(directory="."):
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files

# Find all Markdown files in the current directory and its subdirectories
md_files = find_md_files()

# Loop over each file and modify the categories and tags
for md_file in md_files:
    with open(md_file, "r") as f:
        data = f.read()

    # Extract category and tag lists using regular expressions
    category_match = re.search(r"categories:\s*\n((\s*-\s*[^\n]+\n)+)", data)
    if category_match:
        categories_str = ", ".join([c.strip() for c in category_match.group(1).split("-") if c.strip()])
        data = re.sub(category_match.group(0), f"categories: {categories_str}\n", data)

    tag_match = re.search(r"tags:\s*\n((\s*-\s*[^\n]+\n)+)", data)
    if tag_match:
        tags_str = ", ".join([t.strip() for t in tag_match.group(1).split("-") if t.strip()])
        data = re.sub(tag_match.group(0), f"tags: {tags_str}\n", data)

    # Write modified data back to file
    with open(md_file, "w") as f:
        f.write(data)

