def create_phone_number(n):
    n = ''.join(str(d) for d in n)
    return '({}) {}-{}'.format(''.join(n[:3]),
                                ''.join(n[3:6]),
                                ''.join(n[6:]))