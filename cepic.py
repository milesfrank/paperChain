import random
from collections import Counter
from collatz import collatz

fun = [lambda a,b: a & b] + \
    [lambda a,b: a | b] + \
    [lambda a,b: a ^ b]

def cepic(m):
    n = 8
    m = [m[i:i+n] for i in range(0, len(m), n)]
    e=[]

    for i in range(8):
        b = 0
        for j in range(7):
            b += int(m[j][i])
        e.append(b)

    # for i in range(len(e)-1):
    #     e[i] += e[-1]
    #     e[i] = collatz(e[i], 4)

    # print(e)

    inter = 0
    final = ''
    for i in range(8):
        nextBit = str(((inter >> i) ^ (e[i] << i)) % 10)
        final += nextBit
        inter = e[i]

    return (final)

c = []

for i in range(100):
    # m = ''.join(str(random.randint(0,9)) for _ in range(56))
    m = '0'*(56-(len(str(i)))) + str(i)
    c.append(cepic(m))

cols = 0
count = Counter(c)
for i in count:
    cols += count[i] - 1
print(count)
print(cols)