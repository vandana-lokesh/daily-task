#set>>>>>>unordered, no duplicate, no indexing
s = {1, "ram", True, 8, 9, 10.0}
print(type(s))

#to declare empty set, use set()
s = set()
print(type(s))   #o/p = set

s = {}
print(type(s))   #o/p = dict

s = {1, "ram", True, 8, 9, 10.0}
print(s)  #true is not printed, bcoz true ==1, 1 is already there in given set

#adding elements to set
s = {"ram", "sita", "shiv"}
s.add("vemkat")
print(s)

#update()
s = {1, 2,3, 4}
s1 = {"abc", "pqr"}
s1.update(s)
print(s1)

#removing element from set
#remove() >>>>shows error, if ele not there in 
#discard()  >>>doesnot show error, if ele not there
#pop()  >>>removes last ele but doesnot knoe which ele is removed