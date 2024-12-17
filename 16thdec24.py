d = {"name": "ram", "age": 20, "salary": 30000}
print(d)

for i in d:
    print(i, "=", d[i])

#removing elements from dictionary
print(d)
#del d  #removes variable from memory

#del d["age"]
print(d)

#clear()
#d.clear()
print(d)

#pop()>>>>remove and returns associated values with the given key
print(d.pop("age"))
print(d)

#popitem()>>>>removes and returns keyvalues pair of last element from dict
d1 = {"name": "sita", "age": 20, "salary": 40000, "agee": 30}
print(d1)

d1.popitem()
print(d1)

d1.popitem()
print(d1)

#keys()>>>>returns all keys
d2 = {"name": "sita", "age": 20, "salary": 40000}
print(d2)
print(d2.keys())

#values()>>>>returns all values
print(d2.values())

#items()>>>>>>>pair of key values
print(d2.items())

dd = d2.items()
print(type(dd))