def factorial(n):
    if 0 < n < 13:
        return n * factorial(n-1)
    elif n == 0:
        return 1
    else:
        raise ValueError
        