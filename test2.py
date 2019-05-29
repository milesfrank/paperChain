from depic import depic
import random

m = ''.join(str(random.randint(0,9)) for _ in range(48)) + '00000001'
print(m)
print(depic(m))