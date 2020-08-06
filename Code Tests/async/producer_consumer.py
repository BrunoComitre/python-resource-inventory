from threading import Thread
import time
import queue

q = queue.Queue()
SENTINEL = "END"

def producer(queue):
    for i in range(5):
    # time.sleep (0.01) # Você acha que o resultado será alterado se eu descomentar essa linha?
        print(f"Inserindo Elemento {i}")
        queue.put(i)
    queue.put(SENTINEL)
    print("Insert Sentinel")

def consumer(queue):
    while True:
        item = queue.get()
        if item != SENTINEL:
            print(f"Recuperar elemento {item}")
            queue.task_done()
        else:
            print("Receba SENTINEL, o consumer estará fechado.")
            queue.task_done()
            break

threads = [Thread(target=producer, args=(q, )), Thread(target=consumer, args=(q, )),]

for thread in threads:
    thread.start()

q.join()