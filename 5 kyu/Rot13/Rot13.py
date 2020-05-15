from string import ascii_lowercase as abc
from string import ascii_uppercase as ABC

def encode_char(c):
    alphabet = ''
    if c in abc:
        alphabet = abc
    elif c in ABC:
        alphabet = ABC
    else:
        return c
    if c in alphabet:
        i = alphabet.index(c)
        new_i = (i + 13) % len(alphabet)
        return alphabet[new_i]
        
def rot13(message):
    return ''.join(encode_char(c) for c in message)    