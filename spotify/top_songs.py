#!/usr/bin/env python
import argparse
import spotipy
import spotipy.util as util
"""
top_songs.py

This script requires spotipy: https://github.com/plamere/spotipy

Automates creation of a 'Top Songs' playlist on Spotify.
Takes your top songs over a short, medium, or long period of time,
and creates a playlist. If you already have an existing playlist,
you can specify its URI and this script will update the contents.

If you create a new playlist, the URI will be outputted and
you can save it for future use.

This script requires authorization with Spotify. You should
create a Spotify API app, and save the information in
environment variables.
See: https://spotipy.readthedocs.io/en/latest/#authorized-requests

When you run this for the first time, a spotify OAuth webpage will
open. Authorize the app, then the window should automatically close.
The playlist is then generated.
"""

# Number of recently played songs to go through
DEFAULT_LIMIT = 50

# Valid time ranges for top tracks
TIME_RANGES = {'short': 'short_term',
               'medium': 'medium_term',
               'long': 'long_term'}

# Default name for top tracks playlist
DEFAULT_TOP_PLAYLIST = "Top Songs"


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description=("Automates creation of a 'Top Songs' Spotify playlist"))

    parser.add_argument(
        "username",
        metavar="USER",
        type=str,
        help="Spotify username")

    parser.add_argument("--term", "-t", metavar="TERM", type=check_time_range,
                        default='short',
                        help=("Length of time to get top tracks over. "
                              "Can be: short, medium, or long. "
                              "Default: medium"))

    parser.add_argument("--limit", "-l", metavar="LIMIT", type=int,
                        default=DEFAULT_LIMIT,
                        help=("Number of top tracks to add. "
                              "Default: {}".format(DEFAULT_LIMIT)))

    parser.add_argument("--playlist", "-p", metavar="PLAYLIST", type=str,
                        default=DEFAULT_TOP_PLAYLIST,
                        help=("Top songs playlist name to create."
                              "Default: {}".format(DEFAULT_TOP_PLAYLIST)))

    parser.add_argument("--existing", "-e", metavar="URI", type=str,
                        default=False,
                        help="URI of top songs playlist if exists")
    return parser


def check_time_range(r):
    """ Check that time range is valid """
    if r not in TIME_RANGES:
        raise argparse.ArgumentTypeError("Time range invalid!")
    return r


def auth(username):
    """
    Authenticate with Spotify
    """
    scope = "user-top-read playlist-modify-private"
    token = util.prompt_for_user_token(username, scope, redirect_uri='http://localhost:8080/callback/')

    if not token:
        raise RuntimeError("Authorization failed")
    sp = spotipy.Spotify(auth=token)
    return sp


def parse_tracks(tracks):
    """
    Filter out only the track id of
    return tracks
    """
    tracks = tracks.get('items')
    return [track.get('uri') for track in tracks]


def main():
    parser = create_parser()
    args = parser.parse_args()
    sp = auth(args.username)

    # Get top tracks for time range
    top_tracks = sp.current_user_top_tracks(
        limit=args.limit, time_range=TIME_RANGES.get(args.term))
    top_tracks = parse_tracks(top_tracks)

    # If existing playlist URI was given, use that instead of creating a new
    # playlist
    if args.existing:
        playlist = args.existing
    else:
        playlist = sp.user_playlist_create(
            args.username, args.playlist, public=False).get('uri')
        print(
            "Created {} playlist with URI: {}, please save this.".format(
                args.playlist,
                playlist))

    # Replace current tracks with new tops
    sp.user_playlist_replace_tracks(args.username, playlist, top_tracks)


if __name__ == '__main__':
    main()
