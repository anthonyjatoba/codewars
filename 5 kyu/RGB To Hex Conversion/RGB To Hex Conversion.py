def inttohex(value):
    if value <= 0:
        return '00'
    elif value >= 255:
        return 'FF'
    s = hex(value)[2:].upper()
    return s if len(s) > 1 else '0' + s

def rgb(r, g, b):
    return '{}{}{}'.format(inttohex(r), inttohex(g), inttohex(b))