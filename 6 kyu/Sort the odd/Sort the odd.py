def sort_array(source_array):
    even = [n for n in source_array if n % 2 == 0]
    odd = sorted([n for n in source_array if n % 2 == 1], reverse=True)
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            source_array[i] = odd.pop()
    return source_array