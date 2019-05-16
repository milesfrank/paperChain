import random

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

    for i in range(8):
        w = int(str(e[i])[-1]) + e[i] + i + 2
        e[i] = int(str(w)[0]) * w * (i+1)

    l = []
    for i in range(24):
        a = e[i%8]
        b = e[(i+1)%8]
        l.append(b)
        p = fun[i%3](a,b)
        e[(i+1)%8] = p

    inter = 0
    final = ''
    for i in range(8):
        nextBit = str(((inter >> i) ^ (e[i] << i)) % 10)
        final += nextBit
        inter = e[i]
    return l
    # return int(final)

# for i in range(10):
#     m = '0'*55 + str(i)
#     print(m,cepic(m))

# 0 (000) = 4 (100)
# 1(001) = 6 (110)
# 3 (011) = 7 (111)

m = '0'*55 + '1'
u = cepic(m)
m = '0'*55 + '6'
o = cepic(m)

for i in range(len(u)):
    print(u[i], o[i])