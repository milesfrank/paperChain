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


    for i in range(24):
        a = e[i%8]
        b = e[(i+1)%8]
        p = fun[i%3](a,b)
        e[(i+1)%8] = p

    inter = 0
    final = ''
    for i in range(8):
        nextBit = str(((inter >> i) ^ (e[i] << i)) % 10)
        final += nextBit
        inter = e[i]

    return int(final)

# m = ‘’.join(str(random.randint(0,9)) for _ in range(56))
m = '0'*55 + '4'
print(m,cepic(m))