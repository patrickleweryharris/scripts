#!/bin/bash

# Find instances of home dir in literal form and flag them
BADHOME=`grep -rn $HOME *`

if [[ $BADHOME = '' ]]
then
    exit 0
else
    echo $BADHOME >&2
    exit 1
fi
