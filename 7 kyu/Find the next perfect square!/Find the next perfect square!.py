import math
def find_next_square(sq):
    s = math.sqrt(sq)
    if s.is_integer():
        return (s+1)**2
    else:
        return -1