def reverse_words(text):
    new_text = ''
    word = ''
    for c in text:        
        if c == ' ':
            new_text += word[::-1] + ' '
            word = ''            
        else:
            word += c
    new_text += word[::-1]
    return new_text
            