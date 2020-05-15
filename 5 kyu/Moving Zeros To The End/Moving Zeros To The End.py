def move_zeros(array):
    zeroes = [a for a in array if not isinstance(a, bool) and a == 0]
    array_no_zeroes = [a for a in array if isinstance(a, bool) or a != 0]
    return array_no_zeroes + zeroes