x="learning"
print (x.index("ning"))

arry=("i",1,2,3)
print(arry[1:-1])




s = 0

for i in range(5):
    if i == 2:
        pass
    else:
        s += i

print(s)





a = [4, 1, 3, 2]

b = sorted(a)

print(a)
print(b)




a = [10, 20, 30, 40, 50]

del a[1:4]

print(a)




a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)