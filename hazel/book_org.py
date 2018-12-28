#!/usr/bin/env python
import os
import re
import shutil
import argparse
"""
Script used to organize my epub books.
Books are expected to be placed in $HOME/Dropbox/books
"""
BOOK_PATH = os.getenv("HOME") + '/Dropbox/books'


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description="Process ebooks in this format: last, first - <...>.epub")
    parser.add_argument("book_name", metavar="BOOK", type=check_name_matches,
                        help="Epub file to process")

    return parser


def run(book):
    """
    Move book to dir for the author.

    Create dir for author if it does not exist
    """
    simple = book.split("/")[-1]
    last = book.split(",")[0]
    last = last.split("/")[-1].strip()
    first = book.split(",")[1]
    first = first.split("-")[0].strip()

    full = first + " " + last
    full = BOOK_PATH + "/" + full
    # If a directory for that author does not exist, create it
    if not os.path.exists(full):
        os.mkdir(full)
    shutil.move(book, full + "/" + simple)


def check_name_matches(book):
    cut = book.split("/")[-1]
    book_syntax = r"[A-Za-z]+, [A-Za-z\.]+[ A-Za-z\.]* - .*(\.epub)"
    if not re.match(book_syntax, cut):
        raise argparse.ArgumentTypeError(
            "{} is an invalid file name".format(book))
    return book


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    run(args.book_name)
