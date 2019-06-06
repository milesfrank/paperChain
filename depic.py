import math

def split(message): # returns a list of the first half of message, and the second half of message. if length is odd, return the smaller number first. eg. message = 11001, out = [11,001] 
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

    sumList = [] # list of the sum of the digits in the message

    # sum all the nth digits
    for i in range(8): # for the ith number
        summ = 0
        for j in range(7): # for each chunck in m
            summ += int(m[j][i]) # add the ith digit in the jth chunk to sum
        sumList.append(summ)

    nonceSum = 0
    for i in m[-1]: # sum nonce
        nonceSum += int(i)

    for i in range(8):
        sumList[i] = sumList[i] + nonceSum + i + 1 # for each value in sumList, add sum of nonce, position, and 1 to it

    binSums = ''
    for summ in sumList:
        binSums+=bin(summ)[2:] # convert each sum in sumList to binary, and add it onto binSums

    # create q1,q2,q3,q4 which are all a quarter of binSums
    q1, q2 = split(split(binSums)[0]) 
    q3, q4 = split(split(binSums)[1])

    a = q1+q2
    b = q2+q3
    c = q3+q4
    d = q4+q1

    finalChunks = []

    last = int(m[-1][-1]) # last number of the nonce

    for i in [a,b,c,d]: # loop through a,b,c,d
        s1 = split(i) # split i to create s1
        r1 = [leftRotate(s1[0],last%len(s1[0])),rightRotate(s1[1],last%len(s1[1]))] # left rotate the first item of s1 by 'last' mod the length of the first item, and right rotate the second item of s1 by 'last' mod the length of the second item
        xor1 = bin(int(r1[0],2) ^ int(r1[1],2))[2:] # xor the two rotated ammounts
        s2 = split(xor1) # repeat
        r2 = [rightRotate(s2[0],last%len(s2[0])),leftRotate(s2[1],last%len(s2[1]))] # ^^
        xor2 = bin(int(r2[0],2) ^ int(r2[1],2))[2:] # ^^
        finalChunks.append(str(int(xor2,2))) # add the final value in decimal for

    for i in finalChunks:
        if len(i) == 1:
            pad = str(int(i)+last+1)
            paddedChunk = i + pad
            finalChunks[finalChunks.index(i)] = paddedChunk

    print(finalChunks)

    final = finalChunks[0][0] + finalChunks[1][0] + finalChunks[2][0] + finalChunks[3][0] + finalChunks[0][-1] + finalChunks[1][-1] + finalChunks[2][-1] + finalChunks[3][-1]

    print(final)

    return final