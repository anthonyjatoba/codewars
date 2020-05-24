def accum(s):
    str = ''
    for i in range(1, len(s)+1):
        str += s[i-1].upper() + s[i-1].lower() * (i-1) + '-'
    return str[:-1]