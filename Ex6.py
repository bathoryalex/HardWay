# http://learnpythonthehardway.org/book/ex6.html

x = "There are %d types of people." % 10 # x erteke a mondat, ahol a tipus %d-vel van megadva
binary = "binary" # valtozo es ertek
do_not = "don't"  # szinten
y = "Those who know %s and those who %s." % (binary, do_not) # mondat, behelyettesitve a ket valtozo ertekevel

print (x) # kiirja x erteket
print (y) # kiirja y erteket

print ("I said: %r." % x) # kiirja az x nyers/raw/ erteket. szoval mar behelyettesiti a 10-es szamot.
print ("I also said: '%s'." % y) #szinten y-ra.

hilarious = False # ertekadas - hamis
joke_evaluation = "Isn't that joke so funny?! %r" # minek ide %r? - ja igen, a kovetkezo sor miatt kell. igy csatolja oda a hilar. erteket

print (joke_evaluation % hilarious) # kiirja a joke_evaluation erteket es a hilarious erteket egymas melle.

w = "This is the left side of..."
e = "a string with a right side."

print (w + e) # kiirja w + e erteket egymas melle.



