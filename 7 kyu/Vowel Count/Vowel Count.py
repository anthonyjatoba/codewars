def getCount(inputStr):
    return sum(inputStr.count(v) for v in 'aeiou')