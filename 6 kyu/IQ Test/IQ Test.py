def is_even(n):
    return n%2==0

def iq_test(numbers):
    numbers = [int(n) for n in numbers.split()]
    n_even = sum(is_even(n) for n in numbers[:3])
    if n_even > 3 - n_even:
        # achar o impar
        for i in range(len(numbers)):
            if not is_even(numbers[i]):
                return i+1
    else:
        for i in range(len(numbers)):
            if is_even(numbers[i]):
                return i+1
        