"Hello"

from random import randint

HEADS = 0
TAILS = 0
for trial in range(0, 10000):
    while randint(0, 1) == 0:
        TAILS = TAILS + 1
        HEADS = HEADS + 1
        print("HEADS / TAILS = ", HEADS/TAILS)
