from functools import reduce
from operator import add
def printer_error(s):
    return '{}/{}'.format(sum(s.count(e) for e in 'nopqrstuvwxyz'), len(s))
    
    