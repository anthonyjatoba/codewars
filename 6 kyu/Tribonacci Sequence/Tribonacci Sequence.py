def tribonacci(signature, n):
    if n == 0:
        return []
    list = signature
    while len(list) < n:
        list.append(sum(list[len(list)-3:len(list)]))
    return list[:n]