#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-15 20:45:35
# @copyright by hoojo@2018
# @changelog Added python3 `thread->thread module` example


import threading
import time


'''
threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
    threading.currentThread(): 返回当前的线程变量。
    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
    
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
    run(): 用以表示线程活动的方法。
    start():启动线程活动。
    join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
'''

exit_flag = False

class MyThread(threading.Thread):
    
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        
        self.threadId = threadId
        self.name = name
        self.count = count
        
    def run(self):
        threading.Thread.run(self)    
        
        print('线程开始：%s', self.name)
        print_time(self, self.name, 1, self.count)
        print('线程退出：%s', self.name)
        
    def exit(self):
        print('exit')
        # threading.Thread.exit() 
        
        
def print_time(_thread, threadName, delay, count):
    while count:
        if exit_flag:
            _thread.exit()
        
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        count -= 1


# 创建线程
thread1 = MyThread(1, 'Thread-1', 5)            
thread2 = MyThread(2, 'Thread-2', 5)       

# 启动新线程
thread1.start()
thread2.start()

exit_flag = True
# 等待线程执行完成
thread1.join()
thread2.join()

print("退出主线程")     