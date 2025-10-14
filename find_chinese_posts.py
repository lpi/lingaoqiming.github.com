
import os
import re

# This script finds all posts in the _posts folder with more than two Chinese characters.

def find_chinese_posts():
    posts_dir = '_posts'
    # Regex to match Chinese characters
    chinese_char_re = re.compile(r'[\u4e00-\u9fa5]')

    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Find all Chinese characters in the content
                    chinese_chars = chinese_char_re.findall(content)
                    if len(chinese_chars) > 2:
                        print(filename)
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

if __name__ == "__main__":
    find_chinese_posts()
