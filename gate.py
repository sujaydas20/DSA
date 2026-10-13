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




from operator import itemgetter

data = [(3, 8), (1, 9), (2, 4), (4, 6)]
result = sorted(data, key=itemgetter(1))

print(result[0][0] + result[-1][0])