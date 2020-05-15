import math 
def divisors(integer):
    multiples = [i for i in range(2, math.floor(integer/2)+1) if integer % i == 0]
    return multiples if len(multiples) > 0 else '{} is prime'.format(integer)