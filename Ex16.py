# http://learnpythonthehardway.org/book/ex16.html

"""
close -- Closes the file. Like File->Save.. in your editor.
read -- Reads the contents of the file. You can assign the result to a variable.
readline -- Reads just one line of a text file.
truncate -- Empties the file. Watch out if you care about the file.
write('stuff') -- Writes "stuff" to the file.
"""

from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open (filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to write these to the file.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

target.write("%r\n%r\n%r\n" % (line1, line2, line3)) # target.write egy sorban a harom helyett

print ("And finally, we close it.")
target.close()
