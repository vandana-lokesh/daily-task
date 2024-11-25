#finding of substring in main string
#find()
#index()
#both methods will return index positions on substring in main string
s = "welcome to world"
print(s.find("world"))

print(s.index("world"))

#print(s.index("zzz"))     #if the elements not in string, it will return error
print(s.find("zzzzz"))     #if the element not in string, it will return -1

print(s.find("w"))
print(s.index("e"))

print(s.find("o"))
print(s.index("o"))

print(s.find("w"))
print(s.rfind("w"))    #it will print from right

print(s.rindex("o"))
print(s.index("o"))

print("=============")
str = "python programming"
print(str.find("python"))
print(str.index("python"))

print(str.find("y"))
print(str.index("p"))

print("=============")
print(str.rfind("p"))
print(str.index("p"))

#split()
print("===========")
s ="Hi, welcome to world"
print(len(s))
split_s = s.split()
print(len(split_s))
print(split_s)

ss = s.split("l")
print(ss)
print(len(ss))

#join()
print("=================")
s1 = ["welcome", "to", "python", "programming"]
s1_join = "".join(s1)
print(s1_join)
print(len(s1_join))

j_s1 = "-".join(s1)
print(j_s1)

#changing case of a string
#upper(), lower(), swapcase(), title(), capitalise()

#upper()........converts all charecters into uppercase.
a = "Vandana"
print(a.upper())

#lower()........converts all charecters into lower.
a1 = "Welcome to world"
print(a1.lower())

#swapcase()..........converts all lowercase to uppercase and uppercase to lowercase
a2 = "Welcome To My World"
print(a2.swapcase())

#title()..........converts first charecter in string into uppercase
b1 = "welcome to home"
print(b1.title())

#capitalize().......converts first charecter into uppercase
b2 = "Hi, welcome everyone"
print(b2.capitalize())

#check type of a charecter/string
#isupper()
b3 = "Hello"
print(b3.isupper())

b4 = "HELLO"
print(b4.isupper())

#islower()
print("=================")
c = "Good Morning"
print(c.islower())

c1 = "good morning"
print(c1.islower())

#istitle()
print("===============")
d = "welcome to world"
print(d.istitle())

d1 = "Welcome To World"
print(d1.istitle())

#iscapitalize()
d2 = "hi"
print(d2.capitalize())

#isalnum()
print("=============")
d3 = "Hello123"
print(d3.isalnum())

d4 = "hello, hi"
print(d4.isalnum())

#isdigit()
d5 = "1233"
print(d5.isdigit())

d6 = "Hi12321"
print(d6.isdigit())

#isspace()
d7 = "     "
print(d7.isspace())

d8 = "  ABC     "
print(d8.isspace())

print("===============")
#checking first and last parts of a string
#startswith(), endswith()
email = "vandana@gmail.com"
print(email.startswith("vand"))

s2 = "WELCOME"
print(s2.startswith("W"))

print(email.endswith(".com"))
print(s2.endswith("s"))

