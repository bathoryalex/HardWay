# http://learnpythonthehardway.org/book/ex8.html

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4)) # kiirja a formatter valtozot es erteknek behelyettesiti a negy szamot
print (formatter % ("one", "two", "three", "four")) # kiirja a formatter valtozot es betuvel a szamokat
print (formatter % (True, False, False, True)) # ertekeket ad
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.")
	)
	
