def create_phone_number(n):
    s = ''.join(str(d) for d in n)
    return "({}) {}-{}".format(s[:3], s[3:6], s[6:])