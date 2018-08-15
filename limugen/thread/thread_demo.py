#!/usr/bin/env python3
__Author__ = "limugen"

import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thead.__init__init(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("开始线程:" + self.name)
        print_time(self.time,self.counter,5)
        print("退出线程:" + self.name)

    def print_time(threadName,delay,counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            count -= 1

thread1 = myThread(1,"name1",1)
thread1 = myThread(2,"name2",2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出线程")