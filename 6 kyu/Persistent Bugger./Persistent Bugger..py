from operator import mul
from functools import reduce

def persistence(n):
    s = str(n)
    n = 0
    while len(s) != 1:
        s = str(reduce(mul, (int(d) for d in s)))
        n += 1
    return n