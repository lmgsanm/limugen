#!/bin/bash
REDIS_PASSWD="test"
REDIS_HOME="/usr/local/redis"
REDIS_STATUS_PATH=$REDIS_HOME/var/logs/Redis_status.log
CHECK_STATUS=`$REDIS_HOME/bin/redis-cli -a $REDIS_PASSWD PING 2>/dev/null`

if [ "$CHECK_STATUS" = "PONG" ]
then
    echo $CHECK_STATUS
    date >> $REDIS_STATUS_PATH
    echo "redis is running" >> $REDIS_STATUS_PATH
    exit 0
else
    echo $CHECK_STATUS
    date >> $REDIS_STATUS_PATH
    echo "redis is not ailviliable" >> $REDIS_STATUS_PATH
    exit 1
fi
