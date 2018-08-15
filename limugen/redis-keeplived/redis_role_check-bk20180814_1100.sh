#!/bin/bash
REDIS_PASSWD="test"
REDIS_HOME="/usr/local/redis"
ROLE="MASTER"
VIP="172.16.2.99/24"
ETH="eth0"
REDIS_STATUS_PATH=$REDIS_HOME/var/logs/Redis_status.log
CHECK_STATUS=`$REDIS_HOME/bin/redis-cli -a $REDIS_PASSWD PING 2>/dev/null`
#ROLE_STATUS=`$REDIS_HOME/bin/redis-cli -a $REDIS_PASSWD INFO 2>/dev/null | grep role | grep master`

redis_health_check () {
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
        ip addr del $VIP dev $ETH 
#        exit 1
    fi
}

master_ip_check () {
    $REDIS_HOME/bin/redis-cli -a $REDIS_PASSWD INFO 2>/dev/null | grep role | grep $ROLE
    if [ $? == 0 ]
    then
        ip addr list | grep $VIP 2>&1 /dev/null
        if [ $? == 0 ]
        then
            date >> $REDIS_STATUS_PATH
            echo "Redis is on status of master" >> $REDIS_STATUS_PATH
        else
            ip addr add $VIP dev $ETH
        fi
    else
        date >> $REDIS_STATUS_PATH
        echo "Redis is on status of slave" >> $REDIS_STATUS_PATH
        exit 1
    fi
}
redis_health_check
master_ip_check
