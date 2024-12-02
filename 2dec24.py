#list >>>>>>>>>> collection of multiple datatypes, stored in single variable

#declaring a list
l = []
print(type(l))

l1 = [1, 2, 3, 4, 5, 6]
print(type(l1))
print(l1)

s = "welcome to world"
s1 = s.split()
print(s1)
print(type(s1))

"""l2 = eval(input("enter your list: "))
print(l2)"""

#adding elements to list
#append()....add elemnts to the end of the list
#insert()....add elemnts at a specified position

l3 = []
for i in range(1, 21):
    if i % 2 != 0:
        l3.append(i)
print(l3)

l4 = [1, 2, 3, 4, 5]
for i in l4:
    l3.append(i)
print(l3)

#insert()
l5 = [10, 20, 30, 40, 60, 70]
l5.insert(4, 50)
print(l5)

#accessing elemnts from list:  slicing and indexing
l6 = [1, 2, 43,4, 6, 8]
print(l6[4])

l7 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
print(l7[1:8])

#without using eval, take input user , print list type and int type
l8 = input("enter the string: ")
l8.split()
print(type(l8))


#programm to print integer list of divisable with 7 but not with 5 from 100 to 200
lst = []
for i in range(100, 201):
    if i % 7 == 0 and i %5 != 0:
        lst.append(i)
print(lst)

#program to add multiple elements to the list
lst1 = [1, 2, 3, 4, "hi"]
ext_lst = [8,9]
lst1.extend(ext_lst)
print(lst1)

for i in range(5, 10):
    lst1.append(i)
print(lst1)

lst1.append("hello")
print(lst1)