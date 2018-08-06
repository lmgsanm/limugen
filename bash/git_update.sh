#!/bin/bash

GIT_DIR="/data/limugen/"
DATE=`date '+%Y-%m-%d %H:%M:%S'`
cd $GIT_DIR
#echo "$DATE"
git add --all >dev/null 2>&1
git commit -m "$DATE" >/dev/null 2>&1
git push >/dev/null 2>&1
