def disemvowel(string):
    for v in 'aeiouAEIOU':
        string = string.replace(v, '')
    return string