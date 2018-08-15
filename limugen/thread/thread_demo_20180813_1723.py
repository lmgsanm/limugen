#!/usr/bin/env python3
__Author__ = "limugen"
#!/usr/bin/env python3
__Author__ = "limugen"
import _thread
import time

def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("{0}:{1}".format(threadName,time.ctime(time.time())))
try:
    _thread.start_new_thread(print_time,("nam1",2))
    _thread.start_new_thread(print_time,("nam2",4))
except:
    print("Error:无法启动线程")

while 1:
    pass

# print(print_time("name1",2))