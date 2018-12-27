#!/usr/bin/env python
import os
import sys
import shutil
"""
Script used to organize my epub books.
Books are expected to be placed in $HOME/Dropbox/books
"""
BOOK_PATH = os.getenv("HOME") + '/Dropbox/books'


if __name__ == '__main__':
    # Book is expected to be in the following format:
    # last, first - <other info>.epub
    BOOK = sys.argv[1]
    SIMPLE = BOOK.split("/")[-1]
    last = BOOK.split(",")[0]
    last = last.split("/")[-1].strip()
    first = BOOK.split(",")[1]
    first = first.split("-")[0].strip()

    full = first + " " + last
    full = BOOK_PATH + "/" + full
    # If a directory for that author does not exist, create it
    if not os.path.exists(full):
        os.mkdir(full)
    shutil.move(BOOK, full + "/" + SIMPLE)
