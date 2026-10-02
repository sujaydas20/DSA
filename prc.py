import heapq

a = [7, 2, 9, 1, 5]
heapq.heapify(a)

print(heapq.heappop(a))
print(heapq.heappop(a))



def gen():
    x = 1
    while x < 5:
        yield x
        x += 2

g = gen()

print(next(g))
print(next(g))
print(list(g))



class A:
    x = 10

    @classmethod
    def change(cls, v):
        cls.x += v

A.change(5)
a = A()
a.change(3)

print(A.x, a.x)



import bisect

a = [1, 3, 5, 7]
bisect.insort(a, 4)
bisect.insort(a, 6)

print(a[2] + a[-1])



a = {"x": 1, "y": 2}
b = {"y": 5, "z": 7}

c = {**a, **b}
print(c["x"] + c["y"] + c["z"])




from itertools import chain

a = [1, 2]
b = [3, 4, 5]

c = list(chain(b, a))
print(c[1] + c[-2])




try:
    x = int("5.5")
except ValueError:
    print("A")
except Exception:
    print("B")
else:
    print("C")
finally:
    print("D")






class A:
    def __init__(self, x):
        self._x = x

    @property
    def value(self):
        return self._x * 2

a = A(6)
print(a.value)






from itertools import groupby

a = "aaabbc"
g = groupby(a)

result = [(k, len(list(v))) for k, v in g]

print(result)