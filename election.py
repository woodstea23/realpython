"Hello"

from random import randint

def oneelection():
    "Hello again"
    acount = 0
    # Region 1
    if randint(1, 100) <= 87:
        acount += 1
    # Region 2
    if randint(1, 100) <= 65:
        acount += 1
    # Region 3
    if randint(1, 100) <= 17:
        acount += 1
    if acount >= 2:
        return(1)
    else:
        return(0)

ATOTAL = 0
for i in range(0, 10000):
    ATOTAL = ATOTAL + oneelection()

APROB = float(ATOTAL) / 100
print(f"Probability of candidate A winning is {APROB:.2f}%")
