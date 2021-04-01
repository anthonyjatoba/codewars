def find_missing_number(numbers):
    diff = set(range(1, len(numbers) + 2)) - set(numbers)
    return diff.pop()