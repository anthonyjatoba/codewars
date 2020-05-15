def series_sum(n):
    res = sum(1/(1+3*d) for d in range(n))
    return '{:.2f}'.format(res)