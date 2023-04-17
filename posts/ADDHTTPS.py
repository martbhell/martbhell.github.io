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

    # Modify URLs in the format "https://example.com/blog/post-sdf"
    url_match = re.findall(r"http://guldmyr\.com", data)
    for url in url_match:
        new_url = url.replace(url, "https://guldmyr.com")
        data = data.replace(url, new_url)

    # Write modified data back to file
    with open(md_file, "w") as f:
        f.write(data)

