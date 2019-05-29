import binascii
from modInv import modinv

def NumToText(n):
    return str(binascii.unhexlify(hex(n)[2:]))[2:-1]

def TextToNum(m):
    return int(str(binascii.hexlify(str.encode(m)))[2:-1].upper(),16)

def generateKeys(initPrimes):
    p,q = initPrimes

    b = (p-1)*(q-1)

    n = p*q
    e = 65537 # rel prime to b

    d = modinv(e,b) # d * e mod b = 1

    return [e,n,d]

def encodeNum(message, e, n): # input is int
    if message > n:
        print('message too large')
        return ''
    else:
        return pow(message, e, n)

def decodeNum(encoded, d, n): # output is int
    return pow(encoded,d,n)

def encode(message, e, n): # input is str
    return encodeNum(TextToNum(message), e, n)

def decode(encoded, d, n): # output is str
    return NumToText(decodeNum(encoded, d, n))

initPrimes = [7212610147295474909544523785043492409969382148186765460082500085393519556525921455588705423020751421,
2908511952812557872434704820397229928450530253990158990550731991011846571635621025786879881561814989]

e,n,d = generateKeys(initPrimes)

m = 'jz is a meme'

en = encode(m,e,n)
print(en)
print(decode(en,d,n))