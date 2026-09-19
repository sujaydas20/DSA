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




s = "banana"

s = s.replace("a", "o")

print(s)



a = [[1, 2, 3], [4, 5, 6]]

s = 0

for row in a:
    for x in row:
        if x % 2 == 0:
            s += x

print(s)




def f(x):
    x = x + 5

a = f(10)

print(a)



s = 0

for i in range(10, 2, -2):
    s += i

print(s)



a = 3
b = 4
c = 5

a, b, c = c, a, b

print(a + b * c)








a = [2, 3, 2, 4, 2, 5, 3]

x = a.count(2)
y = a.count(3)

print(x * y)










a = [10, 20, 30, 20, 40]

x = a.index(20)
y = a.index(40)

print(x + y)

a = [10, 20, 30, 40]

x = a.pop(1)
y = a.pop()

print(x + y)
print(a)