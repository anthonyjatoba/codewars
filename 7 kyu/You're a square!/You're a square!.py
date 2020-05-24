from math import sqrt

def is_square(n):
    if n < 0:
        return False
    elif sqrt(n) - int(sqrt(n)) == 0:
        return True
    return False