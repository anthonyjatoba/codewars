def reducible(d1, d2):
    if (d1, d2) == ('NORTH', 'SOUTH') or (d2, d1) == ('NORTH', 'SOUTH'):
        return True
    if (d1, d2) == ('EAST', 'WEST') or (d2, d1) == ('EAST', 'WEST'):
        return True
    return False

def array_is_reducible(arr):
    for i in range(len(arr)-1):
        if reducible(arr[i], arr[i+1]):
            return True
    return False


def dirReduc(arr):
    while array_is_reducible(arr):
        new_arr = []
        i = 0
        while i < len(arr):
            if i == len(arr) - 1:
                new_arr.append(arr[i])
            try:
                if reducible(arr[i], arr[i+1]):
                    i+=2
                else:
                    new_arr.append(arr[i])
                    i+=1
            except:
                i+=1
        arr = new_arr
    return arr