__author__ = 'Tiger'

a = list(map(lambda x: x*x, range(1, 101)))
b = sum(a)
print(b)
c = sum(range(1, 101))
c *= c
print(c)
print(c - b)
print(a)