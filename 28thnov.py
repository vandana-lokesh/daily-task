#Python program to check given character is digit or not  without using isdigit() method.
z = input("enter the charecters: ")
if z.isalnum():    #isnumeric()
    print("given charecters are digit")
else:
    print("not digit")

# Python program to Replace last Occurrence Of Vowel With ‘-‘ in String.
x = input("enter the string: ")
v = "aeiouAEIOU"
re_ch = ""
for i in x:
    if i in v:
        re_ch = i.replace(i[:-1], "-")
print(re_ch)


"""python program to find index values of a mid charector
"learning" > n
"praveen"  > v"""
s = input("enter the string: ")
len_s = len(s) //2
l = s[len_s]
print(l)