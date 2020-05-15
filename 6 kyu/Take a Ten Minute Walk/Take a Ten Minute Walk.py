def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        ncount = walk.count('n') - walk.count('s')
        ecount = walk.count('e') - walk.count('w')
        if ncount != 0 or ecount != 0:
            return False
        return True