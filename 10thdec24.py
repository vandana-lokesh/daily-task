#1.Write a function that takes a tuple and an index as inputs and returns the element at the given index. Handle the case where the index is out of bounds.

"""t = (1, 2, 3, 4, 5, 6)
ind = t[1]
print(ind)"""

t = (1, 2, 3, 4, 5)
ind1 = t[int(input("enter the index: "))]
if ind1 >= len(t) and ind1 < 0:
    print("out of bond")
else:
    #ind1 = t[int(input("enter the index: "))]
    print("value of given index is: ", ind1)

#2.Write a function to concatenate two tuples into one.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
con_t = t1 + t2
print("tuple after concatinating is: ", con_t)

#3.Write a function that takes a tuple and a value as inputs and returns the number of times the value appears in the tuple.
#6.Write a function that takes a tuple and a value as inputs and returns the number of times the value appears in the tuple.
t6 = (1, 2, 3, 3, 2, 2, 1, 4, 1, 1)
count = 0
val = input("enter the input: ")
for i in t6:
    if i == val:
        count = count + 1
print(count)

t3 = (1, 2, 2, 3, 4, 1, 1, 5)
value = t3.count(input("enter the value: "))
#t3.count(value)
print("given value is occured ",value , "times")

#4.Write a function that calculates the length of a tuple without using the built-in `len()` function.
#7.Write a function that calculates the length of a tuple without using the built-in `len()` function.
t4 = (1, 2, 3)
count = 0
for i in t4:
    count = count + 1
print("the length of tuple is: ", i)

#5.Write a function that takes a tuple as input and returns a new tuple with the elements in reverse order.
#8.Write a function that takes a tuple as input and returns a new tuple with the elements in reverse order.

t5 = (1, 2, 3, 4)
t5_reverse = t5[::-1]
print("given tuple in reverse order is: ",t5_reverse)

#9.Write a function that checks if a given element exists in a tuple. Return `True` if it exists, otherwise return `False`.
t9 = (1, 2, 3, 4, 5)
print("original tuple is: ", t9)
va = int(input("enter the tuple item to be found: "))
res =  va in t9
print(res)

#10.Write a function that takes two tuples and returns a tuple containing the common elements.
t10 = (1, 2, 3, 2, 4, 5)
t11 = (2, 7, 6, 3, 1)
com_ele = []
for i in t10:
    if i in t11 and i not in com_ele:
        com_ele.append(i)
print(tuple(com_ele))

"""11.Write a function to unpack nested tuples and flatten them into a single tuple.  
    Example:  
    Input: `((1, 2), (3, 4), 5)`  
    Output: `(1, 2, 3, 4, 5)`"""
t111 = ((1, 2), (3, 4), 5)


