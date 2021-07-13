#######################################################
#  Crawl through a directory of ebooks by author and  #
#  remove all Calibre-created parens (39) from book   #
#  directories.                                       #
#######################################################

import os
import re

ebook_dir = r'C:\Users\cohenja\Documents\Python Scripts\ml\samples'

# Set working directory
os.chdir(ebook_dir)

for item in os.listdir(ebook_dir):
    if os.path.isdir(os.path.join(ebook_dir, item)):
        for sub_item in os.listdir(os.path.join(ebook_dir, item)):
            new_str = re.sub(r'\s+$', '', re.sub(r'\([^)]*\)', '', str(sub_item)))
            os.rename(os.path.join(ebook_dir, item, sub_item), os.path.join(ebook_dir, item, new_str))
