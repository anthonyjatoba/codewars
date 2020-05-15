def tickets(people):
    twenty_fives = 0
    fifties = 0
    for p in people:
        if p == 25:
            twenty_fives += 1
        if p == 50:
            if twenty_fives == 0:
                return 'NO'
            twenty_fives -= 1
            fifties += 1
        if p == 100:
            if fifties >= 1 and twenty_fives >= 1:
                twenty_fives -= 1
                fifties -= 1
            elif twenty_fives >= 3:
                twenty_fives -= 3
            else:
                return 'NO'
    return 'YES'        
