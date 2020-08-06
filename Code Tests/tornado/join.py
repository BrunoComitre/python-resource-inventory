from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue, PriorityQueue, LifoQueue
from threading import Thread
import random

q = Queue(maxsize=2)
# q = PriorityQueue()
# q = LifoQueue()
SENTINEL = "END"

async def consumer():
    async for item in q:
        ts = random.randrange(0,5)
        try:
            while True:
            #     item = queue.get()
                if item != SENTINEL:
                    print(f"CONSUMER :: Trabalho em: {item}, TEMPO :: {ts}")
                    await gen.sleep(ts)
                    queue.task_done()
        finally:
            print("Receba SENTINEL, o consumer estará fechado.")
            print()
            q.task_done()
            break
            # continue

async def producer():
    for item in range(5):
        # time.sleep (0.01)
        await q.put(item)
        print(f"PRODUCER :: Elemento em: {item}")
    q.put(SENTINEL)
    print("Insert Sentinel")

async def main():
    IOLoop.current().spawn_callback(consumer)
    await producer()
    await q.join()
    print('Done')

IOLoop.current().run_sync(main)
