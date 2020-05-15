def growing_plant(upSpeed, downSpeed, desiredHeight):
    height, days = 0, 0    
    if desiredHeight == 0:
        return 1
    while height < desiredHeight:
        days +=1
        height += upSpeed
        if height >= desiredHeight:
            return days
        height -= downSpeed
    return days