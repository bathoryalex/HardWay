# http://learnpythonthehardway.org/book/ex7.html

print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
print ("." * 10) #what'd that do? - tizszer kiirta a pontot

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch taht comma at the end. try removing it to see what happens - ha kitorlom nem valtozik semmi
print (end1 + end2 + end3 + end4 + end5 + end6, end = " ") # miert nem rakja egy sorba a Cheese es a Burger szot, ahogy a peldaban is volt? (meg van a magyarazat)
print (end7 + end8 + end9 + end10 + end11 + end12) # meg van a valasz: mert python 3-ban mar nem eleg a vesszo, kell az end = " "

