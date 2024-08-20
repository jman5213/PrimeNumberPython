from math import sqrt
from time import perf_counter

calcTo: int = int(input("Calculate the nth prime:"))
primesFound: int = 2
currentNum: int = 6
time1 = perf_counter()


def prime(num: int) -> bool:
    """
    Returns a bool representing the primality of the argument

    :param num: a positive integer that follows the pattern 6n+/-1
    :type num: int
    :returns: True if num is prime, False otherwise
    :rtype: bool
    """
    for div in range(5, int(sqrt(num))+1, 6):
        if num % div == 0 or num % (div+2) == 0:
            return False
    return True


def main():
    global primesFound, currentNum
    while primesFound < calcTo:
        primesFound += prime(currentNum-1) + prime(currentNum+1)
        currentNum += 6

    time2 = perf_counter()
    print(f'Your #: {currentNum-7 if primesFound == calcTo else currentNum-5} \
          \nTime: {time2-time1}sec')


if __name__ == "__main__":
    main()
