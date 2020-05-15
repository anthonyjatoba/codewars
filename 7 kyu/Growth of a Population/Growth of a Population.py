def nb_year(p0, percent, aug, p):
    p1 = p0 + (p0 * percent/100) + aug
    if p1 >= p:
        return 1
    else:
        return 1 + nb_year(p1, percent, aug, p)
    