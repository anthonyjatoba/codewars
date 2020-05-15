from math import ceil, log10


def graceful_tipping(bill):
    bill *= 1.15
    if bill < 10:
        return ceil(bill)
    else:
        divisor = 5 * 10**(int(log10(bill)) -1)
        times = int(ceil(bill/divisor))
        return times * divisor