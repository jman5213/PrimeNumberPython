import itertools
import multiprocessing
from math import sqrt
from time import perf_counter


def prime(num: int) -> bool:
    """
    Returns a bool representing the primality of the argument

    :param int num: a positive integer that follows the pattern 6n+/-1
    :returns: True if num is prime, False otherwise
    :rtype: bool
    """
    for div in range(5, int(sqrt(num)) + 1, 6):
        if num % div == 0 or num % (div + 2) == 0:
            return False
    return True


def work(chunk: list) -> list:
    to_return = []
    for num in chunk:
        if prime(num):
            to_return.append(num)
    return to_return


def num_range():
    last = 6
    while True:
        # Find the starting points for `6n - 1` and `6n + 1`
        first_minus_1 = (last + 1) // 6 * 6 - 1
        if first_minus_1 < last:
            first_minus_1 += 6

        first_plus_1 = (last - 1) // 6 * 6 + 1
        if first_plus_1 < last:
            first_plus_1 += 6

        # Generate ranges
        result = []
        minus_iter = range(first_minus_1, last+chunk_size + 1, 6)
        plus_iter = range(first_plus_1, last+chunk_size + 1, 6)

        # Merge the ranges directly
        result.extend(minus_iter)
        result.extend(plus_iter)
        last += chunk_size
        yield result


if __name__ == '__main__':
    calcTo: int = int(input("Calculate the nth prime:"))
    time1 = perf_counter()

    max_processes = multiprocessing.cpu_count()
    chunk_size = 100000
    processes = []
    nums_found = 3
    chunks = num_range()
    current_chunks = []

    with multiprocessing.Pool(max_processes) as pool:
        while True:
            current_chunks = list(itertools.chain(*pool.map(work, [next(chunks) for i in range(max_processes)])))
            if len(current_chunks) + nums_found < calcTo:
                nums_found += len(current_chunks)
            else:
                current_chunks.sort()
                time2 = perf_counter()
                print(f'Your #: {current_chunks[calcTo-nums_found-1]}\nTime: {time2 - time1}sec')
                break
