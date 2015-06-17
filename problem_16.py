from functools import reduce

__author__ = 'Tiger'


as_string = str(2**1000)

sum = reduce(lambda x, y: int(x) + int(y), as_string)
print(sum)

