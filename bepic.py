import time
from collections import Counter

fun = [lambda a,b: a + b] + \
    [lambda a,b: a * b]

def bepic(message):
    message **= 2
    # message += 254
    for i in range(4):
        if i%4 < 2:
            a = int(str(message)[:2])
        else:
            a = int(str(message)[-2:])
        message = fun[i%2](a+2,message)
    return message

print(bepic(1))
print(bepic(11111))