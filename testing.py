from depic import depic
from collections import Counter
import random

c = []

for i in range(0, 100000):
    m = '0'*(56-len(str(i))) + str(i)
    # m = ''.join(str(random.randint(0,9)) for _ in range(48)) + '00000001'
    b = depic(m)
    # m = [m[i:i+8] for i in range(0, len(m), 8)]
    # print(m,b)
   #  print(b)
    c.append(b)

# # collisions
cols = 0
count = Counter(c)
for i in count:
   cols += count[i] - 1
print(cols)

# print(depic('18135928045066397601407902506027075012944460791487977771'))
