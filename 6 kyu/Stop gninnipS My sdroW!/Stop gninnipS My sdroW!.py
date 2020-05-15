def spin_words(sentence):
    s = ''
    for word in sentence.split():
        if len(word) >= 5:
            s += word[::-1] + ' '
        else:
            s += word + ' '
    return s[:-1]