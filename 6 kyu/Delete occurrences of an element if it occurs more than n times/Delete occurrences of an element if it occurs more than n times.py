def delete_nth(order,max_e):
    occurrences = []
    for item in order:
        if occurrences.count(item) < max_e:
            occurrences.append(item)
    return occurrences
        