import multiprocessing

def run():
    books = [
        'pride-and-prejudice.txt',
        'heart-of-darkness.txt',
        'frankenstein.txt',
        'dracula.txt'
    ]
    queue = multiprocessing.Queue()

    print('ENFILEIRANDO ...')
    for book in books:
        print(book)
        queue.put(book)

    print('\nDESENFILEIRANDO ...')
    while not queue.empty():
        print(queue.get())


if __name__ == '__main__':
    run()
