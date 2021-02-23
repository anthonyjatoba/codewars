def always(n=0):
    def f():
        return n
    return f