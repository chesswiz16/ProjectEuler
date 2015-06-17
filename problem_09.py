__author__ = 'Tiger'

for a in range(1, 999):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if (a * a) + (b * b) == c * c:
            print(a, " ", b, " ", c, " ", a * b * c, " ", a + b + c)