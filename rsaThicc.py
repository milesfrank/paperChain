from primeStuff import relPrime, isPrime
import random
import time

# initPrimes = [7753, 7901]
# initPrimes = [1153, 1217]
initPrimes = []

start = time.time()

while len(initPrimes) < 2:
    b = random.randint(1000,8000)
    if isPrime(b):
        initPrimes.append(b)

p,q = initPrimes

b = (p-1)*(q-1)

n = p*q
e = random.choice(relPrime(b)) # rel prime to b

d = 1# e mod b = 1
while (d*e)%b != 1:
    d += 1

stop = time.time()

# m = random.randint(1,n) # anything < n

# mhat= (m**e)%n

# decode = (mhat**d)%n


print(initPrimes)
print('public key',e,n)
print('private key',d)
print('time', stop-start)
# print('message', m)