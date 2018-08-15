#!/bin/bash
REDIS_PASSWD="test"
REDIS_HOME="/usr/local/redis"
VIP="172.16.2.99/24"
ETH="eth0"
REDIS_STATUS_PATH=$REDIS_HOME/var/logs/Redis_status.log
CHECK_STATUS=`$REDIS_HOME/bin/redis-cli -a $REDIS_PASSWD PING 2>/dev/null`
ROLE_STATUS=`$REDIS_HOME/bin/redis-cli -a $REDIS_PASSWD INFO 2>/dev/null | grep role`

if [ "$CHECK_STATUS" = "PONG" ]
then
    echo "`date` redis is running" >> $REDIS_STATUS_PATH
    $REDIS_HOME/bin/redis-cli -a $REDIS_PASSWD INFO 2>/dev/null | grep role| grep master
    #if [ "$ROLE_STATUS" == "role:master" ]
    if [ $? == 0 ]
    then
        echo "`date` Redis is on status of master" >> $REDIS_STATUS_PATH
        ip addr list | grep $VIP 2>&1 /dev/null
        if [ $? == 0 ]
        then
            echo "`date` vip of $VIP is setted on server" >> $REDIS_STATUS_PATH
        else
            ip addr add $VIP dev $ETH
            echo "`date` excute command 'ip addr add $VIP dev $ETH' on server" >> $REDIS_STATUS_PATH
        fi
    else
        ip addr list | grep $VIP 2>&1 /dev/null
        if [ $? == 0 ]
        then
            echo "`date` vip of $VIP is setted on server" >> $REDIS_STATUS_PATH
            echo "`date` excute command 'ip addr del $VIP dev $ETH' on server" >> $REDIS_STATUS_PATH
            ip addr del $VIP dev $ETH
        else
            echo "`date` Redis is on status of slave" >> $REDIS_STATUS_PATH
        fi
    fi
    exit 0
else
    echo "`date` redis is not ailviliable" >> $REDIS_STATUS_PATH
    ip addr list | grep $VIP 2>&1 /dev/null
    if [ $? == 0 ]
    then
        echo "`date` vip of $VIP is setted on server" >> $REDIS_STATUS_PATH
        echo "`date` excute command 'ip addr del $VIP dev $ETH' on server" >> $REDIS_STATUS_PATH
        ip addr del $VIP dev $ETH
    else
        echo "`date` vip of $VIP is not setted on server"
    fi
    echo "`date` redis is not ailviliable" >> $REDIS_STATUS_PATH
    exit 1
fi

