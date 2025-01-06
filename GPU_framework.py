from math import sqrt
from time import perf_counter
from numba import jit

calcTo: int = int(input("Calculate the nth prime:"))
time1 = perf_counter()


@jit(nopython=True)
def prime(num: int) -> bool:
    """
    Returns a bool representing the primality of the argument

    :param int num: a positive integer that follows the pattern 6n+/-1
    :returns: True if num is prime, False otherwise
    :rtype: bool
    """
    for div in range(5, int(sqrt(num))+1, 6):
        if num % div == 0 or num % (div+2) == 0:
            return False
    return True

@jit(nopython=True)
def main():
    primes_found: int = 2
    current_num: int = 1

    while primes_found < calcTo:
        current_num += 4
        primes_found += prime(current_num)

        if primes_found >= calcTo:
            return current_num

        current_num += 2
        primes_found += prime(current_num)

    return current_num


if __name__ == "__main__":
    num = main()
    time2 = perf_counter()
    print(f'Your #: {num} \
          \nTime: {time2-time1}sec')