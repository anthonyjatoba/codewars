def even(n):
    return n % 2 == 0

def find_outlier(ints):
    find_odd = (even(ints[0]) and even(ints[1])) or (even(ints[1]) and even(ints[2])) or (even(ints[0]) and even(ints[2]))
    
    if find_odd:
        for i in ints:
            if not even(i):
                return i
    else:
        for i in ints:
            if even(i):
                return i
    
        
    