def dig_pow(n, p):
    digits = [int(c) for c in str(n)]
    product = 0
    for i in range(len(digits)):
        product += digits[i] ** (p+i)
    div = product/n
    return int(div) if div.is_integer() else -1