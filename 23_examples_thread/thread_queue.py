#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-16 23:10:21
# @copyright by hoojo@2018
# @changelog Added python3 `thread -> thread queue` example


import queue
import threading
import time

'''
Python 的 Queue 模块中提供了同步的、线程安全的队列类，
包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。

这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。

Queue 模块中的常用方法:
    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.full 与 maxsize 大小对应
    Queue.get([block[, timeout]])获取队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''

exit_flag = False

class MyThread(threading.Thread):
    
    def __init__(self, threadId, name, queue):
        threading.Thread.__init__(self)
        
        self.threadId = threadId
        self.name = name
        self.queue = queue
        
        print('---创建线程：%s-%s---' % (threadId, name))
        
    def run(self):
        threading.Thread.run(self)    
        
        print('线程开始：%s' % self.name)
        processing(self.name, self.queue)
        print('线程退出：%s' % self.name)
        
        
def processing(threadName, queue):
    while not exit_flag:
        # 加锁
        queueLock.acquire()
        
        if not workQueue.empty():
            data = workQueue.get()
            # 解锁
            queueLock.release()
            print ("%s processing  %s" % (threadName, data))
        else:
            # 解锁
            queueLock.release()
                
        time.sleep(1)


threadNames = [ "One", "Two", "Three", "Four", "Five" ]
threadList = [ "Thread-1", "Thread-2", "Thread-3" ]

# 创建线程锁
queueLock = threading.Lock()
# 创建线程队列
workQueue = queue.Queue(10)

threadId = 1
threads = []

for name in threadList: 
    # 创建线程
    thread = MyThread(threadId, name, workQueue)            
    
    thread.start()
    
    threads.append(thread)
    threadId += 1


# 填充队列
queueLock.acquire()

for name in threadNames:
    print('填充队列：%s' % name)
    workQueue.put(name)
    
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

exit_flag = True

# 等待所有线程完成
for t in threads:
    t.join()

print ("退出主线程") 