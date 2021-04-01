def expanded_form(num):
    num = str(num)
    components = []
    for i in range(len(num)):
        digito = num[i]
        if digito == '0':
            continue
        components.append(digito + '0' * (len(num) - i - 1))    
    return ' + '.join(components)