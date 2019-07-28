"""
Delete all saved posts / comments on your reddit account with PRAW.

See: https://plh.io/automation/delete-all-saved-reddit-links

Needs Python 3+ and Praw 5.3.0
"""
import argparse
import praw


def create_parser():
    """Create command line argument parser"""
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("client_id", metavar="CLIENT_ID",
                        help="client_id for PRAW")
    parser.add_argument("client_secret", metavar="CLIENT_SECRET",
                        help="client_secret for PRAW")
    parser.add_argument("password", metavar="PASSWORD",
                        help="Reddit password")
    parser.add_argument("username", metavar="USERNAME",
                        help="Reddit username")

    return parser


def run_praw(client_id, client_secret, password, username):
    """
    Delete all saved reddit posts for username

    CLIENT_ID and CLIENT_SECRET come from creating a developer app on reddit
    """
    user_agent = "/u/{} delete all saved entries".format(username)
    r = praw.Reddit(client_id=client_id, client_secret=client_secret,
                    password=password, username=username,
                    user_agent=user_agent)

    saved = r.user.me().saved(limit=1000)
    for s in saved:
        try:
            s.unsave()
        except AttributeError as err:
            print(err)


def main():
    """ Run the program """
    parser = create_parser()
    args = parser.parse_args()
    run_praw(args.client_id, args.client_secret, args.password, args.username)


if __name__ == "__main__":
    main()
