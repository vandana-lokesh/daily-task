#1. Write a program to create a set.
s = {1, 2, 3, 4}
print("the set is: ", s)

#2. Write program to iterate over sets.
s1 = {1, 2, 3, 4, 5, 6}
for i in s1:
    print(i)

#3. Write a Python program to add member to a set.
s2 = {1, 3, 5, 7}
print("before adding,set is: ",s2)
s2.add(9)
print("added set is: ", s2)

#4. Write a Python program to remove item from a given set.
s3 = {2, 4, 6, 8, 10}
print("set before removing is: ", s3)
s3.remove(10)
print("set after removing is: ", s3)

#5. Write a python program to create a intersection of set ?
s4 = {1, 2, 3, 4}
s5 = {5, 6, 7, 1, 2}
s4_inter_s5 = s4.intersection(s5)
print("intersection of s4 and s5 is: ", s4_inter_s5)

#6. Write a python program to createa unionof set ?
s6 = {1, 2, 3}
s7 = {4, 5, 6}
s6_union_s7 = s6.union(s7)
print("union of 2 sets is: ", s6_union_s7)

#7. Write a python program to create set differance ?
s8 = {1, 2, 3}
s9 = {4, 5, 6, 1}
s8_diff_s9 = s8.difference(s9)
print("difference of 2 sets is: ", s8_diff_s9)

#8. Write a python program to create a symmetric defferance ?
s10 = {1, 3, 6}
s11 = (2, 4, 5, 6)
s10_symdiff_s11 = s10.symmetric_difference(s11)
print("symmetric difference of 2 sets is: ", s10_symdiff_s11)

#9. write a python program to find max and min values in a set?
s12 = {1, 2, 3, 20}
max_s12 = max(s12)
min_s12 = min(s12)
print("max of given set is: ", max_s12)
print("min of given set is: ", min_s12)

#10. Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
s13 = {1, 2, 3, 4} 
s14 = {1, 3, 5, 7}
s13.difference_update(s14)
print("set that elements present in set1 not in set 2 is: ", s13)

#11. Write a Python program to remove items 10, 20, 30 from the following set at once.?
s15 = {10, 20, 30, 40, 50}
rem_s15 = {10, 20, 30}
s15.difference_update(rem_s15)
print(s15)

#12. Check if two sets have any elements in common. If yes, display the common elements?
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
common_elements = set1.intersection(set2)
if common_elements == set1.intersection(set2):
    print("Common elements are: ", common_elements)
else:
    print("No common elements in given set")

#13.Update set1 by adding items from set2, except common items?
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
unique_items = set2.difference(set1)  #items in set2 not in set1
set1.update(unique_items)  
print("Updated set1 is: ", set1)

#14. Remove items from set1 that are not common to both set1 and set2?
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1.intersection_update(set2) #common elements from set1 and set2
print("Updated set1 is: ", set1) #removing elemnts from set1, except common elemnts

#15.Write a python program to  add a key to a dictionary ?
d = {"name": "david", "age": 20, "salary": 40000}
print(d)
d["active"] = True
print("dictionary after adding key is: ", d)

#16. Write a python program to check weather the given value is present in the dictionary or not ?
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
given_val = 1
if given_val in d1.values():
    print(f"The value {given_val} is present in the dictionary.")
else:
    print(f"The value {given_val} is not present in the dictionary.")

#17. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
squ_dict = {}
for i in range(1, 16):
    squ_dict[i] = i**2
print(squ_dict) 

#18. Write a python program to create a dictionary from the string ?
str = "hello world"
emp_d = {}
for i in str:
    if i in emp_d:
        emp_d[i] += 1
    else:
        emp_d[i] = 1
print("string count in dict is: ", emp_d)

#19.Write a python program to combine two dictionaries by adding values of common keys ?
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 30, 'c': 40, 'd': 50}
for i in d2:
    if i in d1:
        d1[i] += d2[i]  # Add the values of common keys
    else:
        d1[i] = d2[i]  # If key not present in dict1, add it

print("Combined dictionary is :", d1)

#20. Write a python program to merge two python dictionaries ?
d3 = {'a': 1, 'b': 2, 'c': 3}
d4 = {'d': 4, 'e': 5, 'f': 6}
d3.update(d4)
print("Merged dictionary is: ", d3)

#21. Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
"""Sample string : 'skywavessoftwares'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}"""
str = "skywavessoftwares"
emp_d = {}
for i in str:
    if i in emp_d:
        emp_d[i] += 1
    else:
        emp_d[i] = 1
print("string count in dict is: ", emp_d)

