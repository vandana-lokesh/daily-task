str = 'vandana'
str1 = "Rama"
str2 ="Sita"
print(str)
print(str1)
print(str2)

#indexing----------it allows individual charecters to access by using reposition of indexing
name = "welcome"
print(name[0])
print(name[3])
print(name[6])    #positive indexing

Name = ("Hello world")
print(Name[0])
print(Name[5])
print(Name[7])
print(Name[8])

#negative indexing
print("----------------")
print(name[-1])
print(name[-4])
print("-------------")

#slicing
#variablename[startindex : endindex]
s = "Good Morning"
print(s[0:5])
print(s[5:13])
print(s[5:8])

#variablename[startindex : endindex :step]
x = "python programming"
print(x[0 : 7 : 2])
print(x[8: 16 : 1])

#membership in string
# in & notin 
a = "Hi, welcome everyone"
b = "Hi"
print(b in a)

if b in a:
    print("b is available in a")

#notin
print(b not in a) 

if b not in a:
    print("not available")

#removing spaces from string
#strip()
uname = "krishna "
print(len(uname))
us = uname.strip()
print(us)
print(len(us))

# removing only right side space
print("------------")
uname1 = " krishna1 "
print(len(uname1))
rs = uname1.rstrip()
print(rs)
print(len(rs))

#removing only left side space
print("-------------")
uname2 = " krishna2 "
print(len(uname2))
ls = uname2.lstrip()
print(ls)
print(len(ls))

#replace()
print("------------")
a1 = "Hello, welcome to python programming"
print(a1)
a1_s =a1.replace(" ", "")
print(a1_s)

a1_1 = a1.replace("Hello", "Hi")
print(a1_1)