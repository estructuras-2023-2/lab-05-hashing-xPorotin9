import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from random import choice
%matplotlib inline
class HashTable:
  def __init__(self,h,n=10):
    self.h = h
    self.n = n
    self.bucket = [[] for i in range(n)]

    ## code
    ## code
    ## def insert(self, x)
  def insert(self, x):
    self.bucket[self.h(x)].append(x)

    ## def delete(self, x)
  def delete(self,x):
    poss = self.bucket[self.h(x)]
    for i in range(len(poss)):
      if poss[i] == x:
        return poss.pop[i]
    return None

    ## def findself, x)
  def find(self,x):
    poss = self.bucket[self.h(x)]
    for i in range(len(poss)):
      if poss[i] == x:
        return poss[i]
    return None
def mi_Mod(x,n=10):
    ## CODE
print(mi_Mod(52))
print(mi_Mod(3235235))
HT = HashTable(mi_Modn, 10)

x = 1234567
y = 76554334234
HT.insert(x)

## verificar que la tabla hash funciona
def randomFn(x, n=10):
    ##code
print(randomFn(52))
print(randomFn(3235235))
HT = HashTable(randomFn, 10)

x = 1234567
y = 76554334234
HT.insert(x)
print(randomFn(52))
print(randomFn(3235235))
print(randomFn(52))
print(randomFn(3235235))
def RandomHashFun(M, n=10):
    fnTable = [ None for i in range(M) ]
    for x in range(M):
        fnTable[x] = choice(range(n))
    def randomFn(x):
        return fnTable[x]
    return randomFn
randomFn2 = RandomHashFun(1000, 10)
print(randomFn2(52))
print(randomFn2(324))
print(randomFn2(52))
print(randomFn2(324))
HT = HashTable(randomFnTake2, 10)

x = 123
y = 76
HT.insert(x)

## verificar que la tabla hash funciona
