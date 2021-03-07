def word_mesh(words):
    words_to_mesh = []
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        for j in reversed(range(min(len(word1), len(word1)) + 1)):
            if word1[-j:] == word2[:j]:
                words_to_mesh.append(word1[-j:])
                break
    if len(words_to_mesh) < len(words) - 1:
        return 'failed to mesh'
    else:
        return ''.join(words_to_mesh)
