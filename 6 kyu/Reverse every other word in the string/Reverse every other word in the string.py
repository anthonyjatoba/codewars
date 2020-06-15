def alt_rev(word_list):
    reverse = False
    for word in word_list:
        w = word[::-1] if reverse else word 
        reverse = not reverse
        yield w
        
def reverse_alternate(string):
    word_list = string.split()
    return ' '.join(word for word in alt_rev(word_list))