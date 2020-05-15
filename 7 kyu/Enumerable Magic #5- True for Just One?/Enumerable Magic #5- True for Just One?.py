def one(sq, fun): 
    return [fun(value) for value in sq].count(True) == 1