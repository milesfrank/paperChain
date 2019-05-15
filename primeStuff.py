import math 

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def primeFactors(n): 

    factors = []
      
    while n % 2 == 0: 
        factors.append(2), 
        n = n / 2
          
    for i in range(3,int(math.sqrt(n))+1,2):  # start at 3, go to sqrt n, iterate by 2
        while n % i== 0: 
            factors.append(i), 
            n = n / i 
              
    if n > 2: 
        factors.append(int(n)) 

    return factors

def relPrime(n):
    nFactors = primeFactors(n)
    shareFactors = True
    m = 1
    ms = []
    while shareFactors or len(ms) < 50:
        m += 1
        mFactors = primeFactors(m)
        shareFactors = bool(set(nFactors) & set(mFactors))
        if not shareFactors:
            ms.append(m)

    return ms
