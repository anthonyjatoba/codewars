def get_middle(s):
    l = len(s)
    d = int(l/2)
    if l % 2 == 0:
        return s[d-1:d+1]
    else:    # odd
        return s[d]