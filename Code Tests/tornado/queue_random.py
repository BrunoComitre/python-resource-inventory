from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue, PriorityQueue, LifoQueue
import random


q = Queue(maxsize=2)
# q = PriorityQueue()
# q = LifoQueue()

async def consumer():
    async for item in q:
        ts = random.randrange(0,5)
        print(ts)
        try:
            print(f'Fazendo trabalho em: {item}')
            await gen.sleep(ts)
        finally:
            q.task_done()

async def producer():
    for item in range(5):
        await q.put(item)
        print(f' Colocando em: {item}')

async def main():
    # Inicie o consumer sem esperar (pois nunca termina).
    IOLoop.current().spawn_callback(consumer)
    await producer()     # Aguarde o producer colocar todas as tarefas.
    await q.join()       # Aguarde o consumer concluir todas as tarefas.
    print('Done')

IOLoop.current().run_sync(main)
