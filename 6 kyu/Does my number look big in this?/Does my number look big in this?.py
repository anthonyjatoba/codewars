from functools import reduce
from operator import add
def narcissistic( value ):
    svalue = str(value)
    return value == reduce(add, (int(d) ** len(svalue) for d in svalue))