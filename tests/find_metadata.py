import os
import re

def check_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check for required metadata fields
    required_fields = ['title:', 'tags:', 'lang:', 'date:', 'category:' ]
    for field in required_fields:
        if not re.search(rf'^{field}', content, re.MULTILINE | re.IGNORECASE):
            return False
    return True

def main():
    posts_directory = 'posts'  # Replace with your actual directory path

    for root, dirs, files in os.walk(posts_directory):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Testing {file} for presence of all metadata.")
                if not check_metadata(file_path):
                    print(f"Metadata missing in {file_path}")

        if len(files) == 0:
            print("No files found")
            return False
if __name__ == '__main__':
    main()
  
