def array_diff(a, b):
    for i in b:
        try:
            while True:
                a.remove(i)
        except ValueError:
            continue
    return a