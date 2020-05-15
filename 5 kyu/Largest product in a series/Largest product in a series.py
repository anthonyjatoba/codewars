from functools import reduce
from operator import mul

def greatest_product(n):
    l = [int(c) for c in n]
    max = 0
    for i in range(len(l)-4):
        prod =  reduce(mul, l[i:i+5])
        if prod > max:
            max = prod
    return max