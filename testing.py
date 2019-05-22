from depic import depic
from collections import Counter
import random

# d = []
# for i in range(0, 100000):
#     # m = '0'*(56-len(str(i))) + str(i)
#     m = ''.join(str(random.randint(0,9)) for _ in range(56))
#     b = depic(m)
#     # print(b)
#     d.append(b)

# # collisions
# d = []
# cols = 0
# count = Counter(d)
# for i in count:
#    cols += count[i] - 1
# print(cols)

print(depic('18135928045066397601407902506027075012944460791487977771'))