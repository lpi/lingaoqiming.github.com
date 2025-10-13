import os
import re

def contains_chinese(text):
    return re.search(r'[一-鿿]', text)

def find_chinese_posts(directory):
    chinese_posts = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if contains_chinese(content):
                    chinese_posts.append(filepath)
    return chinese_posts

if __name__ == "__main__":
    posts_dir = os.path.join(os.path.dirname(__file__), '_posts')
    chinese_posts = find_chinese_posts(posts_dir)
    for post in sorted(chinese_posts):
        print(post)