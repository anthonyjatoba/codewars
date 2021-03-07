def hist(s):
    u = s.count('u')
    w = s.count('w')
    x = s.count('x')
    z = s.count('z')

    ustring = 'u  {:6s}{}'.format(str(u), '*' * u) if u else ''
    wstring = 'w  {:6s}{}'.format(str(w), '*' * w) if w else ''
    xstring = 'x  {:6s}{}'.format(str(x), '*' * x) if x else ''
    zstring = 'z  {:6s}{}'.format(str(z), '*' * z) if z else ''
    
    histogram = "\r".join(string for string in [ustring, wstring, xstring, zstring] if string)

    return '{}'.format(histogram)
