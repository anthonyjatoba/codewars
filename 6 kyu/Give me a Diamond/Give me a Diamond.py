import math

def diamond(n):
    if n < 1 or n % 2 == 0:
        return None
    lines = [('*' * (i * 2 + 1)).center(n).rstrip() for i in range(math.ceil(n/2))]
    return '\n'.join(lines + lines[:-1][::-1]) + '\n'

