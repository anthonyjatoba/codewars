from collections import Counter
def is_isogram(string):
    cnt = Counter(string.lower())
    for _, value in cnt.items():
        if value > 1:
            return False
    return True