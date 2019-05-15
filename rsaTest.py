from primeStuff import relPrime
import random

initPrimes = [3,7]

p,q = initPrimes

b = (p-1)*(q-1)

n = p*q
e = random.choice(relPrime(b)) # rel prime to b

d = 1# e mod b = 1
while (d*e)%b != 1:
    d += 1

m = random.randint(1,n) # anything < n

mhat= (m**e)%n

decode = (mhat**d)%n


print(b,e,d)
print(mhat,decode)