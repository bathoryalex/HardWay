# http://learnpythonthehardway.org/book/ex19.html

def cheese_and_crackers(cheese_count, boxes_of_crackers): # create a function, which has 2 variables
	print("You have %d cheses!" % cheese_count) # prints out how many cheeses I have. Requires a decimal number
	print("You have %d boxes of crackers!" % boxes_of_crackers)
	print("Man that's enough for a party!") # prints out a sentence
	print("Get a blanket.\n") # sentence + linebreak
	
	
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # we give the 2 variables directly


print("OR, we can use variables from our script:")
amount_of_cheese = 10 # we name the two variables, and ...
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # ... call these variables inside the function


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # simple math


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #variables + adding numbers

# ==========STUDY DRILLS==========
# Firstly: Comment each line, what it does. 
# Secondly: one more function

def italok_szama(bor, palinka):
	print("%d borod van!" % bor)
	print("%d palinkad van!" % palinka)
	print("Haver, ez kurva sok!")
	print("Hozd a lavort! \n")
	
print("Megadhatjuk a konkret szamokat.")
italok_szama(12, 8)


print("Vagy valtozokat hasznalhatunk a szkriptunkbol.")
bor_mennyiseg = 17
palinka_mennyiseg = 12

italok_szama(bor_mennyiseg, palinka_mennyiseg)


print("Matematikai szamitasokat is csinalhatunk.")
italok_szama(12 + 9, 1 + 18)


print("A kettot kombinalhatjuk is, valtozok es matek.")
italok_szama(bor_mennyiseg + 15, palinka_mennyiseg + 2)

print ("Most mi fogjuk bekerni az adatokat!")
bor = int(input("Add meg a bor mennyiseget! "))
palinka = int(input("Add meg a palinka mennyiseget! "))

italok_szama(bor, palinka)






	