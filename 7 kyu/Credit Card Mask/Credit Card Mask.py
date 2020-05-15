# return masked string
def maskify(cc):
    l = len(cc) 
    if l <= 4:
        return cc
    else:
        return (l-4) * '#' + cc[-4:]