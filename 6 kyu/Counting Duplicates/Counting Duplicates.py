from collections import Counter

def duplicate_count(text):
    counter = Counter(text.lower())
    reps = 0
    for _, value in counter.items():
        if value > 1:
            reps += 1
    return reps