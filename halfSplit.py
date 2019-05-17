import math

def split(m):
    m = m[2:]
    h = math.floor(len(m)/2)
    s = [m[0:h], m[h:]]
    return s