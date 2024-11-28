#1. Python Program to count occurrence of a given characters in string. 
n = input("enter the string: ")
char_count = input("enter the charecter to count: ")
count_n = n.count(char_count)
print("the count of charecter is: ", count_n)

#2. Python Program to check if two Strings are Anagram.
n1 = input("enter the first string: ")
n2 = input("enter the second strong: ")
if sorted(n1) == sorted(n2):
    print("both strings are anagram")
else:
    print("not anagram")

#3. Python program to check a String is palindrome or not.
s = input("enter the string: ")
if s == s[::-1]:
    print("given string is palindrome")
else:
    print("not palindrome")

#4. Python program to replace the string space with a given character. 
#5. Python program to replace the string space with a given character using replace() method. 
s1 = input("enter the string: ")
s2 = input("enter the charecter to replace spaces with: ")
new_string = s1.replace(" ", s2)
print("string before replacing is: ", s1)
print("updated string is: ", new_string)

#6. Python program to convert lowercase char to uppercase of string. 
a = input("enter the string: ")
l_a = a.upper()
print("string after updating to uppercase is: ", l_a)

#7. Python program to convert lowercase vowel to uppercase in string. 
n1 = input("enter the string: ")
vowels = "aeiou"
for i in n1:
    if i in vowels:
        upper_n1 = i.upper()
        s = n1.replace(i, upper_n1)
print("updated string is: ", s)

#8. Python program to separate characters in a given string. 
st = input("enter the string: ")
sep_char = list(st)
print("string after separating is: ",sep_char)

#9. Python program to remove blank space from string. 
n = input("enter the string: ")
rm_space = n.replace(" ", "")
print(n)
print("string after removing blank spaces is: ", rm_space)

#10.Python program to concatenate two strings using join() method. 
p = input("enter the first string: ")
q = input("enter the second string: ")
con_pq = " ".join([p, q])
print("string after concatinating with using join is: ", con_pq)

#11. Python program to concatenate two strings without using join() method. 
a = input("enter the first string: ")
b = input("enter the second string: ")
con_ab = a + b
print("string after cancatinating without using join is: ", con_ab)

#12. Python program to remove repeated character from string. 
n = input("enter the input: ")
emp_n = ""
for i in n:
    if i not in emp_n:
        emp_n = emp_n + i
print(emp_n)

#13. Python program to check given character is vowel or consonant. 
z = input("enter the input: ")
vowels = 'aeiou'
if z in vowels:
    print("it is a vowel")
else:
    print("it is a consonent")

#14. Python program to check given character is digit or not. 
z = input("enter the charecters: ")
if z.isdigit():
    print("given charecter is digit")
else:
    print("given charecter is not digit")

#15. Python program to delete vowels in a given string. 
p = input("enter the string: ")
vow = "aeiou"
emp_s = ""
for i in p:
    if i not in vow:
        emp_s = emp_s + i
print(emp_s)

#16. Python program to count the Occurrence Of Vowels & Consonants in a String. 
n = input("enter the string: ")
vow = 'aeiou'
vow_c = 0
cons_c = 0
for i in n:
    if i in vow:
        vow_c = vow_c + 1
    else:
        cons_c = cons_c + 1
print("vowels count is: ", vow_c)
print("consonents count is: ", cons_c)

#17. Python program to print the highest frequency character in a String. 
b = input("enter the string: ")
d = {}
for i in b:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
hfe = max(d, key = d.get)
r = {hfe : d[hfe]}
print("the heighest frequency element is: ", r)

#18. Python program to Replace First Occurrence Of Vowel With ‘-‘ in String. 
z = input("enter the string: ")
vowelss = "aeiouAEIOU"
e_s = ""
for i in z:
    if i not in vowelss:
        e_s = e_s + i 
    elif "-" not in e_s:
        e_s = e_s + "-"
    elif i in vowelss and "-" in e_s:
        e_s = e_s + i
print("original string is: ",z)
print("string after replacing with - is: ", e_s)


#19. Python program to count alphabets, digits and special characters. 
x = input("enter the string: ")
c_alph = 0
c_d = 0
c_spcl = 0
for i in x:
    if i.isalpha():
        c_alph= c_alph + 1
    elif i.isdigit():
        c_d = c_d + 1
    else:
        c_spcl = c_spcl + 1
print("count of alphabets is: ", c_alph)
print("count of digits is: ", c_d)
print("count of special charecters is: ", c_spcl)


# 20. Python program to check given character is digit or not using isdigit() method. 
z = input("enter the charecters: ")
if z.isdigit():
    print("given charecters are digits")
else:
    print("not digit")

#21. Python program to calculate sum of integers in string. 
n = input("enter the string: ")
s = 0
for i in n:
    if i.isdigit():
        s = s + int(i)
print("sum of integers is: ", s)

#22. Python program to print all non repeating character in string.
x = input("enter the string: ")
n_ch = ""
for i in x:
    if i not in n_ch:
        n_ch = n_ch + i
print("non repating charecters are: ",n_ch)

#23. Python program to copy one string to another string. 
x = input("enter the string: ")
copy_x = x
print("the input string before copying is: ", x)
print("string after copying is: ", copy_x)
