#Class Thread

#thread

# threadpool executor


# from threading import Thread
# import time

# class A(Thread):
#     def run(self):
#         for i in range(10):
#             print(i)
#             time.sleep(1)
# obj=A()
# obj1=A()
# obj.start()
# obj1.start()
# obj.join()# joining obj thread to main thread
# obj1.join()
# print("hello")
#
import threading_que
import time
from concurrent.futures import ThreadPoolExecutor


# def fun(name,x):
#     for i in range(x):
#         print(f"{name}: {i}")
#         time.sleep(1)
# t1=threading.Thread(target=fun,name="thread1",args=("thread-1",10))
# t2=threading.Thread(target=fun,name="thread2",args=("thread-2",10))
# t1.start()
# t2.start()
#
# print(t1.is_alive())
# print(t2.is_alive())
#
# print("Main thread is ended")
# x=0
# def fun1(a):
#     global x
#     for i in range(a):
#         x+=1
#         print(threading.current_thread().name)
#         time.sleep(0.001)
# fun1(10)#
# fun1(10)#
# t1=threading.Thread(target=fun1,name="x",args=(10,))
# t2=threading.Thread(target=fun1,name="y",args=(10,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(x)

# l=threading.Lock()
# def fun1(a):
#     global x
#     for i in range(a):
#         with l:
#             x+=1
#             print(threading.current_thread().name)
#             time.sleep(0.001)
#
# t1=threading.Thread(target=fun1,name="Thread-1",args=(10,))
# t2=threading.Thread(target=fun1,name="Thread-2",args=(10,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(x)



# s=threading.Semaphore(3)
# def fun(name,x):
#     for i in range(x):
#         with s:
#             print(name,i)
#             time.sleep(0.5)
#
# l=[threading.Thread(target=fun,args=(f"Thread-{i}",10)) for i in range(1,11)]
# for t in l:
#     t.start()
# for t in l:
#     t.join()
# print("Main thread ends")



# pubsub -> event, condition

#
# c=threading.Condition()
# l=[]
# def publish():
#     print("publish is started")
#     with c:
#         time.sleep(5)
#         l.append("item")
#         c.notify()
#     print("publish is done")
#
# def consume():
#     print("consume is started")
#     with c:
#         while not l:
#             c.wait()
#         print(l[0])
#     print("consume is done")
#
# t=threading.Thread(target=publish)
# t1=threading.Thread(target=consume)
# t.start()
# t1.start()



# e=threading.Event()
#
# def fun():
#     print("fun is started")
#     e.wait()
#     time.sleep(1)
#     print("fun is done")
# t=threading.Thread(target=fun)
# t.start()
# time.sleep(5)
# e.set()

# def fun():
#     print("hello")
#     for i in range(10):
#         print(f"Thread - {i}")
# t= threading.Timer(5, fun)
# t.start()



# def fun2():
#     raise ValueError("threading error")
#
# t=threading.Thread(target=fun2)
# t.start()
# for i in range(10):
#     print("hello world")

def fun(x):
    time.sleep(1)
    # print(x)
    return x

with ThreadPoolExecutor(max_workers=3) as executor:
    t=executor.submit(fun, 10)
    l= executor.map(fun, [1,12,18,135,6543])
    print(t.result())
    for i in l:
        print(i)
