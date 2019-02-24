#!/usr/bin/env python
import os
import shutil
import argparse
"""
Script used to remove a doubled extension from a file
"""


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description="Remove doubled extensions from files")
    parser.add_argument("filename", metavar="file",
                        help="File to process")

    return parser


def remove_doubles(filename):
    """ Remove double extensions from a file """
    last_dot = filename.rfind(".")
    ext = filename[last_dot:]

    # if st ".<abc>.<abc>" appears, replace with just ".<abc>"
    f = filename.replace(ext + ext, ext)

    # Avoid time consuming file operation if no double extension
    if f == filename:
        return

    if os.path.exists(filename):
        shutil.move(filename, f)
    else:
        raise RuntimeError("File does not exist!")


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    remove_doubles(args.filename)
