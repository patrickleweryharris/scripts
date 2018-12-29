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


def first_last(book):
    """
    Match Format: last, first - <...>.epub
    """
    filename = book.split("/")[-1]
    last = filename.split(",")[0].strip()
    first = book.split(",")[1]
    first = first.split("-")[0].strip()

    author = first + " " + last

    file_book(book, author, filename)


def no_comma(book):
    """
    Match Format: <name> - <...>.epub
    """
    filename = book.split("/")[-1]
    author = filename.split("-")[0].strip()
    file_book(book, author, filename)


def file_book(book, author, filename):
    """
    Move book to dir for the author.

    Create dir for author if it does not exist
    """
    author = BOOK_PATH + "/" + author
    # If a directory for that author does not exist, create it
    if not os.path.exists(author):
        os.mkdir(author)
    shutil.move(book, author + "/" + filename)


def check_name_matches(book):
    cut = book.split("/")[-1]
    book_syntax = r"[ A-Za-z\.,]* - .*(\.epub)"
    if not re.match(book_syntax, cut):
        raise argparse.ArgumentTypeError(
            "{} is an invalid file name".format(book))
    return book


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    book = args.book_name
    # last, first - <...>.epub
    if ',' in book and book.find(',') < book.find('-'):
        first_last(book)
    # <name> - <...>.epub
    else:
        no_comma(book)
