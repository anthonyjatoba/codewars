from string import ascii_lowercase as abc

def high(x):
    def score(word):
        return sum(abc.find(c) + 1 for c in word)
    return sorted(x.split(), key=score, reverse=True)[0]
    