#!/bin/bash

"$@" &

while kill -0 $!; do
    echo '.'
    sleep 2
done

echo '\n'
