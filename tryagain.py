"integer input checking example"

while True:
    try:
        MYVAL = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Nope, try again.")
