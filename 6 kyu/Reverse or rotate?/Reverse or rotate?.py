def split(string, sz):
    for i in range(0, len(string), sz):
        chunk = string[i:i + sz]
        if len(chunk) == sz:
            yield chunk
        else:
            return


def rotate(string):
    return string[1:] + string[: 1]


def revrot(string, sz):
    if sz == 0 or not string or sz > len(string):
        return ''

    chunks = [chunk for chunk in split(string, sz)]
    chunks_rotated = [chunk[::-1] if sum(int(digit) ** 3 for digit in chunk) % 2 == 0
                      else rotate(chunk) for chunk in chunks]
    return ''.join(chunks_rotated)
