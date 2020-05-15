from collections import OrderedDict
def more_zeros(s):
    return list(OrderedDict.fromkeys([c for c in s if '{:b}'.format(ord(c)).count('0') > '{:b}'.format(ord(c)).count('1')]))
    
    