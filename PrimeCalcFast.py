from math import sqrt
from time import perf_counter

calcTo=int(input("calculate the nth prime #: "))
currentNum=1
primesFound=0
time1=perf_counter()

def prime(num):
  for div in range(3,int(sqrt(num))+1,2):
    if num%div == 0:
      return False
  return True
  
while primesFound<calcTo:
  if prime(currentNum):
    primesFound+=1
  currentNum+=2

time2 = perf_counter()
print('Your #:',str(currentNum-2)+'\nTime:',str(time2 -time1)+"sec")