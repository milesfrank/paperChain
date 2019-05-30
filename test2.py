from depicLeg import depic
import random
from collections import Counter

c = []

for i in range(0, 100000):
    # m = '0'*(56-len(str(i))) + str(i)
    m = ''.join(str(random.randint(0,9)) for _ in range(48)) + '00000001'
    c.append(depic(m))

cols = 0
count = Counter(c)
for i in count:
   cols += count[i] - 1
print(cols)