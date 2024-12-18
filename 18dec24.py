
"""
#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"
def greet(name):
    print("Hello,",name,'!')
greet("vandana")
greet("welcome to all")

#2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.
def add_numbers(n1, n2):
    print("sum of 2 numbers is: ", n1 + n2)
add_numbers(1, 2)
add_numbers(5, 6)
add_numbers(-1, -4)

#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
def is_even(n):
    if n%2 == 0:
        print("True")
    else:
        print("False")

n = int(input("enter the number: "))
is_even(n)

#4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
def factorial(n):
    if n == 0 and n <= 1:  #0! = 1 and 1! = 1
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("enter the nmber: "))
print(factorial(n))


#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
def find_max(n1, n2, n3):
    print(max(n1, n2, n3))

n1 = input("enter the first number: ")
n2 = input("enter the second number: ")
n3 = input("enter the third number: ")
find_max(n1, n2, n3)

#6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
def count_vowels(str):
    vowels = "aeiouAEIOU"  # Include uppercase vowels as well
    count = 0
    for i in str:
        if i in vowels:
            count = count + 1
    print("count of vowels in given string is: ",count)

str = input("enter the input: ")
count_vowels(str)


#7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.

#8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).

#9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.
def calculator(num1, num2, operator):
    if operator == "+":
        print("addition of 2 number is: ", num1 + num2)
    elif operator == "-":
        print("substraction of 2 nmbes is: ", num1 - num2)
    elif operator == "*":
        print("multiplication of 2 numbers is: ", num1 * num2)
    elif operator == "/":
        print("division of 2 no is: ",num1 / num2)
    else:
        print("Invalid operator")

num1 = int(input("enter the  firt number: "))
num2 = int(input("enter the second number: "))
operator = input("enter the operator: ")
calculator(num1, num2, operator)


#10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.
common = []
def find_common_elements(l1, l2):
    for i in l1:
        if i in l2:
            common.append(i)
    print(common)
    
l1 = [1, 2, 3, 4, 6]
l2 = [3, 1, 6, 8]
find_common_elements(l1, l2)


#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.
def reverse_string(str):
    rs = str[::-1]
    print(rs)

str = input("enter the string: ")
reverse_string(str)

"""

#12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.
def sort_dict_by_values(d):
    sort_d = list(d.keys())
    sort_d.sort()
    sort_d.reverse()
    for i in sort_d:
       sd = {i : d[i]}
       print(sd)

d = {'ram': 20, 'sita': 8, 'shiv': 10}
sort_dict_by_values(d)


