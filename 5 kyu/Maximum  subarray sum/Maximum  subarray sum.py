def max_sequence(arr):
    if not arr or all(x < 0 for x in arr):
        return 0
        
    memo = {0: arr[0]}
    for i in range(1, len(arr)):
        memo[i] = max(memo[i - 1] + arr[i], arr[i])
    return max(memo.values())