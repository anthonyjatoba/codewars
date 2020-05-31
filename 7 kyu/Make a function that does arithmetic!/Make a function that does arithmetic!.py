from operator import add, sub, mul, truediv

def arithmetic(a, b, operator):
    ops = {'add': add,
           'subtract': sub,
           'multiply': mul,
           'divide': truediv}
    return ops[operator](a, b)