def find_missing_letter(chars):
    all = [chr(c) for c in range(ord(chars[0]), ord(chars[-1]))]
    return (set(all) - set(chars)).pop()
    
    