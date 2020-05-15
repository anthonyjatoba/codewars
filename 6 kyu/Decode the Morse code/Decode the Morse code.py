def decodeMorse(morse_code):
    words_list = morse_code.split('  ')
    words = []
    for word in words_list:
        decoded = ''.join(MORSE_CODE[key] for key in word.split())
        words.append(decoded)
    return ' '.join(words).strip(' ')