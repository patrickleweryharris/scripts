#!/bin/bash

# Download from youtube

# Usage ./youtube-download.sh $File
# Where file is a URL on each line

while IFS='' read -r line || [[ -n "$line" ]]; do
    youtube-dl $line
done <"$1"
