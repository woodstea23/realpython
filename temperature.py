def ctof(tc):
	tf = (tc * 9 / 5) + 32
	return tf

def ftoc(tf):
	tc = (tf - 32) * 5 / 9
	return tc

temp1 = float(input("Enter a Celsius temperature: "))
print("{} degrees Celsius is {:.2f} degrees Fahrenheit.".format(temp1, ctof(temp1)))

temp2 = float(input("Enter a Fahrenheit temperature: "))
print("{} degrees Fahrenheit is {:.2f} degrees Celsius.".format(temp2, ftoc(temp2)))

