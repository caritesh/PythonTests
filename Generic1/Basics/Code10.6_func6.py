import math
x = "welcome"
y = ['hi','hello','welcome']
print(math.sqrt(4))
z = list(map(lambda n: n.upper(),y))
for i in z:
    print(i)
type(z)
print(z)


def testf():
    yield 10
    yield 20
    yield 30
    yield 40

for x in testf():
    print()

def testnum():
    i = 1
    while True:
        yield i*i
        i += 1

for n in testnum():
    if n > 20:
        break
    print(n)
'''
import pandas as pd
import numpy as np
import keras as krs'''

from _functools import reduce
words = ['welcome','cool','welcome','win','win','win','winter','summer']
print(words.count('welcome'))
for i in words:
    print(i,len(i))

for i in words:
    print(i,words.count(i))

