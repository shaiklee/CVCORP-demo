import multiprocessing
def fun(x):
    time.sleep(1)
    for i in range(x):
        print(i)
def fun1():
    t1=threading.Thread(target=fun, args=(10000,))
    t2=threading.Thread(target=fun, args=(20000,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    p1=multiprocessing.Process(target=fun1,args=())
    p2 = multiprocessing.Process(target=fun1, args=())
    p3 = multiprocessing.Process(target=fun1, args=())
    p4 = multiprocessing.Process(target=fun1, args=())
    p5 = multiprocessing.Process(target=fun1, args=())
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    print("Main thread done")
