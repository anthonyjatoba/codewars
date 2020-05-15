from collections import Counter

def is_anagram(w1, w2):
    c1 = Counter(w1)
    c2 = Counter(w2)
    return c1 == c2
    
def anagrams(word, words):
    return [w for w in words if is_anagram(w, word)]