from functools import reduce
from operator import add

def digital_root(n):
    sum = reduce(add, (int(d) for d in str(n)))
    if len(str(sum)) == 1:
        return int(sum)
    else:
        return digital_root(int(sum))