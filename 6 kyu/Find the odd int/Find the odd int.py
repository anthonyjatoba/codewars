def soma(a, b):
    return a + b

def find_it(seq):
    counter = {}
    for item in seq:
        counter[item] = soma(counter.setdefault(item, 0), 1)
    print(counter)
    for key, value in counter.items():
        if value % 2 == 1:
            return key