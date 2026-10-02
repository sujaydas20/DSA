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