"Enrollment stats exercise"

def enrollment_stats(univlist):
    "Cha"
    enrolled = []
    cash = []
    for univ in univlist:
        enrolled.append(univ[1])
        cash.append(univ[2])
    return enrolled, cash

def mean(mylist):
    "Cha"
    mysum = 0
    for myvalue in mylist:
        mysum += float(myvalue)
    return int(mysum / len(mylist))

def median(mylist):
    "Cha"
    mylist.sort()
    length = len(mylist)
    if not length % 2:
        return (mylist[int(length / 2)] + mylist[int(length / 2 - 1)]) / 2.0
    return mylist[int(length / 2)]

UNIVS = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

STATS = enrollment_stats(UNIVS)
print(STATS[0])

print()
print("*****" * 5)
print("Total students:   {}".format(sum(STATS[0])))
print("Total tuition:  $ {}".format(sum(STATS[1])))
print("\nStudent mean:     {}".format(mean(STATS[0])))
print("Student median:   {}".format(median(STATS[0])))
print("\nTuition mean:   $ {}".format(mean(STATS[1])))
print("Tuition median: $ {}".format(median(STATS[1])))
print("*****" * 5)
print()
