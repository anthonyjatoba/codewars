import string 

def string_letter_count(s):
    s = s.lower()
    return ''.join('{}{}'.format(s.count(c), c) for c in string.ascii_lowercase if s.count(c) > 0)       