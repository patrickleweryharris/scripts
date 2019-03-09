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
    echo "$HOMEDIR found in script files! Replace with ~"
    echo $BADHOME >&2
fi

# Do basic bash syntax checking on all bash scripts in dir
for SCRIPT in `grep -lRe "bin/bash" *`
do
    bash -n $SCRIPT
    CHECK=$?
    if [[ $CHECK -ne 0 ]]
    then
        CODE=1
    fi
done

# Do the same for python
flake8 . --ignore=D
CHECK=$?
if [[ $CHECK -ne 0 ]]
then
    CODE=1
fi

exit $CODE

