from collections import Counter
import math
import random

def split(m):
    if len(m) == 1:
        m = '0'+m
    h = math.floor(len(m)/2)
    s = [m[0:h], m[h:]]
    return s

def leftRotate(message, amount): # input message as string
    out = message[amount:] + message[:amount]
    return out

def rightRotate(message, amount): # input message as string
    out = message[len(message)-amount:] + message[:len(message)-amount]
    return out

def getint(m1, m2): # input strings
    i1 = m1.count('1')
    i2 = m2.count('0')
    return str(leftRotate(m1, i1) ^ rightRotate(m2, i2))[-1]

def depic(m):
    n = 8
    m = [m[i:i+n] for i in range(0, len(m), n)] # chuncc
    e = []

    for i in range(8): # split
        b = 0
        for j in range(7):
            b += int(m[j][i])
        e.append(b)

    b = 0
    for i in m[-1]: # sum nonce
        b += int(i)

    for i in range(8): # add stuff
        e[i] = e[i] + b + i + 1 # add sum of nonce, position, and 1

    q = '' # convert to binary
    for i in e:
        q+=bin(i)[2:]

    a, b = split(split(q)[0])
    c, d = split(split(q)[1])

    q = [a+b,b+c,c+d,d+a]
    new = []

    last = int(m[-1][-1])

    for i in q:
        l1 = split(i) # layer 1
        r1 = [leftRotate(l1[0],last%len(l1[0])),rightRotate(l1[1],last%len(l1[1]))] # rotate 1
        xor1 = bin(int(r1[0],2) ^ int(r1[1],2))[2:]
        l2 = split(xor1)
        r2 = [rightRotate(l2[0],last%len(l2[0])),leftRotate(l2[1],last%len(l2[1]))]
        xor2 = bin(int(r1[0],2) ^ int(r1[1],2))[2:]
        new.append(str(int(xor2,2)))


    for i in new:
        if len(i) == 1:
            new[new.index(i)] = i + i

    final = new[0][0] + new[0][1] + new[1][-2] + new[1][-1] + new[2][0] + new[2][-1] + new[3][1] + new[3][-2]

    return final

# depic('0'*55+'1')
m = ''.join(str(random.randint(0,9)) for _ in range(56))
depic(m)