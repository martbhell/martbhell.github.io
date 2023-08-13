""" Make sure we got metadata in the markdowns """
import os
import re


def check_metadata(file_path):
    """with some exceptions, like only require lang if actually in Finnish?"""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Check for required metadata fields
    required_fields = ["title:", "tags:", "date:", "category:"]
    path_split = file_path.split("/")
    year = int(path_split[1])
    if year >= 2023:
        # Because in 2023 I started doing Finnish posts
        required_fields.append("lang:")
    for field in required_fields:
        if not re.search(rf"^{field}", content, re.MULTILINE | re.IGNORECASE):
            return False

## Too many. Need a script to fix it in all first.
#    # Check for metadata delimiters
#    if content.count('---') < 2:
#        return False

    return True


def search_in_subdirectories(directory):
    """traverse!"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".md"):
                file_path = os.path.join(root, file)
                if not check_metadata(file_path):
                    if file_path not in BAD_FILES:
                        BAD_FILES.append(file_path)

        for dire in dirs:
            dir_path = os.path.join(root, dire)
            search_in_subdirectories(dir_path)


def main():
    """the main"""
    posts_directory = "posts/"  # Replace with your actual directory path
    search_in_subdirectories(posts_directory)


if __name__ == "__main__":
    BAD_FILES = []
    main()
    if len(BAD_FILES) != 0:
        print("ERROR: BAD files:")
        for bad_ in sorted(BAD_FILES):
            print(bad_)
        os._exit(2)
    else:
        print("OK: Metadata in all files")
