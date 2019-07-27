#!/usr/bin/python

from sys import argv


def compare(oldsongs, newsongs):
    # Read in old and new playlists, return songs that are in both new and old
    ret = []
    old = open(oldsongs, "r").readlines()
    new = open(newsongs, "r").readlines()
    for song in new:
        if song in old and song.rstrip() != '':
            ret.append(song.rstrip())

    return ret


if __name__ == "__main__":
    print(compare(argv[1], argv[2]))
