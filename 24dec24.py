#print the type of values in given dict
d = {"a": 1, "b": "1"}
val_type = []
for k, v in d.items():
    val_type.append(type(v))
print(val_type)

#print 2 lists of positive and negative list without duplicates:
l = [2, 4, 5, 2, 2, 3, 5, -2, 5, 1, -1 ,9, -10, 9, 5, 7, 4, 10, 10]
pos = []
neg = []
for i in l:
    if i >= 0 and i not in pos:
        pos.append(i)
    if i < 0 and i not in neg:
        neg.append(i)
print(pos)
print(neg)

#find N largest no from list
l1 = [3, 10, 4, 2, 90, 20, 50, 99, 100, 40]
l1.sort()
l1.reverse()
print(l1)
N = int(input("N = "))
for i in range(N):
    print(l1[i])

