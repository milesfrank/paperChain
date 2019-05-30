from depic import depic
from collections import Counter
import random

c = []

# for i in range(0, 1000):
   #  m = '0'*(56-len(str(i))) + str(i)
   # m = ''.join(str(random.randint(0,9)) for _ in range(48)) + '00000001'
   # b = depic(m)
   #  m = [m[i:i+8] for i in range(0, len(m), 8)]
   #  print(m,b)
   # print(b)
   # c.append(b)
# b = ['17037501063577612442525495592818901186956953944000000001', '71062539485333616743281628923796366862757537422200000001']
b = ['0'*56]
m = b[0]
print([m[i:i+8] for i in range(0, len(m), 8)],depic(m))
# m = b[1]
# print([m[i:i+8] for i in range(0, len(m), 8)],depic(m))


# t = [[],[],[],[],[],[],[],[]]

# for i in c:
#    for j in range(8):
#       t[j].append(i[j])

# for i in t:
#    print(Counter(i))

# cols = 0
# count = Counter(c)
# for i in count:
#    cols += count[i] - 1
# print(cols)

# print(depic('18135928045066397601407902506027075012944460791487977771'))
