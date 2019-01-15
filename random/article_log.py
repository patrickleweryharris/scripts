#!/usr/local/bin/python3
import os
import sys
import datetime

DROPBOX = os.getenv("DROPBOX") + "/metrics/read_today.csv"


def log_data(data):
    with open(DROPBOX, "a") as f:
        line = datetime.datetime.today().strftime("%Y-%m-%d")
        line += ","
        line += data
        line += "\n"
        f.write(line)


if __name__ == "__main__":
    args = sys.argv[1:]
    args = " ".join(args)
    log_data(args)
