import itertools
import multiprocessing

max_processes = multiprocessing.cpu_count()
chunk_size = 1000
processes = []

def func(stuff:list) -> list:
    new = []
    for item in stuff:
        if item%5==0:
            new.append(item+2)

    return new


def num_range():
    last = 0
    while True:
        cleaned = []
        for item in range(last,last+chunk_size):
            if item % 5 == 0:
                cleaned.append(item)
        last += chunk_size
        yield cleaned

if __name__ == '__main__':
    goal = 100_000_000
    nums_found = 0
    chunks = num_range()
    current_chunks = []
    with multiprocessing.Pool(max_processes) as pool:
        while True:
            current_chunks = list(itertools.chain(*pool.map(func,[next(chunks) for i in range(max_processes)])))
            if len(current_chunks)+nums_found <= goal:
                nums_found += len(current_chunks)
            else:
                print(current_chunks)
                print(current_chunks[goal-nums_found]-2)
                break