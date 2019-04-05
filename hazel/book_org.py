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
        description="Process ebooks in these formats: " +
                    "Last, First - title.epub; " +
                    "(series name) Last, First - title.epub; " +
                    "First Last - title.epub; " +
                    "(series name) First Last - title.epub")
    parser.add_argument("book_name", metavar="BOOK", type=check_name_matches,
                        help="Epub file to process")

    return parser


def first_last(filename, end_file):
    """
    Match Format: last, first - <...>.epub

    Parameters:
    filename: Original filename
    end_file: Desired name of the file
    """
    last = end_file.split(",")[0].strip()
    first = end_file.split(",")[1]
    first = first.split("-")[0].strip()

    author = first + " " + last

    file_book(filename, author, end_file)


def no_comma(filename, end_file):
    """
    Match Format: <name> - <...>.epub

    Parameters:
    filename: Original filename
    end_file: Desired name of the file
    """
    author = end_file.split("-")[0].strip()
    file_book(filename, author, end_file)


def file_book(filename, author, basename):
    """
    Move book to dir for the author.

    Create dir for author if it does not exist

    Parameters:
    filename: Original filename
    author: Name of Author
    basename: Desired name of the file
    """
    author = BOOK_PATH + "/" + author
    # If a directory for that author does not exist, create it
    if not os.path.exists(author):
        os.mkdir(author)
    shutil.move(filename, author + "/" + basename)


def check_name_matches(book):
    cut = book.split("/")[-1]
    book_syntax = r"[\( A-Za-z0-9\)]*[ A-Za-z\.,]* - .*(\.epub)"
    if not re.match(book_syntax, cut):
        raise argparse.ArgumentTypeError(
            "{} is an invalid file name".format(book))
    return book


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    book = args.book_name

    end_file = book.split("/")[-1].strip()
    if ")" in book:
        end_file = book.split(")")[1].strip()

    # last, first - <...>.epub
    if ',' in book and book.find(',') < book.find('-'):
        first_last(book, end_file)
    # <name> - <...>.epub
    else:
        no_comma(book, end_file)
