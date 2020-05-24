def square_digits(num):
    s = ''
    for d in str(num):
        s += str(int(d) ** 2)
    return int(s)