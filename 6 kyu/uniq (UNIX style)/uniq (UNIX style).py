from itertools import groupby

def uniq(seq): 
    return [key for key, group in groupby(seq)]