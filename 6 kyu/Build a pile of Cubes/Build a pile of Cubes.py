def find_nb(m):
    i = 0
    resto = m
    while resto > i:
        i += 1
        resto = resto - i**3
    return i if resto == 0 else -1        