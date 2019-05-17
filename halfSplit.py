import math

def split(m):
    m = m[2:]
    h = math.floor(len(m)/2)
    s = [m[0:h], m[h:]]
    return s

def leftRotate(x, n): # input x as string
   out = x[n:] + x[:n]
   return out

def rightRotate(x, n): # input x as string
   out = x[len(x)-n:] + x[:len(x)-n]
   return out

print(leftRotate('11100', 2))
print(rightRotate('11100', 2))