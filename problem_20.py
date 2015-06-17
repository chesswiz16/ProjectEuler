from functools import reduce
import math

__author__ = 'Tiger'


r = math.factorial(100)
s = str(r)
a = reduce(lambda x, y: int(x) + int(y), s)
print(r)
print(s)
print(a)
