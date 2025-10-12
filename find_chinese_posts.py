import os
import re

def find_chinese_posts_in_dir(directory):
    """
    Identifies files in a directory that contain Chinese characters.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        list: A list of filenames that contain Chinese characters.
    """
    chinese_post_files = []
    chinese_char_pattern = re.compile(r'[\u4e00-\u9fff]')

    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return []

    for filename in files:
        if not filename.startswith('2013-2-'):
            continue

        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    # Read a sample of the file to check for Chinese characters
                    content_sample = f.read(500)
                    if chinese_char_pattern.search(content_sample):
                        chinese_post_files.append(filename)
            except Exception as e:
                print(f"Could not process file {filename}: {e}")

    return sorted(chinese_post_files)

if __name__ == "__main__":
    posts_directory = '_posts'
    chinese_files = find_chinese_posts_in_dir(posts_directory)

    if chinese_files:
        print("The following posts from February 2013 appear to be in Chinese:")
        for file in chinese_files:
            print(file)
    else:
        print("No posts from February 2013 were found to be in Chinese.")