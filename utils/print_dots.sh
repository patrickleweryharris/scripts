#!/bin/bash

"$@" &

while kill -0 $!; do
    echo -n '.' > /dev/tty
    sleep 1
done

echo "" > /dev/tty
