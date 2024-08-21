from math import sqrt
from time import perf_counter

calcTo: int = int(input("Calculate the nth prime:"))
time1 = perf_counter()


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


def main():
    primesFound: int = 2
    currentNum: int = 1

    while primesFound < calcTo:
        currentNum += 4
        primesFound += prime(currentNum)

        if primesFound >= calcTo:
            return currentNum

        currentNum += 2
        primesFound += prime(currentNum)

    return currentNum


if __name__ == "__main__":
    num = main()
    time2 = perf_counter()
    print(f'Your #: {num} \
          \nTime: {time2-time1}sec')
