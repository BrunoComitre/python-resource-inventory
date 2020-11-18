from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue, PriorityQueue, LifoQueue
import random

from threading import Thread
import time
import queue


q = Queue(maxsize=2)
## q = queue.Queue()
SENTINEL = "END"
# q = PriorityQueue()
# q = LifoQueue()

async def consumer(queue):
     while True:
         item = queue.get()
         try:
         async for item in q:
             if item != SENTINEL:
                 print(f"Recuperar elemento {item}")
                 q.task_done()
                 await gen.sleep(5)
     
        finally:
            print("Receba SENTINEL, o consumer estará fechado.")
            q.task_done()
            break


async def producer(queue):
    for item in range(5):
        # time.sleep (0.01) # Você acha que o resultado será alterado se eu descomentar essa linha?
        print(f"Inserindo Elemento {item}")
        await q.put(item)
    queue.put(SENTINEL)
    print("Insert Sentinel")

async def main():
    threads = [Thread(target=producer, args=(q, )), Thread(target=consumer, args=(q, )),]
    for thread in threads:
        thread.start()
    await q.join()       # Aguarde o consumer concluir todas as tarefas.
    print('Done')
    
IOLoop.current().run_sync(main)
