def order(sentence):
    t = []
    numbers = '123456789'
    for word in sentence.split():
        number = -1
        for n in numbers:
            if n in word:
                number = int(n)
        t.append((number, word))
    t = sorted(t)
    return ' '.join(item[1] for item in t)
    