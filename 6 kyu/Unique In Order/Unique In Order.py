def unique_in_order(iterable):
    new_list = []
    last = 0
    for i in iterable:
        if i != last:
            last = i
            new_list.append(i)
    return new_list