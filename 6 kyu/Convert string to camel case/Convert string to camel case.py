def to_camel_case(text):
    separator = '-' if '-' in text else '_'
    text = text.replace('-', separator).replace('_', separator)
    words = text.split(separator)
    return words[0] + ''.join(word.capitalize() for word in words[1:])