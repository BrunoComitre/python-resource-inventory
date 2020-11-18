from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

q = Queue(maxsize=2)

async def consumer():
    async for item in q:
        try:
            print('Doing work on %s' % item)
            await gen.sleep(0.01)
        finally:
            q.task_done()

async def producer():
    for item in range(5):
        await q.put(item)
        print('Put %s' % item)

async def main():
    # Start consumer without waiting (since it never finishes).
    IOLoop.current().spawn_callback(consumer)
    await producer()     # Wait for producer to put all tasks.
    await q.join()       # Wait for consumer to finish all tasks.
    print('Done')

IOLoop.current().run_sync(main)
