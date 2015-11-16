# http://learnpythonthehardway.org/book/ex21.html

def add(a, b):
	print("A(LA)DDING %d + %d" % (a, b))
	return a + b
	
def substract(a, b):
	print("SUBSTRACTING %d - %d" % (a, b))
	return a - b
	
def multiply(a, b):
	print("MULTIPLYING %d * %d" % (a, b))
	return a * b
	
def divide(a, b):
	print("DIVIDING %d / %d" % (a, b))
	return a / b
	
	
print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))



# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")


# ==========STUDY DRILLS==========

age1 = int(input("Add age1 (adding): "))
age2 = int(input("Add age2 (adding): "))
height1 = int(input("Add height1 (multiplying): "))
height2 = int(input("Add height2 (multiplying): "))
iq1 = int(input("Add iq1 (dividing): "))
iq2 = int(input("Add iq2 (dividing): "))

new_age = add(age1, age2)
new_height = multiply(height1, height2)
new_iq = divide(iq1, iq2)

print("New age: %d, New hight: %d, New IQ: %d" % (new_age, new_height, new_iq))
