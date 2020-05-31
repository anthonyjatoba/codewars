def validBraces(string):
    open = ["(","[","{"]
    close = [")","]","}"]

    stack = []
    for i in string:
        if i in open:
            stack.append(i)
        else:
            pos = close.index(i)
            if len(stack) > 0 and open[pos] == stack[len(stack)-1]:
                stack.pop() 
            else: 
                return False

    return True if len(stack) == 0 else False