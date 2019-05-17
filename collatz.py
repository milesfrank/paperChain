def collat(n):
    if(n%2==0):
        n/=2
    else:
        n*=3
        n+=1
    return n

def collatz(n, t):
    i=0
    if(not t):
        while(n!=1):
            n = collat(n)
            i+=1
        return i
    else:
        for i in range(t):
            n = collat(n)
        return int(n)

l = []
for i in range(1,10):
    l.append(collatz(i, False))

