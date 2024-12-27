#ascending order
lst = [3, 8, 4, 1, 9]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)

print("==============")
#descending order
l = [2, 5, 0, 30, 25, 40 ]
l.sort()
des_lst = []
for i in l:
    des_lst = [i] + des_lst
print(des_lst)

#sum of each elements of 2 lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
sum_lst = []
for i in range(len(l1)):
    sum = l1[i] + l2[i]
    sum_lst.append(sum)
print(sum_lst)

#summation
def summation(initpt, endpt):
    sum = 0
    for i in range(initpt, endpt):
        sum = sum + i
    return sum

a = summation(0, 10)
print(a)

print("=========")

#sum of element
b = [1, 2, 3, 4, 5]
s_b = 0
for i in b:
    s_b = i + s_b
print(s_b)

#square
s = [1, 2, 3, 4]
sq = []
for i in s:
    sq.append(i*i)
print(sq)

#cube
c = [1, 2, 3, 4]
cb = []
for i in c:
    cb.append(i*i*i)
print(cb)

