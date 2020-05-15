def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    smallest = min(numbers)
    copy = list(numbers)
    copy.remove(smallest)
    return copy
    
