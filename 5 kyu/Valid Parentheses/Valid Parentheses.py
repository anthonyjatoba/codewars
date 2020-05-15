def valid_parentheses(string):
    pilha = []
    for c in string:
        if c in ('(', ')'):
            if c == '(':
                pilha.append('x')
            else:
                try:
                    pilha.pop()
                except:
                    return False
    if len(pilha) == 0:
        return True
    else:
        return False