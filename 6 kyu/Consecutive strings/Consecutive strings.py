def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) == 0 or k <= 0:
        return ''
    maxlen, maxstr = 0, ''
    for i in range(len(strarr) - k+1):
        st = ''.join(s for s in strarr[i:i+k])
        if len(st) > maxlen:
            maxlen = len(st)
            maxstr = st
    return maxstr