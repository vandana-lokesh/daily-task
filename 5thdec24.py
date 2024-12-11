#list comprehension
l = [1, 2, 3, 4, 5]
l1 = [i for i in l if i % 2 == 0]
print(l1)

l2 = [1, 2, 3, 4, 5]
l3 = []
for i in l2:
    if i % 2 == 0:
        l3.append(i)
print(l3)

#
no_of_products = 5
total_price = 0
for i in range(5):
    product_price = int(input("enter the price: "))
    print(product_price)
    total_price = total_price + product_price
print(total_price)



#tuple  >>>>>> immutable, cant add and insert 

#declaration of tuple:
t = ()
print(type(t))

t = (2)
print(type(t))    #o/p = int

t1 = (2,)
print(type(t1))    #o/p = tuple

#type conversions:
t2 = ("ram", 1, 4.0, True)
lt = list(t2)
print(lt)
lt.append(1000)
print(lt)

t2 = tuple(lt)
print(t2)

#methods
#t2.count()
#t2.index()

#packing and unpacking
marks = (68, 35, 60, 55)
P , C, M, B = marks
print(P)
print(C)
print(M)
print(B)

#adding 2 tuples
t5 = t2 + marks
print(t5)

# 
for i in t2:
    print(i)