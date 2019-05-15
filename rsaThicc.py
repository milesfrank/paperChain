from primeStuff import relPrime, isPrime
import random
import time
from modInv import modinv
import math


initPrimes = [9013287591422353,20319995244432029]

start = time.time()

p,q = initPrimes

b = (p-1)*(q-1)

n = p*q
e = 65537 # rel prime to b

d = modinv(e,b) # d * e mod b = 1

stop = time.time()

m = random.randint(1,n) # anything < n
mhat= pow(m,e,n)
decode = pow(mhat,d,n)


print(initPrimes)
print('public key',e,n)
print('private key',d)
# print('time', stop-start)
# print(decode == m)
# print(m)
# print(mhat)
# print(decode)