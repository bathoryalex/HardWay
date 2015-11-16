# http://learnpythonthehardway.org/book/ex15.html

# Now, it will import argv from sys module.
from sys import argv

# First value of argv is 'script', and the second is 'filename'.
script, filename = argv

# This line opens the file I give and stores it in the 'txt' variable.
txt = open(filename)

# Calls the files name.
print ("Here's your file %r:" % filename)

# Reads the file and prints it.
print (txt.read())

# Reads a file again and stores it in 'file_again' variable.
print ("Type the filename again: ")
file_again = input("> ")

# Opens it.
txt_again = open(file_again)

# Prints the content of file.
print (txt_again.read())

"""Ha meg akarom nyitni Powershell-ben a fajlt, Python-on keresztul, 
akkor eloszor a 'python' parancsot kell beirni,
majd peldaul: 'open("ex15_sample.txt").read()'
Ekkor beolvassa, es ki is irja a szoveges fajl tartalmat."""
