from tornado.queues import PriorityQueue

q = PriorityQueue()
q.put((1, 'medium-priority item'))
q.put((0, 'high-priority item'))
q.put((10, 'low-priority item'))

print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())
