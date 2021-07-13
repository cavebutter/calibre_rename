# Rename Calibre-Created Directories

## Intro & Use Case
When you create eBook libraries with Calibre, Calibre makes copies of your ebook files and places them in a user-specified location, using a directory structure like:
Library --> Author (###) --> Book --> ebook files

When you move away from Calibre, or want to port your library over to another instance, you have a bunch of directories with names like:
Sue Grafton (322)
Terry Brooks (103)
etc.

*ebook_rename.py* - This short script will remove the parens and whitespace after the author directories.

### make_dirs.py
This script will create a small directory tree like what Calibre generates.  You can use it to test or modify *ebook_rename.py*.
