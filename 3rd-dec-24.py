#removing elements from list......pop, remove, clear, del
#pop()>>>>>removes and return last element from list
l = [1, 2, 3, 4, 5]
l_pop = l.pop()
print(l_pop)
print(l)

#remove() >>>>removes sepcefied element from list
l1 = [11, 12, 13, 14, 15, 16]
print(l1.remove(15))
l_rm = l1.remove(16)
print(l_rm)

#clear()>>>it will removes all elements from list and return empty list
print(l)
l.clear()
print(l)

#del()
print(l1)
del(l1)
#print(l1)

#ordering of list>>>>reverse(), sort()
n = [1, 2, 3, 4, 5, 6]
print(n)
n.reverse()
print(n)

#reverse a list using slicing
print(n[::-1])

#sort()
n1 = [1, 4, 2, 9, -3, -0, -5, 10]
n1.sort()
print(n1)

s = "do what you want"
print(s[::-1])

#aliasing and cloning
x = [1, 2, 3, 4]
y = x
print(id(x))
print(id(y))

x[1] = 20
print(x)
print(y)

#cloning >>>>slicing
x = [20, 30, 40, 50]
y = x[:]
print(id(x))
print(id(y))

y[1] = 100
print(y)
print(x)

#clonig>>>>>copy()
x = [1, 2, 3, 4, 5]
y = x.copy()
print(id(x))
print(id(y))

y[2] = 200
print(x)
print(y)

#comparing of 2 lists
a = [1, 2, 3, 4, 5, 6]
b = [1, 3, 5, 4, 7, 9]
print(a>b)
print(b>a)

x = ["anu", "maya", "ram"]
y = ["sita", "sai", "shiv"]
print(x > y)

a = ["a", "b", "c"]
b = ["a", "b", "c", "d"]
print(a<b)

#membership checking in list
l2 = [11, 12, 13, 14, 15]
print(10 in l2)
print(10 not in l2)

#nested lists
l3 = [1, 2, 3, [4, 5, 6,[7, 8, 9]]]
print(l3[3])
print(l3[3][3])
print(l3[3][3][2])


#output= "od tahw uoy tnaw"
#output = "want you what do"
s = input("enter the string: ")
rev = []
s_split = s.split()
print(s_split)
for i in s_split:
    rev.append(i[::-1])
rev = " ".join(rev)
print(rev)

s1 = "do what you want"
s1_rev = ""
s1_split = s1.split()
print(s1_split)
rev_string = s1_split[::-1]
print(rev_string)



