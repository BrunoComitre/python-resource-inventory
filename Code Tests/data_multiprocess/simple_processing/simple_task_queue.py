import time
import multiprocessing

from tasks import get_word_counts


PROCESSES = multiprocessing.cpu_count() -1
NUMBER_OF_TASKS = 10

def processes_task(task_queue):
    while not task_queue.empty():
        book = task_queue.get()
        get_word_counts(book)
    return True

def add_tasks(task_queue, number_of_tasks):
    for num in range(number_of_tasks):
        task_queue.put('pride-and-prejudice.txt')
        task_queue.put('heart-of-darkness.txt')
        task_queue.put('frankenstein.txt')
        task_queue.put('dracula.txt')
    return task_queue

def run():
    empty_task_queue = multiprocessing.Queue()
    full_task_queue = add_tasks(empty_task_queue, NUMBER_OF_TASKS)
    processes = []
    print(f'RODANDO COM :: {PROCESSES} PROCESSOS!') 
    start = time.time()

    for n in range(PROCESSES):
        p = multiprocessing.Process(target=processes_task, args=(full_task_queue,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'TEMPO GAST0 :: {time.time() - start:.10f}')

if __name__ == "__main__":
    run()
