#!/bin/bash
REDIS_PASSWD="test"
REDIS_HOME="/usr/local/redis"
REDIS_LOG_PATH=$REDIS_HOME/var/logs/keepalived-redis-state.log
echo "[fault]" >> $REDIS_LOG_PATH
date >> $REDIS_LOG_PATH

