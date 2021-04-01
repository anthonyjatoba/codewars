def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    eurekas = []
    for n in range(a, b+1):
        digits = str(n)
        sum_pow = sum(int(digit) ** power for power, digit in enumerate(digits, start=1))
        if sum_pow == n:
            eurekas.append(n)
    return eurekas