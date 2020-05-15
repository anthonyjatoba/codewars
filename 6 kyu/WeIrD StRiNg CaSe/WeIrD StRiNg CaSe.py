def to_weird_case(string):
    new_string = ''
    for word in string.split():
        new_string += ''.join(word[i].upper() if i%2==0 else word[i].lower() for i in range(len(word))) + ' '
    return new_string[:-1]