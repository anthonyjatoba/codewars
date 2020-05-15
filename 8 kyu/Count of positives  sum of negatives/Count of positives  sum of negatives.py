def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    else:
        return [len([pos for pos in arr if pos > 0]), sum(neg for neg in arr if neg < 0)]
     