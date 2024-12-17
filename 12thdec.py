#set joins
#set union()>>>>>it will return both s1 and s2 value
s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9}
print(s1.union(s2))

#set intersection()>>>>>>it will return common elements
s1 = {1, 4, 6, 2, 3, 5}
s2 = {2, 5, 1, 8, 6}
print(s1.intersection(s2))

#difference>>>>returns s1 that values are preent in s1 not in s2
print(s1.difference(s2))

#symmetric difference>>>>returns both s1 and s2 but not in both sets
print(s1.symmetric_difference(s2))

#dictionory
d = {"name": "vandana", "marks":200, "active": True, "percentage":89.999}
print(d)

#declaration
d = {}
print(type(d))

d["name"]= "ram"
d["age"] = 25
d["salary"]= 50000
print(d)

d["name"] = "sita"
d["age"] = 20
print(d)  #name and age is changed

#d = eval(input("enter your input: "))
print(d)
print(type(d))

no_prodcts = 5
products = {}
for i in range(no_prodcts):
    key = input("enter your key: ")
    value = int(input("enter your vale: "))
    products[key] = value
print(products)

#accessing data:
print(d["name"])

ad = d.get("age")
print(ad)

#python program to print sum of all prices
no_prodcts = 5
totalprice = 0
products = {}
for i in range(no_prodcts):
    key = input("enter your key: ")
    value = int(input("enter your vale: "))
    products[key] = value
    totalprice = totalprice + value
print(products)
print(totalprice)