from functools import reduce
from operator import add
def row_sum_odd_numbers(n):
    min_index = reduce(add, range(0, n))
    max_index = reduce(add, range(0, n+1))
    min_odd = min_index * 2 + 1
    max_odd = (max_index) * 2 + 1
    return sum(range(min_odd, max_odd-1, 2))    