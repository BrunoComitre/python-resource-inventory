import os
import logging
import multiprocessing

from tasks import get_word_counts
from redis_queue_worker import worker


PROCESSES = 4


def run():
    processes = []
    print(f'RODANDO COM {PROCESSES} PROCESSOS!')
    while True:
        for w in range(PROCESSES):
            p = multiprocessing.Process(target=worker)
            processes.append(p)
            p.start()
        for p in processes:
            p.join()


if __name__ == '__main__':
    run()
