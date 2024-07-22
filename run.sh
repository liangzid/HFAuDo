#!/bin/bash
######################################################################
#RUN ---

## WARNING: This file can ONLY be used for scientific research and is
# NOT allowed to be utilized for any malicious activities. At the same time,
# the author will NOT be responsible for all consequences caused by the
# illegal use of this document.

# Author: Zi Liang <zi1415926.liang@connect.polyu.hk>
# Copyright © 2024, ZiLiang, all rights reserved.
# Created: 22 July 2024
######################################################################

######################### Commentary ##################################
##  
######################################################################

export DAILY_COMMAND="python run.py"
export TIMES_PERDAY=20

for i in {1..${TIMES_PERDAY}}
do
    export SLEEP_TIME=$((RANDOM % 86400))

    ${DAILY_COMMAND}

    echo "Execute $i time Done, will sleep $SLEEP_TIME seconds."

    sleep $SLEEP_TIME

done

# add the permission
# chmod +x run.sh

# open crontab with `crontab -e`

# fill the file with `0 0 * * * /path/to/run.sh`


echo "RUNNING run.sh DONE."
# run.sh ends here
