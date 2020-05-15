from string import ascii_lowercase as abc

def alphabet_position(text):
    dic = {abc[k]: k + 1 for k in range(len(abc))}
    return ' '.join(str(dic[c]) for c in text.lower() if c in abc)