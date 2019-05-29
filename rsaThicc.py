from modInv import modinv
from conversion import NumberToText, TextToNumber

def generateKeys(initPrimes):
    p,q = initPrimes

    b = (p-1)*(q-1)

    n = p*q
    e = 65537 # rel prime to b

    d = modinv(e,b) # d * e mod b = 1

    return [[e,n],d]

def encode(message, e, n):
    if message > n:
        print('message too large')
        return ''
    else:
        return pow(message, e, n)

def decode(encoded, d, n):
    return pow(mhat,d,n)

initPrimes = [7212610147295474909544523785043492409969382148186765460082500085393519556525921455588705423020751421,
2908511952812557872434704820397229928450530253990158990550731991011846571635621025786879881561814989]

public, private = generateKeys(initPrimes)
e,n = public
d = private

print('public',e,n)
print('private',d)

message = TextToNumber('jz is a meme')

mhat = encode(message, e, n)

print('---')

print(mhat)