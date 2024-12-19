#functions()>>>>>>>>a block of code, exectes wheneve we call it(reusable bloc of code).

#argments: information or data passed to the function as a argument, which specifies after fnction name.
s = "welcome to my world"
rs = s.replace(" ", "$")
print(rs)

"""def functionname(arguments):
    pass
functionname(actual arguments)"""

def space_replace(s):
    rs = s.replace(" ", "=")
    print(rs)
s = input("enter the input: ")
space_replace(s)
space_replace("welcome to programming")

#python function tp print evens as a list
def get_even(x):
    l = []
    for i in x:
        if i % 2 == 0:
            l.append(i)
    print(l)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_even(l1)

#types of arguments:
#1. positional arguments>>>passing argumets to the function in a positional order
def find_greatest(x, y):
    if x > y:
        print(x, "is greater")
    else:
        print(y, "is greater")

x = 10
y = 20
find_greatest(x, y)

#passing data based on position
def sum(a, b):
    print(a + b)
    print(a - b)
x = 20
y = 30
sum(x, y)

#2. keyword arguments
print("======================")
def sum(b, a):
    print(a + b)
    print(a - b)
x = 20
y = 30
sum(a = x, b = y)

def sum(a, b):
    print(a + b)
    print(a - b)
x = 20
y = 30
sum(a = x, b = y)

#
def greet(name, msg):
    print("hi", name, msg)
name = "vandana"
msg = "good morning"
greet(name, msg)

def greet(name, msg):
    print("hi", name, msg)
name = "vandana"
msg = "good morning"
greet(name = name, msg = msg)

#3. variable argument>>>>>>taking no of variables
def sum(*n):
    total = 0
    for i in n:
        total = total + i
    print(total)
sum(10, 20, 30, 40, 50)
sum(1, 2, 3)

#4. keyword variable length
def std_data(**n):
    print(n)
std_data(P = 30, C =  40, M = 50, B = 60)


def std_data(**n):
    print(n)
    for k, v in n.items():
        print(k, "=", v)
std_data(P = 30, C =  40, M = 50, B = 60)

#default arguments:
def greet(name, msg = "Good morning"):
    print("hi", name, msg)
name = "vandana"
msg = "Good morning"
greet(name = name)

def greet(name, msg = "Good morning"):
    print("hi", name, msg)
name = "vandana"
msg = "Good evening"
greet(name = name, msg = msg)  #only take user input data

"""def wish(name, msg):
    return "Hi", name, msg
obj = wish("vandana", "good mrng")
print(obj)
"""
def sum(x, y):
    return x + y
print(sum(100, 20))