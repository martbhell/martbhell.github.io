import os

def add_second_delimiter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    if content.count('---') < 2:
        metadata_lines = content.split('\n')
        metadata_lines.insert(2, '---')
        new_content = '\n'.join(metadata_lines)

        print(f"Would modify {file_path}")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

def search_in_subdirectories(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                add_second_delimiter(file_path)
                os._exit(4)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            search_in_subdirectories(dir_path)

def main():
    posts_directory = 'posts'  # Replace with your actual directory path
    search_in_subdirectories(posts_directory)

if __name__ == '__main__':
    main()
