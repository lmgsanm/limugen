#!/bin/bash

GIT_DIR="/data/limugen/"
DATE=`date '+%Y-%m-%d %H:%M:%S'`
cd $GIT_DIR
#echo "$DATE"
git add --all
git commit -m "$DATE"
git push >> /dev/null 2>&1
