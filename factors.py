"Find all of the integers that divide evenly into an integer provided by the user"

def factors(testint):
    "And here's the main function"

    for i in range(1, testint + 1):
        if testint % i == 0:
            print("{} is a divisor of {}".format(i, testint))

factors(int(input("Enter a positive integer: ")))
