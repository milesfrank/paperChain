import time
import random
from numpy import mean
from collections import Counter

fun = [lambda a,b: a + b] + \
    [lambda a,b: a * b]

def bepic(message):
    message **= 2
    for i in range(4):
        if i%4 < 2:
            a = int(str(message)[:2])
        else:
            a = int(str(message)[-2:])
        message = fun[i%2](a+2,message)
    return str(message)

totalCols = []

for i in range(100):
    for j in range(100000):
        c = []
        m = random.randint(1,10**9)
        c.append(bepic(m))
        cols = 0
        count = Counter(c)
        for k in count:
           cols += count[i] - 1
    totalCols.append(cols)
    print(i)

print(mean(totalCols))