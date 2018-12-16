#!/bin/bash

# Find instances of home dir in literal form and flag them
# Need to seperate HOMEDIR out so this script doesn't get flagged
HOMEDIR='/Users'
HOMEDIR+='/patrickharris'
BADHOME=`grep -rn $HOMEDIR *`
CODE=1
if [[ $BADHOME = '' ]]
then
    CODE=0
else
    echo $BADHOME >&2
fi

exit $CODE

