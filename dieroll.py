"Hello"

from random import randint

def dieroller():
    "Hello again"
    return((randint(1, 6)))

TOTAL=0
for i in range(0, 1000):
    TOTAL = TOTAL + dieroller()

print("Average of rolls is {:.2f}".format(float(TOTAL) / 1000))
