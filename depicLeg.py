from collections import Counter
import math
import random

def split(message): # take a string of any length, return two strings of half the length. if length is odd, return the smaller number first. eg. message = 11001, out = [11,001] 
    if len(message) == 1:
        message = '0'+message # if the message is length 1, add a zero to the front. eg. if message = 1, message = 01
    halfLength = math.floor(len(message)/2)
    out = [message[0:halfLength], message[halfLength:]]
    return out

def leftRotate(message, amount): # message = str, amount = int. eg. leftRotate(11001, 2) = 00111
    out = message[amount:] + message[:amount]
    return out

def rightRotate(message, amount): # message = str, amount = int. eg. rightRotate(11001, 2) = 01110
    out = message[len(message)-amount:] + message[:len(message)-amount]
    return out

def depic(m):
    m = [m[i:i+8] for i in range(0, len(m), 8)] # split 56 digit message into 7 8 digit chuncks

    sumM = [] # list of the sum of the digits in the message

    for i in range(8): # split
        sum_ = 0
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
        # print('l1', l1)
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