import asyncio
import time
import threading
from concurrent.futures import ThreadPoolExecutor


async def basic_coroutine(name, delay):
    print(f"[{name}] started on thread {threading.current_thread().name}")
    await asyncio.sleep(delay)
    print(f"[{name}] finished after {delay}s")
    return name

async def task_demo():

    task1 = asyncio.create_task(basic_coroutine("task", 3))
    task2 = asyncio.create_task(basic_coroutine("task1", 1))
    r1=await task1
    r2=await task2
    print("Task results: ", r1, r2)



async def gather_demo():

    results = await asyncio.gather(
        basic_coroutine("g1", 3),
        basic_coroutine("g2", 2),
        basic_coroutine("g3", 1),
        return_exceptions=True
    )
    print("Gather results:", results)



async def wait_demo():

    tasks = [
        asyncio.create_task(basic_coroutine("w1", 3)),
        asyncio.create_task(basic_coroutine("w2", 1)),
        asyncio.create_task(basic_coroutine("w3", 2)),
    ]

    done, pending = await asyncio.wait(tasks, timeout=2)

    print("Done tasks:")
    for t in done:
        print(" ", t.result())

    print("Pending tasks:")
    for t in pending:
        print(" ", t.get_name())
        t.cancel()


async def as_completed_demo():
    tasks = [
        basic_coroutine("a1", 3),
        basic_coroutine("a2", 1),
        basic_coroutine("a3", 2),
    ]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print("Completed:", result)


async def timeout_demo():
    try:
        await asyncio.wait_for(basic_coroutine("timeout_task", 1.5), timeout=2)
    except asyncio.TimeoutError:
        print("Timeout occurred!")



async def cancellation_demo():
    task = asyncio.create_task(basic_coroutine("cancel_me", 1))
    print("before sleep")
    await asyncio.sleep(2)
    print("after sleep")
    task.cancel()
    try:
        print("before await task")
        await task
        print("after await task")
    except asyncio.CancelledError:
        print("Task was cancelled")



def task_callback(task):
    print("Callback result:", task.result())

async def callback_demo():

    task = asyncio.create_task(basic_coroutine("callback_task", 3))
    task.add_done_callback(task_callback)

    await task



async def future_demo():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    def set_future():
        time.sleep(1)
        future.set_result("Future done")

    t=threading.Thread(target=set_future)
    t.start(); t.join()
    result = await future
    print(result)


lock = asyncio.Lock()

async def lock_worker(name):
    async with lock:
        print(f"{name} acquired lock")
        await asyncio.sleep(1)
        print(f"{name} released lock")

async def lock_demo():
    await asyncio.gather(
        lock_worker("L1"),
        lock_worker("L2"),
        lock_worker("L3"),
    )



semaphore = asyncio.Semaphore(2)

async def semaphore_worker(name):
    async with semaphore:
        print(f"{name} entered semaphore")
        await asyncio.sleep(2)
        print(f"{name} exited semaphore")

async def semaphore_demo():
    await asyncio.gather(
        *(semaphore_worker(f"S{i}") for i in range(5))
    )



async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f"Produced {i}")
        await asyncio.sleep(0.5)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()

async def queue_demo():
    queue = asyncio.Queue()

    prod = asyncio.create_task(producer(queue))
    cons = asyncio.create_task(consumer(queue))

    await prod
    await queue.join()
    cons.cancel()


def blocking_function(x):
    print("Blocking function")
    time.sleep(5)
    return x * x

async def executor_demo():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_function, 5)
        print("Starting or ending")
        print("Executor result:", result)


async def error_task():
    await asyncio.sleep(5)
    raise ValueError("Something went wrong")
async def exception_demo():

    try:
        await error_task()
    except Exception as e:
        print("Caught exception:", e)



async def main():
    # await basic_coroutine("test", 3)
    # await basic_coroutine("test1", 1)
    # await task_demo()
    # await gather_demo()
    # await wait_demo()
    # await as_completed_demo()
    # await timeout_demo()
    # await cancellation_demo()
    # await callback_demo()
    # await future_demo()
    # await lock_demo()
    # await semaphore_demo()
    # await queue_demo()
    # await executor_demo()
    await exception_demo()
    return "hello"

if __name__ == "__main__":
    asyncio.run(main())