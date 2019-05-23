from depic import depic
from collections import Counter
import random

d = [[],[]]
for i in range(0, 100000):
    # m = '0'*(56-len(str(i))) + str(i)
    m = ''.join(str(random.randint(0,9)) for _ in range(56))
    b = depic(m)
    # print(b)
    d[0].append({b:m})
    d[1].append(b)

# collisions
cols = 0
count = Counter(d[1])
for i in count:
   cols += count[i] - 1
   if(count[i] > 1):
        for j in d[0]:
            if(i in j):
                print(j)
