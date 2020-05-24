import sys

def high_and_low(numbers):
    max, min = -sys.maxsize -1, sys.maxsize
    for s in numbers.split():
        n = int(s)
        if n > max:
            max = n
        if n < min:
            min = n
    return '{} {}'.format(max, min)