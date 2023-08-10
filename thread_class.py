"""
Process: The process is a program (set of instructions) in execution
Process cannot share the memory

Thread:
Thread is light weight processess
Threads can be used to perform complicated task in the backgound without interpting the main program
Thread can share memory

Methods:
run(): is the entry point for thread
start(): method starts a thread by calling the run method
join([time]): waits for threads to terminate
isAlive(): method checks whether a thread is still executing
getName(): method returns the name of a thread

"""
#import section
import threading
from threading import *
from time import sleep

class thread1(Thread):
    def run(self):
        for i in range(10):
            print("This is 1st thread",i)
            print(threading.current_thread().getName())
            sleep(2)
class thread2(Thread):
    def run(self):
        for i in range(10):
            print("This is 2st thread",i)
            print(threading.current_thread().getName())
            sleep(2)
t1=thread1()
t2=thread2()
t1.start()
print(t1.is_alive())
t1.join()
print(t1.is_alive())
sleep(1)
t2.start()


#import threading
#print(threading.current_thread().getName())
