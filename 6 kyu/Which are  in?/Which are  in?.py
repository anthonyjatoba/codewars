def in_array(array1, array2):
    new = set()
    for sub in array1:
        for sup in array2:
            if sub in sup:
                new.add(sub)
    return sorted(list(new))