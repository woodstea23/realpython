"Print an amortization table"

def invest(amount, rate, time):
    "And here's the main function"
    print("principal amount: ${}".format(amount))
    print("annual rate of return: {:.2f}%".format(rate * 100))
    for i in range(1, time + 1):
        amount = amount * (1 + rate)
        print("year {}: ${:.2f}".format(i, amount))
        # Here is a comment.
        # Here is a second comment.
        # And a third.

invest(100, .05, 8)
invest(2000, .025, 5)
