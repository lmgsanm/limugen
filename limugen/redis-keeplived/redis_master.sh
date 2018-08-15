#!/bin/bash
REDIS_PASSWD="test"
REDIS_HOME="/usr/local/redis"
REDIS_LOG_PATH=$REDIS_HOME/var/logs/keepalived-redis-state.log
echo "[master]" >> $REDIS_LOG_PATH
date >> $REDIS_LOG_PATH

echo "Beginning master ************" >> $REDIS_LOG_PATH 2>&1
echo "Run SLAVEOF cmd ************" >> $REDIS_LOG_PATH


