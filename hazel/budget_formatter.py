#!/usr/local/bin/python3
import os
import argparse
import pandas as pd

METRICS_PATH = os.getenv("HOME") + '/Desktop/parsed.csv'


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description="Format downloaded CC reports to match with spreadsheet")
    parser.add_argument("filename", metavar="FILE",
                        help="CSV file to process")

    return parser


def process_file(filename):
    """ Turn the file into the correct format """
    f = pd.read_csv(filename, usecols=['Description', 'Date', 'Amount'])
    f = f[['Date', 'Description', 'Amount']]
    f['Amount'] = f['Amount'].apply(lambda x: x * -1)
    f.to_csv(METRICS_PATH, index=False)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    process_file(args.filename)
