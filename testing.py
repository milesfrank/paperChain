from depic import depic
from collections import Counter
import random

c = []
for i in range(0, 100000):
    m = '0'*(56-len(str(i))) + str(i)
   #  m = ''.join(str(random.randint(0,9)) for _ in range(56))
    b = depic(m)
   #  print(b)
    c.append(b)

t = [[],[],[],[],[],[],[],[]]

for i in c:
   for j in range(8):
      t[j].append(i[j])

# for i in t:
#    print(Counter(i))

cols = 0
count = Counter(c)
for i in count:
   cols += count[i] - 1
print(cols)