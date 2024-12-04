#1. Basic List Operations:
#1.Write a Python program to create a list of 5 integers and print the sum of all elements in the list.
n = [1, 2, 3, 4, 5]
n_sum = sum(n)
print("sum of all elements in list is: ",n_sum)

#2.Create a list of strings containing the names of 5 fruits. Access and print the second and fourth elements using indexing.
x = ["grapes", "apples", "banana", "orange", "mango"]
x_2nd_ind = x[1]
x_4th_ind = x[3]
print("second element using indexing is: ", x_2nd_ind)
print("fourth element using indexing is: ", x_4th_ind)

#3.Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, the last three numbers, and every second number in the list.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = l[:3]
print("The first three numbers are:", num)
num1 = l[-3:]
print("The last three numbers are:", num1)
num2 = l[::2]
print("Every second number is:", num2)

#2. Adding and Removing Elements:
#1.Write a Python program that initializes a list with some numbers and:
#2.Adds a new number to the list using the append() method.
l1 = [1, 2, 3, 4, 5, 6]
l1.append(7)
print("list after adding new num is: ", l1)

#3.Inserts a number at the second position using insert().
l1.insert(1, 100)
print("list after inserting num at second position is: ",l1)

#4.Extends the list with another list of numbers.
ext_list = [10, 20, 30]
l1.extend(ext_list)
print("list after extending with another list is: ",l1)

#5.Remove all occurrences of the number 3 from a list of integers.
rem_ele = 3
for i in l1:
    if i == rem_ele:
        l1.remove(i)
print("list after removing all occurences of number 3 is: ",l1)
        
#6.Write a Python program to remove the last element of a list using pop() and print the updated list.
pop_l1 = l1.pop()
print("last removed elemnt is: ", pop_l1)
print("updated list is: ", l1)

#3. Sorting and Reversing Lists:
#1.Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().
l = [2, 3, 11, -1, 56, 20, 11, 6, 0]
l.sort()
print("list in ascending order using sort is: ", l)

l.reverse()
print("list in descending order is: ",l)

#2.Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.
l3 = ["ram", "sita", "hari", "shiv"]
l3_copy = l3.copy()
print("list before reversing and slicing is: ", l3)

l3_copy.reverse()
print("list after using reverse is: ", l3_copy) #using reverse

l3_slice  = l3[::-1]
print("list after using slicing is: ",l3_slice)

#4. Aliasing and Cloning:
#1.Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.
lst = [1, 2, 3, 4, 5]
lst1 = lst   #assigned the list to another variable

lst.append(6)
print("original list is modified: ", lst)
print("another list also modified", lst1)  #second list also changes, if modified original list

copy_lst = lst.copy()     #original list is copied
copy_lst.append(100)
print("list after modification of copied list: ",copy_lst)
print("original list after modification", lst)        #modifying the copy does not affect the original list.

#2.Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.
lst_1 = [11, 12, 13, 14, 15]
alias_lst_1 = lst_1   #alias of original list

lst_1.append(100)  # modifing the original list affects both lists
print("Original list after modification:", lst_1)
print("Alias list after modification:", alias_lst_1)

cloned_list = lst_1.copy()
cloned_list.append(200)    # modifing the cloned list does not affect the original or alias list
print("Original list after modifying cloned list:", lst_1)
print("Alias list after modifying cloned list:", alias_lst_1)
print("Cloned list after modification:", cloned_list)

#5. Mathematical Operations:
#1.Create two lists of numbers, and use the + operator to concatenate them. Then, use the * operator to repeat the elements of one list 3 times.
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a_b = a + b
print("list after concatinating is: ", a_b)

repeat_ele = a * 3  # *used to repeat ele n times
print("list after repeating 3 times is: ", repeat_ele)

#2.Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each element is multiplied by 2).
x = [1, 2, 3, 4, 5]
for i in x:
    double_x = i * 2
    print(double_x)

#6. Membership Operators:
#1.Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."
y = [1, 2, 3, 4, 5, 6, 7, 8]
n = int(input("enter the number: "))
if i in y:
    pos_i = y.index(n)
    print("position of element is: ", pos_i)
else:
    print("element not found")

#Given a list of student names, check if "John" and "Sara" are in the list using the in operator.
stu_names = ["john", "sara"]
if "john" and "sara" in stu_names:
    print("found the elements")
else:
    print("not found")


#7. Nested Lists:
#1.Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.
m = [[1, 2, 3], 
     [4, 5, 6],
     [7, 8, 9]]
for i in m:
    print(i)

ele_m = m[1][2]
print("element in 2nd row and 3rd column is: ",ele_m)

#2.Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.
st_lst = [["ram", "A"], ["sita", "B"], ["david","C"]]
for i in st_lst:
    name, grade = i
    print("name is:",name , "and grade is: ", grade)

#8. Advanced Challenges:
#1.Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#One containing only the even numbers.
#Another containing only the odd numbers.
lst_num = [1, 2, 3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
evn_lst = []
odd_lst = []
for i in lst_num:
    if i % 2 == 0:
        evn_lst.append(i)
    else:
        odd_lst.append(i)    
print("even no list is: ",evn_lst)
print("odd no list is: ",odd_lst)

#2.Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).
l = [4, 3, 5,1 , 3, 4, 2, 7, 6, 5, 4, 1, 8, 9, 8]
em_l = []
for i in l:
    if i not in em_l:
        em_l.append(i)
print(em_l)

#Given a list of tuples representing (name, age), sort the list by age in ascending order.
