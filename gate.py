a = [1, 2]
b = [a, a]

b[0].append(3)

print(a)
print(b)




def counter():
    counter.x += 1
    return counter.x

counter.x = 0

print(counter(), counter(), counter())