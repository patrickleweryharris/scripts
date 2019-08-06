#!/usr/bin/env python
import os
import re
import shutil
import argparse
"""
video-filer.py

Files TV shows in the format in the format
'$show$season$episode$garbage.$ext' to
'$show/$show$season$episode.$ext'

Works well with hazel: https://www.noodlesoft.com/
"""

DEFAULT_DEST = os.getenv("HOME") + "/movies"

SHOW_SYNTAX = (r"([\( A-za-z0-9\.\)]*)"
               r"([Ss]{1}[0-9]+[Ee]{1}[0-9]+).*(\.[a-z0-9]*)")


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description=("Files TV shows in the format 'nameS#E#<garbage>.ext'"
                     "into a directory show/nameS#E#.ext"))
    parser.add_argument("video_name", metavar="video", type=check_name_matches,
                        help="File to process")

    parser.add_argument("--dest", "-d", metavar="DEST", type=check_dir_exists,
                        default=DEFAULT_DEST,
                        help="Dest dir, default={}".format(DEFAULT_DEST))
    return parser


def file_video(filename, show, basename, dest):
    """
    Move video to dir for the show.

    Create dir for show if it does not exist

    Parameters:
    filename: Original filename
    show: Name of show
    basename: Desired name of the file
    dest: Destination directory
    """
    show = dest + "/" + show
    # If a directory for that show does not exist, create it
    if not os.path.exists(show):
        os.mkdir(show)
    shutil.move(filename, show + "/" + basename)


def check_name_matches(video):
    """
    Check that filename is in the form of "showS#E#..."
    """
    cut = video.split("/")[-1]
    if not re.match(SHOW_SYNTAX, cut):
        raise argparse.ArgumentTypeError(
            "{} is an invalid file name".format(video))
    return video


def check_dir_exists(d):
    """
    Check if a directory exists, and raise error if not
    """
    if not os.path.exists(d):
        raise argparse.ArgumentTypeError("{} does not exist!".format(d))
    return d


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    video = args.video_name
    dest = args.dest

    end_file = video.split("/")[-1].strip()
    match = re.match(SHOW_SYNTAX, end_file)
    show = match.group(1)
    show = show.replace(".", "").lower()

    epnum = match.group(2)
    epnum = epnum.replace(".", "").upper()

    ext = match.group(3).lower()

    new_name = "{}-{}{}".format(show, epnum, ext)

    file_video(video, show, new_name, dest)
